import React from 'react';
import { render, screen } from '@testing-library/react';
import NotFound from './NotFound';

// Mock functions are now handled globally in setupTests.js

function renderWithRouter(ui, { initialEntries = ['/'] } = {}) {
  return render(ui);
}

describe('NotFound Component', () => {
  test('renders 404 page content', () => {
    renderWithRouter(<NotFound />);

    expect(screen.getByRole('heading', { name: /page not found/i })).toBeInTheDocument();
    expect(screen.getByText(/sorry, we couldn't find the page/i)).toBeInTheDocument();
  });

  test('provides navigation links back to main areas', () => {
    renderWithRouter(<NotFound />);

    const homeLink = screen.getByRole('link', { name: /go home/i });
    const conversationLink = screen.getByRole('link', { name: /start conversation/i });

    expect(homeLink).toBeInTheDocument();
    expect(homeLink).toHaveAttribute('href', '/');
    
    expect(conversationLink).toBeInTheDocument();
    expect(conversationLink).toHaveAttribute('href', '/conversation');
  });

  test('has accessible and user-friendly messaging', () => {
    renderWithRouter(<NotFound />);

    // Should have encouraging, child-friendly messaging
    expect(screen.getByText(/let's get you back to learning/i)).toBeInTheDocument();
    
    // Should not have intimidating or negative language
    const content = screen.getByText(/sorry, we couldn't find the page/i);
    expect(content).toBeInTheDocument();
    expect(content.textContent).not.toMatch(/error|failed|broken/i);
  });
});