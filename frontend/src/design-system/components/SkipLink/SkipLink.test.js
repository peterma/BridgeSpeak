import React from 'react';
import { render, screen } from '@testing-library/react';
import SkipLink from './SkipLink';

describe('SkipLink', () => {
  test('renders with default props', () => {
    render(<SkipLink />);
    
    const link = screen.getByRole('link', { name: 'Skip to main content' });
    expect(link).toBeInTheDocument();
    expect(link).toHaveAttribute('href', '#main-content');
    expect(link).toHaveClass('ds-skip-link');
  });

  test('renders with custom href', () => {
    render(<SkipLink href="#navigation" />);
    
    const link = screen.getByRole('link');
    expect(link).toHaveAttribute('href', '#navigation');
  });

  test('renders with custom children', () => {
    render(<SkipLink>Skip to navigation</SkipLink>);
    
    const link = screen.getByRole('link', { name: 'Skip to navigation' });
    expect(link).toBeInTheDocument();
  });

  test('supports custom className', () => {
    render(<SkipLink className="custom-skip-link" />);
    
    const link = screen.getByRole('link');
    expect(link).toHaveClass('ds-skip-link', 'custom-skip-link');
  });

  test('forwards ref correctly', () => {
    const ref = React.createRef();
    render(<SkipLink ref={ref} />);
    
    expect(ref.current).toBeInstanceOf(HTMLAnchorElement);
  });

  test('passes through additional props', () => {
    render(
      <SkipLink 
        data-testid="custom-skip-link"
        title="Skip to main content"
        target="_self"
      />
    );
    
    const link = screen.getByTestId('custom-skip-link');
    expect(link).toHaveAttribute('title', 'Skip to main content');
    expect(link).toHaveAttribute('target', '_self');
  });

  test('renders as anchor element', () => {
    render(<SkipLink />);
    
    const link = screen.getByRole('link');
    expect(link.tagName).toBe('A');
  });

  test('maintains accessibility as a link', () => {
    render(<SkipLink href="#content">Skip to content</SkipLink>);
    
    const link = screen.getByRole('link', { name: 'Skip to content' });
    expect(link).toBeInTheDocument();
    expect(link).toHaveAttribute('href', '#content');
  });
});
