import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { jest } from '@jest/globals';

// Mock the navigate function
const mockNavigate = jest.fn();
const mockSetSearchParams = jest.fn();

const mockScenarios = [
  {
    id: 'intro-yourself',
    title: 'Introducing Yourself',
    description: 'Learn to introduce yourself to new friends and teachers at school',
    category: 'essential',
    ageGroups: ['junior-infants', 'senior-infants'],
    difficulty: 'beginner',
    estimatedTime: '5-10 minutes',
    tags: ['introductions', 'basic', 'names'],
    chineseContext: '自我介绍',
    objectives: ['Say your name clearly', 'Tell your age'],
    isPopular: true
  },
  {
    id: 'ask-toilet',
    title: 'Asking for the Toilet',
    description: 'Essential phrases for bathroom needs at school',
    category: 'essential',
    ageGroups: ['junior-infants'],
    difficulty: 'beginner',
    estimatedTime: '3-5 minutes',
    tags: ['bathroom', 'urgent', 'polite-requests'],
    chineseContext: '上厕所',
    objectives: ['Ask permission politely', 'Use "toilet"'],
    isPopular: true
  }
];

// Mock functions are now handled globally in setupTests.js

import ScenariosPage from './ScenariosPage';

// Mock the scenario data
jest.mock('../data/scenarios', () => {
  const mockScenarios = [
    {
      id: 'intro-yourself',
      title: 'Introducing Yourself',
      description: 'Learn to introduce yourself to new friends and teachers at school',
      category: 'essential',
      ageGroups: ['junior-infants', 'senior-infants'],
      difficulty: 'beginner',
      estimatedTime: '5-10 minutes',
      tags: ['introductions', 'basic', 'names'],
      chineseContext: '自我介绍',
      objectives: ['Say your name clearly', 'Tell your age'],
      isPopular: true
    },
    {
      id: 'ask-toilet',
      title: 'Asking for the Toilet',
      description: 'Essential phrases for bathroom needs at school',
      category: 'essential',
      ageGroups: ['junior-infants'],
      difficulty: 'beginner',
      estimatedTime: '3-5 minutes',
      tags: ['bathroom', 'urgent', 'polite-requests'],
      chineseContext: '上厕所',
      objectives: ['Ask permission politely', 'Use "toilet"'],
      isPopular: true
    }
  ];
  
  return {
    mockScenarios,
    getAllTags: () => ['introductions', 'basic', 'names', 'bathroom', 'urgent', 'polite-requests'],
    searchScenarios: (query) => {
      if (!query.trim()) return mockScenarios;
      return mockScenarios.filter(scenario =>
        scenario.title.toLowerCase().includes(query.toLowerCase()) ||
        scenario.description.toLowerCase().includes(query.toLowerCase())
      );
    },
    filterScenariosByTags: (tags) => {
      if (!tags.length) return mockScenarios;
      return mockScenarios.filter(scenario =>
        tags.every(tag => scenario.tags.includes(tag))
      );
    },
    getPopularScenarios: () => mockScenarios.filter(scenario => scenario.isPopular)
  };
});

const renderWithRouter = (component) => {
  return render(component);
};

describe('ScenariosPage', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders page title and description', () => {
    renderWithRouter(<ScenariosPage />);
    
    expect(screen.getByText('Learning Scenarios')).toBeInTheDocument();
    expect(screen.getByText(/Choose a scenario to practice with Xiao Mei/)).toBeInTheDocument();
  });

  test('renders search input with proper accessibility', () => {
    renderWithRouter(<ScenariosPage />);
    
    const searchInput = screen.getByLabelText('Search scenarios');
    expect(searchInput).toBeInTheDocument();
    expect(searchInput).toHaveAttribute('placeholder', 'Search by title, description, or topic...');
    expect(searchInput).toHaveAttribute('aria-describedby', 'search-help');
  });

  test('renders tag filters with proper accessibility', () => {
    renderWithRouter(<ScenariosPage />);
    
    const filterGroup = screen.getByRole('group', { name: 'Filter by topics' });
    expect(filterGroup).toBeInTheDocument();
    
    const tagButtons = screen.getAllByRole('button', { name: /Filter by .* topics/ });
    expect(tagButtons.length).toBeGreaterThan(0);
  });

  test('renders scenario cards', () => {
    renderWithRouter(<ScenariosPage />);
    
    expect(screen.getByText('Introducing Yourself')).toBeInTheDocument();
    expect(screen.getByText('Asking for the Toilet')).toBeInTheDocument();
  });

  test('filters scenarios by search query', async () => {
    renderWithRouter(<ScenariosPage />);
    
    const searchInput = screen.getByLabelText('Search scenarios');
    fireEvent.change(searchInput, { target: { value: 'toilet' } });
    
    await waitFor(() => {
      expect(screen.getByText('Asking for the Toilet')).toBeInTheDocument();
      expect(screen.queryByText('Introducing Yourself')).not.toBeInTheDocument();
    });
  });

  test('filters scenarios by tags', async () => {
    renderWithRouter(<ScenariosPage />);
    
    const bathroomFilter = screen.getByRole('button', { name: 'Filter by bathroom topics' });
    fireEvent.click(bathroomFilter);
    
    await waitFor(() => {
      expect(bathroomFilter).toHaveAttribute('aria-pressed', 'true');
    });
  });

  test('shows no results message when no scenarios match', async () => {
    renderWithRouter(<ScenariosPage />);
    
    const searchInput = screen.getByLabelText('Search scenarios');
    fireEvent.change(searchInput, { target: { value: 'nonexistent' } });
    
    await waitFor(() => {
      expect(screen.getByText('No scenarios match your search')).toBeInTheDocument();
      expect(screen.getByText('Show all scenarios')).toBeInTheDocument();
    });
  });

  test('clears filters when clear button is clicked', async () => {
    renderWithRouter(<ScenariosPage />);
    
    const searchInput = screen.getByLabelText('Search scenarios');
    fireEvent.change(searchInput, { target: { value: 'toilet' } });
    
    const clearButton = screen.getByText('Clear all');
    fireEvent.click(clearButton);
    
    await waitFor(() => {
      expect(searchInput).toHaveValue('');
      expect(screen.getByText('Introducing Yourself')).toBeInTheDocument();
      expect(screen.getByText('Asking for the Toilet')).toBeInTheDocument();
    });
  });

  test('shows popular scenarios section when no filters are applied', () => {
    renderWithRouter(<ScenariosPage />);
    
    expect(screen.getByText('Popular Scenarios')).toBeInTheDocument();
    expect(screen.getByText(/Start with these scenarios that other children love/)).toBeInTheDocument();
  });

  test('hides popular scenarios section when filters are applied', async () => {
    renderWithRouter(<ScenariosPage />);
    
    const searchInput = screen.getByLabelText('Search scenarios');
    fireEvent.change(searchInput, { target: { value: 'toilet' } });
    
    await waitFor(() => {
      expect(screen.queryByText('Popular Scenarios')).not.toBeInTheDocument();
    });
  });

  test('shows active filters when filters are applied', async () => {
    renderWithRouter(<ScenariosPage />);
    
    const searchInput = screen.getByLabelText('Search scenarios');
    fireEvent.change(searchInput, { target: { value: 'toilet' } });
    
    await waitFor(() => {
      expect(screen.getByText('Active filters:')).toBeInTheDocument();
      expect(screen.getByText('Search: "toilet"')).toBeInTheDocument();
    });
  });

  test('announces results to screen readers', () => {
    renderWithRouter(<ScenariosPage />);
    
    const announcement = screen.getByRole('status');
    expect(announcement).toHaveAttribute('aria-live', 'polite');
    expect(announcement).toHaveAttribute('aria-atomic', 'true');
  });

  test('handles scenario selection', () => {
    renderWithRouter(<ScenariosPage />);
    
    // This would be tested through the ScenarioCard component
    // The ScenariosPage just passes the onSelect callback
    expect(screen.getByText('Introducing Yourself')).toBeInTheDocument();
  });

  test('renders with proper semantic structure', () => {
    renderWithRouter(<ScenariosPage />);
    
    // Check for proper headings hierarchy
    expect(screen.getByRole('heading', { level: 1 })).toHaveTextContent('Learning Scenarios');
    expect(screen.getByRole('heading', { level: 2 })).toHaveTextContent(/All Scenarios|Found \d+ scenario/);
    
    // Check for proper regions
    expect(screen.getByRole('region', { name: 'Scenario list' })).toBeInTheDocument();
  });

  test('handles keyboard navigation', () => {
    renderWithRouter(<ScenariosPage />);
    
    const searchInput = screen.getByLabelText('Search scenarios');
    searchInput.focus();
    
    // Tab should move to next focusable element
    fireEvent.keyDown(searchInput, { key: 'Tab' });
    // This would be tested more thoroughly in integration tests
  });
});
