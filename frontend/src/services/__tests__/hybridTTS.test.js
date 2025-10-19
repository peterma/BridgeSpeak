import hybridTTS from '../hybridTTS';
import cartesiaTTS from '../cartesiaTTS';

// Mock cartesiaTTS
jest.mock('../cartesiaTTS', () => ({
  isAvailable: true,
  speak: jest.fn(),
  generateAudio: jest.fn(),
  getCacheStats: jest.fn(() => ({ size: 0, keys: [] })),
  clearCache: jest.fn()
}));

// Mock Web Speech API
const mockSpeechSynthesis = {
  speak: jest.fn(),
  cancel: jest.fn(),
  speaking: false
};

const mockSpeechSynthesisUtterance = jest.fn().mockImplementation((text) => ({
  text,
  rate: 1,
  pitch: 1,
  volume: 1,
  lang: 'en',
  onstart: null,
  onend: null,
  onerror: null
}));

Object.defineProperty(window, 'speechSynthesis', {
  writable: true,
  value: mockSpeechSynthesis
});

Object.defineProperty(window, 'SpeechSynthesisUtterance', {
  writable: true,
  value: mockSpeechSynthesisUtterance
});

describe('HybridTTSService', () => {
  beforeEach(() => {
    jest.clearAllMocks();
    mockSpeechSynthesis.speaking = false;
    hybridTTS.isSpeaking = false;
    hybridTTS.speakingText = null;
  });

  describe('Initialization', () => {
    test('should initialize with available services', () => {
      const status = hybridTTS.getStatus();
      expect(status.cartesiaAvailable).toBe(true);
      expect(status.webSpeechAvailable).toBe(true);
      expect(status.availableServices).toContain('cartesia');
      expect(status.availableServices).toContain('web-speech');
    });

    test('should detect when services are not available', () => {
      // Mock cartesia as unavailable
      cartesiaTTS.isAvailable = false;
      Object.defineProperty(window, 'speechSynthesis', {
        writable: true,
        value: undefined
      });

      const service = new (hybridTTS.constructor)();
      expect(service.isAvailable()).toBe(false);
      expect(service.getAvailableServices()).toEqual([]);
    });
  });

  describe('Speech Synthesis', () => {
    test('should use Cartesia when available', async () => {
      cartesiaTTS.speak.mockResolvedValue();
      
      await hybridTTS.speak('Hello world', 'en-IE');
      
      expect(cartesiaTTS.speak).toHaveBeenCalledWith('Hello world', 'en-IE');
      expect(mockSpeechSynthesis.speak).not.toHaveBeenCalled();
    });

    test('should fallback to Web Speech API when Cartesia fails', async () => {
      cartesiaTTS.speak.mockRejectedValue(new Error('Cartesia error'));
      
      // Mock successful Web Speech API
      const mockUtterance = {
        onstart: null,
        onend: null,
        onerror: null
      };
      mockSpeechSynthesisUtterance.mockReturnValue(mockUtterance);
      
      const speakPromise = hybridTTS.speak('Hello world', 'en-IE');
      
      // Simulate Web Speech API completion
      setTimeout(() => {
        mockUtterance.onend();
      }, 0);
      
      await speakPromise;
      
      expect(cartesiaTTS.speak).toHaveBeenCalled();
      expect(mockSpeechSynthesis.speak).toHaveBeenCalled();
    });

    test('should force Web Speech API when requested', async () => {
      const mockUtterance = {
        onstart: null,
        onend: null,
        onerror: null
      };
      mockSpeechSynthesisUtterance.mockReturnValue(mockUtterance);
      
      const speakPromise = hybridTTS.speak('Hello world', 'en-IE', { forceWebSpeech: true });
      
      // Simulate Web Speech API completion
      setTimeout(() => {
        mockUtterance.onend();
      }, 0);
      
      await speakPromise;
      
      expect(cartesiaTTS.speak).not.toHaveBeenCalled();
      expect(mockSpeechSynthesis.speak).toHaveBeenCalled();
    });

    test('should handle no available services', async () => {
      cartesiaTTS.isAvailable = false;
      Object.defineProperty(window, 'speechSynthesis', {
        writable: true,
        value: undefined
      });

      const service = new (hybridTTS.constructor)();
      
      await expect(service.speak('Hello')).rejects.toThrow('No TTS service available');
    });
  });

  describe('Speech Control', () => {
    test('should stop current speech', async () => {
      hybridTTS.isSpeaking = true;
      hybridTTS.speakingText = 'Hello';
      mockSpeechSynthesis.speaking = true;
      
      await hybridTTS.stop();
      
      expect(mockSpeechSynthesis.cancel).toHaveBeenCalled();
      expect(hybridTTS.isSpeaking).toBe(false);
      expect(hybridTTS.speakingText).toBeNull();
    });

    test('should track speaking state', () => {
      expect(hybridTTS.isCurrentlySpeaking()).toBe(false);
      expect(hybridTTS.getCurrentlySpeakingText()).toBeNull();
      
      hybridTTS.isSpeaking = true;
      hybridTTS.speakingText = 'Hello world';
      
      expect(hybridTTS.isCurrentlySpeaking()).toBe(true);
      expect(hybridTTS.getCurrentlySpeakingText()).toBe('Hello world');
    });
  });

  describe('Audio Preloading', () => {
    test('should preload audio with Cartesia', async () => {
      cartesiaTTS.generateAudio.mockResolvedValue(new Blob());
      
      await hybridTTS.preloadAudio('Hello world', 'en-IE');
      
      expect(cartesiaTTS.generateAudio).toHaveBeenCalledWith('Hello world', 'en-IE');
    });

    test('should handle preload errors gracefully', async () => {
      cartesiaTTS.generateAudio.mockRejectedValue(new Error('Preload error'));
      
      await expect(hybridTTS.preloadAudio('Hello world')).resolves.not.toThrow();
    });
  });

  describe('Cache Management', () => {
    test('should get cache stats from Cartesia', () => {
      const mockStats = { size: 5, keys: ['key1', 'key2'] };
      cartesiaTTS.getCacheStats.mockReturnValue(mockStats);
      
      const stats = hybridTTS.getCacheStats();
      expect(stats).toBe(mockStats);
    });

    test('should clear cache through Cartesia', () => {
      hybridTTS.clearCache();
      expect(cartesiaTTS.clearCache).toHaveBeenCalled();
    });

    test('should handle cache operations when Cartesia unavailable', () => {
      cartesiaTTS.isAvailable = false;
      const service = new (hybridTTS.constructor)();
      
      expect(service.getCacheStats()).toBeNull();
      expect(() => service.clearCache()).not.toThrow();
    });
  });

  describe('Web Speech API Integration', () => {
    test('should configure Web Speech API correctly', async () => {
      cartesiaTTS.speak.mockRejectedValue(new Error('Cartesia error'));
      
      const mockUtterance = {
        onstart: null,
        onend: null,
        onerror: null
      };
      mockSpeechSynthesisUtterance.mockReturnValue(mockUtterance);
      
      const speakPromise = hybridTTS.speak('Hello world', 'zh-CN');
      
      // Simulate Web Speech API completion
      setTimeout(() => {
        mockUtterance.onend();
      }, 0);
      
      await speakPromise;
      
      expect(mockSpeechSynthesisUtterance).toHaveBeenCalledWith('Hello world');
      expect(mockSpeechSynthesis.speak).toHaveBeenCalled();
      
      const utterance = mockSpeechSynthesisUtterance.mock.results[0].value;
      expect(utterance.rate).toBe(0.9);
      expect(utterance.pitch).toBe(1.0);
      expect(utterance.volume).toBe(0.8);
      expect(utterance.lang).toBe('zh-CN');
    });

    test('should handle Web Speech API errors', async () => {
      cartesiaTTS.speak.mockRejectedValue(new Error('Cartesia error'));
      
      const mockUtterance = {
        onstart: null,
        onend: null,
        onerror: null
      };
      mockSpeechSynthesisUtterance.mockReturnValue(mockUtterance);
      
      const speakPromise = hybridTTS.speak('Hello world');
      
      // Simulate Web Speech API error
      setTimeout(() => {
        mockUtterance.onerror({ error: 'synthesis-failed' });
      }, 0);
      
      await expect(speakPromise).rejects.toThrow('Speech synthesis error: synthesis-failed');
    });
  });

  describe('Status Reporting', () => {
    test('should provide comprehensive status', () => {
      const status = hybridTTS.getStatus();
      
      expect(status).toHaveProperty('cartesiaAvailable');
      expect(status).toHaveProperty('webSpeechAvailable');
      expect(status).toHaveProperty('isSpeaking');
      expect(status).toHaveProperty('speakingText');
      expect(status).toHaveProperty('availableServices');
      expect(Array.isArray(status.availableServices)).toBe(true);
    });
  });
});
