/**
 * Cartesia Text-to-Speech Service for Frontend
 * Provides high-quality TTS with caching and fallback support
 */

class CartesiaTTSService {
  constructor() {
    // Use Vite's import.meta.env instead of process.env
    this.apiKey = import.meta.env.VITE_CARTESIA_API_KEY || import.meta.env.REACT_APP_CARTESIA_API_KEY;
    this.baseUrl = 'https://api.cartesia.ai/tts/bytes';
    this.cache = new Map();
    this.cacheExpiry = 24 * 60 * 60 * 1000; // 24 hours
    this.isAvailable = !!this.apiKey;
    
    // Debug logging for environment variables
    if (!this.apiKey) {
      console.warn('Cartesia TTS: No API key found. Service will fall back to Web Speech API.');
      console.log('To enable Cartesia TTS, create a .env file in the frontend directory with:');
      console.log('VITE_CARTESIA_API_KEY=your_cartesia_api_key_here');
      console.log('Available env vars:', {
        VITE_CARTESIA_API_KEY: import.meta.env.VITE_CARTESIA_API_KEY,
        REACT_APP_CARTESIA_API_KEY: import.meta.env.REACT_APP_CARTESIA_API_KEY,
        MODE: import.meta.env.MODE
      });
    } else {
      console.log('Cartesia TTS: API key found, service available');
    }
    
    // Voice configurations for different languages
    this.voiceConfigs = {
      'zh-CN': {
        voice_id: '694f9389-aac1-45b6-b726-9d9369183238', // Chinese voice
        model_id: 'sonic-2'
      },
      'en-IE': {
        voice_id: '694f9389-aac1-45b6-b726-9d9369183238', // Irish English voice
        model_id: 'sonic-2'
      },
      'mixed': {
        voice_id: '694f9389-aac1-45b6-b726-9d9369183238', // Multilingual voice
        model_id: 'sonic-2'
      },
      'default': {
        voice_id: '694f9389-aac1-45b6-b726-9d9369183238', // Default voice
        model_id: 'sonic-2'
      }
    };
  }

  /**
   * Generate cache key for text and language
   */
  getCacheKey(text, language) {
    return `${language}:${text}`;
  }

  /**
   * Check if cached audio is still valid
   */
  isCacheValid(cacheEntry) {
    return cacheEntry && (Date.now() - cacheEntry.timestamp) < this.cacheExpiry;
  }

  /**
   * Get cached audio if available and valid
   */
  getCachedAudio(text, language) {
    const key = this.getCacheKey(text, language);
    const cached = this.cache.get(key);
    
    if (this.isCacheValid(cached)) {
      return cached.audioBlob;
    }
    
    // Remove expired cache entry
    if (cached) {
      this.cache.delete(key);
    }
    
    return null;
  }

  /**
   * Cache audio data
   */
  cacheAudio(text, language, audioBlob) {
    const key = this.getCacheKey(text, language);
    this.cache.set(key, {
      audioBlob,
      timestamp: Date.now()
    });
  }

  /**
   * Generate audio using Cartesia API
   */
  async generateAudio(text, language = 'en-IE') {
    if (!this.isAvailable) {
      throw new Error('Cartesia API key not available');
    }

    // Check cache first
    const cachedAudio = this.getCachedAudio(text, language);
    if (cachedAudio) {
      return cachedAudio;
    }

    const voiceConfig = this.voiceConfigs[language] || this.voiceConfigs.default;
    
    try {
      const response = await fetch(this.baseUrl, {
        method: 'POST',
        headers: {
          'Cartesia-Version': '2025-04-16',
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          transcript: text,
          model_id: voiceConfig.model_id,
          voice: {
            mode: 'id',
            id: voiceConfig.voice_id
          },
          output_format: {
            container: 'wav',
            encoding: 'pcm_f32le',
            sample_rate: 44100
          }
        })
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(`Cartesia API error: ${response.status} - ${errorData.message || response.statusText}`);
      }

      const audioBlob = await response.blob();
      
      // Cache the audio
      this.cacheAudio(text, language, audioBlob);
      
      return audioBlob;
    } catch (error) {
      console.error('Cartesia TTS error:', error);
      throw error;
    }
  }

  /**
   * Play audio from blob
   */
  async playAudio(audioBlob) {
    return new Promise((resolve, reject) => {
      const audio = new Audio();
      const url = URL.createObjectURL(audioBlob);
      
      audio.src = url;
      
      audio.onended = () => {
        URL.revokeObjectURL(url);
        resolve();
      };
      
      audio.onerror = (error) => {
        URL.revokeObjectURL(url);
        reject(error);
      };
      
      audio.play().catch(reject);
    });
  }

  /**
   * Speak text using Cartesia TTS
   */
  async speak(text, language = 'en-IE') {
    try {
      const audioBlob = await this.generateAudio(text, language);
      await this.playAudio(audioBlob);
    } catch (error) {
      console.error('Cartesia TTS speak error:', error);
      throw error;
    }
  }

  /**
   * Get cache statistics
   */
  getCacheStats() {
    return {
      size: this.cache.size,
      keys: Array.from(this.cache.keys())
    };
  }

  /**
   * Clear cache
   */
  clearCache() {
    this.cache.clear();
  }

  /**
   * Preload audio for common phrases
   */
  async preloadCommonPhrases(phrases, language = 'en-IE') {
    const promises = phrases.map(phrase => 
      this.generateAudio(phrase, language).catch(error => {
        console.warn(`Failed to preload phrase: ${phrase}`, error);
        return null;
      })
    );
    
    await Promise.all(promises);
  }

  /**
   * Update voice configuration for a specific language
   */
  setVoiceConfig(language, voiceId, modelId = 'sonic-2') {
    this.voiceConfigs[language] = {
      voice_id: voiceId,
      model_id: modelId
    };
  }

  /**
   * Get current voice configuration
   */
  getVoiceConfig(language = 'default') {
    return this.voiceConfigs[language] || this.voiceConfigs.default;
  }
}

// Create singleton instance
const cartesiaTTS = new CartesiaTTSService();

export default cartesiaTTS;
