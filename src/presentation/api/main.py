from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
from pathlib import Path
from dotenv import load_dotenv
import base64
from datetime import datetime
from fastapi.staticfiles import StaticFiles
import aiohttp
from src.infrastructure.config.dependencies import initialize_services
from src.presentation.api.routers.parent_dashboard import router as parent_dashboard_router


def create_app() -> FastAPI:
    app = FastAPI(title="AI TIK HKT API", version="0.1.0")

    # Enable CORS for the frontend dev server
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "http://localhost:3002",  # Add port 3002 for Vite dev server
            "http://127.0.0.1:3000",
            "http://127.0.0.1:3002",  # Add port 3002 for Vite dev server
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    async def startup_event() -> None:
        # Load environment variables from .env at project root if present
        try:
            project_root = Path(__file__).resolve().parents[3]
        except Exception:
            project_root = Path.cwd()
        load_dotenv(dotenv_path=project_root / ".env")

        # Initialize DI container services at application startup
        initialize_services()

    # Include API routers
    app.include_router(parent_dashboard_router)

    # Serve static files for saved illustrations (moved to end to avoid conflicts)
    static_dir = Path(__file__).resolve().parent.parent / "static"
    static_dir.mkdir(parents=True, exist_ok=True)
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

    @app.get("/api/v1/health")
    def health_check() -> dict[str, str]:
        return {"status": "ok"}

    @app.post("/api/offer")
    async def proxy_webrtc_offer(request: Request) -> Response:
        """CORS-friendly proxy to the Pipecat WebRTC offer endpoint.

        Frontend posts to this backend endpoint; we forward to the Pipecat server
        running on localhost:8080 and return the JSON answer.
        """
        try:
            body = await request.body()
            headers = {"Content-Type": request.headers.get("Content-Type", "application/json")}
            async with aiohttp.ClientSession() as session:
                async with session.post("http://localhost:8080/api/offer", data=body, headers=headers) as resp:
                    data = await resp.read()
                    return Response(content=data, status_code=resp.status, media_type=resp.headers.get("Content-Type", "application/json"))
        except Exception as exc:
            return JSONResponse(status_code=502, content={"error": "Failed to reach Pipecat offer endpoint", "detail": str(exc)})

    class IllustrationRequest(BaseModel):
        prompt: str
        scenario: str | None = None

    class TTSRequest(BaseModel):
        text: str
        language: str = "en-IE"
        voice_name: str | None = None

    @app.get("/api/v1/illustrations/list/{scenario}")
    async def list_scenario_illustrations(scenario: str) -> JSONResponse:
        """List existing illustrations for a specific scenario, sorted by creation date (newest first)."""
        try:
            safe_scenario = scenario.strip().lower().replace(" ", "-")
            scenario_dir = static_dir / "illustrations" / safe_scenario
            
            if not scenario_dir.exists():
                return JSONResponse(content={"illustrations": []})
            
            illustrations = []
            for json_file in scenario_dir.glob("*.json"):
                try:
                    import json
                    with open(json_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    illustrations.append({
                        "file": metadata.get("file", ""),
                        "created_at": metadata.get("created_at", ""),
                        "prompt": metadata.get("prompt", ""),
                        "scenario": metadata.get("scenario", safe_scenario)
                    })
                except Exception:
                    continue
            
            # Sort by creation date (newest first)
            illustrations.sort(key=lambda x: x.get("created_at", ""), reverse=True)
            
            return JSONResponse(content={"illustrations": illustrations})
            
        except Exception as exc:
            return JSONResponse(status_code=500, content={
                "error": "Failed to list illustrations",
                "detail": str(exc)
            })

    @app.post("/api/v1/illustrations/generate")
    async def generate_illustration(req: IllustrationRequest) -> JSONResponse:
        """Generate an illustration using Google's Nano Banana image model.

        Returns a data URL (base64) for quick embedding by the frontend.
        """
        # Lazy import to avoid mandatory dependency at startup
        try:
            from google import genai as google_genai  # type: ignore
        except Exception as import_exc:  # pragma: no cover
            return JSONResponse(status_code=500, content={
                "error": "google-genai not available",
                "detail": str(import_exc),
            })

        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return JSONResponse(status_code=400, content={
                "error": "Missing GEMINI_API_KEY/GOOGLE_API_KEY",
            })

        try:
            client = google_genai.Client(api_key=api_key)
            # Official Gemini image model per docs
            # https://ai.google.dev/gemini-api/docs/image-generation
            model = "gemini-2.5-flash-image"

            # Compose prompt with light safety rails
            full_prompt = req.prompt.strip()
            if req.scenario:
                full_prompt = f"Scenario: {req.scenario}. Create a child-friendly, classroom-appropriate illustration. " + full_prompt
            
            # Add translation requirements for Irish text
            translation_instruction = " CRITICAL: If any Irish text (Gaeilge), signs, labels, or written content appears in the illustration, you MUST include clear English translations or captions alongside the Irish text. This is essential for Chinese students learning English in Ireland."
            full_prompt += translation_instruction

            # Try modern content-generation surface for image outputs
            # Some SDK versions expose image generation via generate_content with image MIME types
            generation_config = {
                "response_mime_type": "image/png"
            }
            try:
                result = client.models.generate_content(
                    model=model,
                    contents=[full_prompt],
                    generation_config=generation_config,
                )
            except Exception:
                # Fallback: older signature without generation_config
                result = client.models.generate_content(
                    model=model,
                    contents=[full_prompt],
                )

            # Normalize response to first image base64 across possible shapes
            image_b64: str | None = None

            def to_b64(maybe):
                if maybe is None:
                    return None
                if isinstance(maybe, (bytes, bytearray)):
                    return base64.b64encode(maybe).decode("utf-8")
                if isinstance(maybe, str):
                    return maybe
                # Some SDKs return objects with .data or .bytes
                data = getattr(maybe, "data", None)
                if isinstance(data, (bytes, bytearray)):
                    return base64.b64encode(data).decode("utf-8")
                if isinstance(data, str):
                    return data
                bytes_attr = getattr(maybe, "bytes", None)
                if isinstance(bytes_attr, (bytes, bytearray)):
                    return base64.b64encode(bytes_attr).decode("utf-8")
                base64_attr = getattr(maybe, "base64", None)
                if isinstance(base64_attr, str):
                    return base64_attr
                return None

            if hasattr(result, "images") and result.images:
                image_b64 = to_b64(result.images[0])
            if not image_b64 and hasattr(result, "image"):
                image_b64 = to_b64(result.image)
            # Newer SDKs often return candidates -> content -> parts with inline_data
            if not image_b64 and hasattr(result, "candidates") and result.candidates:
                cand0 = result.candidates[0]
                image_b64 = (
                    getattr(cand0, "image_base64", None)
                    or getattr(cand0, "base64", None)
                    or to_b64(getattr(cand0, "image", None))
                )
                if not image_b64:
                    content = getattr(cand0, "content", None)
                    parts = getattr(content, "parts", None) if content is not None else None
                    if isinstance(parts, list):
                        for p in parts:
                            inline = getattr(p, "inline_data", None)
                            if inline is not None:
                                data = getattr(inline, "data", None)
                                image_b64 = to_b64(data)
                                if image_b64:
                                    break

            if not image_b64:
                return JSONResponse(status_code=502, content={
                    "error": "No image returned from model"
                })

            # Persist file and metadata under static/illustrations
            safe_scenario = (req.scenario or "unspecified").strip().lower().replace(" ", "-")
            ts = datetime.utcnow().strftime("%Y%m%dT%H%M%S%fZ")
            out_dir = static_dir / "illustrations" / safe_scenario
            out_dir.mkdir(parents=True, exist_ok=True)
            png_path = out_dir / f"{ts}.png"
            meta_path = out_dir / f"{ts}.json"

            try:
                img_bytes = base64.b64decode(image_b64)
                png_path.write_bytes(img_bytes)
            except Exception as write_exc:
                # If write fails, still return data URL
                data_url = f"data:image/png;base64,{image_b64}"
                return JSONResponse(content={
                    "image_data_url": data_url,
                    "warning": f"save_failed: {write_exc}"
                })

            # Write metadata
            import json
            metadata = {
                "scenario": req.scenario,
                "prompt": full_prompt,
                "created_at": ts,
                "file": f"/static/illustrations/{safe_scenario}/{ts}.png"
            }
            try:
                meta_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
            except Exception:
                pass

            # Return both URL and data URL (for immediate display)
            data_url = f"data:image/png;base64,{image_b64}"
            return JSONResponse(content={
                "image_url": metadata["file"],
                "image_data_url": data_url,
                "metadata": metadata,
            })
        except Exception as exc:  # pragma: no cover
            return JSONResponse(status_code=502, content={
                "error": "Illustration generation failed",
                "detail": str(exc)
            })

    @app.post("/api/v1/tts/synthesize")
    async def synthesize_speech(req: TTSRequest) -> JSONResponse:
        """
        Generate speech audio using Google TTS API directly.
        This provides a simple TTS endpoint for sample sentence pronunciation.
        """
        try:
            # Use Google TTS API directly (simpler than Pipecat integration)
            from google.cloud import texttospeech
            import base64
            
            # Initialize Google TTS credentials
            google_creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_PATH")
            if not google_creds_path:
                return JSONResponse(status_code=500, content={
                    "error": "Google TTS credentials not configured",
                    "detail": "GOOGLE_APPLICATION_CREDENTIALS_PATH environment variable not set"
                })
            
            # Create TTS client
            client = texttospeech.TextToSpeechClient.from_service_account_file(google_creds_path)
            
            # Configure synthesis input
            synthesis_input = texttospeech.SynthesisInput(text=req.text)
            
            # Configure voice with proper language/voice matching
            # Map language codes to compatible voices
            language_voice_map = {
                'en-IE': ('en-GB', 'en-GB-Neural2-F'),  # Irish English -> British English voice (more appropriate)
                'en-US': ('en-US', 'en-US-Neural2-F'),
                'en-GB': ('en-GB', 'en-GB-Neural2-F'),
                'zh-CN': ('zh-CN', 'cmn-CN-Chirp3-HD-Despina'),
                'zh': ('zh-CN', 'cmn-CN-Chirp3-HD-Despina'),
            }
            
            # Get compatible language code and voice
            language_code, voice_name = language_voice_map.get(
                req.language, 
                ('en-US', 'en-US-Neural2-F')  # Default fallback
            )
            
            # Override voice if specifically requested and compatible with language
            if req.voice_name:
                # Only override if the requested voice is compatible with the language
                # Check if the voice matches the language pattern
                voice_lang = req.voice_name.split('-')[1] if '-' in req.voice_name else 'US'
                if voice_lang.upper() == language_code.split('-')[1].upper():
                    voice_name = req.voice_name
                # If incompatible, stick with the mapped voice for better UX
            
            voice = texttospeech.VoiceSelectionParams(
                language_code=language_code,
                name=voice_name
            )
            
            # Configure audio output
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
                speaking_rate=1.0
            )
            
            # Perform the text-to-speech synthesis
            response = client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config
            )
            
            # Convert audio content to base64 for JSON response
            audio_base64 = base64.b64encode(response.audio_content).decode('utf-8')
            
            return JSONResponse(content={
                "audio_data": audio_base64,
                "format": "mp3",
                "text": req.text,
                "requested_language": req.language,
                "actual_language": language_code,
                "voice_name": voice_name
            })
            
        except Exception as exc:
            import traceback
            return JSONResponse(status_code=502, content={
                "error": "TTS synthesis failed",
                "detail": str(exc),
                "traceback": traceback.format_exc()
            })

    return app


app = create_app()
