import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { jest } from '@jest/globals';
import Input from './Input';

describe('Input', () => {
  test('renders basic input', () => {
    render(<Input label="Test Input" />);
    
    const input = screen.getByLabelText('Test Input');
    expect(input).toBeInTheDocument();
    expect(input).toHaveClass('ds-input__field', 'ds-input__field--outline', 'ds-input__field--medium');
  });

  test('renders with label', () => {
    render(<Input label="Email Address" />);
    
    const label = screen.getByText('Email Address');
    const input = screen.getByLabelText('Email Address');
    
    expect(label).toBeInTheDocument();
    expect(input).toBeInTheDocument();
    expect(label).toHaveAttribute('for', input.id);
  });

  test('renders without label', () => {
    render(<Input placeholder="Enter text" />);
    
    const input = screen.getByPlaceholderText('Enter text');
    expect(input).toBeInTheDocument();
    expect(screen.queryByRole('label')).not.toBeInTheDocument();
  });

  test('renders different variants', () => {
    const { rerender } = render(<Input label="Test" variant="filled" />);
    expect(screen.getByLabelText('Test')).toHaveClass('ds-input__field--filled');
    
    rerender(<Input label="Test" variant="underline" />);
    expect(screen.getByLabelText('Test')).toHaveClass('ds-input__field--underline');
  });

  test('renders different sizes', () => {
    const { rerender } = render(<Input label="Test" size="small" />);
    expect(screen.getByLabelText('Test')).toHaveClass('ds-input__field--small');
    
    rerender(<Input label="Test" size="large" />);
    expect(screen.getByLabelText('Test')).toHaveClass('ds-input__field--large');
  });

  test('handles disabled state', () => {
    render(<Input label="Disabled Input" disabled />);
    
    const input = screen.getByLabelText('Disabled Input');
    expect(input).toBeDisabled();
    expect(input).toHaveClass('ds-input__field--disabled');
  });

  test('handles required state', () => {
    render(<Input label="Required Input" required />);
    
    const input = screen.getByRole('textbox', { name: /Required Input/ });
    const label = screen.getByText('Required Input');
    
    expect(input).toHaveAttribute('required');
    expect(label).toContainHTML('<span class="ds-input__required" aria-label="required">*</span>');
  });

  test('handles invalid state', () => {
    render(<Input label="Invalid Input" invalid />);
    
    const input = screen.getByLabelText('Invalid Input');
    expect(input).toHaveClass('ds-input__field--invalid');
    expect(input).toHaveAttribute('aria-invalid', 'true');
  });

  test('renders helper text', () => {
    render(<Input label="Test Input" helperText="This is helper text" />);
    
    const helperText = screen.getByText('This is helper text');
    const input = screen.getByLabelText('Test Input');
    
    expect(helperText).toBeInTheDocument();
    expect(helperText).toHaveClass('ds-input__helper-text');
    expect(input).toHaveAttribute('aria-describedby', expect.stringContaining('helper'));
  });

  test('renders error message', () => {
    render(<Input label="Test Input" errorMessage="This is an error" />);
    
    const errorMessage = screen.getByText('This is an error');
    const input = screen.getByLabelText('Test Input');
    
    expect(errorMessage).toBeInTheDocument();
    expect(errorMessage).toHaveClass('ds-input__error-message');
    expect(errorMessage).toHaveAttribute('role', 'alert');
    expect(input).toHaveAttribute('aria-describedby', expect.stringContaining('error'));
  });

  test('prioritizes error message over helper text', () => {
    render(
      <Input 
        label="Test Input" 
        helperText="Helper text"
        errorMessage="Error message"
      />
    );
    
    expect(screen.getByText('Error message')).toBeInTheDocument();
    expect(screen.queryByText('Helper text')).not.toBeInTheDocument();
  });

  test('renders with left icon', () => {
    render(<Input label="Search" leftIcon="🔍" />);
    
    const icon = screen.getByText('🔍');
    const input = screen.getByLabelText('Search');
    
    expect(icon).toBeInTheDocument();
    expect(icon).toHaveClass('ds-input__icon', 'ds-input__icon--left');
    expect(icon).toHaveAttribute('aria-hidden', 'true');
    expect(input).toHaveClass('ds-input__field--with-left-icon');
  });

  test('renders with right icon', () => {
    render(<Input label="Website" rightIcon="🌐" />);
    
    const icon = screen.getByText('🌐');
    const input = screen.getByLabelText('Website');
    
    expect(icon).toBeInTheDocument();
    expect(icon).toHaveClass('ds-input__icon', 'ds-input__icon--right');
    expect(icon).toHaveAttribute('aria-hidden', 'true');
    expect(input).toHaveClass('ds-input__field--with-right-icon');
  });

  test('supports different input types', () => {
    const { rerender } = render(<Input label="Email" type="email" />);
    expect(screen.getByLabelText('Email')).toHaveAttribute('type', 'email');
    
    rerender(<Input label="Password" type="password" />);
    expect(screen.getByLabelText('Password')).toHaveAttribute('type', 'password');
    
    rerender(<Input label="Number" type="number" />);
    expect(screen.getByLabelText('Number')).toHaveAttribute('type', 'number');
  });

  test('supports full width', () => {
    render(<Input label="Full Width" fullWidth />);
    
    const container = screen.getByLabelText('Full Width').closest('.ds-input');
    expect(container).toHaveClass('ds-input--full-width');
  });

  test('supports custom className', () => {
    render(<Input label="Custom" className="custom-input" />);
    
    const container = screen.getByLabelText('Custom').closest('.ds-input');
    expect(container).toHaveClass('custom-input');
  });

  test('supports custom id', () => {
    render(<Input label="Custom ID" id="custom-id" />);
    
    const input = screen.getByLabelText('Custom ID');
    expect(input).toHaveAttribute('id', 'custom-id');
  });

  test('generates unique id when not provided', () => {
    render(<Input label="Auto ID" />);
    
    const input = screen.getByLabelText('Auto ID');
    expect(input).toHaveAttribute('id');
    expect(input.id).toMatch(/^:r[a-z0-9]+:/); // React 18+ useId format
  });

  test('builds aria-describedby correctly', () => {
    render(
      <Input 
        label="Test"
        helperText="Helper"
        errorMessage="Error"
        aria-describedby="custom-desc"
      />
    );
    
    const input = screen.getByLabelText('Test');
    const describedBy = input.getAttribute('aria-describedby');
    
    expect(describedBy).toContain('custom-desc');
    expect(describedBy).toContain('error'); // Error takes precedence
  });

  test('handles input events', () => {
    const handleChange = jest.fn();
    render(<Input label="Test" onChange={handleChange} />);
    
    const input = screen.getByLabelText('Test');
    fireEvent.change(input, { target: { value: 'test value' } });
    
    expect(handleChange).toHaveBeenCalledTimes(1);
  });

  test('forwards ref correctly', () => {
    const ref = React.createRef();
    render(<Input label="Ref Input" ref={ref} />);
    
    expect(ref.current).toBeInstanceOf(HTMLInputElement);
  });

  test('passes through additional props', () => {
    render(
      <Input 
        label="Test"
        placeholder="Enter text"
        maxLength={10}
        data-testid="custom-input"
      />
    );
    
    const input = screen.getByLabelText('Test');
    expect(input).toHaveAttribute('placeholder', 'Enter text');
    expect(input).toHaveAttribute('maxLength', '10');
    expect(input).toHaveAttribute('data-testid', 'custom-input');
  });

  test('maintains proper DOM structure', () => {
    render(
      <Input 
        label="Test Input"
        helperText="Helper text"
        leftIcon="🔍"
        rightIcon="✓"
      />
    );
    
    const container = screen.getByLabelText('Test Input').closest('.ds-input');
    const wrapper = container.querySelector('.ds-input__wrapper');
    
    expect(container).toBeInTheDocument();
    expect(wrapper).toBeInTheDocument();
    expect(wrapper.querySelector('.ds-input__icon--left')).toBeInTheDocument();
    expect(wrapper.querySelector('.ds-input__icon--right')).toBeInTheDocument();
    expect(wrapper.querySelector('.ds-input__field')).toBeInTheDocument();
  });

  test('handles empty states gracefully', () => {
    render(<Input />);
    
    const input = screen.getByRole('textbox');
    expect(input).toBeInTheDocument();
    expect(input).toHaveClass('ds-input__field');
  });
});
