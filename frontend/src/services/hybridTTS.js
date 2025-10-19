/**
 * Hybrid Text-to-Speech Service
 * Uses Cartesia TTS -> Pipecat TTS (Google) -> Web Speech API fallback chain
 */

import cartesiaTTS from './cartesiaTTS';
import pipecatTTS from './pipecatTTS';

class HybridTTSService {
  constructor() {
    this.cartesiaAvailable = cartesiaTTS.isAvailable;
    this.pipecatAvailable = false; // Temporarily disabled due to backend issues
    this.webSpeechAvailable = typeof window !== 'undefined' && 'speechSynthesis' in window;
    this.currentUtterance = null;
    this.isSpeaking = false;
    this.speakingText = null;
  }

  /**
   * Check if Pipecat TTS is available by testing the backend connection
   */
  async checkPipecatAvailability() {
    try {
      const isAvailable = await pipecatTTS.testConnection();
      this.pipecatAvailable = isAvailable;
      return isAvailable;
    } catch (error) {
      this.pipecatAvailable = false;
      return false;
    }
  }

  /**
   * Check if any TTS service is available
   */
  isAvailable() {
    return this.cartesiaAvailable || this.pipecatAvailable || this.webSpeechAvailable;
  }

  /**
   * Get available TTS services
   */
  getAvailableServices() {
    const services = [];
    if (this.cartesiaAvailable) services.push('cartesia');
    if (this.pipecatAvailable) services.push('pipecat');
    if (this.webSpeechAvailable) services.push('web-speech');
    return services;
  }

  /**
   * Speak text using the best available service
   * Fallback chain: Cartesia -> Pipecat TTS (Google) -> Web Speech API
   */
  async speak(text, language = 'en-IE', options = {}) {
    // Stop any currently speaking text
    await this.stop();

    // Try Cartesia first if available
    if (this.cartesiaAvailable && !options.forcePipecat && !options.forceWebSpeech) {
      try {
        this.isSpeaking = true;
        this.speakingText = text;
        await cartesiaTTS.speak(text, language);
        this.isSpeaking = false;
        this.speakingText = null;
        return;
      } catch (error) {
        console.warn('Cartesia TTS failed:', error.message);
        // Check if it's a 402 Payment Required error (credits exhausted)
        if (error.message.includes('402') || error.message.includes('Payment Required')) {
          console.warn('Cartesia credits exhausted, disabling Cartesia TTS');
          this.cartesiaAvailable = false; // Disable Cartesia for this session
        }
        this.isSpeaking = false;
        this.speakingText = null;
      }
    }

    // Try Pipecat TTS as second option (uses Google TTS via backend)
    if (this.pipecatAvailable && !options.forceWebSpeech) {
      try {
        this.isSpeaking = true;
        this.speakingText = text;
        await pipecatTTS.speak(text, language);
        this.isSpeaking = false;
        this.speakingText = null;
        return;
      } catch (error) {
        console.warn('Pipecat TTS failed, falling back to Web Speech API:', error);
        this.isSpeaking = false;
        this.speakingText = null;
      }
    }

    // Final fallback to Web Speech API
    if (this.webSpeechAvailable) {
      try {
        this.isSpeaking = true;
        this.speakingText = text;
        await this.speakWithWebSpeech(text, language);
        this.isSpeaking = false;
        this.speakingText = null;
      } catch (error) {
        console.error('Web Speech API failed:', error);
        this.isSpeaking = false;
        this.speakingText = null;
        throw error;
      }
    } else {
      throw new Error('No TTS service available');
    }
  }

  /**
   * Speak using Web Speech API
   */
  speakWithWebSpeech(text, language = 'en-IE') {
    return new Promise((resolve, reject) => {
      if (!this.webSpeechAvailable) {
        reject(new Error('Web Speech API not available'));
        return;
      }

      // Cancel any existing speech
      if (window.speechSynthesis.speaking) {
        window.speechSynthesis.cancel();
      }

      const utterance = new SpeechSynthesisUtterance(text);
      
      // Configure voice settings
      utterance.rate = 0.9;
      utterance.pitch = 1.0;
      utterance.volume = 0.8;
      utterance.lang = language;

      // Set up event handlers
      utterance.onstart = () => {
        this.isSpeaking = true;
      };

      utterance.onend = () => {
        this.isSpeaking = false;
        this.speakingText = null;
        resolve();
      };

      utterance.onerror = (event) => {
        this.isSpeaking = false;
        this.speakingText = null;
        reject(new Error(`Speech synthesis error: ${event.error}`));
      };

      this.currentUtterance = utterance;
      window.speechSynthesis.speak(utterance);
    });
  }

  /**
   * Stop current speech
   */
  async stop() {
    if (this.isSpeaking) {
      // Stop Web Speech API
      if (this.webSpeechAvailable && window.speechSynthesis.speaking) {
        window.speechSynthesis.cancel();
      }
      
      // Note: Cartesia TTS doesn't have a direct stop method
      // The audio will continue playing until it ends naturally
      
      this.isSpeaking = false;
      this.speakingText = null;
      this.currentUtterance = null;
    }
  }

  /**
   * Check if currently speaking
   */
  isCurrentlySpeaking() {
    return this.isSpeaking;
  }

  /**
   * Get currently speaking text
   */
  getCurrentlySpeakingText() {
    return this.speakingText;
  }

  /**
   * Preload audio for better performance
   */
  async preloadAudio(text, language = 'en-IE') {
    // Try Cartesia first
    if (this.cartesiaAvailable) {
      try {
        await cartesiaTTS.generateAudio(text, language);
        return;
      } catch (error) {
        console.warn('Failed to preload audio with Cartesia:', error);
        // Check if it's a 402 Payment Required error
        if (error.message.includes('402') || error.message.includes('Payment Required')) {
          console.warn('Cartesia credits exhausted, disabling Cartesia TTS');
          this.cartesiaAvailable = false;
        }
      }
    }
    
    // Fallback to Pipecat TTS
    if (this.pipecatAvailable) {
      try {
        await pipecatTTS.generateAudio(text, language);
        return;
      } catch (error) {
        console.warn('Failed to preload audio with Pipecat TTS:', error);
      }
    }
  }

  /**
   * Get service status
   */
  getStatus() {
    return {
      cartesiaAvailable: this.cartesiaAvailable,
      pipecatAvailable: this.pipecatAvailable,
      webSpeechAvailable: this.webSpeechAvailable,
      isSpeaking: this.isSpeaking,
      speakingText: this.speakingText,
      availableServices: this.getAvailableServices()
    };
  }

  /**
   * Get cache statistics (Cartesia and Pipecat TTS)
   */
  getCacheStats() {
    const stats = {};
    if (this.cartesiaAvailable) {
      stats.cartesia = cartesiaTTS.getCacheStats();
    }
    if (this.pipecatAvailable) {
      stats.pipecat = pipecatTTS.getCacheStats();
    }
    return Object.keys(stats).length > 0 ? stats : null;
  }

  /**
   * Clear cache (Cartesia and Pipecat TTS)
   */
  clearCache() {
    if (this.cartesiaAvailable) {
      cartesiaTTS.clearCache();
    }
    if (this.pipecatAvailable) {
      pipecatTTS.clearCache();
    }
  }
}

// Create singleton instance
const hybridTTS = new HybridTTSService();

export default hybridTTS;
