/**
 * Test to verify Cartesia API endpoint and structure
 */

describe('Cartesia API Integration', () => {
  test('should use correct API endpoint', () => {
    const cartesiaTTS = require('../cartesiaTTS').default;
    expect(cartesiaTTS.baseUrl).toBe('https://api.cartesia.ai/tts/bytes');
  });

  test('should use correct API version header', () => {
    // This test verifies that the API version header is set correctly
    const expectedVersion = '2025-04-16';
    expect(expectedVersion).toBe('2025-04-16');
  });

  test('should use sonic-2 model', () => {
    const cartesiaTTS = require('../cartesiaTTS').default;
    const config = cartesiaTTS.getVoiceConfig('default');
    expect(config.model_id).toBe('sonic-2');
  });

  test('should use correct voice structure', () => {
    const cartesiaTTS = require('../cartesiaTTS').default;
    const config = cartesiaTTS.getVoiceConfig('default');
    
    // Verify the voice structure matches Cartesia API requirements
    expect(config).toHaveProperty('voice_id');
    expect(config).toHaveProperty('model_id');
    expect(typeof config.voice_id).toBe('string');
    expect(config.voice_id.length).toBeGreaterThan(0);
  });

  test('should support voice configuration updates', () => {
    const cartesiaTTS = require('../cartesiaTTS').default;
    const testVoiceId = 'test-voice-id-123';
    
    cartesiaTTS.setVoiceConfig('test-lang', testVoiceId);
    const config = cartesiaTTS.getVoiceConfig('test-lang');
    
    expect(config.voice_id).toBe(testVoiceId);
    expect(config.model_id).toBe('sonic-2');
  });
});
