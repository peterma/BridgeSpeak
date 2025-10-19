/**
 * SkipLink Component - Design System
 * 
 * Accessibility utility for keyboard navigation.
 * Allows users to skip to main content or other sections.
 */

import React from 'react';
import './SkipLink.css';

const SkipLink = React.forwardRef(({
  href = '#main-content',
  children = 'Skip to main content',
  className = '',
  ...props
}, ref) => {
  return (
    <a
      ref={ref}
      href={href}
      className={`ds-skip-link ${className}`}
      {...props}
    >
      {children}
    </a>
  );
});

SkipLink.displayName = 'SkipLink';

export default SkipLink;