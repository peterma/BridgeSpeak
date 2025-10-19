import React, { useState, useCallback, useEffect } from 'react';
import AvatarPane from './AvatarPane';
import Controls from './Controls';
import Transcript from './Transcript';
import './ConversationScreen.css';

// Mock messages for demonstration
const MOCK_MESSAGES = [
  {
    id: 1,
    role: 'system',
    content: 'Conversation started. Xiao Mei is ready to help you practice English!',
    timestamp: Date.now() - 60000,
    language: 'en'
  },
  {
    id: 2,
    role: 'assistant',
    content: '你好! Hello! I am Xiao Mei. 我很高兴见到你! I am very happy to meet you!',
    timestamp: Date.now() - 45000,
    language: 'mixed'
  },
  {
    id: 3,
    role: 'user',
    content: 'Hello Xiao Mei, nice to meet you too!',
    timestamp: Date.now() - 30000,
    language: 'en'
  },
  {
    id: 4,
    role: 'assistant',
    content: 'Wonderful! 太棒了! Your English is very good. What would you like to practice today?',
    timestamp: Date.now() - 15000,
    language: 'mixed'
  }
];

function ConversationScreen() {
  // State management for conversation
  const [isActive, setIsActive] = useState(false);
  const [isMicEnabled, setIsMicEnabled] = useState(true);
  const [connectionState, setConnectionState] = useState('disconnected'); // 'disconnected' | 'connecting' | 'connected'
  const [messages, setMessages] = useState([]);
  const [sessionStartTime, setSessionStartTime] = useState(null);

  // Keyboard event handler for global shortcuts
  useEffect(() => {
    const handleKeyDown = (event) => {
      // Space bar to start/stop when not focused on a button
      if (event.code === 'Space' && !event.target.matches('button, input, textarea')) {
        event.preventDefault();
        if (isActive) {
          handleStop();
        } else {
          handleStart();
        }
      }
      
      // M key to toggle microphone when active
      if (event.code === 'KeyM' && isActive && !event.target.matches('input, textarea')) {
        event.preventDefault();
        handleMicToggle();
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [isActive]); // eslint-disable-line react-hooks/exhaustive-deps

  const handleStart = useCallback(async () => {
    if (connectionState === 'connecting') return;
    
    setConnectionState('connecting');
    setSessionStartTime(Date.now());
    
    // Simulate connection delay
    setTimeout(() => {
      setConnectionState('connected');
      setIsActive(true);
      setIsMicEnabled(true);
      
      // Add mock messages after starting
      setMessages(MOCK_MESSAGES);
    }, 1500);
  }, [connectionState]);

  const handleStop = useCallback(() => {
    setIsActive(false);
    setConnectionState('disconnected');
    setIsMicEnabled(false);
    
    // Add session end message
    if (messages.length > 0) {
      const sessionDuration = sessionStartTime ? 
        Math.round((Date.now() - sessionStartTime) / 1000) : 0;
      
      setMessages(prev => [...prev, {
        id: Date.now(),
        role: 'system',
        content: `Conversation ended. Session duration: ${sessionDuration} seconds.`,
        timestamp: Date.now(),
        language: 'en'
      }]);
    }
  }, [messages.length, sessionStartTime]);

  const handleMicToggle = useCallback(() => {
    if (!isActive) return;
    
    const newMicState = !isMicEnabled;
    setIsMicEnabled(newMicState);
    
    // Add system message about mic state
    setMessages(prev => [...prev, {
      id: Date.now(),
      role: 'system',
      content: `Microphone ${newMicState ? 'enabled' : 'disabled'}.`,
      timestamp: Date.now(),
      language: 'en'
    }]);
  }, [isActive, isMicEnabled]);

  const handleClearTranscript = useCallback(() => {
    setMessages([]);
  }, []);

  return (
    <div className="conversation-screen">
      {/* Screen reader announcements for major state changes */}
      <div className="sr-only" aria-live="assertive" aria-atomic="true">
        {connectionState === 'connecting' && 'Connecting to Xiao Mei...'}
        {connectionState === 'connected' && isActive && 'Connected! Conversation started.'}
        {connectionState === 'disconnected' && !isActive && 'Conversation ended.'}
      </div>
      
      {/* Main conversation layout */}
      <div className="conversation-layout">
        <div className="avatar-section">
          <AvatarPane 
            isActive={isActive}
            connectionState={connectionState}
          />
        </div>
        
        <div className="interaction-section">
          <div className="controls-section">
            <Controls
              isActive={isActive}
              onStart={handleStart}
              onStop={handleStop}
              isMicEnabled={isMicEnabled}
              onMicToggle={handleMicToggle}
              connectionState={connectionState}
            />
          </div>
          
          <div className="transcript-section">
            <Transcript
              messages={messages}
              isActive={isActive}
              onClear={handleClearTranscript}
            />
          </div>
        </div>
      </div>
      
      {/* Keyboard shortcuts help */}
      <div className="keyboard-shortcuts" role="complementary" aria-label="Keyboard shortcuts">
        <details className="shortcuts-details">
          <summary className="shortcuts-summary">Keyboard Shortcuts</summary>
          <dl className="shortcuts-list">
            <dt>Spacebar</dt>
            <dd>Start or stop conversation</dd>
            <dt>M</dt>
            <dd>Toggle microphone (when active)</dd>
            <dt>Tab</dt>
            <dd>Navigate between controls</dd>
          </dl>
        </details>
      </div>
    </div>
  );
}

export default ConversationScreen;