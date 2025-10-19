import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { jest } from '@jest/globals';
import Button from './Button';

describe('Button', () => {
  test('renders with default props', () => {
    render(<Button>Click me</Button>);
    
    const button = screen.getByRole('button', { name: 'Click me' });
    expect(button).toBeInTheDocument();
    expect(button).toHaveClass('ds-button', 'ds-button--primary', 'ds-button--medium');
  });

  test('renders different variants', () => {
    const { rerender } = render(<Button variant="secondary">Secondary</Button>);
    expect(screen.getByRole('button')).toHaveClass('ds-button--secondary');
    
    rerender(<Button variant="outline">Outline</Button>);
    expect(screen.getByRole('button')).toHaveClass('ds-button--outline');
    
    rerender(<Button variant="ghost">Ghost</Button>);
    expect(screen.getByRole('button')).toHaveClass('ds-button--ghost');
    
    rerender(<Button variant="danger">Danger</Button>);
    expect(screen.getByRole('button')).toHaveClass('ds-button--danger');
  });

  test('renders different sizes', () => {
    const { rerender } = render(<Button size="small">Small</Button>);
    expect(screen.getByRole('button')).toHaveClass('ds-button--small');
    
    rerender(<Button size="large">Large</Button>);
    expect(screen.getByRole('button')).toHaveClass('ds-button--large');
  });

  test('handles disabled state', () => {
    render(<Button disabled>Disabled</Button>);
    
    const button = screen.getByRole('button');
    expect(button).toBeDisabled();
    expect(button).toHaveClass('ds-button--disabled');
    expect(button).toHaveAttribute('aria-disabled', 'true');
  });

  test('handles loading state', () => {
    render(<Button loading>Loading</Button>);
    
    const button = screen.getByRole('button');
    expect(button).toBeDisabled();
    expect(button).toHaveClass('ds-button--loading');
    expect(button).toHaveAttribute('aria-disabled', 'true');
    expect(screen.getByText('Loading...')).toBeInTheDocument();
  });

  test('shows custom loading text', () => {
    render(<Button loading="Please wait...">Loading</Button>);
    
    expect(screen.getByText('Please wait...')).toBeInTheDocument();
  });

  test('renders with left icon', () => {
    render(<Button leftIcon="🚀">Start</Button>);
    
    const icon = screen.getByText('🚀');
    expect(icon).toBeInTheDocument();
    expect(icon).toHaveClass('ds-button__icon', 'ds-button__icon--left');
    expect(icon).toHaveAttribute('aria-hidden', 'true');
  });

  test('renders with right icon', () => {
    render(<Button rightIcon="→">Continue</Button>);
    
    const icon = screen.getByText('→');
    expect(icon).toBeInTheDocument();
    expect(icon).toHaveClass('ds-button__icon', 'ds-button__icon--right');
    expect(icon).toHaveAttribute('aria-hidden', 'true');
  });

  test('hides right icon when loading', () => {
    render(<Button rightIcon="→" loading>Loading</Button>);
    
    expect(screen.queryByText('→')).not.toBeInTheDocument();
  });

  test('handles click events', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    
    fireEvent.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  test('prevents click when disabled', () => {
    const handleClick = jest.fn();
    render(<Button disabled onClick={handleClick}>Disabled</Button>);
    
    fireEvent.click(screen.getByRole('button'));
    expect(handleClick).not.toHaveBeenCalled();
  });

  test('prevents click when loading', () => {
    const handleClick = jest.fn();
    render(<Button loading onClick={handleClick}>Loading</Button>);
    
    fireEvent.click(screen.getByRole('button'));
    expect(handleClick).not.toHaveBeenCalled();
  });

  test('supports full width', () => {
    render(<Button fullWidth>Full Width</Button>);
    
    expect(screen.getByRole('button')).toHaveClass('ds-button--full-width');
  });

  test('supports custom className', () => {
    render(<Button className="custom-class">Custom</Button>);
    
    expect(screen.getByRole('button')).toHaveClass('custom-class');
  });

  test('supports ARIA attributes', () => {
    render(
      <Button 
        aria-label="Custom label"
        aria-describedby="description"
      >
        Button
      </Button>
    );
    
    const button = screen.getByRole('button');
    expect(button).toHaveAttribute('aria-label', 'Custom label');
    expect(button).toHaveAttribute('aria-describedby', 'description');
  });

  test('supports different button types', () => {
    const { rerender } = render(<Button type="submit">Submit</Button>);
    expect(screen.getByRole('button')).toHaveAttribute('type', 'submit');
    
    rerender(<Button type="reset">Reset</Button>);
    expect(screen.getByRole('button')).toHaveAttribute('type', 'reset');
  });

  test('forwards ref correctly', () => {
    const ref = React.createRef();
    render(<Button ref={ref}>Ref Button</Button>);
    
    expect(ref.current).toBeInstanceOf(HTMLButtonElement);
  });

  test('passes through additional props', () => {
    render(<Button data-testid="custom-button" title="Tooltip">Button</Button>);
    
    const button = screen.getByTestId('custom-button');
    expect(button).toHaveAttribute('title', 'Tooltip');
  });

  test('renders loading spinner', () => {
    render(<Button loading>Loading</Button>);
    
    const spinner = screen.getByRole('button').querySelector('.ds-button__spinner');
    expect(spinner).toBeInTheDocument();
    expect(spinner).toHaveAttribute('aria-hidden', 'true');
  });

  test('maintains button content structure', () => {
    render(<Button leftIcon="🚀" rightIcon="→">Content</Button>);
    
    const content = screen.getByText('Content');
    expect(content).toHaveClass('ds-button__content');
  });
});
