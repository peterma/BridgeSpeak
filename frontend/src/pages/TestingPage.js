/**
 * Testing Page - Fundamental Features Testing
 * 
 * This page provides isolated testing for core functionality:
 * - Speech-to-Text (STT) testing
 * - Text-to-Speech (TTS) testing  
 * - WebRTC connection testing
 * - Microphone access testing
 * - Audio pipeline testing
 */

import React, { useState, useRef, useEffect } from 'react';
import { Button, Card, Input, Chip } from '../design-system';
import ScenarioTester from '../components/ScenarioTester';
import './TestingPage.css';

function TestingPage() {
  // STT Testing State
  const [isListening, setIsListening] = useState(false);
  const [transcript, setTranscript] = useState('');
  const [sttSupported, setSttSupported] = useState(false);
  const [sttError, setSttError] = useState('');
  
  // TTS Testing State
  const [ttsText, setTtsText] = useState('Hello! This is a test of text-to-speech functionality.');
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [ttsSupported, setTtsSupported] = useState(false);
  const [selectedVoice, setSelectedVoice] = useState(null);
  const [availableVoices, setAvailableVoices] = useState([]);
  
  // Microphone Testing State
  const [micPermission, setMicPermission] = useState('unknown'); // 'granted', 'denied', 'prompt', 'unknown'
  const [micStream, setMicStream] = useState(null);
  const [audioLevel, setAudioLevel] = useState(0);
  
  // WebRTC Testing State
  const [webrtcSupported, setWebrtcSupported] = useState(false);
  const [connectionStatus, setConnectionStatus] = useState('disconnected');
  const [connectionError, setConnectionError] = useState('');
  
  // Audio Pipeline Testing State
  const [pipelineStatus, setPipelineStatus] = useState('idle');
  const [pipelineError, setPipelineError] = useState('');
  const [pipelineLogs, setPipelineLogs] = useState([]);
  const [testWebRTCClient, setTestWebRTCClient] = useState(null);
  
  // Audio Analysis
  const audioContextRef = useRef(null);
  const analyserRef = useRef(null);
  const micTestRef = useRef(null);
  const recognitionRef = useRef(null);

  // Initialize testing environment
  useEffect(() => {
    checkBrowserSupport();
    loadVoices();
    
    // Clean up on unmount
    return () => {
      stopMicTest();
      if (recognitionRef.current) {
        recognitionRef.current.stop();
      }
      if (testWebRTCClient) {
        testWebRTCClient.disconnect();
      }
    };
  }, []);

  const checkBrowserSupport = () => {
    // Check STT support
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    setSttSupported(!!SpeechRecognition);
    
    // Check TTS support
    setTtsSupported('speechSynthesis' in window);
    
    // Check WebRTC support
    const hasWebRTC = !!(window.RTCPeerConnection || window.mozRTCPeerConnection || window.webkitRTCPeerConnection);
    const hasGetUserMedia = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
    setWebrtcSupported(hasWebRTC && hasGetUserMedia);
    
    console.log('Browser support check:', {
      stt: !!SpeechRecognition,
      tts: 'speechSynthesis' in window,
      webrtc: hasWebRTC && hasGetUserMedia
    });
  };

  const loadVoices = () => {
    if ('speechSynthesis' in window) {
      const updateVoices = () => {
        const voices = speechSynthesis.getVoices();
        setAvailableVoices(voices);
        
        // Find a good default voice (prefer English)
        const englishVoice = voices.find(v => v.lang.startsWith('en'));
        if (englishVoice) {
          setSelectedVoice(englishVoice);
        } else if (voices.length > 0) {
          setSelectedVoice(voices[0]);
        }
      };
      
      updateVoices();
      speechSynthesis.onvoiceschanged = updateVoices;
    }
  };

  // STT Testing Functions
  const startSTTTest = () => {
    if (!sttSupported) {
      setSttError('Speech recognition not supported in this browser');
      return;
    }

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'en-US';
    
    recognition.onstart = () => {
      setIsListening(true);
      setSttError('');
      setTranscript('');
      console.log('STT: Started listening');
    };
    
    recognition.onresult = (event) => {
      let finalTranscript = '';
      let interimTranscript = '';
      
      for (let i = event.resultIndex; i < event.results.length; i++) {
        const transcript = event.results[i][0].transcript;
        if (event.results[i].isFinal) {
          finalTranscript += transcript;
        } else {
          interimTranscript += transcript;
        }
      }
      
      setTranscript(finalTranscript + interimTranscript);
      console.log('STT result:', { final: finalTranscript, interim: interimTranscript });
    };
    
    recognition.onerror = (event) => {
      setSttError(`Speech recognition error: ${event.error}`);
      setIsListening(false);
      console.error('STT error:', event);
    };
    
    recognition.onend = () => {
      setIsListening(false);
      console.log('STT: Stopped listening');
    };
    
    recognitionRef.current = recognition;
    recognition.start();
  };

  const stopSTTTest = () => {
    if (recognitionRef.current) {
      recognitionRef.current.stop();
    }
    setIsListening(false);
  };

  // TTS Testing Functions
  const startTTSTest = () => {
    if (!ttsSupported) {
      alert('Text-to-speech not supported in this browser');
      return;
    }

    if (speechSynthesis.speaking) {
      speechSynthesis.cancel();
    }

    const utterance = new SpeechSynthesisUtterance(ttsText);
    
    if (selectedVoice) {
      utterance.voice = selectedVoice;
    }
    
    utterance.rate = 0.9;
    utterance.pitch = 1.0;
    utterance.volume = 1.0;
    
    utterance.onstart = () => {
      setIsSpeaking(true);
      console.log('TTS: Started speaking');
    };
    
    utterance.onend = () => {
      setIsSpeaking(false);
      console.log('TTS: Finished speaking');
    };
    
    utterance.onerror = (event) => {
      setIsSpeaking(false);
      console.error('TTS error:', event);
      alert(`TTS error: ${event.error}`);
    };
    
    speechSynthesis.speak(utterance);
  };

  const stopTTSTest = () => {
    speechSynthesis.cancel();
    setIsSpeaking(false);
  };

  // Microphone Testing Functions
  const startMicTest = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ 
        audio: {
          echoCancellation: true,
          noiseSuppression: true,
          autoGainControl: true
        } 
      });
      
      setMicStream(stream);
      setMicPermission('granted');
      
      // Set up audio analysis
      audioContextRef.current = new (window.AudioContext || window.webkitAudioContext)();
      analyserRef.current = audioContextRef.current.createAnalyser();
      const source = audioContextRef.current.createMediaStreamSource(stream);
      source.connect(analyserRef.current);
      
      analyserRef.current.fftSize = 256;
      const bufferLength = analyserRef.current.frequencyBinCount;
      const dataArray = new Uint8Array(bufferLength);
      
      const updateAudioLevel = () => {
        if (analyserRef.current) {
          analyserRef.current.getByteFrequencyData(dataArray);
          const average = dataArray.reduce((sum, value) => sum + value, 0) / bufferLength;
          setAudioLevel(average);
          micTestRef.current = requestAnimationFrame(updateAudioLevel);
        }
      };
      
      updateAudioLevel();
      console.log('Microphone test started successfully');
      
    } catch (error) {
      console.error('Microphone access error:', error);
      setMicPermission('denied');
      alert(`Microphone access denied: ${error.message}`);
    }
  };

  const stopMicTest = () => {
    if (micStream) {
      micStream.getTracks().forEach(track => track.stop());
      setMicStream(null);
    }
    
    if (audioContextRef.current) {
      audioContextRef.current.close();
      audioContextRef.current = null;
    }
    
    if (micTestRef.current) {
      cancelAnimationFrame(micTestRef.current);
      micTestRef.current = null;
    }
    
    setAudioLevel(0);
    console.log('Microphone test stopped');
  };

  // WebRTC Connection Test
  const testWebRTCConnection = async () => {
    if (!webrtcSupported) {
      alert('WebRTC not supported in this browser');
      return;
    }

    setConnectionStatus('connecting');
    setConnectionError('');
    
    try {
      // First, test if the server is running with a simple health check
      const healthResponse = await fetch('http://localhost:8081/', {
        method: 'GET',
      });
      
      if (!healthResponse.ok) {
        throw new Error(`Backend server not responding (${healthResponse.status})`);
      }
      
      // If server is running, test WebRTC endpoint with proper offer
      const pc = new RTCPeerConnection();
      const offer = await pc.createOffer();
      
      const webrtcResponse = await fetch('http://localhost:8081/api/offer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          type: 'offer',
          sdp: offer.sdp
        })
      });
      
      // Clean up the test peer connection
      pc.close();
      
      if (webrtcResponse.ok) {
        setConnectionStatus('connected');
        console.log('WebRTC backend connection test successful');
        setTimeout(() => setConnectionStatus('disconnected'), 3000);
      } else {
        const errorText = await webrtcResponse.text();
        throw new Error(`WebRTC endpoint error (${webrtcResponse.status}): ${errorText}`);
      }
    } catch (error) {
      console.error('WebRTC connection test failed:', error);
      setConnectionStatus('failed');
      
      // Store error details for display
      const errorMessage = error.message;
      if (errorMessage.includes('Failed to fetch')) {
        setConnectionError('Backend server appears to be offline. Please start the Pipecat server.');
      } else if (errorMessage.includes('422')) {
        setConnectionError('Backend server is running but WebRTC endpoint configuration issue. Check API keys and dependencies.');
      } else {
        setConnectionError(errorMessage);
      }
      
      setTimeout(() => {
        setConnectionStatus('disconnected');
        setConnectionError('');
      }, 8000);
    }
  };

  // Audio Pipeline Testing Functions
  const testAudioPipeline = async () => {
    setPipelineStatus('connecting');
    setPipelineError('');
    setPipelineLogs([]);
    
    const addLog = (message) => {
      setPipelineLogs(prev => [...prev, `${new Date().toLocaleTimeString()}: ${message}`]);
    };

    try {
      addLog('Starting audio pipeline test...');
      
      // Import WebRTC client dynamically
      const { WebRTCClient } = await import('../webrtc-client');
      const client = new WebRTCClient('http://localhost:8081');
      setTestWebRTCClient(client);
      
      addLog('WebRTC client created');
      
      // Set up event listeners
      client.on('connected', () => {
        addLog('✅ WebRTC connected successfully');
        setPipelineStatus('connected');
      });
      
      client.on('botReady', () => {
        addLog('✅ Bot ready - AI should start speaking');
        // Keep connection alive for 10 seconds to hear the AI speak
        setTimeout(() => {
          addLog('⏰ Test complete - disconnecting');
          stopAudioPipelineTest();
        }, 10000);
      });
      
      client.on('track', (stream) => {
        addLog('✅ Received audio/video track from bot');
        // Test if we can play the audio
        const audio = new Audio();
        audio.srcObject = stream;
        audio.play().then(() => {
          addLog('✅ Audio playback started');
        }).catch(err => {
          addLog(`❌ Audio playback failed: ${err.message}`);
        });
      });
      
      client.on('error', (err) => {
        addLog(`❌ WebRTC error: ${err.message}`);
        setPipelineError(err.message);
        setPipelineStatus('error');
      });
      
      client.on('connectionStateChange', (state) => {
        addLog(`Connection state: ${state}`);
        if (state === 'failed' || state === 'disconnected') {
          setPipelineStatus('error');
        }
      });
      
      addLog('Connecting to Pipecat server...');
      await client.connect({ 
        scenario: 'intro-yourself',
        enableCam: false // Audio-only test
      });
      
    } catch (error) {
      addLog(`❌ Pipeline test failed: ${error.message}`);
      setPipelineError(error.message);
      setPipelineStatus('error');
    }
  };

  const stopAudioPipelineTest = () => {
    if (testWebRTCClient) {
      testWebRTCClient.disconnect();
      setTestWebRTCClient(null);
    }
    setPipelineStatus('idle');
    setPipelineLogs([]);
  };

  return (
    <div className="min-h-screen px-4 sm:px-6 lg:px-8 py-6 max-w-7xl mx-auto">
      <div className="text-center mb-8 lg:mb-12">
        <div className="max-w-4xl mx-auto">
          <h1 className="page-title">Feature Testing Laboratory</h1>
          <p className="page-description">
            Test and validate core functionality: speech recognition, text-to-speech, and audio pipeline
          </p>
        </div>
      </div>

      <div className="testing-grid">
        {/* Browser Support Overview */}
        <Card className="support-overview">
          <Card.Header>
            <Card.Title level={2}>Browser Support Status</Card.Title>
          </Card.Header>
          <Card.Body>
            <div className="support-items">
              <div className="support-item">
                <Chip variant={sttSupported ? 'success' : 'error'}>
                  {sttSupported ? '✅' : '❌'} Speech-to-Text
                </Chip>
              </div>
              <div className="support-item">
                <Chip variant={ttsSupported ? 'success' : 'error'}>
                  {ttsSupported ? '✅' : '❌'} Text-to-Speech
                </Chip>
              </div>
              <div className="support-item">
                <Chip variant={webrtcSupported ? 'success' : 'error'}>
                  {webrtcSupported ? '✅' : '❌'} WebRTC
                </Chip>
              </div>
              <div className="support-item">
                <Chip variant={micPermission === 'granted' ? 'success' : micPermission === 'denied' ? 'error' : 'warning'}>
                  {micPermission === 'granted' ? '✅' : micPermission === 'denied' ? '❌' : '❓'} Microphone
                </Chip>
              </div>
            </div>
          </Card.Body>
        </Card>

        {/* Speech-to-Text Testing */}
        <Card className="stt-testing">
          <Card.Header>
            <Card.Title level={2}>Speech-to-Text Testing</Card.Title>
            <Card.Subtitle>Test browser-based speech recognition</Card.Subtitle>
          </Card.Header>
          <Card.Body>
            <div className="test-controls">
              <Button 
                variant={isListening ? 'danger' : 'primary'}
                onClick={isListening ? stopSTTTest : startSTTTest}
                disabled={!sttSupported}
                leftIcon={isListening ? '⏹️' : '🎤'}
              >
                {isListening ? 'Stop Listening' : 'Start Speech Recognition'}
              </Button>
            </div>
            
            {sttError && (
              <div className="error-message">
                <strong>Error:</strong> {sttError}
              </div>
            )}
            
            <div className="transcript-area">
              <label htmlFor="stt-transcript">Live Transcript:</label>
              <textarea
                id="stt-transcript"
                value={transcript}
                readOnly
                placeholder={isListening ? "Speak now... your words will appear here" : "Click 'Start Speech Recognition' and speak"}
                className="transcript-output"
              />
            </div>
            
            <div className="stt-status">
              <Chip variant={isListening ? 'info' : 'default'}>
                {isListening ? '🔴 LISTENING' : '⚫ IDLE'}
              </Chip>
            </div>
          </Card.Body>
        </Card>

        {/* Text-to-Speech Testing */}
        <Card className="tts-testing">
          <Card.Header>
            <Card.Title level={2}>Text-to-Speech Testing</Card.Title>
            <Card.Subtitle>Test browser-based speech synthesis</Card.Subtitle>
          </Card.Header>
          <Card.Body>
            <div className="tts-controls">
              <Input
                label="Text to Speak"
                value={ttsText}
                onChange={(e) => setTtsText(e.target.value)}
                placeholder="Enter text to convert to speech..."
              />
              
              {availableVoices.length > 0 && (
                <div className="voice-selector">
                  <label htmlFor="voice-select">Select Voice:</label>
                  <select
                    id="voice-select"
                    value={selectedVoice?.name || ''}
                    onChange={(e) => {
                      const voice = availableVoices.find(v => v.name === e.target.value);
                      setSelectedVoice(voice);
                    }}
                  >
                    {availableVoices.map((voice) => (
                      <option key={voice.name} value={voice.name}>
                        {voice.name} ({voice.lang})
                      </option>
                    ))}
                  </select>
                </div>
              )}
              
              <div className="tts-buttons">
                <Button 
                  variant="primary"
                  onClick={startTTSTest}
                  disabled={!ttsSupported || !ttsText.trim()}
                  leftIcon="🔊"
                >
                  Speak Text
                </Button>
                
                <Button 
                  variant="secondary"
                  onClick={stopTTSTest}
                  disabled={!isSpeaking}
                  leftIcon="⏹️"
                >
                  Stop Speaking
                </Button>
              </div>
            </div>
            
            <div className="tts-status">
              <Chip variant={isSpeaking ? 'info' : 'default'}>
                {isSpeaking ? '🔊 SPEAKING' : '🔇 SILENT'}
              </Chip>
            </div>
          </Card.Body>
        </Card>

        {/* Microphone Testing */}
        <Card className="mic-testing">
          <Card.Header>
            <Card.Title level={2}>Microphone Testing</Card.Title>
            <Card.Subtitle>Test microphone access and audio levels</Card.Subtitle>
          </Card.Header>
          <Card.Body>
            <div className="mic-controls">
              <Button 
                variant={micStream ? 'danger' : 'primary'}
                onClick={micStream ? stopMicTest : startMicTest}
                leftIcon={micStream ? '🔇' : '🎤'}
              >
                {micStream ? 'Stop Mic Test' : 'Test Microphone'}
              </Button>
            </div>
            
            <div className="audio-level">
              <label>Audio Level:</label>
              <div className="level-meter">
                <div 
                  className="level-bar"
                  style={{ width: `${(audioLevel / 255) * 100}%` }}
                />
              </div>
              <span className="level-value">{Math.round((audioLevel / 255) * 100)}%</span>
            </div>
            
            <div className="mic-status">
              <Chip variant={micStream ? 'success' : micPermission === 'denied' ? 'error' : 'default'}>
                {micStream ? '✅ ACTIVE' : micPermission === 'denied' ? '❌ DENIED' : '⚫ INACTIVE'}
              </Chip>
            </div>
          </Card.Body>
        </Card>

        {/* WebRTC Connection Testing */}
        <Card className="webrtc-testing">
          <Card.Header>
            <Card.Title level={2}>WebRTC Backend Connection</Card.Title>
            <Card.Subtitle>Test connection to Pipecat server</Card.Subtitle>
          </Card.Header>
          <Card.Body>
            <div className="webrtc-controls">
              <Button 
                variant="primary"
                onClick={testWebRTCConnection}
                disabled={!webrtcSupported || connectionStatus === 'connecting'}
                leftIcon="🌐"
                loading={connectionStatus === 'connecting'}
              >
                Test Backend Connection
              </Button>
            </div>
            
            <div className="connection-info">
              <p><strong>Backend URL:</strong> http://localhost:8081</p>
              <p><strong>Endpoint:</strong> /api/offer</p>
            </div>
            
            {connectionError && (
              <div className="error-message">
                <strong>Connection Error:</strong> {connectionError}
              </div>
            )}
            
            <div className="connection-status">
              <Chip variant={
                connectionStatus === 'connected' ? 'success' : 
                connectionStatus === 'connecting' ? 'info' : 
                connectionStatus === 'failed' ? 'error' : 'default'
              }>
                {connectionStatus === 'connected' ? '✅ CONNECTED' : 
                 connectionStatus === 'connecting' ? '🔄 CONNECTING' : 
                 connectionStatus === 'failed' ? '❌ FAILED' : '⚫ DISCONNECTED'}
              </Chip>
            </div>
          </Card.Body>
        </Card>

        {/* Audio Pipeline Testing */}
        <Card className="pipeline-testing">
          <Card.Header>
            <Card.Title level={2}>Audio Pipeline Testing</Card.Title>
            <Card.Subtitle>Test full audio pipeline: STT → LLM → TTS → WebRTC</Card.Subtitle>
          </Card.Header>
          <Card.Body>
            <div className="pipeline-controls">
              <Button 
                variant={pipelineStatus === 'idle' ? 'primary' : 'danger'}
                onClick={pipelineStatus === 'idle' ? testAudioPipeline : stopAudioPipelineTest}
                leftIcon={pipelineStatus === 'idle' ? '🎵' : '⏹️'}
                loading={pipelineStatus === 'connecting'}
              >
                {pipelineStatus === 'idle' ? 'Test Audio Pipeline' : 'Stop Pipeline Test'}
              </Button>
            </div>
            
            <div className="pipeline-info">
              <p><strong>Test Mode:</strong> Audio-only (no video)</p>
              <p><strong>Scenario:</strong> intro-yourself</p>
              <p><strong>Expected:</strong> AI teacher should greet you and ask about favorite colors</p>
            </div>
            
            {pipelineError && (
              <div className="error-message">
                <strong>Pipeline Error:</strong> {pipelineError}
              </div>
            )}
            
            <div className="pipeline-status">
              <Chip variant={
                pipelineStatus === 'connected' ? 'success' : 
                pipelineStatus === 'connecting' ? 'info' : 
                pipelineStatus === 'error' ? 'error' : 'default'
              }>
                {pipelineStatus === 'connected' ? '✅ CONNECTED' : 
                 pipelineStatus === 'connecting' ? '🔄 CONNECTING' : 
                 pipelineStatus === 'error' ? '❌ ERROR' : '⚫ IDLE'}
              </Chip>
            </div>
            
            {pipelineLogs.length > 0 && (
              <div className="pipeline-logs">
                <label>Pipeline Logs:</label>
                <div className="logs-container">
                  {pipelineLogs.map((log, index) => (
                    <div key={index} className="log-entry">
                      {log}
                    </div>
                  ))}
                </div>
              </div>
            )}
          </Card.Body>
        </Card>

        {/* Troubleshooting Tips */}
        <Card className="troubleshooting">
          <Card.Header>
            <Card.Title level={2}>Troubleshooting Guide</Card.Title>
          </Card.Header>
          <Card.Body>
            <div className="troubleshooting-tips">
              <h4>Common Issues:</h4>
              <ul>
                <li><strong>STT not working:</strong> Ensure microphone permission is granted and you're using Chrome/Edge</li>
                <li><strong>TTS not working:</strong> Check browser compatibility (Chrome, Firefox, Safari supported)</li>
                <li><strong>Microphone access denied:</strong> Click the microphone icon in address bar to grant permission</li>
                <li><strong>Backend connection failed:</strong> Ensure Pipecat server is running on localhost:8081</li>
                <li><strong>422 Unprocessable Entity error:</strong> Backend server is running but missing dependencies (daily module) or API keys</li>
                <li><strong>Audio levels not showing:</strong> Speak closer to microphone or check system audio settings</li>
              </ul>
              
              <h4>Required for full functionality:</h4>
              <ul>
                <li>Backend server running with required API keys (Deepgram, Cartesia, etc.)</li>
                <li>HTTPS in production (HTTP only works on localhost)</li>
                <li>Modern browser (Chrome 80+, Firefox 75+, Safari 14+)</li>
              </ul>
            </div>
          </Card.Body>
        </Card>

        {/* Scenario Testing Section */}
        <Card className="testing-card">
          <Card.Header>
            <h2>Scenario Testing</h2>
            <p>Test all conversation scenarios to ensure they work correctly</p>
          </Card.Header>
          <Card.Body>
            <ScenarioTester />
          </Card.Body>
        </Card>
      </div>
    </div>
  );
}

export default TestingPage;