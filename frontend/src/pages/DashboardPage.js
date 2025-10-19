import React, { Suspense } from 'react';
import ErrorBoundary from '../components/ErrorBoundary';

// Lazy load the new Parent Dashboard component for Story 4.3.4
const ParentDashboard = React.lazy(() => import('../components/dashboard/ParentDashboard'));

function DashboardPage() {
  return (
    <div className="min-h-screen px-4 sm:px-6 lg:px-8 py-6 max-w-7xl mx-auto">
      <div className="text-center mb-8 lg:mb-12">
        <div className="max-w-4xl mx-auto">
          <h1 className="page-title">Parent Dashboard</h1>
          <p className="page-description">
            Track your child's learning progress and engagement with Xiao Mei.
          </p>
        </div>
      </div>
      
      <ErrorBoundary>
        <Suspense fallback={
          <div className="loading-placeholder">
            <h2>Loading dashboard...</h2>
            <p>Preparing your progress overview</p>
          </div>
        }>
          <ParentDashboard />
        </Suspense>
      </ErrorBoundary>
    </div>
  );
}

export default DashboardPage;