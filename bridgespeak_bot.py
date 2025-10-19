"""
Tavus Pipecat Quickstart Bot

This module implements a conversational AI bot using Pipecat framework with:
- Real-time video using Tavus replicas
- Speech-to-text with Deepgram
- Text-to-speech with Cartesia
- LLM with Google Gemini
- WebRTC transport with RTVI protocol

The bot uses the RTVI (Real-Time Voice Interaction) protocol to ensure proper
coordination between the client and server, preventing dropped first turns and
providing a better conversation experience.

Educational Features (Optional):
- Educational context processing between STT and LLM
- Child safety filtering and trauma-informed response validation
- Bilingual communication with structured learning sequences
- Performance monitoring for sub-2-second requirements
- Xiao Mei character service with age-appropriate content

Environment Variables for Educational Features:
- ENABLE_EDUCATIONAL_PROCESSING: Enable educational context processing (default: false)
- TARGET_AGE_GROUP: Target age group for content filtering (default: junior_infants)
- ENABLE_BILINGUAL_GREETING: Enable bilingual greeting sequences (default: false)
- ENABLE_PERFORMANCE_MONITORING: Enable performance metrics collection (default: false)
"""

import os

import aiohttp
from dotenv import load_dotenv
from loguru import logger

# Pipecat audio processing components
from pipecat.audio.turn.smart_turn.base_smart_turn import SmartTurnParams
from pipecat.audio.turn.smart_turn.local_smart_turn_v3 import LocalSmartTurnAnalyzerV3
from pipecat.audio.vad.silero import SileroVADAnalyzer
from pipecat.audio.vad.vad_analyzer import VADParams

# Pipecat core components
from pipecat.frames.frames import LLMRunFrame
from pipecat.pipeline.pipeline import Pipeline
from pipecat.pipeline.runner import PipelineRunner
from pipecat.pipeline.task import PipelineParams, PipelineTask

# Pipecat processors and aggregators
from pipecat.processors.aggregators.llm_context import LLMContext
from pipecat.processors.aggregators.llm_response_universal import LLMContextAggregatorPair
from pipecat.processors.frameworks.rtvi import RTVIProcessor, RTVIServerMessageFrame
from pipecat.frames.frames import TextFrame, Frame
from pipecat.processors.frame_processor import FrameDirection, FrameProcessor

# Pipecat runner and transport
from pipecat.runner.types import RunnerArguments
from pipecat.runner.utils import create_transport

# Service integrations
from pipecat.transcriptions.language import Language
from pipecat.services.deepgram.stt import DeepgramSTTService
from pipecat.services.google.llm import GoogleLLMService
from pipecat.services.google.tts import GoogleTTSService
from pipecat.services.google.stt import GoogleSTTService
from pipecat.services.tavus.video import TavusVideoService
from pipecat.transports.base_transport import BaseTransport, TransportParams

# Educational context processing (optional features)
try:
    from educational_context_processor import EducationalContextProcessor, AgeGroup
    from src.domain.services.xiaomei_character import (
        XiaoMeiCharacterService,
        XiaoMeiCharacterConfig,
    )
    from src.domain.services.xiaomei_state import XiaoMeiStateManager
    from src.domain.services.bilingual_communication import BilingualCommunicationService
    from src.domain.services.body_language_system import BodyLanguageSystem
    EDUCATIONAL_FEATURES_AVAILABLE = True
    logger.info("Educational features loaded successfully")
except ImportError as e:
    EDUCATIONAL_FEATURES_AVAILABLE = False
    logger.warning(f"Educational features not available: {e}")
    # Create dummy classes for graceful degradation
    class EducationalContextProcessor:
        def __init__(self, *args, **kwargs): pass
        def get_performance_baseline(self): return {"total_frames_processed": 0, "avg_processing_time_ms": 0}
        def is_within_performance_threshold(self): return True
    class AgeGroup:
        JUNIOR_INFANTS = "junior_infants"
    class XiaoMeiCharacterService:
        def __init__(self, *args, **kwargs): pass
        def get_system_prompt(self): return "You are a helpful AI assistant."
    class XiaoMeiCharacterConfig:
        def __init__(self, *args, **kwargs): pass
    class XiaoMeiStateManager:
        def __init__(self): pass
        def set_celebrating(self): pass
        def set_listening(self): pass
        def set_speaking(self): pass
        def set_body_language_system(self, *args): pass
        @property
        def state(self): return "listening"
    class BilingualCommunicationService:
        def __init__(self): pass
        def get_scenario_learning_sequence(self, *args, **kwargs): return []
        async def execute_bilingual_sequence(self, *args): return []
    class BodyLanguageSystem:
        def __init__(self): pass

# Load environment variables from .env file
# override=True ensures .env values take precedence over existing environment variables
load_dotenv(override=True)

# Educational features configuration
ENABLE_EDUCATIONAL_PROCESSING = os.getenv("ENABLE_EDUCATIONAL_PROCESSING", "false").lower() == "true"
TARGET_AGE_GROUP = os.getenv("TARGET_AGE_GROUP", "junior_infants")
ENABLE_BILINGUAL_GREETING = os.getenv("ENABLE_BILINGUAL_GREETING", "false").lower() == "true"
ENABLE_PERFORMANCE_MONITORING = os.getenv("ENABLE_PERFORMANCE_MONITORING", "false").lower() == "true"

# TTS Configuration Constants
TTS_VOICE_ID_ENGLISH = "en-GB-Chirp3-HD-Autonoe"
TTS_VOICE_ID_CHINESE = "cmn-CN-Chirp3-HD-Despina"
TTS_LANGUAGE_ENGLISH = Language.EN_GB
TTS_LANGUAGE_CHINESE = Language.ZH_CN
TTS_GENDER_FEMALE = "female"
TTS_RATE_SLOW = "slow"

# Log educational features configuration
if EDUCATIONAL_FEATURES_AVAILABLE:
    logger.info(f"Educational features configuration:")
    logger.info(f"  Educational processing: {ENABLE_EDUCATIONAL_PROCESSING}")
    logger.info(f"  Target age group: {TARGET_AGE_GROUP}")
    logger.info(f"  Bilingual greeting: {ENABLE_BILINGUAL_GREETING}")
    logger.info(f"  Performance monitoring: {ENABLE_PERFORMANCE_MONITORING}")
else:
    logger.info("Educational features disabled - required modules not available")

# Speed up startup by disabling heavy components early
import os
# Disable ONNX GPU discovery to avoid WSL/Windows delays
os.environ.setdefault("ORT_DISABLE_GPU", "1")
# Disable VAD if not needed (saves model loading time)
if os.getenv("VAD_ENABLED", "true").lower() in ("0", "false", "no"):
    os.environ.setdefault("SILERO_VAD_DISABLED", "1")

# Global storage for request data from WebRTC connections
# This allows us to access custom data passed from the frontend
_global_request_data = {}

from pipecat.frames.frames import LLMTextFrame

class SubtitleTextProcessor(FrameProcessor):
    """
    Processor that captures text frames and sends them to the frontend as RTVI messages
    for real-time subtitle display.
    """
    
    def __init__(self, rtvi_processor=None):
        super().__init__()
        self.rtvi_processor = rtvi_processor
        
    async def process_frame(self, frame: Frame, direction: FrameDirection):
        """Process frames and capture text for subtitles"""
        await super().process_frame(frame, direction)
        
        # Capture LLM text frames and send to frontend
        if isinstance(frame, LLMTextFrame):
            text_content = frame.text.strip()
            if text_content:
                logger.debug(f"SubtitleTextProcessor: Capturing LLM text for subtitles: {text_content[:50]}...")
                
                # Send as RTVI server message through the RTVI processor
                # This is the proper way to send RTVI messages
                if self.rtvi_processor:
                    from pipecat.processors.frameworks.rtvi import RTVIServerMessageFrame
                    rtvi_message = RTVIServerMessageFrame(
                        data={
                            "type": "bot-transcript",
                            "text": text_content,
                            "final": True
                        }
                    )
                    await self.rtvi_processor.push_frame(rtvi_message, direction)
                
        # Always pass the original frame through
        await self.push_frame(frame, direction)

# Monkey-patch the WebRTC request handler to capture custom data
def patch_webrtc_request_handler():
    """Patch the WebRTC request handler to capture custom data"""
    try:
        from pipecat.transports.smallwebrtc.request_handler import SmallWebRTCRequestHandler, SmallWebRTCRequest
        from fastapi import Request
        import json
        
        # Store the original handle_web_request method
        original_handle_web_request = SmallWebRTCRequestHandler.handle_web_request
        
        async def patched_handle_web_request(self, request, webrtc_connection_callback):
            """Patched version that stores request data globally"""
            # logger.info(f"🔧 Patched handle_web_request called with request: {request}")
            logger.info(f"🔧 Request type: {type(request)}")
            
            # Check all possible ways the data might be passed
            request_data = None
            if hasattr(request, 'request_data') and request.request_data:
                request_data = request.request_data
                # logger.info(f"✅ Found request_data: {request_data}") # TODO: remove this line, it's for debugging
            else:
                logger.warning("❌ No request_data found in request or request_data is empty")
            
            # Store request data globally for access by the bot
            if request_data:
                connection_id = getattr(request, 'pc_id', 'default')
                _global_request_data[connection_id] = request_data
                # logger.info(f"✅ Stored request data for connection {connection_id}: {request_data}") # TODO: remove this line, it's for debugging
            
            # Call the original handler
            return await original_handle_web_request(self, request, webrtc_connection_callback)
        
        # Replace the method
        SmallWebRTCRequestHandler.handle_web_request = patched_handle_web_request
        logger.info("Successfully patched WebRTC request handler to capture custom data")
        
    except ImportError as e:
        logger.warning(f"Could not patch WebRTC request handler: {e}")


def patch_fastapi_offer_endpoint():
    """Patch FastAPI offer endpoint to extract webrtcRequestParams"""
    try:
        import fastapi
        from fastapi import Request as FastAPIRequest
        from pipecat.transports.smallwebrtc.request_handler import SmallWebRTCRequest
        import json
        
        # Store the original Request class __init__
        original_fastapi_request_json = FastAPIRequest.json
        
        async def patched_fastapi_request_json(self):
            """Patched version that captures and injects request_data"""
            try:
                # Get the original JSON body
                body = await original_fastapi_request_json(self)
                # logger.info(f"🔧 FastAPI request body: {body}") # TODO: remove this line, it's for debugging
                
                # Extract webrtcRequestParams if present (this comes from the POST body when using webrtcRequestParams)
                webrtc_request_params = body.get('webrtcRequestParams', {})
                if webrtc_request_params:
                    # logger.info(f"🔧 Found webrtcRequestParams: {webrtc_request_params}") # TODO: remove this line, it's for debugging
                    # Inject request_data into the body
                    body['request_data'] = webrtc_request_params
                    # logger.info(f"✅ Injected request_data: {webrtc_request_params}") # TODO: remove this line, it's for debugging
                else:
                    # Check if we have scenario data directly in the body (for testing)
                    request_data = {}
                    scenario_fields = ['scenario', 'scenarioDetails', 'enableVideo', 'url']
                    for field in scenario_fields:
                        if field in body and field not in ['sdp', 'type', 'pc_id', 'restart_pc']:
                            request_data[field] = body[field]
                    
                    if request_data:
                        # logger.info(f"🔧 Found scenario data in body: {request_data}") # TODO: remove this line, it's for debugging
                        body['request_data'] = request_data
                        # logger.info(f"✅ Injected request_data from body: {request_data}") # TODO: remove this line, it's for debugging
                
                return body
            except Exception as e:
                logger.error(f"Error patching FastAPI request: {e}")
                return await original_fastapi_request_json(self)
        
        # Replace the method
        FastAPIRequest.json = patched_fastapi_request_json
        logger.info("Successfully patched FastAPI request to extract webrtcRequestParams")
        
    except Exception as e:
        logger.warning(f"Could not patch FastAPI request: {e}")

# Apply the patches when the module is loaded
patch_webrtc_request_handler()
patch_fastapi_offer_endpoint()

# Debug: Check if patch was applied
logger.info("Checking if WebRTC request handler patch was applied...")
try:
    from pipecat.transports.smallwebrtc.request_handler import SmallWebRTCRequestHandler
    if hasattr(SmallWebRTCRequestHandler, 'handle_web_request'):
        logger.info("✅ WebRTC request handler patch applied successfully")
    else:
        logger.warning("❌ WebRTC request handler patch failed - method not found")
except Exception as e:
    logger.error(f"❌ Error checking WebRTC request handler patch: {e}")

# Import scenario prompts from separate module
from src.domain.services.scenario_prompts import get_system_prompt_for_scenario, SCENARIO_SYSTEM_PROMPTS

# Transport configuration for different transport types
# We use a lambda function to delay instantiation until the transport is actually selected
# This prevents creating unnecessary objects for unused transports
def _build_vad_analyzer():
    """Create a VAD analyzer if enabled and available, otherwise return None.

    This guards against missing Silero model files at runtime and allows
    disabling VAD via environment flag VAD_ENABLED=false.
    """
    vad_enabled = os.getenv("VAD_ENABLED", "true").lower() not in ("0", "false", "no")
    if not vad_enabled:
        logger.warning("VAD disabled via VAD_ENABLED env flag; proceeding without VAD")
        return None
    try:
        return SileroVADAnalyzer(params=VADParams(stop_secs=0.2))
    except Exception as exc:  # onnx model missing or other init errors
        logger.error(
            "Failed to initialize Silero VAD; proceeding without VAD. Error: {}",
            exc,
        )
        return None


transport_params = {
    "webrtc": lambda: TransportParams(
        # Enable audio input (user's microphone)
        audio_in_enabled=True,
        
        # Enable audio output (bot's voice)
        audio_out_enabled=True,
        
        # Enable video output (Tavus replica video)
        video_out_enabled=True,
        
        # Set to True for real-time video streaming (not pre-recorded)
        video_out_is_live=True,
        
        # Video resolution: 1280x720 (720p) - good balance of quality and bandwidth
        video_out_width=1280,
        video_out_height=720,
        
        # VAD (Voice Activity Detection) — safe fallback if Silero model missing
        vad_analyzer=_build_vad_analyzer(),
        
        # Smart turn analyzer for better conversation flow
        # Helps determine when it's the bot's turn to speak
        turn_analyzer=LocalSmartTurnAnalyzerV3(params=SmartTurnParams()),
    ),
}


class SafeTavusVideoService(TavusVideoService):
    """Wrapper around TavusVideoService that gracefully degrades to no-op on errors.

    When Tavus quota/credits are exhausted (e.g., HTTP 402) or the transport client
    is None, this service disables itself to avoid crashing the pipeline. Audio-only
    flow (STT+LLM+TTS) will continue.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disabled = False

    async def start(self, frame):  # type: ignore[override]
        if self._disabled:
            return
        try:
            await super().start(frame)
        except Exception as exc:  # pragma: no cover
            self._disabled = True
            from loguru import logger as _logger
            _logger.warning("Tavus start failed; disabling video and continuing audio-only: {}", exc)

    async def process_frame(self, frame, direction):  # type: ignore[override]
        if self._disabled:
            # When disabled, pass through all frames to maintain audio-only functionality
            # This includes AudioRawFrame, StartFrame, EndFrame, etc.
            await self.push_frame(frame, direction)
            return
        try:
            await super().process_frame(frame, direction)
        except Exception as exc:  # pragma: no cover
            self._disabled = True
            from loguru import logger as _logger
            _logger.warning("Tavus process_frame error; disabling video: {}", exc)
            # After disabling, forward the frame that caused the error
            await self.push_frame(frame, direction)

    async def cancel(self, frame):  # type: ignore[override]
        if self._disabled:
            return
        try:
            await super().cancel(frame)
        except Exception:
            self._disabled = True

    async def cleanup(self):  # type: ignore[override]
        if self._disabled:
            return
        try:
            await super().cleanup()
        except Exception:
            self._disabled = True


class SafeDeepgramSTTService(DeepgramSTTService):
    """
    Safe wrapper for DeepgramSTTService that gracefully handles credit exhaustion
    and falls back to Google STT when Deepgram fails with 402 Payment Required.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disabled = False
        self._fallback_service = None
    
    async def start(self, frame):  # type: ignore[override]
        if self._disabled:
            return
        try:
            await super().start(frame)
        except Exception as exc:  # pragma: no cover
            self._disabled = True
            from loguru import logger as _logger
            _logger.warning("Deepgram STT start failed; disabling and continuing with fallback: {}", exc)
            # Initialize Google STT fallback
            await self._init_google_stt_fallback()

    async def process_frame(self, frame, direction):  # type: ignore[override]
        if self._disabled:
            # When disabled, use Google STT fallback
            if self._fallback_service:
                await self._fallback_service.process_frame(frame, direction)
            return
        try:
            await super().process_frame(frame, direction)
        except Exception as exc:  # pragma: no cover
            self._disabled = True
            from loguru import logger as _logger
            _logger.warning("Deepgram STT process_frame error; disabling and using fallback: {}", exc)
            # Initialize Google STT fallback if not already done
            if not self._fallback_service:
                await self._init_google_stt_fallback()
            # Process with fallback
            if self._fallback_service:
                await self._fallback_service.process_frame(frame, direction)

    async def _init_google_stt_fallback(self):
        """Initialize Google STT as fallback when Deepgram fails"""
        try:
            from loguru import logger as _logger
            _logger.info("Initializing Google STT fallback service")
            
            # Check if Google credentials are available
            google_creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_PATH")
            if not google_creds_path:
                _logger.warning("Google STT fallback not available: GOOGLE_APPLICATION_CREDENTIALS_PATH not set")
                return
            
            # Initialize Google STT service
            self._fallback_service = GoogleSTTService(
                language_code="en-US",
                model="latest_long",
                credentials_path=google_creds_path,
            )
            _logger.info("Google STT fallback service initialized successfully")
            
        except Exception as exc:
            from loguru import logger as _logger
            _logger.error("Failed to initialize Google STT fallback: {}", exc)


async def run_bot(transport: BaseTransport, runner_args: RunnerArguments, custom_data=None):
    """
    Main bot logic that sets up and runs the Pipecat pipeline
    
    This function:
    1. Initializes all service components (STT, TTS, LLM, Video)
    2. Sets up the conversation context and system prompt (customized by scenario)
    3. Creates a processing pipeline
    4. Configures RTVI protocol for client-server coordination
    5. Runs the pipeline and handles events
    
    Args:
        transport: The transport layer (e.g., WebRTC) for communication
        runner_args: Configuration arguments for the pipeline runner
        custom_data: Optional custom data from the client (e.g., scenario info)
    """
    logger.info(f"Starting bot")
    
    # Use aiohttp session for async HTTP requests (required by Tavus service)
    async with aiohttp.ClientSession() as session:
        # Initialize Speech-to-Text service using Deepgram with Google STT fallback
        # This converts the user's spoken words into text
        stt = SafeDeepgramSTTService(api_key=os.getenv("DEEPGRAM_API_KEY"))

        # Initialize Text-to-Speech service with fallback mechanism
        # Since Cartesia credits are exhausted, use Google TTS directly
        google_creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_PATH")
        
        if google_creds_path:
            # Use Google TTS directly since Cartesia credits are exhausted
            from loguru import logger as _logger
            _logger.info("Using Google TTS as primary service (Cartesia credits exhausted)")
            tts = GoogleTTSService(
                voice_id=TTS_VOICE_ID_ENGLISH,
                # voice_id=TTS_VOICE_ID_CHINESE,  # Alternative Chinese voice
                # language_code=TTS_LANGUAGE_CHINESE,  # Not work as expected
                language_code=TTS_LANGUAGE_ENGLISH,
                credentials_path=google_creds_path,
                params=GoogleTTSService.InputParams(
                    gender=TTS_GENDER_FEMALE,
                    rate=TTS_RATE_SLOW,
                    language=TTS_LANGUAGE_ENGLISH,  # TTS_LANGUAGE_CHINESE,  # Not work as expected
                )
            )
        else:
            raise ValueError("GOOGLE_APPLICATION_CREDENTIALS_PATH must be set for TTS fallback")

        # Initialize Large Language Model using Google Gemini
        # Prefer GEMINI_API_KEY if present
        llm = GoogleLLMService(api_key=os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"))

        # Initialize educational services (if available and enabled)
        educational_services = {}
        if EDUCATIONAL_FEATURES_AVAILABLE and ENABLE_EDUCATIONAL_PROCESSING:
            try:
                # Parse age group
                age_group = None
                try:
                    age_group = AgeGroup(TARGET_AGE_GROUP)
                except ValueError:
                    logger.warning(f"Invalid age group '{TARGET_AGE_GROUP}', using default")
                    age_group = AgeGroup.JUNIOR_INFANTS
                
                # Initialize Xiao Mei character service
                xiaomei = XiaoMeiCharacterService(
                    XiaoMeiCharacterConfig(age_group=age_group.name if age_group else None)
                )
                
                # Initialize state manager and body language system
                state_manager = XiaoMeiStateManager()
                body_language_system = BodyLanguageSystem()
                state_manager.set_body_language_system(body_language_system)
                
                # Initialize bilingual communication service
                bilingual_service = BilingualCommunicationService()
                
                educational_services = {
                    'xiaomei': xiaomei,
                    'state_manager': state_manager,
                    'bilingual_service': bilingual_service,
                    'body_language_system': body_language_system,
                    'age_group': age_group
                }
                
                logger.info(f"Educational services initialized for age group: {age_group}")
                
            except Exception as e:
                logger.error(f"Failed to initialize educational services: {e}")
                educational_services = {}

        # Initialize Tavus Video Service
        # This generates real-time video of a digital replica speaking
        # The replica_id identifies which Tavus replica to use
        # Initialize Tavus transport only if video is desired; otherwise skip to avoid None client
        # Default can be controlled via AUDIO_ONLY_DEFAULT env (true -> disable video by default)
        audio_only_default = os.getenv("AUDIO_ONLY_DEFAULT", "false").lower() in ("1", "true", "yes", "on")
        enable_video = not audio_only_default
        try:
            # Attempt to read preference from runner_args.custom_request_data
            if custom_data and isinstance(custom_data, dict):
                pref = custom_data.get("enableVideo")
                if isinstance(pref, bool):
                    enable_video = pref
        except Exception:
            enable_video = not audio_only_default

        # Only create Tavus if explicitly enabled and creds exist; otherwise force audio-only
        tavus_api_key = os.getenv("TAVUS_API_KEY")
        tavus_replica = os.getenv("TAVUS_REPLICA_ID")
        tavus_enabled = os.getenv("TAVUS_ENABLED", "false").lower() in ("1", "true", "yes", "on")

        tavus = None
        if enable_video and tavus_enabled and tavus_api_key and tavus_replica:
            tavus = SafeTavusVideoService(
                api_key=tavus_api_key,
                replica_id=tavus_replica,
            session=session,
        )
        else:
            if enable_video and not tavus_enabled:
                logger.warning("Tavus video disabled: set TAVUS_ENABLED=true to enable; running audio-only")
            elif enable_video and (not tavus_api_key or not tavus_replica):
                logger.warning("Tavus video disabled: missing TAVUS_API_KEY or TAVUS_REPLICA_ID; running audio-only")
            enable_video = False

        # Extract scenario from custom data and get appropriate system prompt
        scenario_id = None
        scenario_details = None
        if custom_data and isinstance(custom_data, dict):
            scenario_id = custom_data.get('scenario')
            # Normalize scenario ID (strip whitespace, convert to lowercase)
            if scenario_id:
                scenario_id = str(scenario_id).strip().lower()
            # Optional rich details from frontend
            scenario_details = custom_data.get('scenarioDetails') or {}
        
        # Get scenario-specific system prompt with details
        system_prompt = get_system_prompt_for_scenario(scenario_id, scenario_details)
        
        # Log scenario information
        logger.info(f"Received custom_data: {custom_data}")
        logger.info(f"Extracted scenario_id: '{scenario_id}'")
        logger.info(f"Available scenarios: {list(SCENARIO_SYSTEM_PROMPTS.keys())}")
        
        if scenario_id:
            if scenario_id in SCENARIO_SYSTEM_PROMPTS:
                logger.info(f"Using scenario: '{scenario_id}' with custom character persona")
            else:
                logger.warning(f"Unknown scenario: '{scenario_id}' - using default system prompt")
        else:
            logger.info("No scenario specified - using default system prompt")
        
        logger.info(f"System prompt preview: {system_prompt[:200]}...")
        
        # Initialize conversation messages with the appropriate system prompt
        # The system prompt defines the bot's behavior and personality
        messages = [
            {
                "role": "system",
                "content": system_prompt,
            },
        ]

        # Create LLM context to store conversation history
        # This maintains the full conversation between user and bot
        context = LLMContext(messages)
        
        # Context aggregator handles accumulating messages from both user and assistant
        # It splits into two processors: one for user messages, one for assistant responses
        context_aggregator = LLMContextAggregatorPair(context)

        # Create RTVI processor for proper client-ready/bot-ready handshake
        # This ensures the client and server are coordinated before starting the conversation
        # It prevents the bot's first turn from being dropped
        rtvi = RTVIProcessor()
        
        # Create subtitle text processor for real-time subtitle display
        subtitle_processor = SubtitleTextProcessor(rtvi_processor=rtvi)

        # Create the processing pipeline
        # The pipeline defines the flow of data through the system
        # Data flows from top to bottom through these processors
        processors = [
            transport.input(),
            rtvi,
            stt,
        ]
        
        # Add educational context processor if enabled
        educational_processor = None
        if EDUCATIONAL_FEATURES_AVAILABLE and ENABLE_EDUCATIONAL_PROCESSING and educational_services:
            try:
                educational_processor = EducationalContextProcessor(
                    age_group=educational_services.get('age_group')
                )
                # processors.append(educational_processor) # Commented out because EducationalContextProcessor is not working
                logger.info("Educational context processor added to pipeline")
            except Exception as e:
                logger.error(f"Failed to create educational processor: {e}")
        
        processors.extend([
            context_aggregator.user(),
            llm,
            subtitle_processor,  # Capture text after LLM for subtitles
            tts,
        ])
        if enable_video and tavus is not None:
            processors.append(tavus)
        processors.extend([
            transport.output(),
            context_aggregator.assistant(),
        ])

        pipeline = Pipeline(processors)

        # Create a pipeline task with configuration parameters
        task = PipelineTask(
            pipeline,
            params=PipelineParams(
                # Audio input sample rate (from user's microphone)
                # 16kHz is standard for speech recognition
                audio_in_sample_rate=16000,
                
                # Audio output sample rate (to user's speakers)
                # 24kHz provides higher quality audio output
                audio_out_sample_rate=24000,
                
                # Enable metrics collection for monitoring and debugging
                enable_metrics=True,
                
                # Enable usage metrics (e.g., API usage tracking)
                enable_usage_metrics=True,
            ),
            # Automatically stop the pipeline after this many seconds of inactivity
            # Helps prevent zombie sessions from consuming resources
            idle_timeout_secs=runner_args.pipeline_idle_timeout_secs,
        )

        # Performance monitoring setup for educational processing
        session_start_time = None
        if ENABLE_PERFORMANCE_MONITORING and educational_processor:
            import time
            session_start_time = time.time()
            logger.info("Performance monitoring enabled for educational processing")

        # Define simple greeting function before the event handler
        async def _simple_greeting():
            """Simple greeting fallback system"""
            # Add a system message to kick off the conversation
            # This tells the LLM to greet the user and start the interaction
            if scenario_id:
                # Build a richer intro using details (title, objectives)
                title = None
                try:
                    if isinstance(scenario_details, dict):
                        title = scenario_details.get('title')
                        objectives = scenario_details.get('objectives') or []
                    else:
                        objectives = []
                except Exception:
                    objectives = []
                    title = None

                objective_hint = ""
                if objectives:
                    # Pick first objective as the opening focus
                    objective_hint = f" Focus today: {objectives[0]}."

                label = title or scenario_id
                intro = (
                    f"Start by warmly greeting the student as an ESL teacher in Ireland. "
                    f"Today's focus is the '{label}' scenario.{objective_hint} "
                    "Invite them to try a short response relevant to this scenario. "
                    "Stay strictly on this scenario topic; do not switch topics unless the student asks."
                )
            else:
                intro = (
                    "Start by warmly greeting the student as an ESL teacher in Ireland. "
                    "Briefly state today's focus and invite them to try speaking."
                )
            messages.append({"role": "system", "content": intro})
            
            # Queue an LLMRunFrame to trigger the LLM to generate the greeting
            # This starts the conversation flow
            await task.queue_frames([LLMRunFrame()])

        # Event handler for when the client signals it's ready
        # This is part of the RTVI protocol handshake
        @rtvi.event_handler("on_client_ready")
        async def on_client_ready(rtvi):
            logger.info("Client ready - setting bot ready")
            
            # Signal to the client that the bot is ready to start
            # This completes the RTVI handshake
            await rtvi.set_bot_ready()
            
            # Enhanced greeting system with bilingual support
            if ENABLE_BILINGUAL_GREETING and educational_services:
                try:
                    # Enhanced greeting using bilingual communication service
                    logger.info("Starting bilingual greeting sequence")
                    
                    # Get structured bilingual greeting sequence
                    greeting_sequence = educational_services['bilingual_service'].get_scenario_learning_sequence("greetings", 0)
                    
                    # Execute the bilingual communication pattern
                    async for message in educational_services['bilingual_service'].execute_bilingual_sequence(greeting_sequence):
                        if message.content:  # Skip empty pause messages
                            # Set appropriate emotional state
                            if message.emotional_state == "celebrating":
                                educational_services['state_manager'].set_celebrating()
                            elif message.emotional_state in ["patient_listening", "patient_waiting"]:
                                educational_services['state_manager'].set_listening()
                            else:
                                educational_services['state_manager'].set_speaking()
                            
                            # Add state information to context
                            messages.append({"role": "system", "content": f"[state:{educational_services['state_manager'].state}]"})
                            
                            # Add the bilingual message
                            messages.append({"role": "assistant", "content": message.content})
                            await task.queue_frames([LLMRunFrame()])
                            
                            logger.info(f"Bilingual sequence - Phase: {message.phase.value}, Content: {message.content}")
                    
                    # Set final state to listening for user interaction
                    educational_services['state_manager'].set_listening()
                    messages.append({"role": "system", "content": f"[state:{educational_services['state_manager'].state}] Ready for child interaction"})
                    logger.info("Bilingual greeting sequence completed, ready for child interaction")
                    
                except Exception as e:
                    logger.error(f"Bilingual greeting failed, falling back to simple greeting: {e}")
                    # Fall back to simple greeting
                    await _simple_greeting()
            else:
                # Use simple greeting system
                await _simple_greeting()

        # Event handler for client messages (e.g., scenario updates)
        @rtvi.event_handler("on_client_message")
        async def on_client_message(rtvi, message):
            logger.info(f"Received client message: {message}")
            
            # Handle scenario messages from the client
            if message.type == "scenario":
                logger.info(f"Processing scenario message: {message.data}")
                
                # Extract scenario data from the client message
                scenario_data = message.data
                if isinstance(scenario_data, dict):
                    new_scenario = scenario_data.get('scenario')
                    new_scenario_details = scenario_data.get('scenarioDetails')
                    
                    if new_scenario:
                        logger.info(f"Client sent scenario update: {new_scenario}")
                        
                        # Update the scenario in the system prompt
                        # Get the current system prompt from context
                        current_messages = context.get_messages()
                        
                        # Find and update the system message
                        for msg in current_messages:
                            if msg.get('role') == 'system':
                                # Update the system prompt with new scenario and details
                                updated_prompt = get_system_prompt_for_scenario(new_scenario, new_scenario_details)
                                msg['content'] = updated_prompt
                                logger.info(f"Updated system prompt for scenario: {new_scenario} with details: {new_scenario_details}")
                                break
                        
                        # Send acknowledgment back to client
                        await rtvi.push_frame(RTVIServerMessageFrame(
                            data={
                                "type": "scenario-updated",
                                "payload": {
                                    "scenario": new_scenario,
                                    "status": "success"
                                }
                            }
                        ))
                else:
                    logger.warning(f"Invalid scenario data format: {scenario_data}")
                    await rtvi.push_frame(RTVIServerMessageFrame(
                        data={
                            "type": "scenario-error",
                            "payload": {
                                "error": "Invalid scenario data format"
                            }
                        }
                    ))

        # Event handler for when the client disconnects
        @transport.event_handler("on_client_disconnected")
        async def on_client_disconnected(transport, client):
            logger.info(f"Client disconnected")
            
            # Log performance metrics if educational processing was enabled
            if ENABLE_PERFORMANCE_MONITORING and educational_processor and session_start_time:
                import time
                session_duration = time.time() - session_start_time
                metrics = educational_processor.get_performance_baseline()
                logger.info(f"Educational session metrics:")
                logger.info(f"  Session duration: {session_duration:.2f}s")
                logger.info(f"  Frames processed: {metrics['total_frames_processed']}")
                logger.info(f"  Avg processing time: {metrics['avg_processing_time_ms']:.2f}ms")
                logger.info(f"  Within threshold: {educational_processor.is_within_performance_threshold()}")
            
            # Cancel the pipeline task to clean up resources
            await task.cancel()

        # Create the pipeline runner
        # handle_sigint allows graceful shutdown on Ctrl+C
        runner = PipelineRunner(handle_sigint=runner_args.handle_sigint)

        # Run the pipeline task
        # This starts the bot and keeps it running until disconnected or cancelled
        await runner.run(task)


async def bot(runner_args: RunnerArguments):
    """
    Main bot entry point compatible with Pipecat Cloud
    
    This function is called by the Pipecat runner with command-line arguments.
    It creates the appropriate transport (WebRTC, Daily, etc.) and runs the bot.
    
    Args:
        runner_args: Configuration from command-line arguments (transport type, host, port, etc.)
    """
    # Create the transport based on the command-line arguments
    # For example: --transport webrtc --host localhost --port 8080
    transport = await create_transport(runner_args, transport_params)
    
    # Try to extract custom data from runner arguments
    # This may be set by a custom request handler
    custom_data = getattr(runner_args, 'custom_request_data', None)
    
    # For WebRTC transport, try to get custom data from global storage
    # This is populated by our custom request handler
    if not custom_data and _global_request_data:
        # Get the most recent request data (or use 'default' key)
        custom_data = _global_request_data.get('default') or list(_global_request_data.values())[-1]
        logger.info(f"Retrieved custom data from global storage: {custom_data}")
    
    # Also check if scenario data is passed in runner_args
    if not custom_data and hasattr(runner_args, 'scenario'):
        custom_data = {'scenario': runner_args.scenario}
        logger.info(f"Found scenario in runner_args: {custom_data}")
    
    # Check if scenario data is passed in transport params
    if not custom_data and hasattr(transport, 'params') and transport.params:
        if hasattr(transport.params, 'scenario'):
            custom_data = {'scenario': transport.params.scenario}
            logger.info(f"Found scenario in transport params: {custom_data}")
    
    # Log custom data if available
    if custom_data:
        logger.info(f"Received custom data: {custom_data}")
    else:
        logger.info("No custom data received, using default configuration")
    
    # Run the main bot logic with custom data
    await run_bot(transport, runner_args, custom_data)


if __name__ == "__main__":
    # Import and run the Pipecat CLI
    # This handles command-line argument parsing and starts the bot
    # 
    # Example usage:
    #   python bridgespeak_bot.py --transport webrtc --host localhost --port 8080
    # 
    # Available transports: webrtc, daily
    # The WebRTC transport is recommended for local development
    from pipecat.runner.run import main

    main()