/**
 * Google Text-to-Speech Service for Frontend
 * Provides high-quality TTS using Google Cloud TTS API
 */

class GoogleTTSService {
  constructor() {
    // Use Vite's import.meta.env for environment variables
    this.apiKey = import.meta.env.VITE_GOOGLE_API_KEY || import.meta.env.REACT_APP_GOOGLE_API_KEY;
    this.baseUrl = 'https://texttospeech.googleapis.com/v1/text:synthesize';
    this.cache = new Map();
    this.cacheExpiry = 24 * 60 * 60 * 1000; // 24 hours
    this.isAvailable = !!this.apiKey;
    
    // Voice configurations for different languages
    this.voiceConfigs = {
      'en-IE': {
        languageCode: 'en-IE',
        name: 'en-IE-Wavenet-A', // Irish English voice
        ssmlGender: 'FEMALE'
      },
      'en-US': {
        languageCode: 'en-US',
        name: 'en-US-Wavenet-A',
        ssmlGender: 'FEMALE'
      },
      'zh-CN': {
        languageCode: 'zh-CN',
        name: 'zh-CN-Wavenet-A',
        ssmlGender: 'FEMALE'
      },
      'default': {
        languageCode: 'en-US',
        name: 'en-US-Wavenet-A',
        ssmlGender: 'FEMALE'
      }
    };
    
    // Debug logging for environment variables
    if (!this.apiKey) {
      console.warn('Google TTS: No API key found. Service will not be available.');
      console.log('To enable Google TTS, add to your .env file:');
      console.log('VITE_GOOGLE_API_KEY=your_google_api_key_here');
    } else {
      console.log('Google TTS: API key found, service available');
    }
  }

  /**
   * Generate cache key for text and language
   */
  getCacheKey(text, language) {
    return `google:${language}:${text}`;
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
   * Generate audio using Google TTS API
   */
  async generateAudio(text, language = 'en-IE') {
    if (!this.isAvailable) {
      throw new Error('Google TTS API key not available');
    }

    // Check cache first
    const cachedAudio = this.getCachedAudio(text, language);
    if (cachedAudio) {
      return cachedAudio;
    }

    const voiceConfig = this.voiceConfigs[language] || this.voiceConfigs.default;
    
    try {
      const response = await fetch(`${this.baseUrl}?key=${this.apiKey}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          input: { text: text },
          voice: {
            languageCode: voiceConfig.languageCode,
            name: voiceConfig.name,
            ssmlGender: voiceConfig.ssmlGender
          },
          audioConfig: {
            audioEncoding: 'MP3',
            speakingRate: 0.9, // Slightly slower for learning
            pitch: 0.0,
            volumeGainDb: 0.0
          }
        })
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(`Google TTS API error: ${response.status} - ${errorData.error?.message || response.statusText}`);
      }

      const data = await response.json();
      
      // Convert base64 audio to blob
      const audioData = data.audioContent;
      const binaryString = atob(audioData);
      const bytes = new Uint8Array(binaryString.length);
      for (let i = 0; i < binaryString.length; i++) {
        bytes[i] = binaryString.charCodeAt(i);
      }
      const audioBlob = new Blob([bytes], { type: 'audio/mp3' });
      
      // Cache the audio
      this.cacheAudio(text, language, audioBlob);
      
      return audioBlob;
    } catch (error) {
      console.error('Google TTS error:', error);
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
   * Speak text using Google TTS
   */
  async speak(text, language = 'en-IE') {
    try {
      const audioBlob = await this.generateAudio(text, language);
      await this.playAudio(audioBlob);
    } catch (error) {
      console.error('Google TTS speak error:', error);
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
  setVoiceConfig(language, voiceName, languageCode, ssmlGender = 'FEMALE') {
    this.voiceConfigs[language] = {
      languageCode,
      name: voiceName,
      ssmlGender
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
const googleTTS = new GoogleTTSService();

export default googleTTS;
