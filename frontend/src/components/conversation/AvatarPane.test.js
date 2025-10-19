import React from 'react';
import { render, screen } from '@testing-library/react';
import AvatarPane from './AvatarPane';

describe('AvatarPane Component', () => {
  test('renders Xiao Mei avatar with correct name and description', () => {
    render(<AvatarPane isActive={false} connectionState="disconnected" />);

    expect(screen.getByText('Xiao Mei (小美)')).toBeInTheDocument();
    expect(screen.getByText('Your friendly English learning companion')).toBeInTheDocument();
  });

  test('displays appropriate status text based on active state', () => {
    const { rerender } = render(<AvatarPane isActive={false} connectionState="disconnected" />);
    
    expect(screen.getByText('Press start to begin')).toBeInTheDocument();

    rerender(<AvatarPane isActive={true} connectionState="connected" />);
    expect(screen.getByText('Ready to chat!')).toBeInTheDocument();
  });

  test('has proper accessibility labels and roles', () => {
    render(<AvatarPane isActive={true} connectionState="connected" />);

    const avatarRegion = screen.getByRole('region', { name: 'Xiao Mei Avatar' });
    expect(avatarRegion).toBeInTheDocument();

    const statusElement = screen.getByRole('status');
    expect(statusElement).toBeInTheDocument();
  });

  test('announces connection state changes for screen readers', () => {
    const { rerender } = render(<AvatarPane isActive={false} connectionState="disconnected" />);
    
    // Check for disconnected state
    expect(screen.getByText('Disconnected from Xiao Mei')).toBeInTheDocument();

    // Test connecting state
    rerender(<AvatarPane isActive={false} connectionState="connecting" />);
    expect(screen.getByText('Connecting to Xiao Mei...')).toBeInTheDocument();

    // Test connected state
    rerender(<AvatarPane isActive={true} connectionState="connected" />);
    expect(screen.getByText('Connected to Xiao Mei')).toBeInTheDocument();
  });

  test('applies correct CSS classes based on active state', () => {
    const { container, rerender } = render(<AvatarPane isActive={false} connectionState="disconnected" />);
    
    const avatarPlaceholder = container.querySelector('.avatar-placeholder');
    expect(avatarPlaceholder).toHaveClass('idle');
    expect(avatarPlaceholder).not.toHaveClass('active');

    rerender(<AvatarPane isActive={true} connectionState="connected" />);
    expect(avatarPlaceholder).toHaveClass('active');
    expect(avatarPlaceholder).not.toHaveClass('idle');
  });

  test('displays connection indicator with appropriate state', () => {
    const { container, rerender } = render(<AvatarPane isActive={false} connectionState="disconnected" />);
    
    const indicator = container.querySelector('.connection-indicator');
    expect(indicator).toHaveClass('disconnected');

    rerender(<AvatarPane isActive={false} connectionState="connecting" />);
    expect(indicator).toHaveClass('connecting');

    rerender(<AvatarPane isActive={true} connectionState="connected" />);
    expect(indicator).toHaveClass('connected');
  });

  test('has appropriate aria-live regions for dynamic content', () => {
    render(<AvatarPane isActive={true} connectionState="connected" />);

    const liveRegions = screen.getAllByRole('status');
    expect(liveRegions.length).toBeGreaterThan(0);
    
    // Check that the main avatar placeholder has aria-live
    const avatarElement = screen.getByLabelText(/Xiao Mei is/);
    expect(avatarElement).toHaveAttribute('aria-live', 'polite');
  });
});