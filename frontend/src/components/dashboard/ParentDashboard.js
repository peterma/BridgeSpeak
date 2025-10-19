/**
 * Parent Dashboard Component - Story 4.3.4
 * 
 * Minimal dashboard showing recent activity and quick navigation links.
 * Follows trauma-informed design principles with clear accessibility.
 */

import React from 'react';
import { Link } from 'react-router-dom';
import './ParentDashboard.css';

// Mock recent sessions data for development
const mockRecentSessions = [
  {
    id: 1,
    date: '2025-10-14',
    duration: '12 minutes',
    scenario: 'Introducing Yourself',
    learningGoals: 3,
    completedGoals: 2
  },
  {
    id: 2,
    date: '2025-10-13',
    duration: '8 minutes',
    scenario: 'Asking for Help',
    learningGoals: 4,
    completedGoals: 4
  },
  {
    id: 3,
    date: '2025-10-12',
    duration: '15 minutes',
    scenario: 'Playground Games',
    learningGoals: 5,
    completedGoals: 3
  },
  {
    id: 4,
    date: '2025-10-11',
    duration: '6 minutes',
    scenario: 'Saying Goodbye',
    learningGoals: 3,
    completedGoals: 3
  }
];

function ParentDashboard() {
  return (
    <main className="parent-dashboard" role="main">
      <header className="dashboard-header">
        <h1 className="dashboard-title">Welcome Back!</h1>
        <p className="dashboard-subtitle">
          Here's an overview of your child's recent learning activities with Xiao Mei.
        </p>
      </header>

      {/* Quick Action Shortcuts */}
      <section className="dashboard-shortcuts" aria-labelledby="shortcuts-heading">
        <h2 id="shortcuts-heading" className="section-title">Quick Actions</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6 mt-6">
          <Link 
            to="/scenarios" 
            className="shortcut-card scenarios-shortcut"
            aria-describedby="scenarios-description"
          >
            <div className="shortcut-icon" aria-hidden="true">🎭</div>
            <h3 className="shortcut-title">Practice Scenarios</h3>
            <p id="scenarios-description" className="shortcut-description">
              Choose from learning scenarios for your child to practice with Xiao Mei
            </p>
          </Link>

          <Link 
            to="/conversation" 
            className="shortcut-card conversation-shortcut"
            aria-describedby="conversation-description"
          >
            <div className="shortcut-icon" aria-hidden="true">💬</div>
            <h3 className="shortcut-title">Start Conversation</h3>
            <p id="conversation-description" className="shortcut-description">
              Begin a free-form conversation practice session
            </p>
          </Link>

          <Link 
            to="/settings" 
            className="shortcut-card settings-shortcut"
            aria-describedby="settings-description"
          >
            <div className="shortcut-icon" aria-hidden="true">⚙️</div>
            <h3 className="shortcut-title">Settings</h3>
            <p id="settings-description" className="shortcut-description">
              Adjust learning preferences and platform settings
            </p>
          </Link>
        </div>
      </section>

      {/* Recent Sessions */}
      <section className="recent-sessions" aria-labelledby="sessions-heading">
        <h2 id="sessions-heading" className="section-title">Recent Learning Sessions</h2>
        <div className="sessions-list" role="list" aria-label="Recent learning sessions">
          {mockRecentSessions.map((session) => (
            <article 
              key={session.id}
              className="session-item"
              role="listitem"
              tabIndex={0}
              aria-labelledby={`session-${session.id}-title`}
              aria-describedby={`session-${session.id}-details`}
            >
              <div className="session-header">
                <h3 id={`session-${session.id}-title`} className="session-scenario">
                  {session.scenario}
                </h3>
                <time className="session-date" dateTime={session.date}>
                  {new Date(session.date).toLocaleDateString('en-IE', {
                    weekday: 'short',
                    month: 'short',
                    day: 'numeric'
                  })}
                </time>
              </div>
              
              <div id={`session-${session.id}-details`} className="session-details">
                <div className="session-duration">
                  <span className="detail-icon" aria-hidden="true">⏱️</span>
                  <span>{session.duration}</span>
                </div>
                
                <div className="session-progress">
                  <span className="detail-icon" aria-hidden="true">✅</span>
                  <span>
                    {session.completedGoals} of {session.learningGoals} goals completed
                  </span>
                </div>
              </div>

              <div className="session-progress-bar" role="progressbar" 
                   aria-valuenow={session.completedGoals} 
                   aria-valuemin={0} 
                   aria-valuemax={session.learningGoals}
                   aria-label={`Progress: ${session.completedGoals} out of ${session.learningGoals} goals completed`}>
                <div 
                  className="progress-fill"
                  style={{ width: `${(session.completedGoals / session.learningGoals) * 100}%` }}
                />
              </div>
            </article>
          ))}
        </div>

        {mockRecentSessions.length === 0 && (
          <div className="no-sessions" role="status">
            <p className="no-sessions-text">
              No recent sessions yet. Start practicing with Xiao Mei to see your progress here!
            </p>
            <Link to="/scenarios" className="start-button">
              Choose Your First Scenario
            </Link>
          </div>
        )}
      </section>

      {/* Encouragement Section */}
      <section className="encouragement-section" aria-labelledby="encouragement-heading">
        <h2 id="encouragement-heading" className="section-title">Keep Going!</h2>
        <div className="encouragement-card">
          <div className="encouragement-icon" aria-hidden="true">🌟</div>
          <p className="encouragement-text">
            Every conversation with Xiao Mei is a step forward in building confidence with English. 
            Take your time and remember that learning happens at your own pace.
          </p>
        </div>
      </section>

      {/* Screen reader announcements */}
      <div className="sr-only" aria-live="polite" aria-atomic="true">
        Dashboard loaded with {mockRecentSessions.length} recent sessions
      </div>
    </main>
  );
}

export default ParentDashboard;