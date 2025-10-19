import React from 'react';
import { Link } from 'react-router-dom';

function NotFound() {
  return (
    <div className="min-h-screen px-4 sm:px-6 lg:px-8 py-6 max-w-7xl mx-auto">
      <div className="text-center mb-8 lg:mb-12">
        <div className="max-w-4xl mx-auto">
          <h1 className="page-title">Page Not Found</h1>
          <p className="page-description">
            Sorry, we couldn't find the page you're looking for. 
            Let's get you back to learning!
          </p>
        </div>
      </div>
      
      <div className="not-found-actions">
        <Link to="/" className="action-button primary">
          Go Home
        </Link>
        <Link to="/conversation" className="action-button secondary">
          Start Conversation
        </Link>
      </div>
    </div>
  );
}

export default NotFound;