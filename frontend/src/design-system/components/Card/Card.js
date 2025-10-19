/**
 * Card Component - Design System
 * 
 * Flexible card container with header and body slots.
 * Provides semantic structure for content organization.
 */

import React from 'react';
import './Card.css';

const Card = React.forwardRef(({
  children,
  variant = 'default',
  padding = 'medium',
  shadow = 'base',
  interactive = false,
  className = '',
  onClick,
  'aria-label': ariaLabel,
  'aria-labelledby': ariaLabelledby,
  'aria-describedby': ariaDescribedby,
  role,
  tabIndex,
  ...props
}, ref) => {
  // Create clean props object with only valid DOM attributes
  const domProps = {};
  Object.keys(props).forEach(key => {
    // Only include standard HTML div attributes
    if (['id', 'title', 'lang', 'dir', 'hidden', 'tabindex'].includes(key) || 
        key.startsWith('data-') || 
        key.startsWith('aria-') || 
        (key.startsWith('on') && key !== 'onClick')) {
      domProps[key] = props[key];
    }
  });
  const cardClasses = [
    'ds-card',
    `ds-card--${variant}`,
    `ds-card--padding-${padding}`,
    `ds-card--shadow-${shadow}`,
    interactive && 'ds-card--interactive',
    className
  ].filter(Boolean).join(' ');

  const cardProps = {
    ref,
    className: cardClasses,
    onClick: interactive ? onClick : undefined,
    'aria-label': ariaLabel,
    'aria-labelledby': ariaLabelledby,
    'aria-describedby': ariaDescribedby,
    role: role || (interactive ? 'button' : undefined),
    tabIndex: interactive ? (tabIndex ?? 0) : tabIndex,
    ...domProps
  };

  return (
    <div {...cardProps}>
      {children}
    </div>
  );
});

const CardHeader = React.forwardRef(({
  children,
  className = '',
  ...props
}, ref) => (
  <header ref={ref} className={`ds-card__header ${className}`} {...props}>
    {children}
  </header>
));

const CardTitle = React.forwardRef(({
  children,
  level = 3,
  className = '',
  ...props
}, ref) => {
  const Tag = `h${level}`;
  return (
    <Tag ref={ref} className={`ds-card__title ${className}`} {...props}>
      {children}
    </Tag>
  );
});

const CardSubtitle = React.forwardRef(({
  children,
  className = '',
  ...props
}, ref) => (
  <p ref={ref} className={`ds-card__subtitle ${className}`} {...props}>
    {children}
  </p>
));

const CardBody = React.forwardRef(({
  children,
  className = '',
  ...props
}, ref) => (
  <div ref={ref} className={`ds-card__body ${className}`} {...props}>
    {children}
  </div>
));

const CardFooter = React.forwardRef(({
  children,
  className = '',
  ...props
}, ref) => (
  <footer ref={ref} className={`ds-card__footer ${className}`} {...props}>
    {children}
  </footer>
));

const CardActions = React.forwardRef(({
  children,
  align = 'end',
  className = '',
  ...props
}, ref) => (
  <div ref={ref} className={`ds-card__actions ds-card__actions--${align} ${className}`} {...props}>
    {children}
  </div>
));

// Set display names for debugging
Card.displayName = 'Card';
CardHeader.displayName = 'Card.Header';
CardTitle.displayName = 'Card.Title';
CardSubtitle.displayName = 'Card.Subtitle';
CardBody.displayName = 'Card.Body';
CardFooter.displayName = 'Card.Footer';
CardActions.displayName = 'Card.Actions';

// Attach sub-components to main component
Card.Header = CardHeader;
Card.Title = CardTitle;
Card.Subtitle = CardSubtitle;
Card.Body = CardBody;
Card.Footer = CardFooter;
Card.Actions = CardActions;

export default Card;