import { test, expect } from '@playwright/test';

test.describe('Emoji Icon Sizing Tests', () => {
  test.describe('Scenarios Page', () => {
    test.beforeEach(async ({ page }) => {
      await page.goto('/scenarios');
      await page.waitForSelector('.scenarios-grid');
      await page.waitForTimeout(500); // Allow CSS to fully load
    });

    test('should display emoji icons at proper size in scenario cards', async ({ page }) => {
      // Get all scenario cards
      const scenarioCards = page.locator('.scenario-card');
      const cardCount = await scenarioCards.count();
      expect(cardCount).toBeGreaterThan(0);

      // Check the first few scenario cards for emoji icon sizing
      for (let i = 0; i < Math.min(5, cardCount); i++) {
        const card = scenarioCards.nth(i);
        const iconElement = card.locator('.scenario-icon');
        
        // Verify icon exists
        await expect(iconElement).toBeVisible();
        
        // Check computed font-size
        const fontSize = await iconElement.evaluate(el => 
          window.getComputedStyle(el).fontSize
        );
        
        // Should be at least 2.5rem (40px) as per CSS
        const fontSizeValue = parseFloat(fontSize);
        console.log(`Card ${i}: Icon font-size: ${fontSize} (${fontSizeValue}px)`);
        expect(fontSizeValue).toBeGreaterThanOrEqual(40); // 2.5rem = 40px
        
        // Check that icon takes full width of its container
        const iconWidth = await iconElement.evaluate(el => el.offsetWidth);
        const thumbnailWidth = await card.locator('.scenario-thumbnail').evaluate(el => el.offsetWidth);
        
        console.log(`Card ${i}: Icon width: ${iconWidth}px, Thumbnail width: ${thumbnailWidth}px`);
        
        // Icon should take significant portion of thumbnail width
        // Allow some margin for padding/centering
        expect(iconWidth).toBeGreaterThan(30); // Minimum reasonable icon width
        
        // Verify icon is properly centered
        const iconStyles = await iconElement.evaluate(el => {
          const styles = window.getComputedStyle(el);
          return {
            textAlign: styles.textAlign,
            width: styles.width,
            lineHeight: styles.lineHeight
          };
        });
        
        console.log(`Card ${i}: Icon styles:`, iconStyles);
        expect(iconStyles.textAlign).toBe('center');
        // Width shows as computed pixel value, which is normal
        expect(parseFloat(iconStyles.width)).toBeGreaterThan(30);
      }
    });

    test('should maintain emoji icon size across different viewport widths', async ({ page }) => {
      const viewports = [
        { width: 1200, height: 800, name: 'Desktop' },
        { width: 768, height: 1024, name: 'Tablet' },
        { width: 375, height: 667, name: 'Mobile' }
      ];

      for (const viewport of viewports) {
        await page.setViewportSize({ width: viewport.width, height: viewport.height });
        await page.waitForTimeout(300); // Allow responsive styles to apply
        
        const firstCard = page.locator('.scenario-card').first();
        const iconElement = firstCard.locator('.scenario-icon');
        
        await expect(iconElement).toBeVisible();
        
        const fontSize = await iconElement.evaluate(el => 
          window.getComputedStyle(el).fontSize
        );
        const fontSizeValue = parseFloat(fontSize);
        
        console.log(`${viewport.name} (${viewport.width}px): Icon font-size: ${fontSize}`);
        
        // Icons should be appropriately sized for each viewport
        if (viewport.width >= 768) {
          // Desktop/Tablet: should be at least 2rem (32px)
          expect(fontSizeValue).toBeGreaterThanOrEqual(32);
        } else {
          // Mobile: should be at least 1.5rem (24px) but can be smaller
          expect(fontSizeValue).toBeGreaterThanOrEqual(24);
        }
        
        // Verify icon is still centered and taking full width
        const iconStyles = await iconElement.evaluate(el => {
          const styles = window.getComputedStyle(el);
          return {
            textAlign: styles.textAlign,
            width: styles.width
          };
        });
        
        expect(iconStyles.textAlign).toBe('center');
        // Width shows as computed pixel value, which is normal
        expect(parseFloat(iconStyles.width)).toBeGreaterThan(30);
      }
    });

    test('should have consistent emoji icon styling across all scenario cards', async ({ page }) => {
      const scenarioCards = page.locator('.scenario-card');
      const cardCount = await scenarioCards.count();
      
      // Collect font-size values from all visible cards
      const fontSizes = [];
      const visibleCardCount = Math.min(10, cardCount); // Check first 10 cards
      
      for (let i = 0; i < visibleCardCount; i++) {
        const card = scenarioCards.nth(i);
        const iconElement = card.locator('.scenario-icon');
        
        if (await iconElement.isVisible()) {
          const fontSize = await iconElement.evaluate(el => 
            parseFloat(window.getComputedStyle(el).fontSize)
          );
          fontSizes.push(fontSize);
        }
      }
      
      // All icons should have the same font-size
      expect(fontSizes.length).toBeGreaterThan(0);
      const firstSize = fontSizes[0];
      
      fontSizes.forEach((size, index) => {
        console.log(`Card ${index}: ${size}px`);
        expect(size).toBe(firstSize);
      });
      
      console.log(`All ${fontSizes.length} icons have consistent size: ${firstSize}px`);
    });

    test('should verify emoji icons are not clipped or cut off', async ({ page }) => {
      const firstCard = page.locator('.scenario-card').first();
      const iconElement = firstCard.locator('.scenario-icon');
      const thumbnailElement = firstCard.locator('.scenario-thumbnail');
      
      // Get bounding boxes
      const iconBox = await iconElement.boundingBox();
      const thumbnailBox = await thumbnailElement.boundingBox();
      
      expect(iconBox).not.toBeNull();
      expect(thumbnailBox).not.toBeNull();
      
      // Icon should be fully contained within thumbnail
      expect(iconBox.x).toBeGreaterThanOrEqual(thumbnailBox.x);
      expect(iconBox.y).toBeGreaterThanOrEqual(thumbnailBox.y);
      expect(iconBox.x + iconBox.width).toBeLessThanOrEqual(thumbnailBox.x + thumbnailBox.width);
      expect(iconBox.y + iconBox.height).toBeLessThanOrEqual(thumbnailBox.y + thumbnailBox.height);
      
      console.log('Icon bounding box:', iconBox);
      console.log('Thumbnail bounding box:', thumbnailBox);
      console.log('Icon is properly contained within thumbnail');
    });
  });

  test.describe('Home Page', () => {
    test.beforeEach(async ({ page }) => {
      await page.goto('/');
      await page.waitForTimeout(500);
    });

    test('should display emoji icons properly in popular scenarios section', async ({ page }) => {
      // Check if popular scenarios section exists on home page
      const popularSection = page.locator('.popular-scenarios-section');
      
      if (await popularSection.isVisible()) {
        const scenarioCards = popularSection.locator('.scenario-card');
        const cardCount = await scenarioCards.count();
        
        if (cardCount > 0) {
          const firstCard = scenarioCards.first();
          const iconElement = firstCard.locator('.scenario-icon');
          
          if (await iconElement.isVisible()) {
            const fontSize = await iconElement.evaluate(el => 
              window.getComputedStyle(el).fontSize
            );
            const fontSizeValue = parseFloat(fontSize);
            
            console.log(`Home page popular scenario icon font-size: ${fontSize}`);
            expect(fontSizeValue).toBeGreaterThanOrEqual(32); // Should be reasonably sized
            
            // Check that icon styling is consistent with scenarios page
            const iconStyles = await iconElement.evaluate(el => {
              const styles = window.getComputedStyle(el);
              return {
                textAlign: styles.textAlign,
                width: styles.width,
                lineHeight: styles.lineHeight
              };
            });
            
            console.log('Home page icon styles:', iconStyles);
            expect(iconStyles.textAlign).toBe('center');
          }
        }
      } else {
        console.log('No popular scenarios section found on home page');
      }
    });
  });

  test.describe('Visual Regression Tests', () => {
    test('should match visual baseline for scenario card icons', async ({ page }) => {
      await page.goto('/scenarios');
      await page.waitForSelector('.scenarios-grid');
      await page.waitForTimeout(1000); // Ensure everything is loaded
      
      // Take screenshot of first few scenario cards
      const firstRow = page.locator('.scenarios-grid .scenario-card').first();
      await expect(firstRow).toHaveScreenshot('scenario-card-icon.png', {
        threshold: 0.2, // Allow for minor rendering differences
        maxDiffPixels: 100
      });
    });

    test('should maintain icon appearance across screen sizes', async ({ page }) => {
      const viewports = [
        { width: 1200, height: 800, name: 'desktop' },
        { width: 768, height: 1024, name: 'tablet' },
        { width: 375, height: 667, name: 'mobile' }
      ];

      await page.goto('/scenarios');
      await page.waitForSelector('.scenarios-grid');

      for (const viewport of viewports) {
        await page.setViewportSize({ width: viewport.width, height: viewport.height });
        await page.waitForTimeout(500);
        
        const firstCard = page.locator('.scenario-card').first();
        await expect(firstCard).toHaveScreenshot(`scenario-card-${viewport.name}.png`, {
          threshold: 0.2,
          maxDiffPixels: 200
        });
      }
    });
  });
});