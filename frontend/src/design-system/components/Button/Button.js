/**
 * Button Component - Design System
 * 
 * Accessible button component with variants for different use cases.
 * Follows trauma-informed design with gentle interactions.
 * Enhanced with child-friendly animations for Story 5.2.
 */

import React, { useRef, useEffect } from 'react';
import './Button.css';
import { childFriendlyAnimations, triggerSuccessCelebration } from '../../animations';

const Button = React.forwardRef(({
  children,
  variant = 'primary',
  size = 'medium',
  disabled = false,
  loading = false,
  fullWidth = false,
  leftIcon,
  rightIcon,
  className = '',
  onClick,
  type = 'button',
  childFriendly = false, // New prop for child-friendly animations
  celebration = null, // Optional celebration type on click
  'aria-label': ariaLabel,
  'aria-describedby': ariaDescribedby,
  id,
  name,
  value,
  form,
  formaction,
  formenctype,
  formmethod,
  formnovalidate,
  formtarget,
  autofocus,
  tabindex,
  ...otherProps
}, ref) => {
  const internalRef = useRef(null);
  const buttonRef = ref || internalRef;
  // Only pass valid DOM attributes to the button element
  const domProps = {
    ...(id && { id }),
    ...(name && { name }),
    ...(value && { value }),
    ...(form && { form }),
    ...(formaction && { formaction }),
    ...(formenctype && { formenctype }),
    ...(formmethod && { formmethod }),
    ...(formnovalidate && { formnovalidate }),
    ...(formtarget && { formtarget }),
    ...(autofocus && { autofocus }),
    ...(tabindex && { tabindex })
  };
  
  // Add data-* and aria-* attributes from otherProps
  Object.keys(otherProps).forEach(key => {
    if (key.startsWith('data-') || key.startsWith('aria-')) {
      domProps[key] = otherProps[key];
    }
  });
  const buttonClasses = [
    'ds-button',
    `ds-button--${variant}`,
    `ds-button--${size}`,
    disabled && 'ds-button--disabled',
    loading && 'ds-button--loading',
    fullWidth && 'ds-button--full-width',
    childFriendly && 'child-friendly-button',
    className
  ].filter(Boolean).join(' ');

  const handleClick = (event) => {
    if (disabled || loading) {
      event.preventDefault();
      return;
    }
    
    // Apply child-friendly animations if enabled
    if (childFriendly && buttonRef.current) {
      childFriendlyAnimations.buttonBounce(buttonRef.current);
    }
    
    // Trigger celebration if specified
    if (celebration && !disabled && !loading) {
      triggerSuccessCelebration(celebration);
    }
    
    onClick?.(event);
  };

  // Add child-friendly hover effects
  useEffect(() => {
    if (!childFriendly || !buttonRef.current) return;
    
    const button = buttonRef.current;
    
    const handleMouseEnter = () => {
      if (!disabled && !loading) {
        childFriendlyAnimations.gentleHover(button);
      }
    };
    
    const handleMouseLeave = () => {
      if (!disabled && !loading) {
        childFriendlyAnimations.resetHover(button);
      }
    };
    
    button.addEventListener('mouseenter', handleMouseEnter);
    button.addEventListener('mouseleave', handleMouseLeave);
    
    return () => {
      button.removeEventListener('mouseenter', handleMouseEnter);
      button.removeEventListener('mouseleave', handleMouseLeave);
    };
  }, [childFriendly, disabled, loading]);

  return (
    <button
      ref={buttonRef}
      type={type}
      className={buttonClasses}
      disabled={disabled || loading}
      onClick={handleClick}
      aria-label={ariaLabel}
      aria-describedby={ariaDescribedby}
      aria-disabled={disabled || loading}
      {...domProps}
    >
      {leftIcon && (
        <span className="ds-button__icon ds-button__icon--left" aria-hidden="true">
          {leftIcon}
        </span>
      )}
      
      <span className="ds-button__content">
        {loading ? (
          <>
            <span className="ds-button__spinner" aria-hidden="true" />
            <span className="ds-button__loading-text">
              {typeof loading === 'string' ? loading : 'Loading...'}
            </span>
          </>
        ) : (
          children
        )}
      </span>
      
      {rightIcon && !loading && (
        <span className="ds-button__icon ds-button__icon--right" aria-hidden="true">
          {rightIcon}
        </span>
      )}
    </button>
  );
});

Button.displayName = 'Button';

export default Button;