/**
 * Style Guide Page - Design System Demo
 * 
 * Showcases all design system components with examples.
 * Useful for development and testing.
 */

import React, { useState } from 'react';
import { 
  Button, 
  Card, 
  Input, 
  Chip, 
  SkipLink, 
  VisuallyHidden 
} from '../design-system';
import './pages.css';
import './StyleGuidePage.css';

function StyleGuidePage() {
  const [inputValue, setInputValue] = useState('');
  const [inputError, setInputError] = useState('');
  const [selectedChips, setSelectedChips] = useState(['React', 'Accessibility']);
  const [buttonLoading, setButtonLoading] = useState(false);

  const handleInputChange = (e) => {
    const value = e.target.value;
    setInputValue(value);
    
    // Demo validation
    if (value.length > 0 && value.length < 3) {
      setInputError('Must be at least 3 characters');
    } else {
      setInputError('');
    }
  };

  const handleChipToggle = (chipValue) => {
    setSelectedChips(prev => 
      prev.includes(chipValue) 
        ? prev.filter(c => c !== chipValue)
        : [...prev, chipValue]
    );
  };

  const handleChipRemove = (chipValue) => {
    setSelectedChips(prev => prev.filter(c => c !== chipValue));
  };

  const handleLoadingDemo = () => {
    setButtonLoading(true);
    setTimeout(() => setButtonLoading(false), 2000);
  };

  return (
    <div className="min-h-screen px-4 sm:px-6 lg:px-8 py-6 max-w-7xl mx-auto">
      <SkipLink />
      
      <div className="text-center mb-8 lg:mb-12">
        <div className="max-w-4xl mx-auto">
          <h1 className="page-title">Design System Style Guide</h1>
          <p className="page-description">
            Interactive showcase of all design system components with trauma-informed design principles.
          </p>
        </div>
      </div>

      <div className="style-guide-content">
        {/* Colors Section */}
        <section className="style-guide-section" aria-labelledby="colors-heading">
          <h2 id="colors-heading">Color Palette</h2>
          <div className="color-grid">
            <div className="color-swatch color-swatch--primary">
              <div className="color-preview"></div>
              <div className="color-info">
                <span className="color-name">Primary</span>
                <span className="color-value">#E8B4B8</span>
              </div>
            </div>
            <div className="color-swatch color-swatch--secondary">
              <div className="color-preview"></div>
              <div className="color-info">
                <span className="color-name">Secondary</span>
                <span className="color-value">#A8D8A8</span>
              </div>
            </div>
            <div className="color-swatch color-swatch--accent">
              <div className="color-preview"></div>
              <div className="color-info">
                <span className="color-name">Accent</span>
                <span className="color-value">#F4D03F</span>
              </div>
            </div>
          </div>
        </section>

        {/* Typography Section */}
        <section className="style-guide-section" aria-labelledby="typography-heading">
          <h2 id="typography-heading">Typography</h2>
          <div className="typography-examples">
            <div className="typography-sample" style={{ fontSize: '2rem', fontWeight: 'bold', marginBottom: '1rem' }}>Heading 1 - Main Page Title</div>
            <h2 className="typography-sample">Heading 2 - Section Title</h2>
            <h3 className="typography-sample">Heading 3 - Subsection Title</h3>
            <p className="typography-sample">
              Body text - This is regular paragraph text used throughout the application. 
              It's designed to be readable and accessible for all users.
            </p>
            <small className="typography-sample">Small text - Used for helper text and captions</small>
          </div>
        </section>

        {/* Button Section */}
        <section className="style-guide-section" aria-labelledby="buttons-heading">
          <h2 id="buttons-heading">Buttons</h2>
          
          <div className="component-group">
            <h3>Variants</h3>
            <div className="component-examples">
              <Button variant="primary">Primary Button</Button>
              <Button variant="secondary">Secondary Button</Button>
              <Button variant="outline">Outline Button</Button>
              <Button variant="ghost">Ghost Button</Button>
              <Button variant="danger">Danger Button</Button>
            </div>
          </div>

          <div className="component-group">
            <h3>Sizes</h3>
            <div className="component-examples">
              <Button size="small">Small Button</Button>
              <Button size="medium">Medium Button</Button>
              <Button size="large">Large Button</Button>
            </div>
          </div>

          <div className="component-group">
            <h3>States</h3>
            <div className="component-examples">
              <Button>Normal</Button>
              <Button disabled>Disabled</Button>
              <Button loading={buttonLoading} onClick={handleLoadingDemo}>
                {buttonLoading ? 'Loading...' : 'Click for Loading'}
              </Button>
            </div>
          </div>

          <div className="component-group">
            <h3>With Icons</h3>
            <div className="component-examples">
              <Button leftIcon="🚀">Start Journey</Button>
              <Button rightIcon="→">Continue</Button>
              <Button leftIcon="❤️" variant="secondary">Favorite</Button>
            </div>
          </div>
        </section>

        {/* Card Section */}
        <section className="style-guide-section" aria-labelledby="cards-heading">
          <h2 id="cards-heading">Cards</h2>
          
          <div className="component-group">
            <h3>Card Examples</h3>
            <div className="cards-grid">
              <Card>
                <Card.Header>
                  <Card.Title>Basic Card</Card.Title>
                  <Card.Subtitle>This is a subtitle</Card.Subtitle>
                </Card.Header>
                <Card.Body>
                  This is the card body content. It can contain any type of content
                  including text, images, and other components.
                </Card.Body>
                <Card.Footer>
                  <Card.Actions>
                    <Button size="small" variant="outline">Cancel</Button>
                    <Button size="small">Save</Button>
                  </Card.Actions>
                </Card.Footer>
              </Card>

              <Card variant="primary" interactive onClick={() => console.log('Card clicked')}>
                <Card.Header>
                  <Card.Title>Interactive Card</Card.Title>
                  <Card.Subtitle>Click me!</Card.Subtitle>
                </Card.Header>
                <Card.Body>
                  This card is clickable and will respond to user interaction.
                  Perfect for navigation or selection purposes.
                </Card.Body>
              </Card>

              <Card variant="success" shadow="lg">
                <Card.Body>
                  <h4 style={{ margin: 0, marginBottom: '0.5rem' }}>Success Card</h4>
                  <p style={{ margin: 0 }}>
                    This card uses the success variant to indicate positive status or completion.
                  </p>
                </Card.Body>
              </Card>
            </div>
          </div>
        </section>

        {/* Input Section */}
        <section className="style-guide-section" aria-labelledby="inputs-heading">
          <h2 id="inputs-heading">Inputs</h2>
          
          <div className="component-group">
            <h3>Basic Inputs</h3>
            <div className="inputs-grid">
              <Input
                label="Text Input"
                placeholder="Enter some text..."
                helperText="This is helper text to guide the user"
              />
              
              <Input
                label="Email Address"
                type="email"
                placeholder="user@example.com"
                required
              />
              
              <Input
                label="Password"
                type="password"
                placeholder="Enter password"
                helperText="Must be at least 8 characters"
              />
              
              <Input
                label="Validation Demo"
                value={inputValue}
                onChange={handleInputChange}
                placeholder="Type at least 3 characters"
                errorMessage={inputError}
                invalid={!!inputError}
              />
            </div>
          </div>

          <div className="component-group">
            <h3>Input Variants</h3>
            <div className="inputs-grid">
              <Input
                label="Outline (Default)"
                variant="outline"
                placeholder="Outline input"
              />
              
              <Input
                label="Filled"
                variant="filled"
                placeholder="Filled input"
              />
              
              <Input
                label="Underline"
                variant="underline"
                placeholder="Underline input"
              />
            </div>
          </div>

          <div className="component-group">
            <h3>With Icons</h3>
            <div className="inputs-grid">
              <Input
                label="Search"
                leftIcon="🔍"
                placeholder="Search scenarios..."
              />
              
              <Input
                label="Website"
                rightIcon="🌐"
                placeholder="https://example.com"
              />
            </div>
          </div>
        </section>

        {/* Chip Section */}
        <section className="style-guide-section" aria-labelledby="chips-heading">
          <h2 id="chips-heading">Chips</h2>
          
          <div className="component-group">
            <h3>Basic Chips</h3>
            <div className="chips-container">
              <Chip>Default Chip</Chip>
              <Chip variant="primary">Primary Chip</Chip>
              <Chip variant="secondary">Secondary Chip</Chip>
              <Chip variant="accent">Accent Chip</Chip>
              <Chip variant="success">Success Chip</Chip>
              <Chip variant="info">Info Chip</Chip>
              <Chip variant="warning">Warning Chip</Chip>
              <Chip variant="error">Error Chip</Chip>
            </div>
          </div>

          <div className="component-group">
            <h3>Interactive Chips</h3>
            <div className="chips-container">
              {['React', 'Vue', 'Angular', 'Svelte', 'Accessibility'].map(tech => (
                <Chip
                  key={tech}
                  clickable
                  selected={selectedChips.includes(tech)}
                  onClick={() => handleChipToggle(tech)}
                  aria-label={`Toggle ${tech}`}
                >
                  {tech}
                </Chip>
              ))}
            </div>
            <p className="helper-text">Click chips to toggle selection</p>
          </div>

          <div className="component-group">
            <h3>Removable Chips</h3>
            <div className="chips-container">
              {selectedChips.map(chip => (
                <Chip
                  key={`removable-${chip}`}
                  variant="primary"
                  removable
                  onRemove={() => handleChipRemove(chip)}
                >
                  {chip}
                </Chip>
              ))}
            </div>
            <p className="helper-text">Click × to remove or use Delete/Backspace keys</p>
          </div>

          <div className="component-group">
            <h3>Chip Sizes</h3>
            <div className="chips-container">
              <Chip size="small">Small</Chip>
              <Chip size="medium">Medium</Chip>
              <Chip size="large">Large</Chip>
            </div>
          </div>
        </section>

        {/* Utility Components */}
        <section className="style-guide-section" aria-labelledby="utilities-heading">
          <h2 id="utilities-heading">Utility Components</h2>
          
          <div className="component-group">
            <h3>SkipLink</h3>
            <p>
              A SkipLink is present at the top of this page. 
              <strong>Press Tab to see it appear</strong> and allow keyboard users 
              to skip directly to main content.
            </p>
            <div className="utility-demo">
              <SkipLink href="#main-content">Skip to main content</SkipLink>
            </div>
          </div>

          <div className="component-group">
            <h3>VisuallyHidden</h3>
            <p>
              VisuallyHidden content is present but invisible. Screen readers will announce:
              <VisuallyHidden>This text is hidden visually but available to screen readers</VisuallyHidden>
              "This text is hidden visually but available to screen readers"
            </p>
            <div className="utility-demo">
              <Button>
                Delete
                <VisuallyHidden>item permanently</VisuallyHidden>
              </Button>
            </div>
          </div>
        </section>

        {/* Accessibility Features */}
        <section className="style-guide-section" aria-labelledby="accessibility-heading">
          <h2 id="accessibility-heading">Accessibility Features</h2>
          
          <div className="a11y-features">
            <div className="feature">
              <h3>Focus Management</h3>
              <p>All interactive elements have visible focus indicators using <code>:focus-visible</code></p>
            </div>
            
            <div className="feature">
              <h3>Color Contrast</h3>
              <p>All color combinations meet WCAG 2.1 AA contrast requirements (4.5:1 ratio)</p>
            </div>
            
            <div className="feature">
              <h3>Screen Reader Support</h3>
              <p>Proper ARIA labels, semantic HTML, and role attributes throughout</p>
            </div>
            
            <div className="feature">
              <h3>Keyboard Navigation</h3>
              <p>All interactive elements are accessible via keyboard navigation</p>
            </div>
            
            <div className="feature">
              <h3>Reduced Motion</h3>
              <p>Respects <code>prefers-reduced-motion</code> user preference</p>
            </div>
            
            <div className="feature">
              <h3>High Contrast Mode</h3>
              <p>Components adapt to <code>prefers-contrast: high</code> setting</p>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}

export default StyleGuidePage;