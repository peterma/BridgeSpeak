import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Controls from './Controls';

const defaultProps = {
  isActive: false,
  onStart: jest.fn(),
  onStop: jest.fn(),
  isMicEnabled: true,
  onMicToggle: jest.fn(),
  connectionState: 'disconnected'
};

describe('Controls Component', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders start button when conversation is not active', () => {
    render(<Controls {...defaultProps} />);

    const startButton = screen.getByRole('button', { name: /start conversation/i });
    expect(startButton).toBeInTheDocument();
    expect(startButton).not.toBeDisabled();
  });

  test('renders stop button when conversation is active', () => {
    render(<Controls {...defaultProps} isActive={true} connectionState="connected" />);

    const stopButton = screen.getByRole('button', { name: /stop conversation/i });
    expect(stopButton).toBeInTheDocument();
  });

  test('calls onStart when start button is clicked', () => {
    render(<Controls {...defaultProps} />);

    const startButton = screen.getByRole('button', { name: /start conversation/i });
    fireEvent.click(startButton);

    expect(defaultProps.onStart).toHaveBeenCalledTimes(1);
  });

  test('calls onStop when stop button is clicked', () => {
    render(<Controls {...defaultProps} isActive={true} connectionState="connected" />);

    const stopButton = screen.getByRole('button', { name: /stop conversation/i });
    fireEvent.click(stopButton);

    expect(defaultProps.onStop).toHaveBeenCalledTimes(1);
  });

  test('microphone button shows correct state and is properly labeled', () => {
    const { rerender } = render(<Controls {...defaultProps} isActive={true} isMicEnabled={true} />);

    let micButton = screen.getByRole('button', { name: /microphone is on/i });
    expect(micButton).toBeInTheDocument();
    expect(micButton).toHaveTextContent('Mic On');

    rerender(<Controls {...defaultProps} isActive={true} isMicEnabled={false} />);
    micButton = screen.getByRole('button', { name: /microphone is off/i });
    expect(micButton).toHaveTextContent('Mic Off');
  });

  test('calls onMicToggle when microphone button is clicked', () => {
    render(<Controls {...defaultProps} isActive={true} />);

    const micButton = screen.getByRole('button', { name: /microphone is/i });
    fireEvent.click(micButton);

    expect(defaultProps.onMicToggle).toHaveBeenCalledTimes(1);
  });

  test('microphone button is disabled when conversation is not active', () => {
    render(<Controls {...defaultProps} isActive={false} />);

    const micButton = screen.getByRole('button', { name: /microphone is/i });
    expect(micButton).toBeDisabled();
  });

  test('start button is disabled when connecting', () => {
    render(<Controls {...defaultProps} connectionState="connecting" />);

    const startButton = screen.getByRole('button', { name: /connecting/i });
    expect(startButton).toBeDisabled();
    expect(startButton).toHaveTextContent('Connecting...');
  });

  test('handles keyboard events correctly', () => {
    render(<Controls {...defaultProps} />);

    const startButton = screen.getByRole('button', { name: /start conversation/i });
    
    // Test Enter key
    fireEvent.keyDown(startButton, { key: 'Enter' });
    expect(defaultProps.onStart).toHaveBeenCalledTimes(1);

    // Test Space key
    fireEvent.keyDown(startButton, { key: ' ' });
    expect(defaultProps.onStart).toHaveBeenCalledTimes(2);
  });

  test('displays connection status correctly', () => {
    const { container, rerender } = render(<Controls {...defaultProps} connectionState="disconnected" />);
    
    let statusLabel = container.querySelector('.connection-status .status-label');
    expect(statusLabel).toHaveTextContent('Disconnected');

    rerender(<Controls {...defaultProps} connectionState="connecting" />);
    statusLabel = container.querySelector('.connection-status .status-label');
    expect(statusLabel).toHaveTextContent('Connecting...');

    rerender(<Controls {...defaultProps} connectionState="connected" />);
    statusLabel = container.querySelector('.connection-status .status-label');
    expect(statusLabel).toHaveTextContent('Connected');
  });

  test('has proper accessibility structure with regions and descriptions', () => {
    render(<Controls {...defaultProps} />);

    const controlsRegion = screen.getByRole('region', { name: 'Conversation Controls' });
    expect(controlsRegion).toBeInTheDocument();

    // Check for help text associations
    const startButton = screen.getByRole('button', { name: /start conversation/i });
    expect(startButton).toHaveAttribute('aria-describedby', 'start-button-help');
  });

  test('announces state changes for screen readers', () => {
    const { container, rerender } = render(<Controls {...defaultProps} isActive={false} />);

    // Test conversation started announcement
    rerender(<Controls {...defaultProps} isActive={true} connectionState="connected" />);
    const statusElement = container.querySelector('[aria-live="polite"][role="status"]');
    expect(statusElement).toHaveTextContent('Conversation started');
    expect(statusElement).toHaveTextContent('Microphone enabled');
  });

  test('applies correct CSS classes based on microphone state', () => {
    const { container, rerender } = render(<Controls {...defaultProps} isActive={true} isMicEnabled={true} />);
    
    let micButton = container.querySelector('.mic-on');
    expect(micButton).toBeInTheDocument();

    rerender(<Controls {...defaultProps} isActive={true} isMicEnabled={false} />);
    micButton = container.querySelector('.mic-off');
    expect(micButton).toBeInTheDocument();
  });
});