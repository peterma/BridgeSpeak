/**
 * Chip Component - Design System
 * 
 * Small interactive element for tags, filters, and selections.
 * Supports selected/unselected states and removal functionality.
 */

import React from 'react';
import './Chip.css';

const Chip = React.forwardRef(({
  children,
  variant = 'default',
  size = 'medium',
  selected = false,
  disabled = false,
  removable = false,
  clickable = false,
  leftIcon,
  className = '',
  onClick,
  onRemove,
  'aria-label': ariaLabel,
  'aria-pressed': ariaPressed,
  ...props
}, ref) => {
  // Create clean props object with only valid DOM attributes
  const domProps = {};
  Object.keys(props).forEach(key => {
    // Only include standard HTML span attributes
    if (['id', 'title', 'lang', 'dir', 'hidden', 'tabindex'].includes(key) || 
        key.startsWith('data-') || 
        key.startsWith('aria-') || 
        (key.startsWith('on') && !['onClick', 'onKeyDown', 'onKeyUp', 'onKeyPress'].includes(key))) {
      domProps[key] = props[key];
    }
  });
  const chipClasses = [
    'ds-chip',
    `ds-chip--${variant}`,
    `ds-chip--${size}`,
    selected && 'ds-chip--selected',
    disabled && 'ds-chip--disabled',
    clickable && 'ds-chip--clickable',
    removable && 'ds-chip--removable',
    className
  ].filter(Boolean).join(' ');

  const handleClick = (event) => {
    if (disabled) {
      event.preventDefault();
      return;
    }
    onClick?.(event);
  };

  const handleRemove = (event) => {
    event.stopPropagation();
    if (disabled) return;
    onRemove?.(event);
  };

  const handleKeyDown = (event) => {
    if (disabled) return;
    
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      onClick?.(event);
    }
    
    if (removable && (event.key === 'Delete' || event.key === 'Backspace')) {
      event.preventDefault();
      onRemove?.(event);
    }
  };

  const chipProps = {
    ref,
    className: chipClasses,
    onClick: clickable ? handleClick : undefined,
    onKeyDown: (clickable || removable) ? handleKeyDown : undefined,
    'aria-label': ariaLabel,
    'aria-pressed': clickable ? (ariaPressed ?? selected) : undefined,
    'aria-disabled': disabled,
    role: clickable ? 'button' : undefined,
    tabIndex: (clickable || removable) && !disabled ? 0 : undefined,
    ...domProps
  };

  return (
    <span {...chipProps}>
      {leftIcon && (
        <span className="ds-chip__icon ds-chip__icon--left" aria-hidden="true">
          {leftIcon}
        </span>
      )}
      
      <span className="ds-chip__content">
        {children}
      </span>
      
      {removable && (
        <button
          type="button"
          className="ds-chip__remove"
          onClick={handleRemove}
          disabled={disabled}
          aria-label={`Remove ${typeof children === 'string' ? children : 'item'}`}
          tabIndex={-1} // Let parent handle tab navigation
        >
          <span aria-hidden="true">×</span>
        </button>
      )}
    </span>
  );
});

Chip.displayName = 'Chip';

export default Chip;