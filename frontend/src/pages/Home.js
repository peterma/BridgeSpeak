import React from 'react';
import './pages.css';

function Home() {
  // 12 most popular/essential scenarios for beginners
  const popularScenarios = [
    {
      id: 'introducing-yourself',
      title: 'Introducing Yourself',
      icon: '👋',
      description: 'Learn to introduce yourself in various social situations',
      category: 'Social Skills'
    },
    {
      id: 'asking-for-help',
      title: 'Asking for Help',
      icon: '🙋',
      description: 'Learn to ask for help when you need support',
      category: 'Classroom'
    },
    {
      id: 'asking-for-toilet',
      title: 'Asking for the Toilet',
      icon: '🚻',
      description: 'Learn to politely ask for toilet permission in school',
      category: 'Basic Needs'
    },
    {
      id: 'saying-goodbye',
      title: 'Saying Goodbye',
      icon: '👋',
      description: 'Learn various ways to say goodbye appropriately',
      category: 'Social Skills'
    },
    {
      id: 'expressing-hunger',
      title: 'Expressing Hunger',
      icon: '🍽️',
      description: 'Learn to express hunger and food needs appropriately',
      category: 'Basic Needs'
    },
    {
      id: 'making-new-friends',
      title: 'Making New Friends',
      icon: '🤗',
      description: 'Learn to make friends in the school playground',
      category: 'Social Skills'
    },
    {
      id: 'asking-teacher-question',
      title: 'Asking Teacher a Question',
      icon: '❓',
      description: 'Learn to ask your teacher questions politely',
      category: 'Classroom'
    },
    {
      id: 'playground-games',
      title: 'Playing Playground Games',
      icon: '⚽',
      description: 'Learn to join and organize playground games',
      category: 'Play & Sports'
    },
    {
      id: 'describing-food-preferences',
      title: 'Describing Food Preferences',
      icon: '😋',
      description: 'Learn to express likes and dislikes about food',
      category: 'Daily Life'
    },
    {
      id: 'family-outing-planning',
      title: 'Planning Family Outings',
      icon: '🚗',
      description: 'Learn to participate in family trip planning discussions',
      category: 'Family'
    },
    {
      id: 'apologizing-appropriately',
      title: 'Making Appropriate Apologies',
      icon: '🙏',
      description: 'Learn to apologize sincerely when you make mistakes',
      category: 'Social Skills'
    },
    {
      id: 'sharing-playground-equipment',
      title: 'Sharing Playground Equipment',
      icon: '🤲',
      description: 'Learn to share and take turns with playground equipment',
      category: 'Play & Sports'
    }
  ];

  return (
    <div className="home-page">
      <div className="home-header">
        <h1 className="page-title">Welcome to BridgeSpeak</h1>
        <p className="page-description">
          Bridging languages and cultures through AI-powered conversation practice for children worldwide.
        </p>
      </div>
      
      {/* Quick Actions */}
      <div className="home-actions">
        <a href="/scenarios" className="action-button secondary">
          Browse All Scenarios
        </a>
        <a href="/conversation" className="action-button primary">
          Start Conversation
        </a>
      </div>

      {/* Popular Scenarios Section */}
      <div className="popular-scenarios-section">
        <h2 className="section-title">Popular Scenarios</h2>
        <p className="section-description">
          Start with these essential conversation scenarios designed for beginners
        </p>
        
        <div className="popular-scenarios-grid">
          {popularScenarios.map((scenario) => (
            <a 
              key={scenario.id}
              href={`/conversation?scenario=${scenario.id}`}
              className="scenario-card"
            >
              <div className="scenario-icon">{scenario.icon}</div>
              <div className="scenario-content">
                <h3 className="scenario-title">{scenario.title}</h3>
                <p className="scenario-description">{scenario.description}</p>
                <span className="scenario-category">{scenario.category}</span>
              </div>
            </a>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Home;