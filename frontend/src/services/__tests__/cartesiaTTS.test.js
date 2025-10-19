import cartesiaTTS from '../cartesiaTTS';

// Mock fetch
global.fetch = jest.fn();

// Mock URL.createObjectURL and URL.revokeObjectURL
global.URL.createObjectURL = jest.fn(() => 'mock-audio-url');
global.URL.revokeObjectURL = jest.fn();

// Mock Audio
global.Audio = jest.fn().mockImplementation(() => ({
  play: jest.fn().mockResolvedValue(),
  onended: null,
  onerror: null,
  src: ''
}));

describe('CartesiaTTSService', () => {
  beforeEach(() => {
    jest.clearAllMocks();
    cartesiaTTS.clearCache();
    
    // Reset environment
    delete process.env.REACT_APP_CARTESIA_API_KEY;
  });

  describe('Initialization', () => {
    test('should initialize without API key', () => {
      expect(cartesiaTTS.isAvailable).toBe(false);
    });

    test('should initialize with API key', () => {
      process.env.REACT_APP_CARTESIA_API_KEY = 'test-key';
      const service = new (cartesiaTTS.constructor)();
      expect(service.isAvailable).toBe(true);
    });
  });

  describe('Cache Management', () => {
    test('should generate correct cache key', () => {
      const key = cartesiaTTS.getCacheKey('Hello world', 'en-IE');
      expect(key).toBe('en-IE:Hello world');
    });

    test('should cache and retrieve audio', () => {
      const mockBlob = new Blob(['audio data'], { type: 'audio/mp3' });
      cartesiaTTS.cacheAudio('Hello', 'en-IE', mockBlob);
      
      const cached = cartesiaTTS.getCachedAudio('Hello', 'en-IE');
      expect(cached).toBe(mockBlob);
    });

    test('should return null for expired cache', () => {
      const mockBlob = new Blob(['audio data'], { type: 'audio/mp3' });
      cartesiaTTS.cacheAudio('Hello', 'en-IE', mockBlob);
      
      // Mock expired timestamp
      const cache = cartesiaTTS.cache;
      const key = cartesiaTTS.getCacheKey('Hello', 'en-IE');
      cache.set(key, {
        audioBlob: mockBlob,
        timestamp: Date.now() - (25 * 60 * 60 * 1000) // 25 hours ago
      });
      
      const cached = cartesiaTTS.getCachedAudio('Hello', 'en-IE');
      expect(cached).toBeNull();
    });

    test('should clear cache', () => {
      const mockBlob = new Blob(['audio data'], { type: 'audio/mp3' });
      cartesiaTTS.cacheAudio('Hello', 'en-IE', mockBlob);
      
      expect(cartesiaTTS.cache.size).toBe(1);
      cartesiaTTS.clearCache();
      expect(cartesiaTTS.cache.size).toBe(0);
    });

    test('should provide cache statistics', () => {
      const mockBlob = new Blob(['audio data'], { type: 'audio/mp3' });
      cartesiaTTS.cacheAudio('Hello', 'en-IE', mockBlob);
      
      const stats = cartesiaTTS.getCacheStats();
      expect(stats.size).toBe(1);
      expect(stats.keys).toContain('en-IE:Hello');
    });
  });

  describe('Audio Generation', () => {
    beforeEach(() => {
      process.env.REACT_APP_CARTESIA_API_KEY = 'test-key';
    });

    test('should throw error when API key not available', async () => {
      delete process.env.REACT_APP_CARTESIA_API_KEY;
      const service = new (cartesiaTTS.constructor)();
      
      await expect(service.generateAudio('Hello')).rejects.toThrow('Cartesia API key not available');
    });

    test('should generate audio successfully', async () => {
      const mockBlob = new Blob(['audio data'], { type: 'audio/mp3' });
      fetch.mockResolvedValueOnce({
        ok: true,
        blob: () => Promise.resolve(mockBlob)
      });

      const audioBlob = await cartesiaTTS.generateAudio('Hello world', 'en-IE');
      
      expect(fetch).toHaveBeenCalledWith(
        'https://api.cartesia.ai/tts/bytes',
        expect.objectContaining({
          method: 'POST',
          headers: {
            'Cartesia-Version': '2025-04-16',
            'Authorization': 'Bearer test-key',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            transcript: 'Hello world',
            model_id: 'sonic-2',
            voice: {
              mode: 'id',
              id: '694f9389-aac1-45b6-b726-9d9369183238'
            },
            output_format: {
              container: 'wav',
              encoding: 'pcm_f32le',
              sample_rate: 44100
            }
          })
        })
      );
      
      expect(audioBlob).toBe(mockBlob);
    });

    test('should handle API errors', async () => {
      fetch.mockResolvedValueOnce({
        ok: false,
        status: 400,
        statusText: 'Bad Request',
        json: () => Promise.resolve({ message: 'Invalid request' })
      });

      await expect(cartesiaTTS.generateAudio('Hello')).rejects.toThrow('Cartesia API error: 400 - Invalid request');
    });

    test('should use cached audio when available', async () => {
      const mockBlob = new Blob(['cached audio'], { type: 'audio/mp3' });
      cartesiaTTS.cacheAudio('Hello', 'en-IE', mockBlob);
      
      const audioBlob = await cartesiaTTS.generateAudio('Hello', 'en-IE');
      
      expect(fetch).not.toHaveBeenCalled();
      expect(audioBlob).toBe(mockBlob);
    });
  });

  describe('Audio Playback', () => {
    test('should play audio successfully', async () => {
      const mockBlob = new Blob(['audio data'], { type: 'audio/mp3' });
      const mockAudio = {
        play: jest.fn().mockResolvedValue(),
        onended: null,
        onerror: null,
        src: ''
      };
      
      global.Audio.mockReturnValue(mockAudio);
      
      const playPromise = cartesiaTTS.playAudio(mockBlob);
      
      // Simulate audio ending
      setTimeout(() => {
        mockAudio.onended();
      }, 0);
      
      await playPromise;
      
      expect(global.URL.createObjectURL).toHaveBeenCalledWith(mockBlob);
      expect(mockAudio.src).toBe('mock-audio-url');
      expect(mockAudio.play).toHaveBeenCalled();
      expect(global.URL.revokeObjectURL).toHaveBeenCalledWith('mock-audio-url');
    });

    test('should handle audio playback errors', async () => {
      const mockBlob = new Blob(['audio data'], { type: 'audio/mp3' });
      const mockAudio = {
        play: jest.fn().mockRejectedValue(new Error('Playback failed')),
        onended: null,
        onerror: null,
        src: ''
      };
      
      global.Audio.mockReturnValue(mockAudio);
      
      await expect(cartesiaTTS.playAudio(mockBlob)).rejects.toThrow('Playback failed');
    });
  });

  describe('Voice Configuration', () => {
    test('should use correct voice config for different languages', () => {
      const zhConfig = cartesiaTTS.voiceConfigs['zh-CN'];
      const enConfig = cartesiaTTS.voiceConfigs['en-IE'];
      const mixedConfig = cartesiaTTS.voiceConfigs['mixed'];
      const defaultConfig = cartesiaTTS.voiceConfigs['default'];
      
      expect(zhConfig.voice_id).toBe('694f9389-aac1-45b6-b726-9d9369183238');
      expect(enConfig.voice_id).toBe('694f9389-aac1-45b6-b726-9d9369183238');
      expect(mixedConfig.voice_id).toBe('694f9389-aac1-45b6-b726-9d9369183238');
      expect(defaultConfig.voice_id).toBe('694f9389-aac1-45b6-b726-9d9369183238');
      expect(zhConfig.model_id).toBe('sonic-2');
    });

    test('should allow updating voice configuration', () => {
      const customVoiceId = 'custom-voice-id-123';
      cartesiaTTS.setVoiceConfig('en-IE', customVoiceId, 'sonic-2');
      
      const config = cartesiaTTS.getVoiceConfig('en-IE');
      expect(config.voice_id).toBe(customVoiceId);
      expect(config.model_id).toBe('sonic-2');
    });

    test('should return default config for unknown language', () => {
      const config = cartesiaTTS.getVoiceConfig('unknown-language');
      expect(config.voice_id).toBe('694f9389-aac1-45b6-b726-9d9369183238');
      expect(config.model_id).toBe('sonic-2');
    });
  });

  describe('Preloading', () => {
    beforeEach(() => {
      process.env.REACT_APP_CARTESIA_API_KEY = 'test-key';
    });

    test('should preload common phrases', async () => {
      const mockBlob = new Blob(['audio data'], { type: 'audio/mp3' });
      fetch.mockResolvedValue({
        ok: true,
        blob: () => Promise.resolve(mockBlob)
      });

      const phrases = ['Hello', 'Goodbye', 'Thank you'];
      await cartesiaTTS.preloadCommonPhrases(phrases, 'en-IE');
      
      expect(fetch).toHaveBeenCalledTimes(3);
      expect(cartesiaTTS.cache.size).toBe(3);
    });

    test('should handle preload errors gracefully', async () => {
      fetch.mockRejectedValue(new Error('Network error'));
      
      const phrases = ['Hello', 'Goodbye'];
      await expect(cartesiaTTS.preloadCommonPhrases(phrases, 'en-IE')).resolves.not.toThrow();
    });
  });
});
