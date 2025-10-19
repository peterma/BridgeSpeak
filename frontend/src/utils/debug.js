// Debug utilities for development
// To enable: Add ?debug=true to URL or set localStorage.debug = 'true'

export const useViewportDebug = (gridSelector = '.scenarios-grid') => {
  const isDebugEnabled = () => {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('debug') === 'true' || localStorage.getItem('debug') === 'true';
  };

  const updateViewportInfo = () => {
    if (!isDebugEnabled()) return;

    const width = window.innerWidth;
    const height = window.innerHeight;
    console.log(`Viewport: ${width}x${height}`);
    
    // Create debug banner
    const existingBanner = document.getElementById('viewport-debug');
    if (existingBanner) existingBanner.remove();
    
    const banner = document.createElement('div');
    banner.id = 'viewport-debug';
    banner.style.cssText = `
      position: fixed;
      top: 10px;
      left: 10px;
      background: green;
      color: white;
      padding: 10px;
      z-index: 10000;
      font-size: 14px;
      border-radius: 4px;
      font-family: monospace;
      max-width: 300px;
      line-height: 1.4;
    `;
    
    // Check actual grid styles
    const gridElement = document.querySelector(gridSelector);
    const gridStyles = gridElement ? window.getComputedStyle(gridElement) : null;
    const gridColumns = gridStyles ? gridStyles.getPropertyValue('grid-template-columns') : 'Not found';
    const columnCount = gridColumns !== 'Not found' ? gridColumns.split(' ').length : 0;
    
    // Check container styles
    const mainContent = document.querySelector('.main-content');
    const containerStyles = mainContent ? window.getComputedStyle(mainContent) : null;
    const maxWidth = containerStyles ? containerStyles.getPropertyValue('max-width') : 'Not found';
    
    banner.innerHTML = `
      <strong>Debug Mode</strong><br>
      Viewport: ${width}x${height}px<br>
      Container: ${maxWidth}<br>
      Grid Columns: ${columnCount}<br>
      <small>URL: ?debug=true or localStorage.debug='true'</small>
    `;
    document.body.appendChild(banner);
  };

  const cleanup = () => {
    const banner = document.getElementById('viewport-debug');
    if (banner) banner.remove();
  };

  return { updateViewportInfo, cleanup, isDebugEnabled };
};

// React hook version
export const useViewportDebugEffect = (gridSelector) => {
  if (typeof React !== 'undefined') {
    React.useEffect(() => {
      const { updateViewportInfo, cleanup } = useViewportDebug(gridSelector);
      
      updateViewportInfo();
      window.addEventListener('resize', updateViewportInfo);
      
      return () => {
        window.removeEventListener('resize', updateViewportInfo);
        cleanup();
      };
    }, [gridSelector]);
  }
};

// Console commands for easy debugging
if (typeof window !== 'undefined') {
  window.debugViewport = {
    enable: () => {
      localStorage.setItem('debug', 'true');
      console.log('Viewport debug enabled. Refresh page to see debug info.');
    },
    disable: () => {
      localStorage.removeItem('debug');
      const banner = document.getElementById('viewport-debug');
      if (banner) banner.remove();
      console.log('Viewport debug disabled.');
    },
    toggle: () => {
      const isEnabled = localStorage.getItem('debug') === 'true';
      if (isEnabled) {
        window.debugViewport.disable();
      } else {
        window.debugViewport.enable();
      }
    }
  };
}