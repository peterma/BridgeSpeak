/**
 * Accessibility Tests for Child-Friendly Color Palette - Story 5.1
 * 
 * These tests verify WCAG AA compliance for the new child-friendly color system
 */

// Color contrast testing helper function
function calculateColorContrast(color1, color2) {
  // Convert hex to RGB
  function hexToRgb(hex) {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
      r: parseInt(result[1], 16),
      g: parseInt(result[2], 16),
      b: parseInt(result[3], 16)
    } : null;
  }

  // Calculate relative luminance
  function relativeLuminance(color) {
    const rgb = hexToRgb(color);
    if (!rgb) return 0;
    
    const { r, g, b } = rgb;
    const [rs, gs, bs] = [r, g, b].map(c => {
      c = c / 255;
      return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
    });
    
    return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
  }

  const lum1 = relativeLuminance(color1);
  const lum2 = relativeLuminance(color2);
  const lighter = Math.max(lum1, lum2);
  const darker = Math.min(lum1, lum2);
  
  return (lighter + 0.05) / (darker + 0.05);
}

// Test color combinations for WCAG AA compliance
const colorTests = [
  {
    name: 'Primary text on light cream background',
    foreground: '#2D3748', // --text-primary
    background: '#FFF8E7', // --bg-primary
    minContrast: 4.5 // WCAG AA for normal text
  },
  {
    name: 'Secondary text on light cream background',
    foreground: '#4A5568', // --text-secondary
    background: '#FFF8E7', // --bg-primary
    minContrast: 4.5
  },
  {
    name: 'Primary blue on white background',
    foreground: '#4ECDC4', // --primary-blue
    background: '#FFFFFF', // --bg-card
    minContrast: 3.0 // WCAG AA for large text/non-text
  },
  {
    name: 'Primary blue dark on white background',
    foreground: '#2C9B97', // --primary-blue-dark
    background: '#FFFFFF', // --bg-card
    minContrast: 4.5
  },
  {
    name: 'Text on primary blue background',
    foreground: '#FFFFFF', // --text-on-primary
    background: '#4ECDC4', // --primary-blue
    minContrast: 4.5
  },
  {
    name: 'Accent green on white background',
    foreground: '#88E5A3', // --accent-green
    background: '#FFFFFF', // --bg-card
    minContrast: 3.0
  },
  {
    name: 'Secondary yellow on white background',
    foreground: '#FFD93D', // --secondary-yellow
    background: '#FFFFFF', // --bg-card
    minContrast: 3.0
  }
];

// Run accessibility tests
function runAccessibilityTests() {
  console.log('=== Child-Friendly Color Palette Accessibility Tests ===\n');
  
  let passedTests = 0;
  let totalTests = colorTests.length;
  
  colorTests.forEach(test => {
    const contrast = calculateColorContrast(test.foreground, test.background);
    const passed = contrast >= test.minContrast;
    
    console.log(`${passed ? '✅' : '❌'} ${test.name}`);
    console.log(`   Contrast: ${contrast.toFixed(2)}:1 (required: ${test.minContrast}:1)`);
    console.log(`   Colors: ${test.foreground} on ${test.background}\n`);
    
    if (passed) passedTests++;
  });
  
  console.log(`=== Results: ${passedTests}/${totalTests} tests passed ===`);
  
  if (passedTests === totalTests) {
    console.log('🎉 All accessibility tests passed! WCAG AA compliant.');
  } else {
    console.log('⚠️  Some accessibility tests failed. Review color combinations.');
  }
  
  return passedTests === totalTests;
}

// Export for testing frameworks
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { runAccessibilityTests, calculateColorContrast };
}

// Run tests if in browser environment
if (typeof window !== 'undefined') {
  // Wait for DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runAccessibilityTests);
  } else {
    runAccessibilityTests();
  }
}