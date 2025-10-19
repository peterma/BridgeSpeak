import React from 'react';
import { RouterProvider } from 'react-router-dom';
import { router } from './router';
import './App.css';
import './components/ErrorBoundary.css';
import './components/Loading.css';
import './pages/pages.css';

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;