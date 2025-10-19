/**
 * Child-Friendly Animation Framework - Story 5.2
 * 
 * Animation utilities designed for child users (ages 6-11) with emphasis on
 * positive feedback, gentle micro-interactions, and accessibility compliance.
 */

/**
 * Child-friendly animation utilities
 */
export const childFriendlyAnimations = {
  /**
   * Gentle button bounce animation on interaction
   * @param {HTMLElement} element - Button element to animate
   * @param {number} intensity - Scale intensity (default: 1.05)
   */
  buttonBounce: (element, intensity = 1.05) => {
    if (!element || !element.style) return;
    
    // Check for reduced motion preference
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      element.style.backgroundColor = 'var(--primary-blue-light)';
      return;
    }
    
    element.style.transform = `scale(${intensity}) translateY(-2px)`;
    element.style.transition = 'transform 0.2s cubic-bezier(0.68, -0.55, 0.265, 1.55)';
    
    // Reset after animation
    setTimeout(() => {
      if (element.style) {
        element.style.transform = '';
      }
    }, 200);
  },

  /**
   * Success celebration animations
   * @param {string} type - Type of celebration ('confetti', 'sparkles', 'hearts')
   * @param {HTMLElement} container - Container element for animation
   */
  celebrate: (type = 'confetti', container = document.body) => {
    if (!container) return;
    
    // Check for reduced motion preference
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      // Show a gentle flash instead
      const flash = document.createElement('div');
      flash.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: var(--secondary-yellow-light);
        opacity: 0.3;
        pointer-events: none;
        z-index: 9999;
        transition: opacity 0.3s ease;
      `;
      container.appendChild(flash);
      
      setTimeout(() => {
        flash.style.opacity = '0';
        setTimeout(() => container.removeChild(flash), 300);
      }, 100);
      return;
    }

    switch(type) {
      case 'confetti':
        createConfettiAnimation(container);
        break;
      case 'sparkles':
        createSparkleAnimation(container);
        break;
      case 'hearts':
        createHeartAnimation(container);
        break;
      default:
        createConfettiAnimation(container);
    }
  },

  /**
   * Child-friendly loading animation
   * @param {HTMLElement} container - Container for the loading animation
   * @param {string} message - Optional loading message
   */
  friendlyLoader: (container, message = 'Getting ready...') => {
    if (!container) return null;
    
    const loader = document.createElement('div');
    loader.className = 'friendly-loader';
    loader.innerHTML = `
      <div class="bouncing-dots">
        <div class="dot"></div>
        <div class="dot"></div>
        <div class="dot"></div>
      </div>
      <p class="loading-message">${message}</p>
    `;
    
    container.appendChild(loader);
    return loader;
  },

  /**
   * Remove loading animation
   * @param {HTMLElement} loader - Loader element to remove
   */
  removeFriendlyLoader: (loader) => {
    if (loader && loader.parentNode) {
      loader.style.opacity = '0';
      loader.style.transition = 'opacity 0.3s ease';
      setTimeout(() => {
        if (loader.parentNode) {
          loader.parentNode.removeChild(loader);
        }
      }, 300);
    }
  },

  /**
   * Gentle hover effect for interactive elements
   * @param {HTMLElement} element - Element to animate
   */
  gentleHover: (element) => {
    if (!element || !element.style) return;
    
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      element.style.backgroundColor = 'var(--hover-overlay)';
      return;
    }
    
    element.style.transform = 'translateY(-1px) scale(1.02)';
    element.style.boxShadow = '0 4px 12px var(--hover-overlay)';
    element.style.transition = 'all 0.2s ease';
  },

  /**
   * Reset hover effect
   * @param {HTMLElement} element - Element to reset
   */
  resetHover: (element) => {
    if (!element || !element.style) return;
    
    element.style.transform = '';
    element.style.boxShadow = '';
    element.style.backgroundColor = '';
  },

  /**
   * Pulse animation for attention
   * @param {HTMLElement} element - Element to pulse
   * @param {number} duration - Duration in milliseconds
   */
  attentionPulse: (element, duration = 2000) => {
    if (!element || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    
    element.style.animation = `gentle-pulse 1s ease-in-out 2`;
    
    setTimeout(() => {
      if (element.style) {
        element.style.animation = '';
      }
    }, duration);
  }
};

/**
 * Create confetti animation
 * @param {HTMLElement} container - Container for confetti
 */
function createConfettiAnimation(container) {
  const colors = [
    'var(--secondary-yellow)',
    'var(--accent-green)',
    'var(--primary-blue-light)',
    '#FFB6C1', // Light pink
    '#DDA0DD'  // Plum
  ];
  
  const confettiCount = 50;
  const confettiElements = [];
  
  for (let i = 0; i < confettiCount; i++) {
    const confetti = document.createElement('div');
    confetti.className = 'confetti-piece';
    confetti.style.cssText = `
      position: fixed;
      width: ${Math.random() * 8 + 6}px;
      height: ${Math.random() * 8 + 6}px;
      background: ${colors[Math.floor(Math.random() * colors.length)]};
      left: ${Math.random() * 100}vw;
      top: -10px;
      border-radius: ${Math.random() > 0.5 ? '50%' : '0'};
      opacity: 0.8;
      pointer-events: none;
      z-index: 9999;
      animation: confetti-fall ${Math.random() * 2 + 2}s linear forwards;
    `;
    
    container.appendChild(confetti);
    confettiElements.push(confetti);
  }
  
  // Clean up after animation
  setTimeout(() => {
    confettiElements.forEach(confetti => {
      if (confetti.parentNode) {
        confetti.parentNode.removeChild(confetti);
      }
    });
  }, 4000);
}

/**
 * Create sparkle animation
 * @param {HTMLElement} container - Container for sparkles
 */
function createSparkleAnimation(container) {
  const sparkleCount = 20;
  const sparkleElements = [];
  
  for (let i = 0; i < sparkleCount; i++) {
    const sparkle = document.createElement('div');
    sparkle.innerHTML = '✨';
    sparkle.style.cssText = `
      position: fixed;
      font-size: ${Math.random() * 20 + 15}px;
      left: ${Math.random() * 100}vw;
      top: ${Math.random() * 100}vh;
      pointer-events: none;
      z-index: 9999;
      animation: sparkle-twinkle ${Math.random() * 1 + 1}s ease-in-out forwards;
    `;
    
    container.appendChild(sparkle);
    sparkleElements.push(sparkle);
  }
  
  // Clean up after animation
  setTimeout(() => {
    sparkleElements.forEach(sparkle => {
      if (sparkle.parentNode) {
        sparkle.parentNode.removeChild(sparkle);
      }
    });
  }, 2000);
}

/**
 * Create heart animation
 * @param {HTMLElement} container - Container for hearts
 */
function createHeartAnimation(container) {
  const heartCount = 15;
  const heartElements = [];
  
  for (let i = 0; i < heartCount; i++) {
    const heart = document.createElement('div');
    heart.innerHTML = '💖';
    heart.style.cssText = `
      position: fixed;
      font-size: ${Math.random() * 15 + 10}px;
      left: ${Math.random() * 100}vw;
      top: 100vh;
      pointer-events: none;
      z-index: 9999;
      animation: hearts-float ${Math.random() * 2 + 3}s ease-out forwards;
    `;
    
    container.appendChild(heart);
    heartElements.push(heart);
  }
  
  // Clean up after animation
  setTimeout(() => {
    heartElements.forEach(heart => {
      if (heart.parentNode) {
        heart.parentNode.removeChild(heart);
      }
    });
  }, 5000);
}

/**
 * Initialize animation event listeners for child-friendly interactions
 */
export function initializeChildFriendlyAnimations() {
  // Add delegation for child-friendly button interactions
  document.addEventListener('mouseenter', (e) => {
    if (e.target && e.target.classList && e.target.classList.contains('child-friendly-button')) {
      childFriendlyAnimations.gentleHover(e.target);
    }
  });
  
  document.addEventListener('mouseleave', (e) => {
    if (e.target && e.target.classList && e.target.classList.contains('child-friendly-button')) {
      childFriendlyAnimations.resetHover(e.target);
    }
  });
  
  document.addEventListener('click', (e) => {
    if (e.target && e.target.classList && e.target.classList.contains('child-friendly-button')) {
      childFriendlyAnimations.buttonBounce(e.target);
    }
  });
  
  // Add support for success triggers
  document.addEventListener('childFriendlySuccess', (e) => {
    const { type = 'confetti', container } = e.detail || {};
    childFriendlyAnimations.celebrate(type, container);
  });
}

/**
 * Trigger a success celebration
 * @param {string} type - Type of celebration
 * @param {HTMLElement} container - Container element
 */
export function triggerSuccessCelebration(type = 'confetti', container = document.body) {
  const event = new CustomEvent('childFriendlySuccess', {
    detail: { type, container }
  });
  document.dispatchEvent(event);
}

// Auto-initialize when module is loaded
if (typeof window !== 'undefined') {
  // Wait for DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeChildFriendlyAnimations);
  } else {
    initializeChildFriendlyAnimations();
  }
}