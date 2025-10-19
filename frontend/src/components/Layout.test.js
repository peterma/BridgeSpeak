import React from 'react';
import { render, screen } from '@testing-library/react';
import Layout from './Layout';

// Mock functions are now handled globally in setupTests.js

// Helper function to render with router
function renderWithRouter(ui, { initialEntries = ['/'] } = {}) {
  return render(ui);
}

describe('Layout Component', () => {
  test('renders main navigation elements', () => {
    renderWithRouter(
      <Layout>
        <div>Test Content</div>
      </Layout>
    );

    // Check for main structural elements
    expect(screen.getByRole('banner')).toBeInTheDocument();
    expect(screen.getByRole('main')).toBeInTheDocument();
    expect(screen.getByRole('contentinfo')).toBeInTheDocument();
    expect(screen.getByRole('navigation')).toBeInTheDocument();

    // Check for navigation links
    expect(screen.getByRole('link', { name: /home/i })).toBeInTheDocument();
    expect(screen.getByRole('link', { name: /conversation/i })).toBeInTheDocument();
    expect(screen.getByRole('link', { name: /scenarios/i })).toBeInTheDocument();
    expect(screen.getByRole('link', { name: /dashboard/i })).toBeInTheDocument();
  });

  test('renders skip link for accessibility', () => {
    renderWithRouter(
      <Layout>
        <div>Test Content</div>
      </Layout>
    );

    const skipLink = screen.getByRole('link', { name: /skip to main content/i });
    expect(skipLink).toBeInTheDocument();
    expect(skipLink).toHaveAttribute('href', '#main-content');
  });

  test('renders children content in main area', () => {
    renderWithRouter(
      <Layout>
        <div data-testid="child-content">Test Child Content</div>
      </Layout>
    );

    const childContent = screen.getByTestId('child-content');
    expect(childContent).toBeInTheDocument();
    expect(childContent.textContent).toBe('Test Child Content');
    
    // Ensure child content is within main element
    const mainElement = screen.getByRole('main');
    expect(mainElement).toContainElement(childContent);
  });

  test('navigation has proper ARIA labels', () => {
    renderWithRouter(
      <Layout>
        <div>Test Content</div>
      </Layout>
    );

    const navigation = screen.getByRole('navigation');
    expect(navigation).toHaveAttribute('aria-label', 'Main navigation');
  });

  test('main content has proper ID for skip link', () => {
    renderWithRouter(
      <Layout>
        <div>Test Content</div>
      </Layout>
    );

    const mainContent = screen.getByRole('main');
    expect(mainContent).toHaveAttribute('id', 'main-content');
  });
});