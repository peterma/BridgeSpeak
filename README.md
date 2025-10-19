# BridgeSpeak - AI-Powered Language Learning Platform

An AI-powered educational assistant designed to help Chinese children learning English in Ireland. Features Xiao Mei (小美), a trauma-informed AI companion that provides scenario-based learning experiences for real-world social situations in Irish schools and communities.

## 🎯 Project Purpose

This educational AI assistant helps children from diverse backgrounds, particularly those learning English as a second language, practice important social interactions in a safe, supportive environment. The system uses trauma-informed design principles to create positive learning experiences that build confidence and language skills.

### Key Educational Features
- **Scenario-Based Learning**: Practice real-world situations like introducing yourself, asking for help, or making friends
- **Trauma-Informed Design**: Safe, gentle interactions that respect diverse backgrounds and experiences
- **Cultural Context**: Specifically designed for the Irish school system and social environment
- **Age-Appropriate**: Tailored for primary school children (Junior Infants through 4th Class)
- **Multilingual Support**: Understands the challenges of learning English while maintaining cultural identity

## 🎭 Learning Scenarios

The system includes comprehensive scenarios for common situations children encounter:

### School Scenarios
- **Introducing Yourself**: Meeting new classmates and teachers
- **Asking for Help**: Getting assistance with schoolwork or finding locations
- **Asking for the Toilet**: Essential bathroom permission requests
- **Lunch Time**: Navigating cafeteria interactions and food conversations
- **Playground Games**: Joining activities and making friends during break time
- **Group Work**: Collaborating on class projects and assignments

### Social Scenarios
- **Making Friends**: Starting conversations and building relationships
- **Conflict Resolution**: Handling disagreements respectfully
- **Expressing Feelings**: Communicating emotions and needs appropriately
- **Asking Questions**: Seeking clarification in academic and social contexts
- **Sharing and Taking Turns**: Cooperative play and classroom behavior

### Daily Life Scenarios
- **Shopping**: Basic transactions and polite interactions
- **Public Transport**: Using buses and asking for directions
- **Doctor Visits**: Describing symptoms and understanding instructions
- **Community Events**: Participating in local activities and celebrations

Each scenario includes:
- Age-appropriate vocabulary and phrases
- Cultural context for Irish society
- Interactive practice with Xiao Mei
- Sample sentences and conversation patterns
- Progress tracking and gentle feedback

## 🌟 What This Project Does

The AI assistant creates immersive learning experiences that:
- **Listens** to children's speech in real-time with patience and understanding
- **Responds** with Xiao Mei's gentle, encouraging voice and video presence
- **Adapts** to each child's learning pace and emotional needs
- **Teaches** practical English phrases for real-world situations
- **Visualizes** learning scenarios with AI-generated illustrations that appear automatically during conversations
- **Builds** confidence through positive reinforcement and trauma-informed interactions
- **Supports** cultural diversity while helping integration into Irish society

All interactions happen in real-time with natural conversation flow, enhanced by contextual visual learning aids, making learning feel like talking with a friendly companion rather than a formal lesson.

## ✨ Recent Updates & Improvements

### Latest: Complete Sample Sentences Implementation (v5.0)
- **📚 Sample Sentences Coverage**: 45 out of 60 scenarios now have comprehensive sample sentences with TTS playback
- **🎵 Hybrid TTS System**: Integrated Cartesia and Google TTS with automatic language detection and caching
- **🎨 Dynamic Illustration Generation**: Real-time AI-generated illustrations for each learning scenario using Gemini 2.5 Flash
- **📱 Enhanced UI/UX**: Improved responsive design with trauma-informed animations and child-friendly interactions
- **🔧 FastAPI Backend**: Modular REST API on port 8081 with illustration generation and TTS synthesis endpoints
- **📊 Progress Tracking**: Comprehensive analytics for sample sentence usage and learning progress

### Build System & Styling Overhaul (v4.4)
- **⚡ Vite Migration**: Migrated from Create React App to Vite for faster builds and modern tooling
- **🎨 Tailwind CSS v3**: Upgraded to stable Tailwind CSS v3.4 with full utility class generation
- **📱 Responsive Design**: Comprehensive mobile-first responsive components and utility system
- **🔧 Component Library**: Added responsive grid utilities, responsive text components, and mobile-optimized layouts
- **🛠️ Build Performance**: Significantly faster development server and production builds
- **📐 Design Tokens**: Enhanced design system with proper CSS variable integration

### Frontend UI Polish & Accessibility (v4.3)
- **🎨 Design System**: Complete design system with Button, Card, Input, Chip, and utility components
- **♿ Accessibility**: WCAG AA compliant with proper ARIA labels, semantic HTML, and keyboard navigation
- **🧪 Testing**: Comprehensive test suite with Jest and React Testing Library (21/23 tests passing)
- **🔧 Component Architecture**: Clean, reusable components with proper prop handling and TypeScript-like prop validation
- **📱 Responsive Design**: Mobile-first approach with trauma-informed design principles
- **🎯 User Experience**: Interactive style guide, seamless navigation, and intuitive user flows

### Educational Features & Context Processing
- **Scenario-aware Conversation**: `VideoConversation` reads URL parameters to load specific learning scenarios
- **Educational Context Processor**: Specialized AI processing for age-appropriate, culturally-sensitive responses
- **Age & Variant Filtering**: Scenario content adapts to different age groups and learning levels
- **Dynamic Illustration Generation**: The ConversationPage automatically generates scenario-specific illustrations using AI to enhance visual learning and engagement
- **Interactive Visual Learning**: Real-time image generation provides contextual visual support for each learning scenario
- **Progress Tracking**: Monitor learning goals and conversation improvements over time

### Quality Assurance Improvements
- **✅ Jest Module Resolution**: Fixed react-router-dom mocking and test infrastructure
- **✅ Component Prop Handling**: Resolved React warnings for non-DOM attributes
- **✅ Accessibility Violations**: Fixed duplicate headings, form control associations, and semantic structure
- **✅ Test Coverage**: Improved from initial failures to 91% test pass rate
- **✅ Code Quality**: ESLint compliance and consistent coding standards
- **✅ Tailwind CSS Resolution**: Fixed utility class generation and PostCSS configuration issues

## 🚀 Quick Start

**Get the educational AI assistant running in 5 minutes!** See **[QUICKSTART.md](QUICKSTART.md)** for detailed step-by-step instructions.

```bash
# 1. Install dependencies
uv sync                          # Backend (Python)
cd frontend && npm install       # Frontend (React)

# 2. Configure API keys in .env (repo root)
# Required for AI services:
# GEMINI_API_KEY=your_key_here
# DEEPGRAM_API_KEY=your_key_here
# CARTESIA_API_KEY=your_key_here
# TAVUS_API_KEY=your_key_here
# TAVUS_REPLICA_ID=your_replica_id

# 3. Run servers (3 terminals)
# A) Pipecat media server (RTVI / 8080)
uv run python bridgespeak_bot.py --transport webrtc --host localhost --port 8080
# or to log files as well
uv run python bridgespeak_bot.py --transport webrtc --host localhost --port 8080 2>&1 | tee "logs/pipecat_$(date +%Y%m%d_%H%M%S).log"

# B) FastAPI backend (API / 8081)
uv run uvicorn src.presentation.api.main:app --reload --port 8081

# C) Frontend (Vite / 3000)
cd frontend && npm run dev

# 4. Open browser at http://localhost:3000
# 5. Navigate to /scenarios to choose a learning scenario
# 6. Start practicing with Xiao Mei!
```

👉 **[See QUICKSTART.md for detailed instructions, troubleshooting, and API key setup](QUICKSTART.md)**

## 📁 Project Structure

```
bridgespeak/
├── src/                          # Main application code (Clean Architecture)
│   ├── domain/                   # Business logic and entities
│   ├── application/              # Use cases and educational workflows
│   ├── infrastructure/           # External services, repositories, config
│   └── presentation/             # API and Pipecat server
│       ├── api/                  # FastAPI REST endpoints
│       └── static/               # Generated illustrations and assets
├── docs/                         # Documentation and educational stories
│   ├── stories/                  # Feature stories and acceptance criteria
│   ├── qa/                       # Quality assurance gates and reports
│   ├── prd/                      # Product requirements and specifications
│   └── architecture.md           # System architecture documentation
├── frontend/                     # React web application (Vite + Tailwind)
│   ├── src/
│   │   ├── components/           # Reusable UI components
│   │   │   ├── scenarios/        # Scenario-specific components
│   │   │   └── VideoConversation.js # Main conversation interface
│   │   ├── design-system/        # Design system components and animations
│   │   ├── pages/                # Page components and routing
│   │   │   ├── Home.js           # Landing page
│   │   │   ├── ScenariosPage.js  # Scenario selection and filtering
│   │   │   └── ConversationPage.js # AI conversation interface
│   │   ├── router/               # React Router configuration
│   │   ├── data/                 # Scenario data and transcript management
│   │   ├── services/             # TTS and other service integrations
│   │   └── webrtc-client/        # WebRTC client wrapper
│   ├── public/                   # Static assets and scenario transcripts
│   ├── vite.config.mjs           # Vite configuration
│   ├── tailwind.config.js        # Tailwind CSS configuration
│   ├── postcss.config.js         # PostCSS configuration
│   └── package.json              # Frontend dependencies
├── scripts/                      # Utility scripts and tools
│   └── test_gemini_image.py      # Lists models and generates educational illustrations
├── tests/                        # Unit, integration, e2e tests
├── bridgespeak_bot.py            # Main Pipecat server with educational context
├── pyproject.toml                # Python dependencies (uv)
├── requirements.txt              # Legacy requirements (pip)
└── QUICKSTART.md                 # Detailed setup guide
```

For the full structure and rationale, see `docs/architecture.md`.

## 🔧 How It Works

**Educational AI Pipeline:**

```
Child speaks → 🎤 Deepgram (STT) → 🎓 Educational Context Processor → 🧠 Gemini (LLM) → 🗣️ Cartesia (TTS) → 🎥 Tavus (Xiao Mei) → Gentle AI response
```

**Architecture:**

```
┌──────────────────┐
│  React Frontend  │  ← Parent/child browser interface
│   RTVI Client    │     • Scenario selection
│   Educational UI │     • Sample sentences with TTS
│   Illustration   │     • Progress tracking
└────────┬─────────┘     • Trauma-informed design
         │ WebRTC Connection
         ↓
┌──────────────────┐
│ Python Backend   │  ← Educational AI processing
│  Pipecat Server  │     • Speech-to-Text (Deepgram)
│  (Port 8080)     │     • Educational Context Processor
│                  │     • Scenario-aware prompting
│                  │     • Age-appropriate response generation (Gemini)
│                  │     • Gentle text-to-speech (Cartesia)
│                  │     • Xiao Mei video avatar (Tavus)
└────────┬─────────┘
         │
┌──────────────────┐
│ FastAPI Backend  │  ← REST API services
│  (Port 8081)     │     • Illustration generation (Gemini 2.5 Flash)
│                  │     • TTS synthesis for sample sentences
│                  │     • Static file serving
│                  │     • Health monitoring
└──────────────────┘
```

All processing happens in **real-time** with **trauma-informed** responses, making learning safe and encouraging for children from all backgrounds.

## 🛠️ Technologies

### Backend (Python)
- **Pipecat Framework**: Voice AI pipeline orchestration with educational context
- **Deepgram**: Real-time speech-to-text optimized for children's voices
- **Cartesia**: High-quality, gentle text-to-speech for Xiao Mei
- **Google Gemini**: Educational content generation and age-appropriate responses
- **Tavus**: Xiao Mei AI video avatar with consistent personality
- **WebRTC**: Real-time communication with low latency for natural conversation
- **Educational Context Processor**: Custom logic for trauma-informed, culturally-sensitive responses

Clean Architecture layers implemented in `src/` (Domain, Application, Infrastructure, Presentation). See `docs/architecture.md`.

### Frontend (JavaScript/React)
- **React**: UI framework with hooks and modern patterns
- **Vite**: Next-generation frontend build tool with fast HMR
- **React Router DOM**: Client-side routing and navigation
- **Tailwind CSS v3**: Utility-first CSS framework with full responsive design
- **Pipecat RTVI SDK** (`@pipecat-ai/client-js`): RTVI protocol client
- **Small WebRTC Transport**: Lightweight WebRTC implementation
- **Hybrid TTS System**: Cartesia + Google TTS with automatic language detection
- **Dynamic Illustrations**: Real-time AI-generated images using Gemini 2.5 Flash
- **Design System**: Reusable, accessible UI components with trauma-informed animations
- **Sample Sentences**: Comprehensive transcript system with TTS playback
- **Jest & React Testing Library**: Comprehensive testing framework
- **ESLint**: Code quality and consistency

### Environment & API Keys
- Place keys in `.env` at repo root; backend loads `.env` automatically on startup.
- **Required for basic functionality:**
  - `GEMINI_API_KEY` (preferred) or `GOOGLE_API_KEY` - For educational content generation and illustrations
- **Primary services (with fallbacks):**
  - `DEEPGRAM_API_KEY` - Speech-to-Text optimized for children (falls back to Google STT)
  - `CARTESIA_API_KEY` - Gentle text-to-speech for Xiao Mei (falls back to Google TTS)
  - `TAVUS_API_KEY` + `TAVUS_REPLICA_ID` - Xiao Mei video avatar (falls back to audio-only)
- **Fallback services:**
  - `GOOGLE_APPLICATION_CREDENTIALS_PATH` - Path to Google Cloud service account key file for TTS/STT fallbacks
- **Optional configuration:**
  - `AUDIO_ONLY_DEFAULT=true` - Start in audio-only mode by default
  - `VAD_ENABLED=false` - Disable voice activity detection for faster startup

### Fallback Mechanisms
The system includes robust fallback mechanisms to ensure continuous learning:

1. **TTS Fallback**: Cartesia → Google TTS (when Cartesia credits exhausted)
2. **STT Fallback**: Deepgram → Google STT (when Deepgram credits exhausted)  
3. **Video Fallback**: Tavus Video → Audio-only mode (when Tavus credits exhausted)

All fallbacks maintain the educational and trauma-informed approach, ensuring children always have a positive experience.

## 🎨 Customization

The educational system is designed to be easily customizable:

### Educational Content
- **Scenario Library**: Add new learning scenarios in `frontend/src/data/scenarios.js`
- **Sample Sentences**: Extend transcript system in `frontend/src/data/transcripts/`
- **Age Groups**: Modify age ranges and appropriate content for different classes
- **Cultural Context**: Adapt scenarios for different countries or communities
- **Learning Objectives**: Customize educational goals and progress tracking
- **Illustrations**: Customize AI-generated images via FastAPI endpoints

### Xiao Mei Personality
- **Character Traits**: Edit system prompt in `bridgespeak_bot.py` for Xiao Mei's personality
- **Voice & Tone**: Change Cartesia `voice_id` for different vocal characteristics
- **Response Style**: Adjust trauma-informed response patterns in educational context processor
- **Visual Appearance**: Customize Tavus replica for Xiao Mei's video avatar

### Technical Customization
- **Video Quality**: Adjust resolution settings for different devices
- **LLM Provider**: Swap Gemini for other educational-focused language models
- **TTS Services**: Configure Cartesia and Google TTS fallback chains
- **Illustration Generation**: Customize Gemini 2.5 Flash prompts and safety settings
- **UI Components**: Customize design system components in `frontend/src/design-system/`
- **Responsive Design**: Modify mobile-first layouts for different screen sizes
- **Accessibility**: Enhance ARIA labels and semantic HTML for diverse learners
- **API Endpoints**: Extend FastAPI backend with new educational services

### Design System Components
- **Button**: Primary, secondary, outline, ghost, and danger variants
- **Card**: Interactive cards with headers, bodies, and footers
- **Input**: Form inputs with validation, labels, and error states
- **Chip**: Selectable and removable chips for tags and filters
- **FriendlyLoader**: Child-friendly loading animations with trauma-informed design
- **ResponsiveGrid**: Flexible grid utilities for mobile-first layouts
- **ResponsiveText**: Typography components that scale across breakpoints
- **SkipLink & VisuallyHidden**: Accessibility utilities
- **Animations**: Success celebrations and gentle transitions for positive reinforcement

### Responsive Design Features
- **Mobile-First**: All components designed for mobile devices first
- **Breakpoint System**: Consistent breakpoints (sm: 640px, md: 768px, lg: 1024px, xl: 1280px)
- **Responsive Utilities**: Grid, typography, spacing, and visibility utilities
- **Touch-Friendly**: Optimized for touch interactions on mobile devices
- **Demo Page**: Interactive responsive design showcase at `/responsive-demo`

See [QUICKSTART.md](QUICKSTART.md#next-steps) for detailed customization examples.

## 📚 Learn More

### Educational Resources
- **Architecture Overview**: See `docs/architecture.md` for Clean Architecture design and educational service layers
- **Scenario Library**: See `docs/stories/` for detailed educational scenarios and learning objectives
- **Sample Sentences Analysis**: See `docs/sample-sentences-analysis.md` for comprehensive coverage analysis
- **Quality Assurance**: See `docs/qa/` for QA gates, testing reports, and accessibility compliance
- **Design System**: Explore the interactive style guide at `/style-guide` in the running application
- **Responsive Demo**: Visit `/responsive-demo` to see mobile-first design patterns
- **Baby Steps Implementation**: See `docs/baby-steps-sample-sentences-implementation.md` for trauma-informed development approach

### Development & Testing
- **Run Development Server**: `cd frontend && npm run dev` - Fast Vite development server with HMR
- **Build for Production**: `cd frontend && npm run build` - Optimized production build
- **Preview Production Build**: `cd frontend && npm run preview` - Preview production build locally
- **Run Tests**: `cd frontend && npm test` - Comprehensive test suite with Jest and React Testing Library
- **Test Coverage**: `cd frontend && npm test -- --coverage` - View test coverage reports
- **Linting**: `cd frontend && npm run lint` - ESLint code quality checks (if configured)
- **Accessibility**: Built-in WCAG AA compliance with ARIA labels and semantic HTML

### Troubleshooting

**Frontend Build Issues:**
- If Tailwind styles aren't working: Ensure `tailwind.config.js` exists and `content` paths are correct
- If Vite dev server won't start: Check for port conflicts and try different ports
- If npm commands fail: Try `npm install` to refresh dependencies

**Educational AI Issues:**
- If Xiao Mei doesn't respond: Check API keys in `.env` file
- If scenarios don't load: Verify scenario data files in `frontend/src/data/`
- If audio quality is poor: Check microphone permissions and Deepgram configuration
- If sample sentences don't play: Check TTS service configuration and API keys
- If illustrations don't generate: Verify Gemini API key and check FastAPI backend logs

**Common Solutions:**
```bash
# Reset frontend dependencies
cd frontend && rm -rf node_modules package-lock.json && npm install

# Clear Vite cache
cd frontend && rm -rf .vite

# Verify Tailwind CSS is working
cd frontend && npm run build  # Should show CSS file around 32KB

# Test Gemini image generation for educational illustrations
uv run python scripts/test_gemini_image.py

# Test FastAPI backend endpoints
curl http://localhost:8081/api/v1/health
curl -X POST http://localhost:8081/api/v1/illustrations/generate -H "Content-Type: application/json" -d '{"prompt": "test illustration", "scenario": "test"}'
```

### External Resources
- **[Pipecat Docs](https://docs.pipecat.ai/)** - Framework documentation for voice AI pipelines
- **[Pipecat Examples](https://github.com/pipecat-ai/pipecat-examples)** - More example projects
- **[Pipecat Discord](https://discord.gg/pipecat)** - Community support for voice AI development
- **[Vite Guide](https://vitejs.dev/guide/)** - Vite documentation and best practices
- **[Tailwind CSS Docs](https://tailwindcss.com/docs)** - Tailwind CSS documentation
- **[React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)** - Testing best practices
- **[WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)** - Web accessibility standards

### Educational Development Resources
- **Trauma-Informed Design**: Principles for creating safe learning environments
- **Child-Computer Interaction**: Best practices for designing for young learners
- **Language Learning**: Second language acquisition theories and practices
- **Cultural Sensitivity**: Inclusive design for diverse backgrounds

## 📄 License

See LICENSE file for details.