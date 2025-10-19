import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { jest } from '@jest/globals';
import StyleGuidePage from './StyleGuidePage';

// Mock the design system components
jest.mock('../design-system', () => ({
  Button: ({ children, onClick, loading, ...props }) => (
    <button onClick={onClick} disabled={loading} {...props}>
      {loading ? 'Loading...' : children}
    </button>
  ),
  Card: ({ children, onClick, ...props }) => (
    <div onClick={onClick} {...props}>
      {children}
    </div>
  ),
  Card: Object.assign(
    ({ children, onClick, ...props }) => (
      <div onClick={onClick} {...props}>
        {children}
      </div>
    ),
    {
      Header: ({ children }) => <header>{children}</header>,
      Title: ({ children }) => <h3>{children}</h3>,
      Subtitle: ({ children }) => <p>{children}</p>,
      Body: ({ children }) => <div>{children}</div>,
      Footer: ({ children }) => <footer>{children}</footer>,
      Actions: ({ children }) => <div>{children}</div>
    }
  ),
  Input: ({ label, value, onChange, errorMessage, ...props }) => (
    <div>
      {label && <label>{label}</label>}
      <input value={value} onChange={onChange} {...props} />
      {errorMessage && <div role="alert">{errorMessage}</div>}
    </div>
  ),
  Chip: ({ children, selected, onClick, onRemove, removable, ...props }) => (
    <span 
      onClick={onClick} 
      aria-pressed={selected}
      {...props}
    >
      {children}
      {removable && (
        <button onClick={onRemove} aria-label={`Remove ${children}`}>
          ×
        </button>
      )}
    </span>
  ),
  SkipLink: ({ children, href }) => (
    <a href={href}>{children}</a>
  ),
  VisuallyHidden: ({ children }) => (
    <span style={{ position: 'absolute', left: '-10000px' }}>
      {children}
    </span>
  )
}));

describe('StyleGuidePage', () => {
  test('renders page title and description', () => {
    render(<StyleGuidePage />);
    
    expect(screen.getByText('Design System Style Guide')).toBeInTheDocument();
    expect(screen.getByText(/Interactive showcase of all design system components/)).toBeInTheDocument();
  });

  test('renders color palette section', () => {
    render(<StyleGuidePage />);
    
    expect(screen.getByText('Color Palette')).toBeInTheDocument();
    expect(screen.getByText('Primary')).toBeInTheDocument();
    expect(screen.getByText('Secondary')).toBeInTheDocument();
    expect(screen.getByText('Accent')).toBeInTheDocument();
    expect(screen.getByText('#E8B4B8')).toBeInTheDocument();
    expect(screen.getByText('#A8D8A8')).toBeInTheDocument();
    expect(screen.getByText('#F4D03F')).toBeInTheDocument();
  });

  test('renders typography section', () => {
    render(<StyleGuidePage />);
    
    expect(screen.getByText('Typography')).toBeInTheDocument();
    expect(screen.getByText('Heading 1 - Main Page Title')).toBeInTheDocument();
    expect(screen.getByText('Heading 2 - Section Title')).toBeInTheDocument();
    expect(screen.getByText('Heading 3 - Subsection Title')).toBeInTheDocument();
    expect(screen.getByText(/Body text - This is regular paragraph text/)).toBeInTheDocument();
    expect(screen.getByText('Small text - Used for helper text and captions')).toBeInTheDocument();
  });

  test('renders button variants', () => {
    render(<StyleGuidePage />);
    
    expect(screen.getByText('Buttons')).toBeInTheDocument();
    expect(screen.getByText('Primary Button')).toBeInTheDocument();
    expect(screen.getByText('Secondary Button')).toBeInTheDocument();
    expect(screen.getByText('Outline Button')).toBeInTheDocument();
    expect(screen.getByText('Ghost Button')).toBeInTheDocument();
    expect(screen.getByText('Danger Button')).toBeInTheDocument();
  });

  test('renders button sizes', () => {
    render(<StyleGuidePage />);
    
    expect(screen.getByText('Small Button')).toBeInTheDocument();
    expect(screen.getByText('Medium Button')).toBeInTheDocument();
    expect(screen.getByText('Large Button')).toBeInTheDocument();
  });

  test('renders button states', () => {
    render(<StyleGuidePage />);
    
    expect(screen.getByText('Normal')).toBeInTheDocument();
    expect(screen.getByText('Disabled')).toBeInTheDocument();
    expect(screen.getByText('Click for Loading')).toBeInTheDocument();
  });

  test('renders buttons with icons', () => {
    render(<StyleGuidePage />);
    
    expect(screen.getByText('Start Journey')).toBeInTheDocument();
    expect(screen.getByText('Continue')).toBeInTheDocument();
    expect(screen.getByText('Favorite')).toBeInTheDocument();
  });

  test('handles loading button demo', async () => {
    render(<StyleGuidePage />);
    
    const loadingButton = screen.getByText('Click for Loading');
    fireEvent.click(loadingButton);
    
    await waitFor(() => {
      expect(screen.getByText('Loading...')).toBeInTheDocument();
    });
  });

  test('renders card examples', () => {
    render(<StyleGuidePage />);
    
    expect(screen.getByText('Cards')).toBeInTheDocument();
    expect(screen.getByText('Basic Card')).toBeInTheDocument();
    expect(screen.getByText('Interactive Card')).toBeInTheDocument();
    expect(screen.getByText('Success Card')).toBeInTheDocument();
  });

  test('renders input examples', () => {
    render(<StyleGuidePage />);
    
    expect(screen.getByText('Inputs')).toBeInTheDocument();
    expect(screen.getByText('Text Input')).toBeInTheDocument();
    expect(screen.getByText('Email Address')).toBeInTheDocument();
    expect(screen.getByText('Password')).toBeInTheDocument();
    expect(screen.getByText('Validation Demo')).toBeInTheDocument();
  });

  test('handles input validation demo', () => {
    render(<StyleGuidePage />);
    
    const validationInput = screen.getByLabelText('Validation Demo');
    fireEvent.change(validationInput, { target: { value: 'ab' } });
    
    expect(screen.getByText('Must be at least 3 characters')).toBeInTheDocument();
  });

  test('renders chip examples', () => {
    render(<StyleGuidePage />);
    
    expect(screen.getByText('Chips')).toBeInTheDocument();
    expect(screen.getByText('Default Chip')).toBeInTheDocument();
    expect(screen.getByText('Primary Chip')).toBeInTheDocument();
    expect(screen.getByLabelText('Toggle React')).toBeInTheDocument();
    expect(screen.getByLabelText('Toggle Accessibility')).toBeInTheDocument();
  });

  test('handles chip interactions', () => {
    render(<StyleGuidePage />);
    
    const reactChip = screen.getByLabelText('Toggle React');
    fireEvent.click(reactChip);
    
    // Should toggle selection
    expect(reactChip).toHaveAttribute('aria-pressed', 'false');
  });

  test('handles chip removal', () => {
    render(<StyleGuidePage />);
    
    const removeButton = screen.getByLabelText('Remove React');
    fireEvent.click(removeButton);
    
    // React chip should be removed from removable chips
    expect(screen.queryByLabelText('Remove React')).not.toBeInTheDocument();
    // But should still be in interactive chips
    expect(screen.getByLabelText('Toggle React')).toBeInTheDocument();
  });

  test('renders utility components section', () => {
    render(<StyleGuidePage />);
    
    expect(screen.getByText('Utility Components')).toBeInTheDocument();
    expect(screen.getByText('SkipLink')).toBeInTheDocument();
    expect(screen.getByText('VisuallyHidden')).toBeInTheDocument();
  });

  test('renders accessibility features section', () => {
    render(<StyleGuidePage />);
    
    expect(screen.getByText('Accessibility Features')).toBeInTheDocument();
    expect(screen.getByText('Focus Management')).toBeInTheDocument();
    expect(screen.getByText('Color Contrast')).toBeInTheDocument();
    expect(screen.getByText('Screen Reader Support')).toBeInTheDocument();
    expect(screen.getByText('Keyboard Navigation')).toBeInTheDocument();
    expect(screen.getByText('Reduced Motion')).toBeInTheDocument();
    expect(screen.getByText('High Contrast Mode')).toBeInTheDocument();
  });

  test('renders with proper semantic structure', () => {
    render(<StyleGuidePage />);
    
    // Check for main landmark
    const main = screen.getByRole('main');
    expect(main).toBeInTheDocument();
    
    // Check for proper headings hierarchy
    expect(screen.getByRole('heading', { level: 1 })).toHaveTextContent('Design System Style Guide');
    
    const h2s = screen.getAllByRole('heading', { level: 2 });
    expect(h2s.length).toBeGreaterThan(0);
    
    const h3s = screen.getAllByRole('heading', { level: 3 });
    expect(h3s.length).toBeGreaterThan(0);
  });

  test('renders sections with proper ARIA labels', () => {
    render(<StyleGuidePage />);
    
    const sections = screen.getAllByRole('region');
    expect(sections.length).toBeGreaterThan(0);
    
    // Check that sections have proper aria-labelledby
    sections.forEach(section => {
      expect(section).toHaveAttribute('aria-labelledby');
    });
  });

  test('renders skip link', () => {
    render(<StyleGuidePage />);
    
    const skipLink = screen.getByRole('link', { name: 'Skip to main content' });
    expect(skipLink).toBeInTheDocument();
    expect(skipLink).toHaveAttribute('href', '#main-content');
  });

  test('renders visually hidden content', () => {
    render(<StyleGuidePage />);
    
    // VisuallyHidden content should be present but not visible
    const hiddenContent = screen.getByText('This text is hidden visually but available to screen readers');
    expect(hiddenContent).toBeInTheDocument();
  });

  test('renders interactive examples', () => {
    render(<StyleGuidePage />);
    
    // Check for interactive elements
    const buttons = screen.getAllByRole('button');
    expect(buttons.length).toBeGreaterThan(0);
    
    const inputs = screen.getAllByRole('textbox');
    expect(inputs.length).toBeGreaterThan(0);
  });

  test('maintains component state across interactions', () => {
    render(<StyleGuidePage />);
    
    // Test that input state is maintained
    const validationInput = screen.getByLabelText('Validation Demo');
    fireEvent.change(validationInput, { target: { value: 'test' } });
    
    expect(validationInput).toHaveValue('test');
  });

  test('renders all component variants', () => {
    render(<StyleGuidePage />);
    
    // Verify that all major component variants are shown
    expect(screen.getByText('Variants')).toBeInTheDocument();
    expect(screen.getByText('Sizes')).toBeInTheDocument();
    expect(screen.getByText('States')).toBeInTheDocument();
    
    // Check for both "With Icons" sections (buttons and inputs)
    const withIconsHeadings = screen.getAllByText('With Icons');
    expect(withIconsHeadings.length).toBe(2);
  });
});
