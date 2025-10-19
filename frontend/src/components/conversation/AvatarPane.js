import React from 'react';
import './AvatarPane.css';

function AvatarPane({ isActive, connectionState }) {
  return (
    <div className="avatar-pane" role="region" aria-label="Xiao Mei Avatar">
      <div className="avatar-container">
        {/* Placeholder for video avatar */}
        <div 
          className={`avatar-placeholder ${isActive ? 'active' : 'idle'}`}
          aria-live="polite"
          aria-label={`Xiao Mei is ${isActive ? 'ready to talk' : 'waiting to start'}`}
        >
          <div className="avatar-circle">
            <span className="avatar-initials" aria-hidden="true">小美</span>
          </div>
          <div className="avatar-status">
            <span className="status-text">
              {isActive ? 'Ready to chat!' : 'Press start to begin'}
            </span>
            <div className={`connection-indicator ${connectionState}`} aria-hidden="true">
              <span className="connection-dot"></span>
            </div>
          </div>
        </div>
        
        {/* Connection state announcement for screen readers */}
        <div 
          className="sr-only" 
          aria-live="polite" 
          aria-atomic="true"
          role="status"
        >
          {connectionState === 'connected' && 'Connected to Xiao Mei'}
          {connectionState === 'connecting' && 'Connecting to Xiao Mei...'}
          {connectionState === 'disconnected' && 'Disconnected from Xiao Mei'}
        </div>
      </div>
      
      <div className="avatar-info">
        <h2 className="avatar-name">Xiao Mei (小美)</h2>
        <p className="avatar-description">
          Your friendly English learning companion
        </p>
      </div>
    </div>
  );
}

export default AvatarPane;