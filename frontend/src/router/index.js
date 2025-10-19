import React, { Suspense } from 'react';
import { createBrowserRouter } from 'react-router-dom';
import Layout from '../components/Layout';
import ErrorBoundary from '../components/ErrorBoundary';
import Home from '../pages/Home';
import NotFound from '../pages/NotFound';

// Lazy-loaded components for code splitting
const ConversationPage = React.lazy(() => import('../pages/ConversationPage'));
const ScenariosPage = React.lazy(() => import('../pages/ScenariosPage'));
const TranscriptsPage = React.lazy(() => import('../pages/TranscriptsPage'));
const DashboardPage = React.lazy(() => import('../pages/DashboardPage'));
const SettingsPage = React.lazy(() => import('../pages/SettingsPage'));
const StyleGuidePage = React.lazy(() => import('../pages/StyleGuidePage'));
const TestingPage = React.lazy(() => import('../pages/TestingPage'));
const ShadcnDemoPage = React.lazy(() => import('../pages/ShadcnDemoPage'));
const ResponsiveDemo = React.lazy(() => import('../pages/ResponsiveDemo'));

// Loading component for Suspense fallback
function LoadingFallback({ message = "Loading..." }) {
  return (
    <div className="loading-placeholder">
      <div className="loading-content">
        <div className="loading-spinner"></div>
        <h2>{message}</h2>
        <p>Please wait while we prepare your experience</p>
      </div>
    </div>
  );
}

// Wrapper component for lazy-loaded routes
function LazyRoute({ children, fallbackMessage }) {
  return (
    <ErrorBoundary>
      <Suspense fallback={<LoadingFallback message={fallbackMessage} />}>
        {children}
      </Suspense>
    </ErrorBoundary>
  );
}

// Router configuration using createBrowserRouter
export const router = createBrowserRouter([
  {
    path: "/",
    element: (
      <ErrorBoundary>
        <Layout>
          <Home />
        </Layout>
      </ErrorBoundary>
    ),
    errorElement: (
      <Layout>
        <ErrorBoundary>
          <NotFound />
        </ErrorBoundary>
      </Layout>
    ),
  },
  {
    path: "/conversation",
    element: (
      <Layout>
        <LazyRoute fallbackMessage="Loading conversation...">
          <ConversationPage />
        </LazyRoute>
      </Layout>
    ),
  },
  {
    path: "/scenarios",
    element: (
      <Layout>
        <LazyRoute fallbackMessage="Loading scenarios...">
          <ScenariosPage />
        </LazyRoute>
      </Layout>
    ),
  },
  {
    path: "/scenarios/:scenarioId/transcripts",
    element: (
      <Layout>
        <LazyRoute fallbackMessage="Loading transcripts...">
          <TranscriptsPage />
        </LazyRoute>
      </Layout>
    ),
  },
  {
    path: "/dashboard",
    element: (
      <Layout>
        <LazyRoute fallbackMessage="Loading dashboard...">
          <DashboardPage />
        </LazyRoute>
      </Layout>
    ),
  },
  {
    path: "/settings",
    element: (
      <Layout>
        <LazyRoute fallbackMessage="Loading settings...">
          <SettingsPage />
        </LazyRoute>
      </Layout>
    ),
  },
  {
    path: "/style-guide",
    element: (
      <Layout>
        <LazyRoute fallbackMessage="Loading style guide...">
          <StyleGuidePage />
        </LazyRoute>
      </Layout>
    ),
  },
  {
    path: "/testing",
    element: (
      <Layout>
        <LazyRoute fallbackMessage="Loading testing page...">
          <TestingPage />
        </LazyRoute>
      </Layout>
    ),
  },
  {
    path: "/shadcn-demo",
    element: (
      <Layout>
        <LazyRoute fallbackMessage="Loading shadcn demo...">
          <ShadcnDemoPage />
        </LazyRoute>
      </Layout>
    ),
  },
  {
    path: "/responsive-demo",
    element: (
      <Layout>
        <LazyRoute fallbackMessage="Loading responsive demo...">
          <ResponsiveDemo />
        </LazyRoute>
      </Layout>
    ),
  },
  {
    path: "*",
    element: (
      <Layout>
        <NotFound />
      </Layout>
    ),
  },
]);