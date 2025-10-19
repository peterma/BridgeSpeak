import React from 'react';
import { NavLink } from 'react-router-dom';
import './Layout.css';

function Layout({ children }) {
  return (
    <div className="app-layout">
      <a href="#main-content" className="skip-link">
        Skip to main content
      </a>
      
      <header className="app-header" role="banner">
        <div className="header-content">
          <h1 className="app-title">BridgeSpeak</h1>
          <nav className="main-nav" role="navigation" aria-label="Main navigation">
            <ul className="nav-list">
              <li>
                <NavLink 
                  to="/" 
                  className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}
                  aria-current={({ isActive }) => isActive ? 'page' : undefined}
                  title="Home"
                >
                  <span className="nav-icon" aria-hidden="true">🏠</span>
                  <span className="nav-text">Home</span>
                </NavLink>
              </li>
              <li>
                <NavLink 
                  to="/scenarios"
                  className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}
                  aria-current={({ isActive }) => isActive ? 'page' : undefined}
                  title="Scenarios"
                >
                  <span className="nav-icon" aria-hidden="true">🎭</span>
                  <span className="nav-text">Scenarios</span>
                </NavLink>
              </li>
              <li>
                <NavLink 
                  to="/conversation"
                  className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}
                  aria-current={({ isActive }) => isActive ? 'page' : undefined}
                  title="Conversation"
                >
                  <span className="nav-icon" aria-hidden="true">💬</span>
                  <span className="nav-text">Conversation</span>
                </NavLink>
              </li>
              <li>
                <NavLink 
                  to="/dashboard"
                  className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}
                  aria-current={({ isActive }) => isActive ? 'page' : undefined}
                  title="Dashboard"
                >
                  <span className="nav-icon" aria-hidden="true">📋</span>
                  <span className="nav-text">Dashboard</span>
                </NavLink>
              </li>
              <li>
                <NavLink 
                  to="/style-guide"
                  className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}
                  aria-current={({ isActive }) => isActive ? 'page' : undefined}
                  title="Style Guide"
                >
                  <span className="nav-icon" aria-hidden="true">🎨</span>
                  {/* <span className="nav-text">Style Guide</span> */}
                </NavLink>
              </li>
              <li>
                <NavLink 
                  to="/testing"
                  className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}
                  aria-current={({ isActive }) => isActive ? 'page' : undefined}
                  title="Testing Lab"
                >
                  <span className="nav-icon" aria-hidden="true">🧪</span>
                  {/* <span className="nav-text">Testing Lab</span> */}
                </NavLink>
              </li>
            </ul>
          </nav>
        </div>
      </header>

      <main id="main-content" className="main-content" role="main">
        {children}
      </main>

      <footer className="app-footer" role="contentinfo">
        <div className="footer-content">
          <p>&copy; 2025 BridgeSpeak. Bridging languages and cultures for children worldwide.</p>
        </div>
      </footer>
    </div>
  );
}

export default Layout;