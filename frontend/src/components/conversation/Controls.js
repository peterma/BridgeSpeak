import React from 'react';
import './Controls.css';

function Controls({ 
  isActive, 
  onStart, 
  onStop, 
  isMicEnabled, 
  onMicToggle,
  connectionState 
}) {
  const handleKeyDown = (event, action) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      action();
    }
  };

  return (
    <div className="controls-panel" role="region" aria-label="Conversation Controls">
      <div className="main-controls">
        {!isActive ? (
          <button
            className="control-button primary start-button"
            onClick={onStart}
            onKeyDown={(e) => handleKeyDown(e, onStart)}
            disabled={connectionState === 'connecting'}
            aria-describedby="start-button-help"
          >
            <span className="button-icon" aria-hidden="true">▶️</span>
            <span className="button-text">
              {connectionState === 'connecting' ? 'Connecting...' : 'Start Conversation'}
            </span>
          </button>
        ) : (
          <button
            className="control-button secondary stop-button"
            onClick={onStop}
            onKeyDown={(e) => handleKeyDown(e, onStop)}
            aria-describedby="stop-button-help"
          >
            <span className="button-icon" aria-hidden="true">⏹️</span>
            <span className="button-text">Stop Conversation</span>
          </button>
        )}
        
        <button
          className={`control-button ${isMicEnabled ? 'mic-on' : 'mic-off'}`}
          onClick={onMicToggle}
          onKeyDown={(e) => handleKeyDown(e, onMicToggle)}
          disabled={!isActive}
          aria-label={`Microphone is ${isMicEnabled ? 'on' : 'off'}`}
          aria-describedby="mic-button-help"
        >
          <span className="button-icon" aria-hidden="true">
            {isMicEnabled ? '🎤' : '🔇'}
          </span>
          <span className="button-text">
            {isMicEnabled ? 'Mic On' : 'Mic Off'}
          </span>
        </button>
      </div>
      
      {/* Help text for screen readers and cognitive accessibility */}
      <div className="control-help">
        <div id="start-button-help" className="help-text">
          Press to begin talking with Xiao Mei
        </div>
        <div id="stop-button-help" className="help-text">
          Press to end the conversation
        </div>
        <div id="mic-button-help" className="help-text">
          Toggle your microphone on or off
        </div>
      </div>
      
      {/* Status announcements for screen readers */}
      <div 
        className="sr-only" 
        aria-live="polite" 
        aria-atomic="true"
        role="status"
      >
        {isActive && 'Conversation started'}
        {!isActive && connectionState === 'disconnected' && 'Conversation ended'}
        {isMicEnabled && isActive && 'Microphone enabled'}
        {!isMicEnabled && isActive && 'Microphone disabled'}
      </div>
      
      {/* Connection status indicator */}
      <div className="connection-status">
        <span className={`status-indicator ${connectionState}`}>
          <span className="status-dot" aria-hidden="true"></span>
          <span className="status-label">
            {connectionState === 'connected' && 'Connected'}
            {connectionState === 'connecting' && 'Connecting...'}
            {connectionState === 'disconnected' && 'Disconnected'}
          </span>
        </span>
      </div>
    </div>
  );
}

export default Controls;