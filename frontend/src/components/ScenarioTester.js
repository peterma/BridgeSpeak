import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { mockScenarios } from '../data/scenarios';

function ScenarioTester() {
  const [selectedScenario, setSelectedScenario] = useState('');
  const navigate = useNavigate();

  const handleTestScenario = () => {
    if (selectedScenario) {
      navigate(`/conversation?scenario=${selectedScenario}`);
    }
  };

  const testAllScenarios = () => {
    // Open each scenario in a new tab for quick testing
    mockScenarios.forEach((scenario, index) => {
      setTimeout(() => {
        window.open(`/conversation?scenario=${scenario.id}`, '_blank');
      }, index * 500); // Stagger the openings
    });
  };

  const testInvalidScenario = () => {
    navigate('/conversation?scenario=invalid-scenario-test');
  };

  return (
    <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
      <h1>Scenario Tester</h1>
      <p>Use this tool to test that all scenarios work correctly.</p>
      
      <div style={{ marginBottom: '20px' }}>
        <h3>Test Individual Scenario</h3>
        <select 
          value={selectedScenario} 
          onChange={(e) => setSelectedScenario(e.target.value)}
          style={{ marginRight: '10px', padding: '8px' }}
        >
          <option value="">Select a scenario...</option>
          {mockScenarios.map(scenario => (
            <option key={scenario.id} value={scenario.id}>
              {scenario.title} ({scenario.id})
            </option>
          ))}
        </select>
        <button 
          onClick={handleTestScenario} 
          disabled={!selectedScenario}
          style={{ padding: '8px 16px' }}
        >
          Test Scenario
        </button>
      </div>

      <div style={{ marginBottom: '20px' }}>
        <h3>Bulk Test</h3>
        <button 
          onClick={testAllScenarios}
          style={{ padding: '8px 16px', marginRight: '10px' }}
        >
          Test All Scenarios (opens in new tabs)
        </button>
        <button 
          onClick={testInvalidScenario}
          style={{ padding: '8px 16px' }}
        >
          Test Invalid Scenario
        </button>
      </div>

      <div>
        <h3>Available Scenarios</h3>
        <ul>
          {mockScenarios.map(scenario => (
            <li key={scenario.id} style={{ marginBottom: '8px' }}>
              <strong>{scenario.title}</strong> ({scenario.id}) - {scenario.difficulty}
              <br />
              <small>{scenario.description}</small>
              <br />
              <a 
                href={`/conversation?scenario=${scenario.id}`} 
                target="_blank" 
                rel="noopener noreferrer"
                style={{ fontSize: '12px', marginLeft: '10px' }}
              >
                → Test this scenario
              </a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default ScenarioTester;