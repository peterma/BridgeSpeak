/**
 * Test for VideoConversation sample sentence deduplication
 * Tests the fix for bug #55 - duplicate sample sentences
 */

import React from 'react';
import { render, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import VideoConversation from './VideoConversation';

// Mock the transcript loader to return test data with duplicates
jest.mock('../data/transcriptLoader', () => ({
  getTranscriptMetadata: jest.fn(() => [
    { transcriptId: 'test1', ageGroup: 'senior-infants', variant: 'variant1' },
    { transcriptId: 'test2', ageGroup: 'senior-infants', variant: 'variant2' }
  ]),
  loadTranscript: jest.fn((id) => {
    // Return transcript data with duplicate sentences
    return Promise.resolve({
      messages: [
        {
          phase: 'child_practice',
          content: 'Hello, I am Li Wei. I am 6 years old.',
          language: 'en-IE'
        },
        {
          phase: 'child_practice', 
          content: 'Hello, I am Li Wei. I am 6 years old.', // Duplicate
          language: 'en-IE'
        },
        {
          phase: 'child_practice',
          content: 'My name is Sarah.',
          language: 'en-IE'
        }
      ]
    });
  })
}));

// Mock the scenarios data
jest.mock('../data/scenarios', () => ({
  mockScenarios: [
    { id: 'intro-yourself', title: 'Introducing Yourself' }
  ]
}));

// Mock the hybrid TTS service
jest.mock('../services/hybridTTS', () => ({
  __esModule: true,
  default: {
    isAvailable: () => false,
    getStatus: () => ({ available: false }),
    checkPipecatAvailability: () => Promise.resolve(),
    preloadAudio: () => Promise.resolve()
  }
}));

// Mock the WebRTC client
jest.mock('../webrtc-client', () => ({
  WebRTCClient: jest.fn()
}));

describe('VideoConversation - Sample Sentence Deduplication', () => {
  test('should not display duplicate sample sentences', async () => {
    // Mock URL search params to include a scenario
    const mockSearchParams = new URLSearchParams('?scenario=intro-yourself');
    jest.spyOn(URLSearchParams.prototype, 'get').mockImplementation((key) => {
      return mockSearchParams.get(key);
    });

    const { container } = render(
      <BrowserRouter>
        <VideoConversation />
      </BrowserRouter>
    );

    // Wait for sample sentences to load
    await waitFor(() => {
      const sampleSentences = container.querySelectorAll('.sample-sentence-item');
      expect(sampleSentences.length).toBeGreaterThan(0);
    }, { timeout: 3000 });

    // Get all sample sentence text content
    const sampleTexts = Array.from(container.querySelectorAll('.sample-text'))
      .map(el => el.textContent);

    // Check that there are no duplicates
    const uniqueTexts = [...new Set(sampleTexts)];
    expect(sampleTexts.length).toBe(uniqueTexts.length);

    // Specifically check that the duplicate sentence appears only once
    const duplicateSentenceCount = sampleTexts.filter(text => 
      text.includes('Hello, I am Li Wei. I am 6 years old.')
    ).length;
    expect(duplicateSentenceCount).toBe(1);
  });

  test('should handle empty transcript data gracefully', async () => {
    // Override the mock to return empty transcript
    const { loadTranscript } = require('../data/transcriptLoader');
    loadTranscript.mockImplementation(() => Promise.resolve({ messages: [] }));

    const mockSearchParams = new URLSearchParams('?scenario=intro-yourself');
    jest.spyOn(URLSearchParams.prototype, 'get').mockImplementation((key) => {
      return mockSearchParams.get(key);
    });

    const { container } = render(
      <BrowserRouter>
        <VideoConversation />
      </BrowserRouter>
    );

    // Wait for loading to complete
    await waitFor(() => {
      const noExamplesText = container.querySelector('.muted');
      expect(noExamplesText).toBeInTheDocument();
      expect(noExamplesText.textContent).toBe('No examples available');
    }, { timeout: 3000 });
  });
});