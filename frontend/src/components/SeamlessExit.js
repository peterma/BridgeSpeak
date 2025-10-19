/**
 * Seamless Exit Component for Trauma-Informed Design
 * 
 * Provides always-available exit functionality without penalty or guilt messaging.
 * Ensures children can leave conversations at any time without pressure.
 */

import React, { useState } from 'react';
import './SeamlessExit.css';

const SeamlessExit = ({ onExit, onPause, sessionId, showAlways = true }) => {
  const [showExitOptions, setShowExitOptions] = useState(false);
  const [exiting, setExiting] = useState(false);

  const handleExit = async (exitType = 'gentle') => {
    setExiting(true);
    
    try {
      // Call parent component's exit handler
      if (onExit) {
        await onExit(exitType, sessionId);
      }
      
      // Show positive exit message
      const exitMessages = {
        gentle: "好的! (Hǎo de!) Thanks for spending time with me today. I'll be here whenever you want to practice again!",
        break: "没关系 (Méi guānxi) - that's perfectly okay! Take your time. I'll be here when you're ready.",
        pause: "Let's pause here. You can come back anytime you want to continue our learning adventure!"
      };
      
      // In a real implementation, this would be displayed by Xiao Mei
      console.log('Exit message:', exitMessages[exitType]);
      
    } catch (error) {
      console.error('Error during exit:', error);
    } finally {
      setExiting(false);
      setShowExitOptions(false);
    }
  };

  const handlePause = async () => {
    setExiting(true);
    
    try {
      if (onPause) {
        await onPause(sessionId);
      }
      
      // Show pause message
      console.log('Pause message: 慢慢来 (Màn màn lái) - take your time! I\'ll wait here for you.');
      
    } catch (error) {
      console.error('Error during pause:', error);
    } finally {
      setExiting(false);
      setShowExitOptions(false);
    }
  };

  if (!showAlways && !showExitOptions) {
    return (
      <button 
        className="exit-toggle-button"
        onClick={() => setShowExitOptions(true)}
        aria-label="Show exit options"
        title="Take a break or exit"
      >
        ⏸️
      </button>
    );
  }

  return (
    <div className="seamless-exit">
      {showExitOptions && (
        <div className="exit-overlay">
          <div className="exit-modal">
            <div className="exit-header">
              <h3>Take Your Time</h3>
              <p>You can pause or exit anytime - no pressure!</p>
            </div>
            
            <div className="exit-options">
              <button
                className="exit-option pause-option"
                onClick={handlePause}
                disabled={exiting}
              >
                <span className="option-icon">⏸️</span>
                <div className="option-content">
                  <strong>Take a Break</strong>
                  <p>Pause and come back later</p>
                </div>
              </button>
              
              <button
                className="exit-option gentle-exit"
                onClick={() => handleExit('gentle')}
                disabled={exiting}
              >
                <span className="option-icon">👋</span>
                <div className="option-content">
                  <strong>Gentle Exit</strong>
                  <p>Finish for today with positive message</p>
                </div>
              </button>
              
              <button
                className="exit-option break-exit"
                onClick={() => handleExit('break')}
                disabled={exiting}
              >
                <span className="option-icon">💤</span>
                <div className="option-content">
                  <strong>Need a Break</strong>
                  <p>Exit with reassurance message</p>
                </div>
              </button>
            </div>
            
            <div className="exit-footer">
              <button
                className="cancel-button"
                onClick={() => setShowExitOptions(false)}
                disabled={exiting}
              >
                Continue Learning
              </button>
            </div>
            
            {exiting && (
              <div className="exiting-indicator">
                <div className="spinner"></div>
                <p>Taking care of you...</p>
              </div>
            )}
          </div>
        </div>
      )}
      
      {/* Always-visible exit button */}
      <button
        className="always-available-exit"
        onClick={() => setShowExitOptions(true)}
        disabled={exiting}
        aria-label="Exit or take a break"
        title="You can exit anytime - no pressure!"
      >
        <span className="exit-icon">🚪</span>
        <span className="exit-text">Exit</span>
      </button>
    </div>
  );
};

export default SeamlessExit;
