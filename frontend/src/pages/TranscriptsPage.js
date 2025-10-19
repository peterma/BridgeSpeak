import React from 'react';
import { useParams, useLocation, useNavigate } from 'react-router-dom';
import TranscriptViewer from '../components/transcripts/TranscriptViewer';
import { mockScenarios } from '../data/scenarios';
import './TranscriptsPage.css';

function TranscriptsPage() {
  const { scenarioId } = useParams();
  const location = useLocation();
  const navigate = useNavigate();
  
  // Get scenario data from location state or find by ID
  const scenario = location.state?.selectedScenario || 
    mockScenarios.find(s => s.id === scenarioId);

  const handleBackToScenarios = () => {
    navigate('/scenarios');
  };

  if (!scenario) {
    return (
      <div className="transcripts-page">
        <div className="transcripts-page-header">
          <button 
            onClick={handleBackToScenarios}
            className="back-button"
            aria-label="Back to scenarios"
          >
            ← Back to Scenarios
          </button>
          <h1>Scenario Not Found</h1>
        </div>
        <div className="transcripts-content">
          <p>The requested scenario could not be found.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen px-4 sm:px-6 lg:px-8 py-6 max-w-7xl mx-auto">
      <div className="text-center mb-8 lg:mb-12">
        <div className="max-w-4xl mx-auto">
          <button 
            onClick={handleBackToScenarios}
            className="back-button mb-4"
            aria-label="Back to scenarios"
          >
            ← Back to Scenarios
          </button>
          <h1 className="page-title">Sample Transcripts</h1>
          <h2 className="scenario-title">{scenario.title}</h2>
          <p className="page-description">{scenario.description}</p>
        </div>
      </div>

      <div className="transcripts-content">
        <TranscriptViewer 
          scenarioId={scenario.id}
          scenarioTitle={scenario.title}
        />
      </div>
    </div>
  );
}

export default TranscriptsPage;
