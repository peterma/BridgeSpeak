import React, { useEffect, useRef, useState } from 'react';
import hybridTTS from '../../services/hybridTTS';
import './Transcript.css';

function Transcript({ messages, isActive, isSampleTranscript = false }) {
  const transcriptEndRef = useRef(null);
  const transcriptListRef = useRef(null);
  const [speakingMessageId, setSpeakingMessageId] = useState(null);
  const [ttsStatus, setTtsStatus] = useState(null);

  // Initialize TTS service
  useEffect(() => {
    setTtsStatus(hybridTTS.getStatus());
  }, []);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    if (transcriptEndRef.current && transcriptEndRef.current.scrollIntoView) {
      transcriptEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

  const formatTime = (timestamp) => {
    const date = new Date(timestamp);
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  const getRoleLabel = (role) => {
    switch (role) {
      case 'user':
        return 'You';
      case 'assistant':
        return 'Xiao Mei';
      case 'system':
        return 'System';
      default:
        return role;
    }
  };

  const getRoleClass = (role) => {
    switch (role) {
      case 'user':
        return 'user-message';
      case 'assistant':
        return 'assistant-message';
      case 'system':
        return 'system-message';
      default:
        return 'unknown-message';
    }
  };

  const handlePlayMessage = async (message, messageId) => {
    if (!ttsStatus || (!ttsStatus.cartesiaAvailable && !ttsStatus.webSpeechAvailable)) {
      console.warn('No TTS service available');
      return;
    }

    // Stop any currently speaking message
    if (speakingMessageId) {
      await hybridTTS.stop();
      setSpeakingMessageId(null);
    }

    // If clicking the same message, just stop
    if (speakingMessageId === messageId) {
      setSpeakingMessageId(null);
      return;
    }

    try {
      // Set speaking state
      setSpeakingMessageId(messageId);
      
      // Determine language
      const language = message.language || 'en-IE';
      
      // Speak using hybrid TTS service
      await hybridTTS.speak(message.content, language);
      
      // Clear speaking state
      setSpeakingMessageId(null);
    } catch (error) {
      console.error('TTS error:', error);
      setSpeakingMessageId(null);
    }
  };

  const isMessageSpeaking = (messageId) => {
    return speakingMessageId === messageId;
  };

  return (
    <div className="transcript-panel" role="region" aria-label="Conversation Transcript">
      <div className="transcript-header">
        <h3 className="transcript-title">Conversation</h3>
        <div className="transcript-status">
          <span className={`status-badge ${isActive ? 'active' : 'inactive'}`}>
            {isActive ? 'Recording' : 'Stopped'}
          </span>
          {isSampleTranscript && ttsStatus && (
            <span className="tts-status-badge" title={`TTS: ${ttsStatus.availableServices.join(', ')}`}>
              🔊 {ttsStatus.cartesiaAvailable ? 'Cartesia' : 'Web Speech'}
            </span>
          )}
        </div>
      </div>
      
      <div className="transcript-content">
        {messages.length === 0 ? (
          <div className="empty-transcript" role="status">
            <p className="empty-message">
              {isActive 
                ? 'Your conversation will appear here...' 
                : 'Start a conversation to see the transcript'
              }
            </p>
          </div>
        ) : (
          <ul 
            className="message-list" 
            role="log" 
            aria-label="Conversation messages"
            aria-live="polite"
            aria-relevant="additions"
            ref={transcriptListRef}
          >
            {messages.map((message, index) => (
              <li 
                key={`${message.id || index}-${message.timestamp}`}
                className={`message-item ${getRoleClass(message.role)}`}
              >
                <div className="message-header">
                  <span className="message-role" aria-label={`Message from ${getRoleLabel(message.role)}`}>
                    {getRoleLabel(message.role)}
                  </span>
                  <time 
                    className="message-time" 
                    dateTime={new Date(message.timestamp).toISOString()}
                    aria-label={`at ${formatTime(message.timestamp)}`}
                  >
                    {formatTime(message.timestamp)}
                  </time>
                </div>
                <div className="message-content">
                  {message.content}
                </div>
                {isSampleTranscript && (
                  <div className="message-actions">
                    <button
                      className={`play-button ${isMessageSpeaking(message.id || index) ? 'playing' : ''}`}
                      onClick={() => handlePlayMessage(message, message.id || index)}
                      aria-label={`${isMessageSpeaking(message.id || index) ? 'Stop' : 'Play'} message: ${message.content.substring(0, 50)}...`}
                      title={isMessageSpeaking(message.id || index) ? 'Stop playback' : 'Play message'}
                    >
                      {isMessageSpeaking(message.id || index) ? (
                        <span className="play-icon">⏸️</span>
                      ) : (
                        <span className="play-icon">🔊</span>
                      )}
                    </button>
                  </div>
                )}
                {message.language && message.language !== 'en' && (
                  <div className="message-language" aria-label={`Language: ${message.language}`}>
                    <span className="language-tag">{message.language}</span>
                  </div>
                )}
              </li>
            ))}
            <div ref={transcriptEndRef} aria-hidden="true" />
          </ul>
        )}
      </div>
      
      <div className="transcript-footer">
        <button 
          className="clear-transcript-button"
          onClick={() => {/* TODO: Implement clear functionality */}}
          disabled={messages.length === 0}
          aria-label="Clear conversation transcript"
        >
          Clear Transcript
        </button>
      </div>
      
      {/* Screen reader announcements */}
      <div className="sr-only" aria-live="polite" aria-atomic="false">
        {messages.length > 0 && `${messages.length} messages in conversation`}
      </div>
    </div>
  );
}

export default Transcript;