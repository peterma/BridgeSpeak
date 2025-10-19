/**
 * Pipecat Text-to-Speech Service for Frontend
 * Uses the existing Pipecat backend TTS service (Google TTS)
 */

class PipecatTTSService {
  constructor() {
    this.baseUrl = 'http://localhost:8081/api/v1/tts/synthesize';
    this.cache = new Map();
    this.cacheExpiry = 24 * 60 * 60 * 1000; // 24 hours
    this.isAvailable = true; // Will be checked dynamically
    
    // Voice configurations for different languages
    this.voiceConfigs = {
      'en-IE': {
        language: 'en-IE',
        voice_name: 'en-US-Neural2-F' // Irish English voice
      },
      'en-US': {
        language: 'en-US',
        voice_name: 'en-US-Neural2-F'
      },
      'zh-CN': {
        language: 'zh-CN',
        voice_name: 'zh-CN-Wavenet-A'
      },
      'default': {
        language: 'en-IE',
        voice_name: 'en-US-Neural2-F'
      }
    };
    
    console.log('Pipecat TTS: Service initialized, using backend TTS endpoint');
  }

  /**
   * Generate cache key for text and language
   */
  getCacheKey(text, language) {
    return `pipecat:${language}:${text}`;
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
   * Generate audio using Pipecat backend TTS API
   */
  async generateAudio(text, language = 'en-IE') {
    // Check if backend is available first
    const isBackendAvailable = await this.testConnection();
    if (!isBackendAvailable) {
      throw new Error('Pipecat TTS backend not available');
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
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: text,
          language: voiceConfig.language,
          voice_name: voiceConfig.voice_name
        })
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(`Pipecat TTS API error: ${response.status} - ${errorData.error || response.statusText}`);
      }

      const data = await response.json();
      
      // Convert base64 audio to blob
      const audioData = data.audio_data;
      const binaryString = atob(audioData);
      const bytes = new Uint8Array(binaryString.length);
      for (let i = 0; i < binaryString.length; i++) {
        bytes[i] = binaryString.charCodeAt(i);
      }
      const audioBlob = new Blob([bytes], { type: 'audio/wav' });
      
      // Cache the audio
      this.cacheAudio(text, language, audioBlob);
      
      return audioBlob;
    } catch (error) {
      console.error('Pipecat TTS error:', error);
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
   * Speak text using Pipecat TTS
   */
  async speak(text, language = 'en-IE') {
    try {
      const audioBlob = await this.generateAudio(text, language);
      await this.playAudio(audioBlob);
    } catch (error) {
      console.error('Pipecat TTS speak error:', error);
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
  setVoiceConfig(language, voiceName, languageCode) {
    this.voiceConfigs[language] = {
      language: languageCode,
      voice_name: voiceName
    };
  }

  /**
   * Get current voice configuration
   */
  getVoiceConfig(language = 'default') {
    return this.voiceConfigs[language] || this.voiceConfigs.default;
  }

  /**
   * Test if the backend TTS service is available
   */
  async testConnection() {
    try {
      const response = await fetch('http://localhost:8081/api/v1/health');
      return response.ok;
    } catch (error) {
      console.warn('Pipecat TTS backend not available:', error);
      return false;
    }
  }
}

// Create singleton instance
const pipecatTTS = new PipecatTTSService();

export default pipecatTTS;
