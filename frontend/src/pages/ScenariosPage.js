import React, { useState, useMemo, useCallback } from 'react';
import { useSearchParams } from 'react-router-dom';
import ScenarioCard from '../components/scenarios/ScenarioCard';
import { 
  mockScenarios, 
  getAllTags, 
  searchScenarios, 
  filterScenariosByTags,
  getPopularScenarios,
  DIFFICULTY_LEVELS
} from '../data/scenarios';
import { useViewportDebugEffect } from '../utils/debug';
import './ScenariosPage.css';

function ScenariosPage() {
  // const navigate = useNavigate();
  const [searchParams, setSearchParams] = useSearchParams();
  
  // State for filters
  const [searchQuery, setSearchQuery] = useState(searchParams.get('search') || '');
  const [selectedTags, setSelectedTags] = useState(
    searchParams.get('tags') ? searchParams.get('tags').split(',') : []
  );
  const [selectedDifficulty, setSelectedDifficulty] = useState(
    searchParams.get('difficulty') || ''
  );
  const [showPopularOnly, setShowPopularOnly] = useState(false);

  // Available tags for filtering
  const allTags = useMemo(() => getAllTags(), []);

  // Filtered scenarios based on search, tags, and difficulty
  const filteredScenarios = useMemo(() => {
    let filtered = mockScenarios;

    // Apply search filter
    if (searchQuery.trim()) {
      filtered = searchScenarios(searchQuery);
    }

    // Apply tag filter
    if (selectedTags.length > 0) {
      filtered = filterScenariosByTags(selectedTags).filter(scenario =>
        searchQuery.trim() ? searchScenarios(searchQuery).includes(scenario) : true
      );
    }

    // Apply difficulty filter
    if (selectedDifficulty) {
      filtered = filtered.filter(scenario => scenario.difficulty === selectedDifficulty);
    }

    // Apply popularity filter
    if (showPopularOnly) {
      filtered = filtered.filter(scenario => scenario.isPopular);
    }

    return filtered;
  }, [searchQuery, selectedTags, selectedDifficulty, showPopularOnly]);

  // Update URL search params when filters change
  const updateSearchParams = useCallback((newQuery, newTags, newDifficulty) => {
    const params = new URLSearchParams();
    if (newQuery.trim()) params.set('search', newQuery);
    if (newTags.length > 0) params.set('tags', newTags.join(','));
    if (newDifficulty) params.set('difficulty', newDifficulty);
    setSearchParams(params);
  }, [setSearchParams]);

  const handleSearchChange = useCallback((event) => {
    const newQuery = event.target.value;
    setSearchQuery(newQuery);
    updateSearchParams(newQuery, selectedTags, selectedDifficulty);
  }, [selectedTags, selectedDifficulty, updateSearchParams]);

  const handleTagToggle = useCallback((tag) => {
    const newTags = selectedTags.includes(tag)
      ? selectedTags.filter(t => t !== tag)
      : [...selectedTags, tag];
    
    setSelectedTags(newTags);
    updateSearchParams(searchQuery, newTags, selectedDifficulty);
  }, [selectedTags, searchQuery, selectedDifficulty, updateSearchParams]);

  const handleDifficultyChange = useCallback((difficulty) => {
    setSelectedDifficulty(difficulty);
    updateSearchParams(searchQuery, selectedTags, difficulty);
  }, [searchQuery, selectedTags, updateSearchParams]);

  const handleClearFilters = useCallback(() => {
    setSearchQuery('');
    setSelectedTags([]);
    setSelectedDifficulty('');
    setShowPopularOnly(false);
    setSearchParams(new URLSearchParams());
  }, [setSearchParams]);

  const handleScenarioSelect = useCallback((scenario) => {
    // This could be used for analytics or state management
    console.log('Selected scenario:', scenario.id);
  }, []);

  // Debug viewport (only active when debug=true in URL or localStorage)
  useViewportDebugEffect('.scenarios-grid');


  return (
    <div className="scenarios-page">
      <div className="text-center mb-8 lg:mb-12">
        <div className="max-w-4xl mx-auto">
          <h1 className="page-title">Learning Scenarios</h1>
          <p className="page-description">
            Choose a scenario to practice with Xiao Mei (小美). Each scenario helps you learn 
            important English phrases for school and daily life in Ireland.
          </p>
        </div>
      </div>

      <div className="bg-white rounded-lg shadow-sm border p-4 md:p-6 mb-6 lg:mb-8">
        <div className="search-section">
          <label htmlFor="scenario-search" className="search-label">
            Search scenarios
          </label>
          <div className="search-input-container">
            <input
              id="scenario-search"
              type="text"
              className="search-input"
              placeholder="Search by title, description, or topic..."
              value={searchQuery}
              onChange={handleSearchChange}
              aria-describedby="search-help"
            />
            <span className="search-icon" aria-hidden="true">🔍</span>
          </div>
          <div id="search-help" className="search-help">
            Try searching for "help", "toilet", or "friends"
          </div>
        </div>

        <div className="mt-6">
          <div>
            <h3 className="text-lg font-semibold text-gray-900 mb-3">Filter by topics</h3>
            <div className="flex flex-wrap gap-2" role="group" aria-label="Filter by topics">
              {allTags.map(tag => (
                <button
                  key={tag}
                  className={`px-3 py-1.5 text-sm rounded-full border transition-colors ${
                    selectedTags.includes(tag) 
                      ? 'bg-blue-600 text-white border-blue-600' 
                      : 'bg-gray-100 text-gray-700 border-gray-300 hover:bg-gray-200'
                  }`}
                  onClick={() => handleTagToggle(tag)}
                  aria-pressed={selectedTags.includes(tag)}
                  aria-label={`Filter by ${tag} topics`}
                >
                  {tag}
                </button>
              ))}
            </div>
          </div>

          <div className="mt-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-3">Filter by difficulty</h3>
            <div className="flex flex-wrap gap-2" role="group" aria-label="Filter by difficulty">
              <button
                className={`px-3 py-1.5 text-sm rounded-full border transition-colors ${
                  selectedDifficulty === '' 
                    ? 'bg-blue-600 text-white border-blue-600' 
                    : 'bg-gray-100 text-gray-700 border-gray-300 hover:bg-gray-200'
                }`}
                onClick={() => handleDifficultyChange('')}
                aria-pressed={selectedDifficulty === ''}
                aria-label="Show all difficulty levels"
              >
                All Levels
              </button>
              {Object.entries(DIFFICULTY_LEVELS).map(([key, value]) => (
                <button
                  key={value}
                  className={`px-3 py-1.5 text-sm rounded-full border transition-colors ${
                    selectedDifficulty === value 
                      ? 'bg-blue-600 text-white border-blue-600' 
                      : 'bg-gray-100 text-gray-700 border-gray-300 hover:bg-gray-200'
                  }`}
                  onClick={() => handleDifficultyChange(value)}
                  aria-pressed={selectedDifficulty === value}
                  aria-label={`Filter by ${key.toLowerCase()} difficulty`}
                >
                  {key}
                </button>
              ))}
            </div>
          </div>

          <div className="mt-4">
            <label className="flex items-center space-x-2 cursor-pointer">
              <input
                type="checkbox"
                checked={showPopularOnly}
                onChange={(e) => setShowPopularOnly(e.target.checked)}
                className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
              />
              <span className="text-sm text-gray-700">Show popular scenarios only</span>
            </label>
          </div>

          {(searchQuery || selectedTags.length > 0 || selectedDifficulty || showPopularOnly) && (
            <div className="active-filters">
              <span className="active-filters-label">Active filters:</span>
              {searchQuery && (
                <span className="active-filter">
                  Search: "{searchQuery}"
                </span>
              )}
              {selectedTags.map(tag => (
                <span key={tag} className="active-filter">
                  Topic: {tag}
                  <button
                    className="remove-filter"
                    onClick={() => handleTagToggle(tag)}
                    aria-label={`Remove ${tag} filter`}
                  >
                    ×
                  </button>
                </span>
              ))}
              {selectedDifficulty && (
                <span className="active-filter">
                  Difficulty: {Object.keys(DIFFICULTY_LEVELS).find(key => DIFFICULTY_LEVELS[key] === selectedDifficulty)}
                  <button
                    className="remove-filter"
                    onClick={() => handleDifficultyChange('')}
                    aria-label="Remove difficulty filter"
                  >
                    ×
                  </button>
                </span>
              )}
              {showPopularOnly && (
                <span className="active-filter">Popular only</span>
              )}
              <button
                className="clear-filters-button"
                onClick={handleClearFilters}
                aria-label="Clear all filters"
              >
                Clear all
              </button>
            </div>
          )}
        </div>
      </div>

      <div className="scenarios-results">
        <div className="results-header">
          <h2 className="results-title">
            {filteredScenarios.length === mockScenarios.length 
              ? `All Scenarios (${filteredScenarios.length})` 
              : `Found ${filteredScenarios.length} scenario${filteredScenarios.length !== 1 ? 's' : ''}`
            }
          </h2>
          {filteredScenarios.length === 0 && (
            <div className="no-results" role="status">
              <p className="no-results-text">
                No scenarios match your search. Try different keywords or remove some filters.
              </p>
              <button 
                className="clear-filters-button"
                onClick={handleClearFilters}
              >
                Show all scenarios
              </button>
            </div>
          )}
        </div>

        {filteredScenarios.length > 0 && (
          <div className="scenarios-grid" role="region" aria-label="Scenario list">
            {filteredScenarios.map(scenario => (
              <ScenarioCard
                key={scenario.id}
                scenario={scenario}
                onSelect={handleScenarioSelect}
              />
            ))}
          </div>
        )}
      </div>

      {/* Quick access to popular scenarios */}
      {!showPopularOnly && filteredScenarios.length === mockScenarios.length && (
        <div className="popular-scenarios-section">
          <h2 className="section-title">Popular Scenarios</h2>
          <p className="section-description">
            Start with these scenarios that other children love practicing
          </p>
          <div className="popular-scenarios-grid">
            {getPopularScenarios().slice(0, 3).map(scenario => (
              <ScenarioCard
                key={`popular-${scenario.id}`}
                scenario={scenario}
                onSelect={handleScenarioSelect}
              />
            ))}
          </div>
        </div>
      )}

      {/* Screen reader announcements */}
      <div className="sr-only" aria-live="polite" aria-atomic="true">
        {filteredScenarios.length > 0 && 
          `${filteredScenarios.length} scenarios available for practice`
        }
      </div>
    </div>
  );
}

export default ScenariosPage;