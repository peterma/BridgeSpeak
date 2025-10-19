import React, { Suspense } from 'react';
import ErrorBoundary from '../components/ErrorBoundary';

// Use the real VideoConversation component with WebRTC
const VideoConversation = React.lazy(() => import('../components/VideoConversation'));

function ConversationPage() {
  return (
    <div className="conversation-page">
      <ErrorBoundary>
        <Suspense fallback={
          <div className="loading-placeholder">
            <div className="loading-content">
              <div className="loading-spinner"></div>
              <h2>Loading conversation...</h2>
              <p>Preparing your learning session</p>
            </div>
          </div>
        }>
          <VideoConversation />
        </Suspense>
      </ErrorBoundary>
    </div>
  );
}

export default ConversationPage;