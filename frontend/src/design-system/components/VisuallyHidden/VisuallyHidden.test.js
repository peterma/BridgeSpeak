import React from 'react';
import { render, screen } from '@testing-library/react';
import VisuallyHidden from './VisuallyHidden';

describe('VisuallyHidden', () => {
  test('renders with default span element', () => {
    render(<VisuallyHidden>Hidden content</VisuallyHidden>);
    
    const hidden = screen.getByText('Hidden content');
    expect(hidden).toBeInTheDocument();
    expect(hidden.tagName).toBe('SPAN');
    expect(hidden).toHaveClass('ds-visually-hidden');
  });

  test('renders with custom element', () => {
    render(<VisuallyHidden as="div">Hidden div</VisuallyHidden>);
    
    const hidden = screen.getByText('Hidden div');
    expect(hidden.tagName).toBe('DIV');
    expect(hidden).toHaveClass('ds-visually-hidden');
  });

  test('renders with heading element', () => {
    render(<VisuallyHidden as="h1">Hidden heading</VisuallyHidden>);
    
    const hidden = screen.getByText('Hidden heading');
    expect(hidden.tagName).toBe('H1');
    expect(hidden).toHaveClass('ds-visually-hidden');
  });

  test('renders with paragraph element', () => {
    render(<VisuallyHidden as="p">Hidden paragraph</VisuallyHidden>);
    
    const hidden = screen.getByText('Hidden paragraph');
    expect(hidden.tagName).toBe('P');
    expect(hidden).toHaveClass('ds-visually-hidden');
  });

  test('supports custom className', () => {
    render(<VisuallyHidden className="custom-hidden">Custom hidden</VisuallyHidden>);
    
    const hidden = screen.getByText('Custom hidden');
    expect(hidden).toHaveClass('ds-visually-hidden', 'custom-hidden');
  });

  test('forwards ref correctly', () => {
    const ref = React.createRef();
    render(<VisuallyHidden ref={ref}>Ref hidden</VisuallyHidden>);
    
    expect(ref.current).toBeInstanceOf(HTMLSpanElement);
  });

  test('forwards ref correctly with custom element', () => {
    const ref = React.createRef();
    render(<VisuallyHidden as="div" ref={ref}>Ref div</VisuallyHidden>);
    
    expect(ref.current).toBeInstanceOf(HTMLDivElement);
  });

  test('passes through additional props', () => {
    render(
      <VisuallyHidden 
        data-testid="custom-hidden"
        id="hidden-content"
        role="status"
      >
        Custom props
      </VisuallyHidden>
    );
    
    const hidden = screen.getByTestId('custom-hidden');
    expect(hidden).toHaveAttribute('id', 'hidden-content');
    expect(hidden).toHaveAttribute('role', 'status');
  });

  test('renders complex content', () => {
    render(
      <VisuallyHidden>
        <span>Complex</span> hidden <strong>content</strong>
      </VisuallyHidden>
    );
    
    const hidden = screen.getByText('Complex');
    expect(hidden).toBeInTheDocument();
    expect(screen.getByText('hidden')).toBeInTheDocument();
    expect(screen.getByText('content')).toBeInTheDocument();
  });

  test('maintains semantic meaning while being visually hidden', () => {
    render(
      <VisuallyHidden as="h2" id="page-title">
        Page Title for Screen Readers
      </VisuallyHidden>
    );
    
    const hidden = screen.getByText('Page Title for Screen Readers');
    expect(hidden.tagName).toBe('H2');
    expect(hidden).toHaveAttribute('id', 'page-title');
    expect(hidden).toHaveClass('ds-visually-hidden');
  });

  test('works with form elements', () => {
    render(
      <VisuallyHidden as="label" htmlFor="hidden-input">
        Hidden label
      </VisuallyHidden>
    );
    
    const hidden = screen.getByText('Hidden label');
    expect(hidden.tagName).toBe('LABEL');
    expect(hidden).toHaveAttribute('for', 'hidden-input');
  });

  test('renders empty content', () => {
    const { container } = render(<VisuallyHidden />);
    
    const hidden = container.querySelector('.ds-visually-hidden');
    expect(hidden).toBeInTheDocument();
    expect(hidden).toHaveClass('ds-visually-hidden');
    expect(hidden).toBeEmptyDOMElement();
  });

  test('renders with React elements as children', () => {
    const ChildComponent = () => <span>Child component</span>;
    
    render(
      <VisuallyHidden>
        <ChildComponent />
      </VisuallyHidden>
    );
    
    expect(screen.getByText('Child component')).toBeInTheDocument();
  });
});
