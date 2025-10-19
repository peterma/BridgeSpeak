/**
 * VisuallyHidden Component - Design System
 * 
 * Hides content visually while keeping it accessible to screen readers.
 * Essential for providing context to assistive technologies.
 */

import React from 'react';
import './VisuallyHidden.css';

const VisuallyHidden = React.forwardRef(({
  children,
  as: Component = 'span',
  className = '',
  ...props
}, ref) => {
  return (
    <Component
      ref={ref}
      className={`ds-visually-hidden ${className}`}
      {...props}
    >
      {children}
    </Component>
  );
});

VisuallyHidden.displayName = 'VisuallyHidden';

export default VisuallyHidden;