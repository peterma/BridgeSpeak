import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { jest } from '@jest/globals';

// Mock the navigate function
const mockNavigate = jest.fn();

// Mock functions are now handled globally in setupTests.js

import ScenarioCard from './ScenarioCard';

const mockScenario = {
  id: 'intro-yourself',
  title: 'Introducing Yourself',
  description: 'Learn to introduce yourself to new friends and teachers at school',
  category: 'essential',
  ageGroups: ['junior-infants', 'senior-infants', 'first-class'],
  difficulty: 'beginner',
  estimatedTime: '5-10 minutes',
  tags: ['introductions', 'basic', 'names', 'friendship'],
  chineseContext: '自我介绍 - 学会在学校向新朋友和老师介绍自己',
  objectives: [
    'Say your name clearly',
    'Tell your age',
    'Share where you come from',
    'Practice polite greetings'
  ],
  isPopular: true
};

const mockOnSelect = jest.fn();

const renderWithRouter = (component) => {
  return render(component);
};

describe('ScenarioCard', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders scenario information correctly', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    expect(screen.getByText('Introducing Yourself')).toBeInTheDocument();
    expect(screen.getByText('Learn to introduce yourself to new friends and teachers at school')).toBeInTheDocument();
    expect(screen.getByText('beginner')).toBeInTheDocument();
    expect(screen.getByText('Essential')).toBeInTheDocument();
    expect(screen.getByText('5-10 minutes')).toBeInTheDocument();
  });

  test('shows popularity badge for popular scenarios', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    expect(screen.getByText('⭐ Popular')).toBeInTheDocument();
  });

  test('does not show popularity badge for non-popular scenarios', () => {
    const nonPopularScenario = { ...mockScenario, isPopular: false };
    
    renderWithRouter(
      <ScenarioCard scenario={nonPopularScenario} onSelect={mockOnSelect} />
    );
    
    expect(screen.queryByText('⭐ Popular')).not.toBeInTheDocument();
  });

  test('renders Chinese context', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    const chineseText = screen.getByText('自我介绍 - 学会在学校向新朋友和老师介绍自己');
    expect(chineseText).toBeInTheDocument();
    expect(chineseText).toHaveAttribute('lang', 'zh-CN');
  });

  test('renders scenario tags', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    expect(screen.getByText('introductions')).toBeInTheDocument();
    expect(screen.getByText('basic')).toBeInTheDocument();
    expect(screen.getByText('names')).toBeInTheDocument();
    expect(screen.getByText('friendship')).toBeInTheDocument();
  });

  test('renders learning objectives', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    expect(screen.getByText('You will learn to:')).toBeInTheDocument();
    expect(screen.getByText('Say your name clearly')).toBeInTheDocument();
    expect(screen.getByText('Tell your age')).toBeInTheDocument();
    expect(screen.getByText('Share where you come from')).toBeInTheDocument();
  });

  test('shows "more objectives" indicator when there are more than 3 objectives', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    expect(screen.getByText('+1 more skills')).toBeInTheDocument();
  });

  test('navigates to conversation page when card is clicked', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    const card = screen.getByRole('button', { name: /Practice Introducing Yourself scenario/ });
    fireEvent.click(card);
    
    expect(mockNavigate).toHaveBeenCalledWith('/conversation?scenario=intro-yourself', {
      state: { selectedScenario: mockScenario }
    });
  });

  test('calls onSelect callback when card is clicked', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    const card = screen.getByRole('button', { name: /Practice Introducing Yourself scenario/ });
    fireEvent.click(card);
    
    expect(mockOnSelect).toHaveBeenCalledWith(mockScenario);
  });

  test('navigates when start button is clicked', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    const startButton = screen.getByRole('button', { name: 'Start practicing Introducing Yourself' });
    fireEvent.click(startButton);
    
    expect(mockNavigate).toHaveBeenCalledWith('/conversation?scenario=intro-yourself', {
      state: { selectedScenario: mockScenario }
    });
  });

  test('handles keyboard navigation with Enter key', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    const card = screen.getByRole('button', { name: /Practice Introducing Yourself scenario/ });
    fireEvent.keyDown(card, { key: 'Enter' });
    
    expect(mockNavigate).toHaveBeenCalledWith('/conversation?scenario=intro-yourself', {
      state: { selectedScenario: mockScenario }
    });
  });

  test('handles keyboard navigation with Space key', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    const card = screen.getByRole('button', { name: /Practice Introducing Yourself scenario/ });
    fireEvent.keyDown(card, { key: ' ' });
    
    expect(mockNavigate).toHaveBeenCalledWith('/conversation?scenario=intro-yourself', {
      state: { selectedScenario: mockScenario }
    });
  });

  test('prevents default behavior for Enter and Space keys', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    const card = screen.getByRole('button', { name: /Practice Introducing Yourself scenario/ });
    
    const enterEvent = new KeyboardEvent('keydown', { key: 'Enter' });
    const spaceEvent = new KeyboardEvent('keydown', { key: ' ' });
    
    const preventDefaultSpy = jest.spyOn(enterEvent, 'preventDefault');
    const preventDefaultSpy2 = jest.spyOn(spaceEvent, 'preventDefault');
    
    fireEvent.keyDown(card, enterEvent);
    fireEvent.keyDown(card, spaceEvent);
    
    expect(preventDefaultSpy).toHaveBeenCalled();
    expect(preventDefaultSpy2).toHaveBeenCalled();
  });

  test('has proper accessibility attributes', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    const card = screen.getByRole('button', { name: /Practice Introducing Yourself scenario/ });
    
    expect(card).toHaveAttribute('tabIndex', '0');
    expect(card).toHaveAttribute('aria-label', 'Practice Introducing Yourself scenario');
    expect(card).toHaveAttribute('aria-describedby', 'scenario-intro-yourself-description scenario-intro-yourself-tags');
  });

  test('renders proper semantic structure', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    // Check for article element
    const article = screen.getByRole('button', { name: /Practice Introducing Yourself scenario/ });
    expect(article.tagName).toBe('ARTICLE');
    
    // Check for heading
    expect(screen.getByRole('heading', { level: 3 })).toHaveTextContent('Introducing Yourself');
    
    // Check for list of objectives
    expect(screen.getByRole('list')).toBeInTheDocument();
    expect(screen.getAllByRole('listitem')).toHaveLength(4); // 3 objectives + "more skills"
  });

  test('displays correct difficulty color class', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    const difficultyBadge = screen.getByText('beginner');
    expect(difficultyBadge).toHaveClass('difficulty-badge', 'beginner');
  });

  test('displays correct category label', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    expect(screen.getByText('Essential')).toBeInTheDocument();
  });

  test('displays age groups count', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    expect(screen.getByText('3 age groups')).toBeInTheDocument();
  });

  test('displays single age group correctly', () => {
    const singleAgeScenario = { ...mockScenario, ageGroups: ['junior-infants'] };
    
    renderWithRouter(
      <ScenarioCard scenario={singleAgeScenario} onSelect={mockOnSelect} />
    );
    
    expect(screen.getByText('1 age group')).toBeInTheDocument();
  });

  test('renders appropriate icon for category', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} onSelect={mockOnSelect} />
    );
    
    // Essential category should show star icon
    expect(screen.getByText('🌟')).toBeInTheDocument();
  });

  test('does not call onSelect when onSelect is not provided', () => {
    renderWithRouter(
      <ScenarioCard scenario={mockScenario} />
    );
    
    const card = screen.getByRole('button', { name: /Practice Introducing Yourself scenario/ });
    fireEvent.click(card);
    
    // Should still navigate but not call onSelect
    expect(mockNavigate).toHaveBeenCalled();
  });
});
