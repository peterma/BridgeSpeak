import React from 'react';
import { render, screen } from '@testing-library/react';
import ParentDashboard from './ParentDashboard';

// Mock functions are now handled globally in setupTests.js

const renderWithRouter = (component) => {
  return render(component);
};

describe('ParentDashboard', () => {
  test('renders dashboard title and subtitle', () => {
    renderWithRouter(<ParentDashboard />);
    
    expect(screen.getByText('Welcome Back!')).toBeInTheDocument();
    expect(screen.getByText(/Here's an overview of your child's recent learning activities/)).toBeInTheDocument();
  });

  test('renders quick action shortcuts', () => {
    renderWithRouter(<ParentDashboard />);
    
    expect(screen.getByText('Quick Actions')).toBeInTheDocument();
    expect(screen.getByText('Practice Scenarios')).toBeInTheDocument();
    expect(screen.getByText('Start Conversation')).toBeInTheDocument();
    expect(screen.getByText('Settings')).toBeInTheDocument();
  });

  test('shortcuts have proper links and accessibility', () => {
    renderWithRouter(<ParentDashboard />);
    
    const scenariosLink = screen.getByRole('link', { name: /Practice Scenarios/ });
    const conversationLink = screen.getByRole('link', { name: /Start Conversation/ });
    const settingsLink = screen.getByRole('link', { name: /Settings/ });
    
    expect(scenariosLink).toHaveAttribute('href', '/scenarios');
    expect(conversationLink).toHaveAttribute('href', '/conversation');
    expect(settingsLink).toHaveAttribute('href', '/settings');
    
    // Check for proper ARIA descriptions
    expect(scenariosLink).toHaveAttribute('aria-describedby', 'scenarios-description');
    expect(conversationLink).toHaveAttribute('aria-describedby', 'conversation-description');
    expect(settingsLink).toHaveAttribute('aria-describedby', 'settings-description');
  });

  test('renders recent sessions section', () => {
    renderWithRouter(<ParentDashboard />);
    
    expect(screen.getByText('Recent Learning Sessions')).toBeInTheDocument();
    expect(screen.getByText('Introducing Yourself')).toBeInTheDocument();
    expect(screen.getByText('Asking for Help')).toBeInTheDocument();
    expect(screen.getByText('Playground Games')).toBeInTheDocument();
    expect(screen.getByText('Saying Goodbye')).toBeInTheDocument();
  });

  test('displays session details correctly', () => {
    renderWithRouter(<ParentDashboard />);
    
    // Check for duration information
    expect(screen.getByText('12 minutes')).toBeInTheDocument();
    expect(screen.getByText('8 minutes')).toBeInTheDocument();
    expect(screen.getByText('15 minutes')).toBeInTheDocument();
    expect(screen.getByText('6 minutes')).toBeInTheDocument();
    
    // Check for progress information
    expect(screen.getByText('2 of 3 goals completed')).toBeInTheDocument();
    expect(screen.getByText('4 of 4 goals completed')).toBeInTheDocument();
    expect(screen.getByText('3 of 5 goals completed')).toBeInTheDocument();
    expect(screen.getByText('3 of 3 goals completed')).toBeInTheDocument();
  });

  test('renders session dates in correct format', () => {
    renderWithRouter(<ParentDashboard />);
    
    // Check for formatted dates (these will be in Irish locale format)
    expect(screen.getByText(/Mon, Oct 14/)).toBeInTheDocument();
    expect(screen.getByText(/Sun, Oct 13/)).toBeInTheDocument();
    expect(screen.getByText(/Sat, Oct 12/)).toBeInTheDocument();
    expect(screen.getByText(/Fri, Oct 11/)).toBeInTheDocument();
  });

  test('has proper semantic structure for sessions', () => {
    renderWithRouter(<ParentDashboard />);
    
    // Check for proper list structure
    const sessionsList = screen.getByRole('list', { name: 'Recent learning sessions' });
    expect(sessionsList).toBeInTheDocument();
    
    const sessionItems = screen.getAllByRole('listitem');
    expect(sessionItems).toHaveLength(4);
  });

  test('session items have proper accessibility attributes', () => {
    renderWithRouter(<ParentDashboard />);
    
    const firstSession = screen.getByRole('listitem');
    expect(firstSession).toHaveAttribute('tabIndex', '0');
    expect(firstSession).toHaveAttribute('aria-labelledby', 'session-1-title');
    expect(firstSession).toHaveAttribute('aria-describedby', 'session-1-details');
  });

  test('progress bars have proper ARIA attributes', () => {
    renderWithRouter(<ParentDashboard />);
    
    const progressBars = screen.getAllByRole('progressbar');
    expect(progressBars).toHaveLength(4);
    
    // Check first progress bar attributes
    const firstProgressBar = progressBars[0];
    expect(firstProgressBar).toHaveAttribute('aria-valuenow', '2');
    expect(firstProgressBar).toHaveAttribute('aria-valuemin', '0');
    expect(firstProgressBar).toHaveAttribute('aria-valuemax', '3');
    expect(firstProgressBar).toHaveAttribute('aria-label', 'Progress: 2 out of 3 goals completed');
  });

  test('renders encouragement section', () => {
    renderWithRouter(<ParentDashboard />);
    
    expect(screen.getByText('Keep Going!')).toBeInTheDocument();
    expect(screen.getByText(/Every conversation with Xiao Mei is a step forward/)).toBeInTheDocument();
  });

  test('has proper main landmark', () => {
    renderWithRouter(<ParentDashboard />);
    
    const main = screen.getByRole('main');
    expect(main).toBeInTheDocument();
    expect(main).toHaveClass('parent-dashboard');
  });

  test('has proper section headings with ARIA labels', () => {
    renderWithRouter(<ParentDashboard />);
    
    const shortcutsSection = screen.getByRole('region', { name: /Quick Actions/ });
    const sessionsSection = screen.getByRole('region', { name: /Recent Learning Sessions/ });
    const encouragementSection = screen.getByRole('region', { name: /Keep Going/ });
    
    expect(shortcutsSection).toBeInTheDocument();
    expect(sessionsSection).toBeInTheDocument();
    expect(encouragementSection).toBeInTheDocument();
  });

  test('displays screen reader announcement', () => {
    renderWithRouter(<ParentDashboard />);
    
    const announcement = screen.getByRole('status');
    expect(announcement).toHaveAttribute('aria-live', 'polite');
    expect(announcement).toHaveAttribute('aria-atomic', 'true');
    expect(announcement).toHaveTextContent('Dashboard loaded with 4 recent sessions');
  });

  test('renders icons with proper accessibility', () => {
    renderWithRouter(<ParentDashboard />);
    
    const icons = screen.getAllByText(/🎭|💬|⚙️|⏱️|✅|🌟/);
    expect(icons.length).toBeGreaterThan(0);
    
    // All icons should have aria-hidden="true"
    icons.forEach(icon => {
      expect(icon).toHaveAttribute('aria-hidden', 'true');
    });
  });

  test('handles empty sessions state', () => {
    // This would be tested if we had a way to pass empty sessions
    // For now, we test that the component renders with mock data
    renderWithRouter(<ParentDashboard />);
    
    // Should show sessions, not empty state
    expect(screen.getByText('Recent Learning Sessions')).toBeInTheDocument();
    expect(screen.queryByText('No recent sessions yet')).not.toBeInTheDocument();
  });

  test('has proper heading hierarchy', () => {
    renderWithRouter(<ParentDashboard />);
    
    // Check heading levels
    const h1 = screen.getByRole('heading', { level: 1 });
    expect(h1).toHaveTextContent('Welcome Back!');
    
    const h2s = screen.getAllByRole('heading', { level: 2 });
    expect(h2s).toHaveLength(3);
    expect(h2s[0]).toHaveTextContent('Quick Actions');
    expect(h2s[1]).toHaveTextContent('Recent Learning Sessions');
    expect(h2s[2]).toHaveTextContent('Keep Going!');
    
    const h3s = screen.getAllByRole('heading', { level: 3 });
    expect(h3s.length).toBeGreaterThan(0); // Shortcut titles and session scenarios
  });

  test('shortcut descriptions are properly associated', () => {
    renderWithRouter(<ParentDashboard />);
    
    const scenariosDescription = screen.getByText(/Choose from learning scenarios for your child/);
    const conversationDescription = screen.getByText(/Begin a free-form conversation practice/);
    const settingsDescription = screen.getByText(/Adjust learning preferences and platform/);
    
    expect(scenariosDescription).toHaveAttribute('id', 'scenarios-description');
    expect(conversationDescription).toHaveAttribute('id', 'conversation-description');
    expect(settingsDescription).toHaveAttribute('id', 'settings-description');
  });

  test('session items have proper time elements', () => {
    renderWithRouter(<ParentDashboard />);
    
    const timeElements = screen.getAllByRole('time');
    expect(timeElements).toHaveLength(4);
    
    // Check that time elements have proper dateTime attributes
    timeElements.forEach(timeElement => {
      expect(timeElement).toHaveAttribute('dateTime');
    });
  });
});