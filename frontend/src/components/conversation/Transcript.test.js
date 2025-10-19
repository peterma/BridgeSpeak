import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import Transcript from './Transcript';

// Mock speech synthesis
const mockSpeechSynthesis = {
  speak: jest.fn(),
  cancel: jest.fn(),
  getVoices: jest.fn(() => [])
};

const mockSpeechSynthesisUtterance = jest.fn().mockImplementation((text) => {
  const utterance = {
    text,
    rate: 1,
    pitch: 1,
    volume: 1,
    lang: 'en',
    onstart: jest.fn(),
    onend: jest.fn(),
    onerror: jest.fn()
  };
  return utterance;
});

// Mock scrollIntoView
const mockScrollIntoView = jest.fn();

// Mock window.speechSynthesis and scrollIntoView
Object.defineProperty(window, 'speechSynthesis', {
  writable: true,
  value: mockSpeechSynthesis
});

Object.defineProperty(window, 'SpeechSynthesisUtterance', {
  writable: true,
  value: mockSpeechSynthesisUtterance
});

// Mock Element.prototype.scrollIntoView
Object.defineProperty(Element.prototype, 'scrollIntoView', {
  writable: true,
  value: mockScrollIntoView
});

const sampleMessages = [
  {
    id: 1,
    role: 'assistant',
    content: '你好! 我是小美。让我们学习如何介绍自己。',
    timestamp: 1760574005.6508672,
    language: 'zh-CN'
  },
  {
    id: 2,
    role: 'user',
    content: 'Hello, I am Li Wei. I am 6 years old.',
    timestamp: 1760574011.6508672,
    language: 'en-IE'
  },
  {
    id: 3,
    role: 'assistant',
    content: '太棒了! You\'re getting better! Well done!',
    timestamp: 1760574014.6508672,
    language: 'mixed'
  }
];

const defaultProps = {
  messages: [],
  isActive: false,
  isSampleTranscript: false
};

describe('Transcript Component', () => {
  beforeEach(() => {
    jest.clearAllMocks();
    mockSpeechSynthesis.speak.mockClear();
    mockSpeechSynthesis.cancel.mockClear();
    mockScrollIntoView.mockClear();
    mockSpeechSynthesisUtterance.mockClear();
  });

  test('renders empty transcript when no messages', () => {
    render(<Transcript {...defaultProps} />);

    expect(screen.getByText('Start a conversation to see the transcript')).toBeInTheDocument();
    expect(screen.getByRole('region', { name: 'Conversation Transcript' })).toBeInTheDocument();
  });

  test('renders messages correctly', () => {
    render(<Transcript {...defaultProps} messages={sampleMessages} />);

    expect(screen.getByText('你好! 我是小美。让我们学习如何介绍自己。')).toBeInTheDocument();
    expect(screen.getByText('Hello, I am Li Wei. I am 6 years old.')).toBeInTheDocument();
    expect(screen.getByText('太棒了! You\'re getting better! Well done!')).toBeInTheDocument();
  });

  test('displays correct role labels', () => {
    render(<Transcript {...defaultProps} messages={sampleMessages} />);

    expect(screen.getAllByText('Xiao Mei')).toHaveLength(2);
    expect(screen.getByText('You')).toBeInTheDocument();
  });

  test('shows play buttons only for sample transcripts', () => {
    const { rerender } = render(<Transcript {...defaultProps} messages={sampleMessages} />);
    
    // Should not show play buttons for regular transcripts
    expect(screen.queryByRole('button', { name: /play message/i })).not.toBeInTheDocument();

    // Should show play buttons for sample transcripts
    rerender(<Transcript {...defaultProps} messages={sampleMessages} isSampleTranscript={true} />);
    
    const playButtons = screen.getAllByRole('button', { name: /play message/i });
    expect(playButtons).toHaveLength(3);
  });

  test('play button calls speech synthesis when clicked', async () => {
    render(<Transcript {...defaultProps} messages={sampleMessages} isSampleTranscript={true} />);

    const playButtons = screen.getAllByRole('button', { name: /play message/i });
    fireEvent.click(playButtons[0]);

    await waitFor(() => {
      expect(mockSpeechSynthesisUtterance).toHaveBeenCalledWith('你好! 我是小美。让我们学习如何介绍自己。');
      expect(mockSpeechSynthesis.speak).toHaveBeenCalled();
    });
  });

  test('play button stops current speech when clicked again', async () => {
    render(<Transcript {...defaultProps} messages={sampleMessages} isSampleTranscript={true} />);

    const playButtons = screen.getAllByRole('button', { name: /play message/i });
    
    // First click starts speech
    fireEvent.click(playButtons[0]);
    
    await waitFor(() => {
      expect(mockSpeechSynthesis.speak).toHaveBeenCalledTimes(1);
    });

    // Simulate speech start to set speaking state
    const utterance = mockSpeechSynthesisUtterance.mock.results[0].value;
    utterance.onstart();

    // Second click stops speech
    fireEvent.click(playButtons[0]);
    
    await waitFor(() => {
      expect(mockSpeechSynthesis.cancel).toHaveBeenCalled();
    });
  });

  test('play button changes to stop button when speaking', async () => {
    render(<Transcript {...defaultProps} messages={sampleMessages} isSampleTranscript={true} />);

    const playButton = screen.getAllByRole('button', { name: /play message/i })[0];
    
    // Initially shows play icon
    expect(playButton).toHaveTextContent('🔊');

    // Click to start speaking
    fireEvent.click(playButton);

    // Simulate speech start
    const utterance = mockSpeechSynthesisUtterance.mock.results[0].value;
    utterance.onstart();

    await waitFor(() => {
      expect(playButton).toHaveTextContent('⏸️');
    });
  });

  test('handles speech synthesis errors gracefully', async () => {
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});
    
    render(<Transcript {...defaultProps} messages={sampleMessages} isSampleTranscript={true} />);

    const playButton = screen.getAllByRole('button', { name: /play message/i })[0];
    fireEvent.click(playButton);

    // Simulate speech error
    const utterance = mockSpeechSynthesisUtterance.mock.results[0].value;
    utterance.onerror({ error: 'synthesis-failed' });

    await waitFor(() => {
      expect(consoleSpy).toHaveBeenCalledWith('Speech synthesis error:', { error: 'synthesis-failed' });
    });

    consoleSpy.mockRestore();
  });

  test('sets correct language for speech synthesis', async () => {
    render(<Transcript {...defaultProps} messages={sampleMessages} isSampleTranscript={true} />);

    const playButtons = screen.getAllByRole('button', { name: /play message/i });
    
    // Test Chinese message
    fireEvent.click(playButtons[0]);
    let utterance = mockSpeechSynthesisUtterance.mock.results[0].value;
    expect(utterance.lang).toBe('zh-CN');

    // Test English message
    fireEvent.click(playButtons[1]);
    utterance = mockSpeechSynthesisUtterance.mock.results[1].value;
    expect(utterance.lang).toBe('en-IE');

    // Test mixed language message
    fireEvent.click(playButtons[2]);
    utterance = mockSpeechSynthesisUtterance.mock.results[2].value;
    expect(utterance.lang).toBe('mixed');
  });

  test('uses default language when message language is not specified', async () => {
    const messagesWithoutLanguage = [
      {
        id: 1,
        role: 'assistant',
        content: 'Hello, how are you?',
        timestamp: 1760574005.6508672
      }
    ];

    render(<Transcript {...defaultProps} messages={messagesWithoutLanguage} isSampleTranscript={true} />);

    const playButton = screen.getByRole('button', { name: /play message/i });
    fireEvent.click(playButton);

    const utterance = mockSpeechSynthesisUtterance.mock.results[0].value;
    expect(utterance.lang).toBe('en-IE');
  });

  test('configures speech synthesis with correct settings', async () => {
    render(<Transcript {...defaultProps} messages={sampleMessages} isSampleTranscript={true} />);

    const playButton = screen.getAllByRole('button', { name: /play message/i })[0];
    fireEvent.click(playButton);

    const utterance = mockSpeechSynthesisUtterance.mock.results[0].value;
    expect(utterance.rate).toBe(0.9);
    expect(utterance.pitch).toBe(1.0);
    expect(utterance.volume).toBe(0.8);
  });

  test('handles missing speech synthesis gracefully', () => {
    // Mock missing speech synthesis
    Object.defineProperty(window, 'speechSynthesis', {
      writable: true,
      value: undefined
    });

    const consoleSpy = jest.spyOn(console, 'warn').mockImplementation(() => {});

    render(<Transcript {...defaultProps} messages={sampleMessages} isSampleTranscript={true} />);

    const playButton = screen.getAllByRole('button', { name: /play message/i })[0];
    fireEvent.click(playButton);

    expect(consoleSpy).toHaveBeenCalledWith('Speech synthesis not available');
    expect(mockSpeechSynthesis.speak).not.toHaveBeenCalled();

    consoleSpy.mockRestore();
  });

  test('displays language tags for messages with language specified', () => {
    render(<Transcript {...defaultProps} messages={sampleMessages} />);

    expect(screen.getByText('zh-CN')).toBeInTheDocument();
    expect(screen.getByText('mixed')).toBeInTheDocument();
    expect(screen.getByText('en-IE')).toBeInTheDocument(); // All messages with language specified show language tag
  });

  test('formats timestamps correctly', () => {
    render(<Transcript {...defaultProps} messages={sampleMessages} />);

    // Check that timestamps are displayed (exact format may vary by locale)
    const timeElements = screen.getAllByRole('time');
    expect(timeElements).toHaveLength(3);
    
    timeElements.forEach(timeElement => {
      expect(timeElement).toHaveAttribute('dateTime');
    });
  });

  test('has proper accessibility attributes', () => {
    render(<Transcript {...defaultProps} messages={sampleMessages} isSampleTranscript={true} />);

    // Check main region
    expect(screen.getByRole('region', { name: 'Conversation Transcript' })).toBeInTheDocument();
    
    // Check message log
    expect(screen.getByRole('log', { name: 'Conversation messages' })).toBeInTheDocument();
    
    // Check play buttons have proper labels
    const playButtons = screen.getAllByRole('button', { name: /play message/i });
    playButtons.forEach(button => {
      expect(button).toHaveAttribute('aria-label');
      expect(button).toHaveAttribute('title');
    });
  });

  test('shows correct status badge based on isActive prop', () => {
    const { rerender } = render(<Transcript {...defaultProps} isActive={false} />);
    
    expect(screen.getByText('Stopped')).toBeInTheDocument();

    rerender(<Transcript {...defaultProps} isActive={true} />);
    
    expect(screen.getByText('Recording')).toBeInTheDocument();
  });

  test('clear transcript button is disabled when no messages', () => {
    render(<Transcript {...defaultProps} messages={[]} />);

    const clearButton = screen.getByRole('button', { name: /clear conversation transcript/i });
    expect(clearButton).toBeDisabled();
  });

  test('clear transcript button is enabled when messages exist', () => {
    render(<Transcript {...defaultProps} messages={sampleMessages} />);

    const clearButton = screen.getByRole('button', { name: /clear conversation transcript/i });
    expect(clearButton).not.toBeDisabled();
  });
});
