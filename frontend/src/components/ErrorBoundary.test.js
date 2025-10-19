import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import ErrorBoundary from './ErrorBoundary';

// Component that throws an error for testing
function ThrowError({ shouldThrow }) {
  if (shouldThrow) {
    throw new Error('Test error for ErrorBoundary');
  }
  return <div>Normal content</div>;
}

describe('ErrorBoundary Component', () => {
  // Suppress console.error for these tests
  const originalError = console.error;
  beforeAll(() => {
    console.error = jest.fn();
  });
  afterAll(() => {
    console.error = originalError;
  });

  test('renders children when there is no error', () => {
    render(
      <ErrorBoundary>
        <ThrowError shouldThrow={false} />
      </ErrorBoundary>
    );

    expect(screen.getByText('Normal content')).toBeInTheDocument();
  });

  test('renders error UI when child component throws', () => {
    render(
      <ErrorBoundary>
        <ThrowError shouldThrow={true} />
      </ErrorBoundary>
    );

    expect(screen.getByRole('alert')).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: /something went wrong/i })).toBeInTheDocument();
    expect(screen.getByText(/we're sorry, but something unexpected happened/i)).toBeInTheDocument();
  });

  test('provides refresh button when error occurs', () => {
    // Mock window.location.reload
    delete window.location;
    window.location = { reload: jest.fn() };

    render(
      <ErrorBoundary>
        <ThrowError shouldThrow={true} />
      </ErrorBoundary>
    );

    const refreshButton = screen.getByRole('button', { name: /refresh page/i });
    expect(refreshButton).toBeInTheDocument();

    fireEvent.click(refreshButton);
    expect(window.location.reload).toHaveBeenCalled();
  });

  test('shows technical details in collapsible section', () => {
    render(
      <ErrorBoundary>
        <ThrowError shouldThrow={true} />
      </ErrorBoundary>
    );

    const details = screen.getByText(/technical details/i);
    expect(details).toBeInTheDocument();
    
    // Should be a details/summary element for collapsible behavior
    expect(details.closest('details')).toBeInTheDocument();
  });

  test('has trauma-informed, gentle error messaging', () => {
    render(
      <ErrorBoundary>
        <ThrowError shouldThrow={true} />
      </ErrorBoundary>
    );

    // Should not have harsh or blame-oriented language
    const errorContent = screen.getByRole('alert').textContent;
    expect(errorContent).not.toMatch(/failed|broken|your fault|wrong with you/i);
    
    // Should have encouraging, supportive language
    expect(screen.getByText(/we're sorry/i)).toBeInTheDocument();
    expect(screen.getByText(/try refreshing/i)).toBeInTheDocument();
  });
});