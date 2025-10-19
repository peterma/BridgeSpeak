/**
 * Input Component - Design System
 * 
 * Accessible input component with label association and error states.
 * Supports various input types and validation states.
 */

import React, { useId } from 'react';
import './Input.css';

const Input = React.forwardRef(({
  label,
  helperText,
  errorMessage,
  size = 'medium',
  variant = 'outline',
  type = 'text',
  disabled = false,
  required = false,
  invalid = false,
  fullWidth = false,
  leftIcon,
  rightIcon,
  className = '',
  id: providedId,
  'aria-describedby': providedAriaDescribedby,
  // Standard HTML input attributes
  name,
  value,
  defaultValue,
  placeholder,
  readOnly,
  autoComplete,
  autoFocus,
  form,
  formaction,
  formenctype,
  formmethod,
  formnovalidate,
  formtarget,
  list,
  max,
  maxLength,
  min,
  minLength,
  pattern,
  step,
  tabindex,
  title,
  // Event handlers
  onChange,
  onFocus,
  onBlur,
  onKeyDown,
  onKeyUp,
  onKeyPress,
  ...otherProps
}, ref) => {
  // Create clean props object with only valid DOM attributes
  const domProps = {
    ...(name && { name }),
    ...(value && { value }),
    ...(defaultValue && { defaultValue }),
    ...(placeholder && { placeholder }),
    ...(readOnly && { readOnly }),
    ...(autoComplete && { autoComplete }),
    ...(autoFocus && { autoFocus }),
    ...(form && { form }),
    ...(formaction && { formaction }),
    ...(formenctype && { formenctype }),
    ...(formmethod && { formmethod }),
    ...(formnovalidate && { formnovalidate }),
    ...(formtarget && { formtarget }),
    ...(list && { list }),
    ...(max && { max }),
    ...(maxLength && { maxLength }),
    ...(min && { min }),
    ...(minLength && { minLength }),
    ...(pattern && { pattern }),
    ...(step && { step }),
    ...(tabindex && { tabindex }),
    ...(title && { title }),
    ...(onChange && { onChange }),
    ...(onFocus && { onFocus }),
    ...(onBlur && { onBlur }),
    ...(onKeyDown && { onKeyDown }),
    ...(onKeyUp && { onKeyUp }),
    ...(onKeyPress && { onKeyPress })
  };
  
  const generatedId = useId();
  const id = providedId || generatedId;
  
  // Add data-* and aria-* attributes from otherProps
  Object.keys(otherProps).forEach(key => {
    if (key.startsWith('data-') || key.startsWith('aria-')) {
      domProps[key] = otherProps[key];
    }
  });
  const helperTextId = `${id}-helper`;
  const errorId = `${id}-error`;
  
  // Build aria-describedby
  const ariaDescribedby = [
    providedAriaDescribedby,
    helperText && helperTextId,
    errorMessage && errorId
  ].filter(Boolean).join(' ') || undefined;

  const inputClasses = [
    'ds-input__field',
    `ds-input__field--${variant}`,
    `ds-input__field--${size}`,
    disabled && 'ds-input__field--disabled',
    invalid && 'ds-input__field--invalid',
    leftIcon && 'ds-input__field--with-left-icon',
    rightIcon && 'ds-input__field--with-right-icon'
  ].filter(Boolean).join(' ');

  const containerClasses = [
    'ds-input',
    fullWidth && 'ds-input--full-width',
    className
  ].filter(Boolean).join(' ');

  return (
    <div className={containerClasses}>
      {label && (
        <label htmlFor={id} className="ds-input__label">
          {label}
          {required && (
            <span className="ds-input__required" aria-label="required">
              *
            </span>
          )}
        </label>
      )}
      
      <div className="ds-input__wrapper">
        {leftIcon && (
          <span className="ds-input__icon ds-input__icon--left" aria-hidden="true">
            {leftIcon}
          </span>
        )}
        
        <input
          ref={ref}
          type={type}
          className={inputClasses}
          disabled={disabled}
          required={required}
          aria-invalid={invalid}
          aria-describedby={ariaDescribedby}
          {...domProps}
          id={id}
        />
        
        {rightIcon && (
          <span className="ds-input__icon ds-input__icon--right" aria-hidden="true">
            {rightIcon}
          </span>
        )}
      </div>
      
      {helperText && !errorMessage && (
        <div id={helperTextId} className="ds-input__helper-text">
          {helperText}
        </div>
      )}
      
      {errorMessage && (
        <div id={errorId} className="ds-input__error-message" role="alert">
          {errorMessage}
        </div>
      )}
    </div>
  );
});

Input.displayName = 'Input';

export default Input;