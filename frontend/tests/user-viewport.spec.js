import { test, expect } from '@playwright/test';

test('User actual viewport 2235px', async ({ page }) => {
  await page.goto('/scenarios');
  
  // Set to user's actual current viewport size
  await page.setViewportSize({ width: 2235, height: 1677 });
  await page.waitForSelector('.scenarios-grid');
  await page.waitForTimeout(500);

  // Check which media query is active
  const mainContent = page.locator('.main-content');
  const containerWidth = await mainContent.evaluate(el => 
    parseInt(window.getComputedStyle(el).maxWidth)
  );
  
  console.log(`2235px viewport - Container max-width: ${containerWidth}px`);
  
  // 2235px is less than 2400px, so should hit 1600px breakpoint
  expect(containerWidth).toBe(1600);
  
  // Check grid columns
  const grid = page.locator('.scenarios-grid');
  const gridColumns = await grid.evaluate(el => 
    window.getComputedStyle(el).gridTemplateColumns
  );
  console.log(`2235px viewport - Grid columns: ${gridColumns}`);
  
  const columnCount = gridColumns.split(' ').length;
  console.log(`2235px viewport - Column count: ${columnCount}`);
  
  // Should show more than 3 columns now
  expect(columnCount).toBeGreaterThanOrEqual(4);
});