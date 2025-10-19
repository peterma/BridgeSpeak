# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Backend (Python)
```bash
# Install dependencies (recommended)
uv sync

# Alternative using pip
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .

# Run the bot server
uv run python bridgespeak_bot.py --transport webrtc --host localhost --port 8080
# Run on Ubuntu from WSL
uv run python bridgespeak_bot.py --transport webrtc --host 0.0.0.0 --port 8080

# Lint code (if using dev dependencies)
uv run ruff check .
uv run ruff format .
```

### Frontend (React)
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start

# Build for production
npm run build

# Run tests
npm test
```

### Environment Setup
Copy `env.example` to `.env` and configure required API keys:
- `DEEPGRAM_API_KEY` - Speech-to-text service
- `CARTESIA_API_KEY` - Text-to-speech service  
- `GOOGLE_API_KEY` - Gemini LLM service
- `TAVUS_API_KEY` - Video replica service
- `TAVUS_REPLICA_ID` - Specific replica identifier

## Architecture Overview

This is a real-time conversational AI system with video avatars using the RTVI (Real-Time Voice Interaction) protocol.

### High-Level Flow
```
User Speech → Deepgram STT → Google Gemini LLM → Cartesia TTS → Tavus Video → User Display
```

### Backend Architecture (`bridgespeak_bot.py`)
- **Framework**: Pipecat - orchestrates the voice AI pipeline
- **Transport**: WebRTC with RTVI protocol for client-server coordination  
- **Pipeline Flow**: 
  1. `transport.input()` - receives WebRTC audio/video
  2. `RTVIProcessor` - handles client-ready/bot-ready handshake
  3. `DeepgramSTTService` - converts speech to text
  4. `LLMContextAggregatorPair` - manages conversation context
  5. `GoogleLLMService` - generates responses
  6. `CartesiaTTSService` - converts text to speech
  7. `TavusVideoService` - generates real-time avatar video
  8. `transport.output()` - sends audio/video via WebRTC

### Frontend Architecture
- **Framework**: React with functional components and hooks
- **WebRTC Client**: Custom wrapper (`webrtc-client.js`) around Pipecat RTVI SDK
- **Main Component**: `VideoConversation.js` - handles UI state and media streams
- **RTVI Integration**: Uses `@pipecat-ai/client-js` and `@pipecat-ai/small-webrtc-transport`

### Key Technical Details

**RTVI Protocol**: Ensures proper client-server synchronization via client-ready/bot-ready handshake, preventing dropped first turns and audio glitches.

**Voice Activity Detection**: Uses Silero VAD with 0.2s stop detection for natural conversation flow.

**Video Configuration**: 720p (1280x720) real-time streaming with live avatar generation.

**Audio Processing**: 16kHz input, 24kHz output with echo cancellation and noise suppression.

## Code Patterns

### Backend Customization
- **Bot personality**: Modify system prompt in `bridgespeak_bot.py:135`
- **Voice selection**: Change `voice_id` in CartesiaTTSService initialization  
- **Video quality**: Adjust `video_out_width`/`video_out_height` in transport params
- **LLM provider**: Replace GoogleLLMService with OpenAI, Anthropic, etc.

### Frontend Patterns
- State management uses React hooks (`useState`, `useRef`, `useEffect`)
- WebRTC client is initialized once and managed via refs
- Event-driven architecture with callback registration
- Media stream handling separates local (user) and remote (bot) tracks

### File Organization
```
├── bridgespeak_bot.py           # Main bot server implementation
├── frontend/
│   ├── src/
│   │   ├── webrtc-client.js   # RTVI WebRTC client wrapper
│   │   ├── components/
│   │   │   └── VideoConversation.js  # Main UI component
│   │   └── App.js             # Root component
│   └── package.json           # Frontend dependencies
├── pyproject.toml             # Python dependencies (uv format)
└── requirements.txt           # Legacy pip format
```

## Development Notes

- Always run both backend and frontend servers for full functionality
- Backend must be running on port 8080 before starting frontend
- Browser requires camera/microphone permissions for WebRTC
- Environment variables are required for all external services
- The project uses modern async/await patterns throughout
- WebRTC connections require HTTPS in production (use localhost for development)

### Debug Utilities

**Viewport Debug Mode** - for testing responsive layouts:
```javascript
// Enable debug mode (shows viewport info overlay)
window.debugViewport.enable()  // or add ?debug=true to URL

// Disable debug mode
window.debugViewport.disable()

// Toggle debug mode
window.debugViewport.toggle()
```

When enabled, shows a green overlay with:
- Current viewport dimensions
- Container max-width
- Grid column count
- Active media query information