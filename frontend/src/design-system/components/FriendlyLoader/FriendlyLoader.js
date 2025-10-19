/**
 * Friendly Loader Component - Story 5.2
 * 
 * Child-friendly loading animation component with encouraging messages
 * and gentle bouncing dots animation.
 */

import React, { useState, useEffect } from 'react';
import './FriendlyLoader.css';

const FriendlyLoader = ({
  message = 'Getting ready...',
  messages = [
    'Getting ready...',
    'Almost there...',
    'Just a moment...',
    'Preparing something special...',
    'Loading your adventure...'
  ],
  showProgressiveMessages = true,
  size = 'medium',
  className = '',
  'aria-label': ariaLabel = 'Loading content'
}) => {
  const [currentMessageIndex, setCurrentMessageIndex] = useState(0);
  const [displayMessage, setDisplayMessage] = useState(message);

  // Cycle through progressive messages if enabled
  useEffect(() => {
    if (!showProgressiveMessages || messages.length <= 1) {
      setDisplayMessage(message);
      return;
    }

    const interval = setInterval(() => {
      setCurrentMessageIndex((prevIndex) => {
        const nextIndex = (prevIndex + 1) % messages.length;
        setDisplayMessage(messages[nextIndex]);
        return nextIndex;
      });
    }, 2000); // Change message every 2 seconds

    return () => clearInterval(interval);
  }, [showProgressiveMessages, messages, message]);

  const loaderClasses = [
    'friendly-loader',
    `friendly-loader--${size}`,
    className
  ].filter(Boolean).join(' ');

  return (
    <div 
      className={loaderClasses}
      role="status"
      aria-live="polite"
      aria-label={ariaLabel}
    >
      <div className="friendly-loader__animation">
        <div className="bouncing-dots">
          <div className="dot dot--1"></div>
          <div className="dot dot--2"></div>
          <div className="dot dot--3"></div>
        </div>
      </div>
      
      <p className="friendly-loader__message">
        {displayMessage}
      </p>
      
      {/* Hidden text for screen readers */}
      <span className="sr-only">
        Loading in progress. Please wait.
      </span>
    </div>
  );
};

export default FriendlyLoader;