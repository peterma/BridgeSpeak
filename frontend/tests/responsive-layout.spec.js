import { test, expect } from '@playwright/test';

test.describe('Scenarios Page Responsive Layout', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/scenarios');
  });

  test('1600px viewport - should show 1600px container and ~4-5 cards per row', async ({ page }) => {
    await page.setViewportSize({ width: 1600, height: 900 });
    await page.waitForSelector('.scenarios-grid');
    
    // Check container width
    const mainContent = page.locator('.main-content');
    const containerWidth = await mainContent.evaluate(el => 
      parseInt(window.getComputedStyle(el).maxWidth)
    );
    expect(containerWidth).toBe(1600);
    
    // Check grid columns
    const grid = page.locator('.scenarios-grid');
    const gridColumns = await grid.evaluate(el => 
      window.getComputedStyle(el).gridTemplateColumns
    );
    console.log(`1600px viewport - Grid columns: ${gridColumns}`);
    
    // Should have multiple columns with 320px minimum
    expect(gridColumns).toContain('320px');
    const columnCount = gridColumns.split(' ').length;
    expect(columnCount).toBeGreaterThanOrEqual(4);
  });

  test('2400px viewport - should show 2400px container and ~8-10 cards per row', async ({ page }) => {
    await page.setViewportSize({ width: 2400, height: 1200 });
    await page.waitForSelector('.scenarios-grid');
    
    // Check container width
    const mainContent = page.locator('.main-content');
    const containerWidth = await mainContent.evaluate(el => 
      parseInt(window.getComputedStyle(el).maxWidth)
    );
    expect(containerWidth).toBe(2400);
    
    // Check grid columns
    const grid = page.locator('.scenarios-grid');
    const gridColumns = await grid.evaluate(el => 
      window.getComputedStyle(el).gridTemplateColumns
    );
    console.log(`2400px viewport - Grid columns: ${gridColumns}`);
    
    // Should have more columns with 240px minimum
    expect(gridColumns).toContain('240px');
    const columnCount = gridColumns.split(' ').length;
    expect(columnCount).toBeGreaterThanOrEqual(8);
  });

  test('3200px viewport - should show 2500px container and ~10+ cards per row', async ({ page }) => {
    await page.setViewportSize({ width: 3200, height: 1600 });
    await page.waitForSelector('.scenarios-grid');
    
    // Check container width
    const mainContent = page.locator('.main-content');
    const containerWidth = await mainContent.evaluate(el => 
      parseInt(window.getComputedStyle(el).maxWidth)
    );
    expect(containerWidth).toBe(2500);
    
    // Check grid columns
    const grid = page.locator('.scenarios-grid');
    const gridColumns = await grid.evaluate(el => 
      window.getComputedStyle(el).gridTemplateColumns
    );
    console.log(`3200px viewport - Grid columns: ${gridColumns}`);
    
    // Should have many columns with 230px minimum
    expect(gridColumns).toContain('230px');
    const columnCount = gridColumns.split(' ').length;
    expect(columnCount).toBeGreaterThanOrEqual(10);
  });

  test('Your exact viewport 3198px - should behave like 2400px+', async ({ page }) => {
    await page.setViewportSize({ width: 3198, height: 1677 });
    await page.waitForSelector('.scenarios-grid');
    
    // Wait a moment for styles to apply
    await page.waitForTimeout(500);
    
    // Check which media query is active
    const mainContent = page.locator('.main-content');
    const containerWidth = await mainContent.evaluate(el => 
      parseInt(window.getComputedStyle(el).maxWidth)
    );
    
    console.log(`3198px viewport - Container max-width: ${containerWidth}px`);
    
    // Should hit the 2400px+ breakpoint, not 1600px
    expect(containerWidth).toBe(2400);
    
    // Check grid columns
    const grid = page.locator('.scenarios-grid');
    const gridColumns = await grid.evaluate(el => 
      window.getComputedStyle(el).gridTemplateColumns
    );
    console.log(`3198px viewport - Grid columns: ${gridColumns}`);
    
    // Should use 240px minimum, not 320px
    expect(gridColumns).toContain('240px');
    expect(gridColumns).not.toContain('320px');
    
    const columnCount = gridColumns.split(' ').length;
    console.log(`3198px viewport - Column count: ${columnCount}`);
    expect(columnCount).toBeGreaterThanOrEqual(8);
  });

  test('Debug: Check all active media queries', async ({ page }) => {
    const viewports = [
      { width: 1600, height: 900, name: '1600px' },
      { width: 2400, height: 1200, name: '2400px' },
      { width: 3198, height: 1677, name: '3198px (your actual)' },
      { width: 3200, height: 1600, name: '3200px' },
    ];

    for (const viewport of viewports) {
      await page.setViewportSize({ width: viewport.width, height: viewport.height });
      await page.waitForSelector('.scenarios-grid');
      await page.waitForTimeout(200);

      const mainContent = page.locator('.main-content');
      const containerWidth = await mainContent.evaluate(el => 
        parseInt(window.getComputedStyle(el).maxWidth)
      );
      
      const grid = page.locator('.scenarios-grid');
      const gridColumns = await grid.evaluate(el => 
        window.getComputedStyle(el).gridTemplateColumns
      );
      
      const columnCount = gridColumns.split(' ').length;
      
      console.log(`\n${viewport.name}:`);
      console.log(`  Container: ${containerWidth}px`);
      console.log(`  Grid: ${gridColumns}`);
      console.log(`  Columns: ${columnCount}`);
    }
  });
});