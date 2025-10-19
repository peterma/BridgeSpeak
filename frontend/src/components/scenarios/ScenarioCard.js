import React from 'react';
import { useNavigate } from 'react-router-dom';
import { getTranscriptStats } from '../../data/transcriptLoader';
import './ScenarioCard.css';

function ScenarioCard({ scenario, onSelect }) {
  const navigate = useNavigate();
  
  // Get transcript information for this scenario
  const transcriptStats = React.useMemo(() => {
    try {
      return getTranscriptStats(scenario.id);
    } catch (error) {
      console.warn(`Failed to get transcript stats for scenario ${scenario.id}:`, error);
      return { totalTranscripts: 0, ageGroups: [], variants: [] };
    }
  }, [scenario.id]);

  const handleCardClick = () => {
    if (onSelect) {
      onSelect(scenario);
    }
    // Navigate to conversation with scenario context
    navigate(`/conversation?scenario=${scenario.id}`, {
      state: { selectedScenario: scenario }
    });
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      handleCardClick();
    }
  };

  // const getDifficultyColor = (difficulty) => {
  //   switch (difficulty) {
  //     case 'beginner': return 'green';
  //     case 'intermediate': return 'orange';
  //     case 'advanced': return 'red';
  //     default: return 'gray';
  //   }
  // };

  const getCategoryLabel = (category) => {
    switch (category) {
      case 'essential': return 'Essential';
      case 'school': return 'School';
      case 'social': return 'Social';
      case 'daily-life': return 'Daily Life';
      case 'cultural': return 'Cultural';
      default: return category;
    }
  };

  return (
    <article 
      className="scenario-card"
      tabIndex={0}
      onClick={handleCardClick}
      onKeyDown={handleKeyDown}
      role="button"
      aria-label={`Practice ${scenario.title} scenario`}
      aria-describedby={`scenario-${scenario.id}-description scenario-${scenario.id}-tags`}
    >
      {scenario.isPopular && (
        <div className="popularity-badge" aria-label="Popular scenario">
          ⭐ Popular
        </div>
      )}
      
      <div className="scenario-thumbnail">
        <div className="scenario-icon" aria-hidden="true">
          {scenario.icon || (
            <>
              {scenario.category === 'essential' && '🌟'}
              {scenario.category === 'school' && '🏫'}
              {scenario.category === 'social' && '👥'}
              {scenario.category === 'daily-life' && '🏠'}
              {scenario.category === 'cultural' && '🎎'}
            </>
          )}
        </div>
      </div>
      
      <div className="scenario-content">
        <header className="scenario-header">
          <h3 className="scenario-title">{scenario.title}</h3>
          <div className="scenario-meta">
            <span className={`difficulty-badge ${scenario.difficulty}`}>
              {scenario.difficulty}
            </span>
            <span className="category-badge">
              {getCategoryLabel(scenario.category)}
            </span>
          </div>
        </header>
        
        <div 
          id={`scenario-${scenario.id}-description`}
          className="scenario-description"
        >
          {scenario.description}
        </div>
        
        <div className="scenario-details">
          <div className="time-estimate">
            <span className="detail-icon" aria-hidden="true">⏱️</span>
            <span>{scenario.estimatedTime}</span>
          </div>
          
          <div className="age-groups">
            <span className="detail-icon" aria-hidden="true">👶</span>
            <span>{scenario.ageGroups.length} age group{scenario.ageGroups.length !== 1 ? 's' : ''}</span>
          </div>
          
          {transcriptStats.totalTranscripts > 0 && (
            <div className="transcript-count">
              <span className="detail-icon" aria-hidden="true">📝</span>
              <span>{transcriptStats.totalTranscripts} sample transcript{transcriptStats.totalTranscripts !== 1 ? 's' : ''}</span>
            </div>
          )}
        </div>
        
        <div className="chinese-context">
          <span className="chinese-text" lang="zh-CN">
            {scenario.chineseContext}
          </span>
        </div>
        
        <div 
          id={`scenario-${scenario.id}-tags`}
          className="scenario-tags"
          aria-label="Scenario topics"
        >
          {scenario.tags.map(tag => (
            <span 
              key={tag} 
              className="tag-chip"
              aria-label={`Topic: ${tag}`}
            >
              {tag}
            </span>
          ))}
        </div>
        
        <div className="scenario-objectives">
          <h4 className="objectives-title">You will learn to:</h4>
          <ul className="objectives-list">
            {scenario.objectives.slice(0, 3).map((objective, index) => (
              <li key={index} className="objective-item">
                {objective}
              </li>
            ))}
            {scenario.objectives.length > 3 && (
              <li className="objective-item more-objectives">
                +{scenario.objectives.length - 3} more skills
              </li>
            )}
          </ul>
        </div>
      </div>
      
      <div className="scenario-footer">
        <div className="scenario-actions">
          <button 
            className="start-scenario-button"
            onClick={(e) => {
              e.stopPropagation();
              handleCardClick();
            }}
            aria-label={`Start practicing ${scenario.title}`}
          >
            <span className="button-icon" aria-hidden="true">▶️</span>
            <span className="button-text">Start Practice</span>
          </button>
          
          {transcriptStats.totalTranscripts > 0 && (
            <button 
              className="view-transcripts-button"
              onClick={(e) => {
                e.stopPropagation();
                navigate(`/scenarios/${scenario.id}/transcripts`, {
                  state: { selectedScenario: scenario }
                });
              }}
              aria-label={`View sample transcripts for ${scenario.title}`}
            >
              <span className="button-icon" aria-hidden="true">📝</span>
              <span className="button-text">View Samples</span>
            </button>
          )}
        </div>
      </div>
    </article>
  );
}

export default ScenarioCard;