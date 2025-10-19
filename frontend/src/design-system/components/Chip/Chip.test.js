import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { jest } from '@jest/globals';
import Chip from './Chip';

describe('Chip', () => {
  test('renders basic chip', () => {
    render(<Chip>Basic Chip</Chip>);
    
    const chip = screen.getByText('Basic Chip').closest('.ds-chip');
    expect(chip).toBeInTheDocument();
    expect(chip).toHaveClass('ds-chip', 'ds-chip--default', 'ds-chip--medium');
  });

  test('renders different variants', () => {
    const { rerender } = render(<Chip variant="primary">Primary</Chip>);
    expect(screen.getByText('Primary').closest('.ds-chip')).toHaveClass('ds-chip--primary');
    
    rerender(<Chip variant="secondary">Secondary</Chip>);
    expect(screen.getByText('Secondary').closest('.ds-chip')).toHaveClass('ds-chip--secondary');
    
    rerender(<Chip variant="success">Success</Chip>);
    expect(screen.getByText('Success').closest('.ds-chip')).toHaveClass('ds-chip--success');
    
    rerender(<Chip variant="error">Error</Chip>);
    expect(screen.getByText('Error').closest('.ds-chip')).toHaveClass('ds-chip--error');
  });

  test('renders different sizes', () => {
    const { rerender } = render(<Chip size="small">Small</Chip>);
    expect(screen.getByText('Small').closest('.ds-chip')).toHaveClass('ds-chip--small');
    
    rerender(<Chip size="large">Large</Chip>);
    expect(screen.getByText('Large').closest('.ds-chip')).toHaveClass('ds-chip--large');
  });

  test('handles selected state', () => {
    render(<Chip selected>Selected Chip</Chip>);
    
    const chip = screen.getByText('Selected Chip').closest('.ds-chip');
    expect(chip).toHaveClass('ds-chip--selected');
  });

  test('handles disabled state', () => {
    render(<Chip disabled>Disabled Chip</Chip>);
    
    const chip = screen.getByText('Disabled Chip').closest('.ds-chip');
    expect(chip).toHaveClass('ds-chip--disabled');
    expect(chip).toHaveAttribute('aria-disabled', 'true');
  });

  test('handles clickable state', () => {
    const handleClick = jest.fn();
    render(<Chip clickable onClick={handleClick}>Clickable Chip</Chip>);
    
    const chip = screen.getByText('Clickable Chip').closest('.ds-chip');
    expect(chip).toHaveClass('ds-chip--clickable');
    expect(chip).toHaveAttribute('role', 'button');
    expect(chip).toHaveAttribute('tabIndex', '0');
    
    fireEvent.click(chip);
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  test('handles removable state', () => {
    const handleRemove = jest.fn();
    render(<Chip removable onRemove={handleRemove}>Removable Chip</Chip>);
    
    const chip = screen.getByText('Removable Chip').closest('.ds-chip');
    const removeButton = screen.getByRole('button', { name: 'Remove Removable Chip' });
    
    expect(chip).toHaveClass('ds-chip--removable');
    expect(removeButton).toBeInTheDocument();
    expect(removeButton).toHaveAttribute('tabIndex', '-1');
    
    fireEvent.click(removeButton);
    expect(handleRemove).toHaveBeenCalledTimes(1);
  });

  test('renders with left icon', () => {
    render(<Chip leftIcon="🏷️">Tagged Chip</Chip>);
    
    const icon = screen.getByText('🏷️');
    expect(icon).toBeInTheDocument();
    expect(icon).toHaveClass('ds-chip__icon', 'ds-chip__icon--left');
    expect(icon).toHaveAttribute('aria-hidden', 'true');
  });

  test('handles click events', () => {
    const handleClick = jest.fn();
    render(<Chip clickable onClick={handleClick}>Clickable</Chip>);
    
    const chip = screen.getByText('Clickable').closest('.ds-chip');
    fireEvent.click(chip);
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  test('prevents click when disabled', () => {
    const handleClick = jest.fn();
    render(<Chip clickable disabled onClick={handleClick}>Disabled</Chip>);
    
    const chip = screen.getByText('Disabled').closest('.ds-chip');
    fireEvent.click(chip);
    expect(handleClick).not.toHaveBeenCalled();
  });

  test('handles keyboard navigation', () => {
    const handleClick = jest.fn();
    render(<Chip clickable onClick={handleClick}>Keyboard Chip</Chip>);
    
    const chip = screen.getByText('Keyboard Chip').closest('.ds-chip');
    
    fireEvent.keyDown(chip, { key: 'Enter' });
    expect(handleClick).toHaveBeenCalledTimes(1);
    
    fireEvent.keyDown(chip, { key: ' ' });
    expect(handleClick).toHaveBeenCalledTimes(2);
  });

  test('handles remove keyboard navigation', () => {
    const handleRemove = jest.fn();
    render(<Chip removable onRemove={handleRemove}>Removable</Chip>);
    
    const chip = screen.getByText('Removable').closest('.ds-chip');
    
    fireEvent.keyDown(chip, { key: 'Delete' });
    expect(handleRemove).toHaveBeenCalledTimes(1);
    
    fireEvent.keyDown(chip, { key: 'Backspace' });
    expect(handleRemove).toHaveBeenCalledTimes(2);
  });

  test('prevents keyboard events when disabled', () => {
    const handleClick = jest.fn();
    const handleRemove = jest.fn();
    render(
      <Chip 
        clickable 
        removable 
        disabled 
        onClick={handleClick} 
        onRemove={handleRemove}
      >
        Disabled
      </Chip>
    );
    
    const chip = screen.getByText('Disabled').closest('.ds-chip');
    
    fireEvent.keyDown(chip, { key: 'Enter' });
    fireEvent.keyDown(chip, { key: 'Delete' });
    
    expect(handleClick).not.toHaveBeenCalled();
    expect(handleRemove).not.toHaveBeenCalled();
  });

  test('stops propagation on remove click', () => {
    const handleClick = jest.fn();
    const handleRemove = jest.fn();
    render(
      <Chip 
        clickable 
        removable 
        onClick={handleClick} 
        onRemove={handleRemove}
      >
        Test
      </Chip>
    );
    
    const removeButton = screen.getByRole('button', { name: 'Remove Test' });
    const clickEvent = new MouseEvent('click', { bubbles: true });
    const stopPropagationSpy = jest.spyOn(clickEvent, 'stopPropagation');
    
    fireEvent(removeButton, clickEvent);
    
    expect(stopPropagationSpy).toHaveBeenCalled();
    expect(handleRemove).toHaveBeenCalledTimes(1);
    expect(handleClick).not.toHaveBeenCalled();
  });

  test('supports custom className', () => {
    render(<Chip className="custom-chip">Custom</Chip>);
    
    const chip = screen.getByText('Custom').closest('.ds-chip');
    expect(chip).toHaveClass('custom-chip');
  });

  test('supports ARIA attributes', () => {
    render(
      <Chip 
        clickable
        aria-label="Custom chip"
        aria-pressed={true}
      >
        Custom
      </Chip>
    );
    
    const chip = screen.getByText('Custom').closest('.ds-chip');
    expect(chip).toHaveAttribute('aria-label', 'Custom chip');
    expect(chip).toHaveAttribute('aria-pressed', 'true');
  });

  test('uses selected state for aria-pressed when not explicitly set', () => {
    render(<Chip clickable selected>Selected</Chip>);
    
    const chip = screen.getByText('Selected').closest('.ds-chip');
    expect(chip).toHaveAttribute('aria-pressed', 'true');
  });

  test('forwards ref correctly', () => {
    const ref = React.createRef();
    render(<Chip ref={ref}>Ref Chip</Chip>);
    
    expect(ref.current).toBeInstanceOf(HTMLSpanElement);
  });

  test('passes through additional props', () => {
    render(<Chip data-testid="custom-chip" title="Chip tooltip">Test</Chip>);
    
    const chip = screen.getByTestId('custom-chip');
    expect(chip).toHaveAttribute('title', 'Chip tooltip');
  });

  test('maintains proper DOM structure', () => {
    render(
      <Chip 
        leftIcon="🏷️" 
        removable
        clickable
      >
        Structured Chip
      </Chip>
    );
    
    const chip = screen.getByText('Structured Chip').closest('.ds-chip');
    const content = chip.querySelector('.ds-chip__content');
    const icon = chip.querySelector('.ds-chip__icon--left');
    const removeButton = chip.querySelector('.ds-chip__remove');
    
    expect(content).toBeInTheDocument();
    expect(icon).toBeInTheDocument();
    expect(removeButton).toBeInTheDocument();
  });

  test('handles remove button disabled state', () => {
    render(<Chip removable disabled>Disabled Removable</Chip>);
    
    const removeButton = screen.getByRole('button', { name: 'Remove Disabled Removable' });
    expect(removeButton).toBeDisabled();
  });

  test('generates proper remove button aria-label', () => {
    render(<Chip removable>Simple Text</Chip>);
    
    const removeButton = screen.getByRole('button', { name: 'Remove Simple Text' });
    expect(removeButton).toBeInTheDocument();
  });

  test('handles non-string children in remove button aria-label', () => {
    render(
      <Chip removable>
        <span>Complex Content</span>
      </Chip>
    );
    
    const removeButton = screen.getByRole('button', { name: 'Remove item' });
    expect(removeButton).toBeInTheDocument();
  });

  test('does not render remove button when not removable', () => {
    render(<Chip>Non-removable</Chip>);
    
    expect(screen.queryByRole('button')).not.toBeInTheDocument();
  });

  test('does not have interactive attributes when not clickable or removable', () => {
    render(<Chip>Basic</Chip>);
    
    const chip = screen.getByText('Basic').closest('.ds-chip');
    expect(chip).not.toHaveAttribute('role');
    expect(chip).not.toHaveAttribute('tabIndex');
    expect(chip).not.toHaveAttribute('aria-pressed');
  });
});