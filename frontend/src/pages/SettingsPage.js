/**
 * Settings Page - Placeholder for Story 4.3.4
 * 
 * Basic settings page placeholder to support dashboard navigation.
 * Will be expanded in future stories.
 */

import React from 'react';
import { Link } from 'react-router-dom';
import './pages.css';

function SettingsPage() {
  return (
    <div className="min-h-screen px-4 sm:px-6 lg:px-8 py-6 max-w-7xl mx-auto">
      <div className="text-center mb-8 lg:mb-12">
        <div className="max-w-4xl mx-auto">
          <h1 className="page-title">Settings</h1>
          <p className="page-description">
            Customize your learning experience with Xiao Mei
          </p>
        </div>
      </div>

      <div className="settings-content">
        <div className="placeholder-card">
          <div className="placeholder-icon" aria-hidden="true">⚙️</div>
          <h2>Settings Coming Soon</h2>
          <p>
            This page will include options to customize your child's learning experience, 
            including language preferences, difficulty settings, and accessibility options.
          </p>
          
          <div className="placeholder-actions">
            <Link to="/dashboard" className="back-button">
              ← Back to Dashboard
            </Link>
            <Link to="/scenarios" className="scenarios-button">
              Explore Scenarios
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SettingsPage;