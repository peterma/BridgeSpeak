/**
 * Design System Component Exports
 * 
 * Centralized exports for all design system components.
 * Import tokens CSS separately in your app root.
 */

// Import all component styles
import './components/Button/Button.css';
import './components/Card/Card.css';
import './components/Input/Input.css';
import './components/Chip/Chip.css';
import './components/SkipLink/SkipLink.css';
import './components/VisuallyHidden/VisuallyHidden.css';
import './components/FriendlyLoader/FriendlyLoader.css';
import './animations.css';

// Export components
export { default as Button } from './components/Button/Button';
export { default as Card } from './components/Card/Card';
export { default as Input } from './components/Input/Input';
export { default as Chip } from './components/Chip/Chip';
export { default as SkipLink } from './components/SkipLink/SkipLink';
export { default as VisuallyHidden } from './components/VisuallyHidden/VisuallyHidden';
export { default as FriendlyLoader } from './components/FriendlyLoader/FriendlyLoader';

// Export animation utilities
export { 
  childFriendlyAnimations, 
  triggerSuccessCelebration, 
  initializeChildFriendlyAnimations 
} from './animations';

// Re-export tokens for JS usage (e.g., for theme switching)
export const tokens = {
  colors: {
    primary: 'var(--color-primary)',
    secondary: 'var(--color-secondary)',
    accent: 'var(--color-accent)',
    background: 'var(--color-background)',
    text: {
      primary: 'var(--color-text-primary)',
      secondary: 'var(--color-text-secondary)',
      muted: 'var(--color-text-muted)',
      inverse: 'var(--color-text-inverse)'
    },
    border: 'var(--color-border)',
    focus: 'var(--color-focus)'
  },
  spacing: {
    0: 'var(--space-0)',
    1: 'var(--space-1)',
    2: 'var(--space-2)',
    3: 'var(--space-3)',
    4: 'var(--space-4)',
    5: 'var(--space-5)',
    6: 'var(--space-6)',
    8: 'var(--space-8)',
    10: 'var(--space-10)',
    12: 'var(--space-12)',
    16: 'var(--space-16)',
    20: 'var(--space-20)',
    24: 'var(--space-24)',
    32: 'var(--space-32)'
  },
  radius: {
    none: 'var(--radius-none)',
    sm: 'var(--radius-sm)',
    base: 'var(--radius-base)',
    md: 'var(--radius-md)',
    lg: 'var(--radius-lg)',
    xl: 'var(--radius-xl)',
    '2xl': 'var(--radius-2xl)',
    '3xl': 'var(--radius-3xl)',
    full: 'var(--radius-full)'
  },
  shadows: {
    sm: 'var(--shadow-sm)',
    base: 'var(--shadow-base)',
    md: 'var(--shadow-md)',
    lg: 'var(--shadow-lg)',
    xl: 'var(--shadow-xl)',
    '2xl': 'var(--shadow-2xl)',
    focus: 'var(--shadow-focus)'
  },
  typography: {
    fontFamily: {
      primary: 'var(--font-family-primary)',
      mono: 'var(--font-family-mono)'
    },
    fontSize: {
      xs: 'var(--font-size-xs)',
      sm: 'var(--font-size-sm)',
      base: 'var(--font-size-base)',
      lg: 'var(--font-size-lg)',
      xl: 'var(--font-size-xl)',
      '2xl': 'var(--font-size-2xl)',
      '3xl': 'var(--font-size-3xl)',
      '4xl': 'var(--font-size-4xl)',
      '5xl': 'var(--font-size-5xl)'
    },
    fontWeight: {
      normal: 'var(--font-weight-normal)',
      medium: 'var(--font-weight-medium)',
      semibold: 'var(--font-weight-semibold)',
      bold: 'var(--font-weight-bold)'
    },
    lineHeight: {
      tight: 'var(--line-height-tight)',
      normal: 'var(--line-height-normal)',
      relaxed: 'var(--line-height-relaxed)'
    }
  },
  transitions: {
    fast: 'var(--transition-fast)',
    base: 'var(--transition-base)',
    slow: 'var(--transition-slow)'
  },
  zIndex: {
    dropdown: 'var(--z-index-dropdown)',
    sticky: 'var(--z-index-sticky)',
    fixed: 'var(--z-index-fixed)',
    modal: 'var(--z-index-modal)',
    popover: 'var(--z-index-popover)',
    tooltip: 'var(--z-index-tooltip)'
  }
};