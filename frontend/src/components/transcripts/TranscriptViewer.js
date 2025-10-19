import React, { useState, useEffect, useCallback } from 'react';
import { 
  loadScenarioTranscripts, 
  getRandomTranscript 
} from '../../data/transcriptLoader';
import Transcript from '../conversation/Transcript';
import './TranscriptViewer.css';

function TranscriptViewer({ scenarioId, scenarioTitle }) {
  const [transcripts, setTranscripts] = useState([]);
  const [selectedTranscript, setSelectedTranscript] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showRandom, setShowRandom] = useState(false);

  useEffect(() => {
    loadTranscripts();
  }, [scenarioId]); // eslint-disable-line react-hooks/exhaustive-deps

  const loadTranscripts = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      
      const transcriptData = await loadScenarioTranscripts(scenarioId);
      setTranscripts(transcriptData);
      
      // Set the first transcript as default
      if (transcriptData.length > 0) {
        setSelectedTranscript(transcriptData[0]);
      }
    } catch (err) {
      console.error('Failed to load transcripts:', err);
      setError('Failed to load sample transcripts');
    } finally {
      setLoading(false);
    }
  }, [scenarioId]);

  const handleTranscriptSelect = (transcript) => {
    setSelectedTranscript(transcript);
    setShowRandom(false);
  };

  const handleRandomTranscript = async () => {
    try {
      setLoading(true);
      const randomTranscript = await getRandomTranscript(scenarioId);
      setSelectedTranscript(randomTranscript);
      setShowRandom(true);
    } catch (err) {
      console.error('Failed to load random transcript:', err);
      setError('Failed to load random transcript');
    } finally {
      setLoading(false);
    }
  };

  const getTranscriptDisplayName = (transcript) => {
    const metadata = transcript.metadata;
    const variant = metadata.difficulty_variant.replace('variant', 'Variant ');
    const ageGroup = metadata.age_group.replace('-', ' ');
    return `${variant} (${ageGroup})`;
  };

  if (loading && transcripts.length === 0) {
    return (
      <div className="transcript-viewer">
        <div className="transcript-viewer-header">
          <h3>Sample Transcripts</h3>
        </div>
        <div className="transcript-loading">
          <p>Loading sample transcripts...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="transcript-viewer">
        <div className="transcript-viewer-header">
          <h3>Sample Transcripts</h3>
        </div>
        <div className="transcript-error">
          <p>{error}</p>
          <button onClick={loadTranscripts} className="retry-button">
            Try Again
          </button>
        </div>
      </div>
    );
  }

  if (transcripts.length === 0) {
    return (
      <div className="transcript-viewer">
        <div className="transcript-viewer-header">
          <h3>Sample Transcripts</h3>
        </div>
        <div className="transcript-empty">
          <p>No sample transcripts available for this scenario.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="transcript-viewer">
      <div className="transcript-viewer-header">
        <h3>Sample Transcripts</h3>
        <p className="transcript-description">
          View sample conversations for "{scenarioTitle}" to see how Xiao Mei helps children learn.
        </p>
      </div>

      <div className="transcript-controls">
        <div className="transcript-selector">
          <label htmlFor="transcript-select">Choose a transcript:</label>
          <select
            id="transcript-select"
            value={selectedTranscript?.metadata?.transcript_id || ''}
            onChange={(e) => {
              const transcript = transcripts.find(t => t.metadata.transcript_id === e.target.value);
              if (transcript) {
                handleTranscriptSelect(transcript);
              }
            }}
            className="transcript-select"
          >
            {transcripts.map((transcript) => (
              <option 
                key={transcript.metadata.transcript_id} 
                value={transcript.metadata.transcript_id}
              >
                {getTranscriptDisplayName(transcript)}
              </option>
            ))}
          </select>
        </div>

        <button 
          onClick={handleRandomTranscript}
          className="random-transcript-button"
          disabled={loading}
        >
          {loading ? 'Loading...' : 'Random Transcript'}
        </button>
      </div>

      {selectedTranscript && (
        <div className="transcript-content">
          <div className="transcript-info">
            <div className="transcript-metadata">
              <span className="transcript-variant">
                {selectedTranscript.metadata.difficulty_variant.replace('variant', 'Variant ')}
              </span>
              <span className="transcript-age-group">
                {selectedTranscript.metadata.age_group.replace('-', ' ')}
              </span>
              {showRandom && (
                <span className="random-indicator">Random</span>
              )}
            </div>
            {selectedTranscript.metadata.description && (
              <p className="transcript-description">
                {selectedTranscript.metadata.description}
              </p>
            )}
          </div>

          <div className="transcript-display">
            <Transcript 
              messages={selectedTranscript.messages} 
              isActive={false}
              isSampleTranscript={true}
            />
          </div>
        </div>
      )}

      <div className="transcript-footer">
        <p className="transcript-help">
          These are sample conversations showing how Xiao Mei helps children practice English. 
          Each transcript demonstrates different conversation paths and age-appropriate language.
        </p>
      </div>
    </div>
  );
}

export default TranscriptViewer;
