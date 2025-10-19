/**
 * Transcript loading and management utilities
 * 
 * This module provides functions to load, parse, and transform transcript data
 * from JSON files into formats compatible with frontend components.
 */

// Import all transcript files
// Note: In a real application, you might want to use dynamic imports or a build-time process
// For now, we'll create a mapping of scenario IDs to their available transcripts

const TRANSCRIPT_MAP = {
  // Basic social scenarios
  'introducing-yourself': [
    'intro-yourself_variant1_junior-infants',
    'intro-yourself_variant2_senior-infants', 
    'intro-yourself_variant3_first-class'
  ],
  'intro-yourself': [
    'intro-yourself_variant1_junior-infants',
    'intro-yourself_variant2_senior-infants', 
    'intro-yourself_variant3_first-class'
  ],

  // School basic needs
  'asking-for-toilet': [
    'ask-toilet_variant1_junior-infants',
    'ask-toilet_variant2_senior-infants',
    'ask-toilet_variant3_first-class'
  ],
  'ask-toilet': [
    'ask-toilet_variant1_junior-infants',
    'ask-toilet_variant2_senior-infants',
    'ask-toilet_variant3_first-class'
  ],

  // Help and support scenarios
  'asking-for-help': [
    'ask-help_variant1_junior-infants',
    'ask-help_variant2_senior-infants',
    'ask-help_variant3_first-class'
  ],
  'ask-help': [
    'ask-help_variant1_junior-infants',
    'ask-help_variant2_senior-infants',
    'ask-help_variant3_first-class'
  ],
  'asking-classmate-help': [
    'classmate-help_variant1_first-class'
  ],
  'asking-teacher-question': [
    'teacher-questions_variant1_first-class',
    'ask-help_variant2_senior-infants',
    'ask-help_variant3_first-class'
  ],
  'asking-lunch-help': [
    'ask-help_variant1_junior-infants',
    'ask-help_variant2_senior-infants',
    'ask-help_variant3_first-class'
  ],

  // Food and hunger scenarios  
  'expressing-hunger': [
    'express-hunger_variant1_junior-infants',
    'express-hunger_variant2_senior-infants'
  ],
  'express-hunger': [
    'express-hunger_variant1_junior-infants',
    'express-hunger_variant2_senior-infants'
  ],
  'lunch-food-conversation': [
    'express-hunger_variant1_junior-infants',
    'express-hunger_variant2_senior-infants',
    'lunch-food-conversation_variant1_junior-infants'
  ],
  'sharing-cultural-food': [
    'cultural-foods_variant1_second-class',
    'express-hunger_variant2_senior-infants'
  ],
  'describing-food-preferences': [
    'food-preferences_variant1_first-class'
  ],
  'canteen-politeness': [
    'express-hunger_variant1_junior-infants',
    'express-hunger_variant2_senior-infants'
  ],

  // Farewell scenarios
  'saying-goodbye': [
    'saying-goodbye_variant1_junior-infants',
    'saying-goodbye_variant2_senior-infants',
    'saying-goodbye_variant3_first-class'
  ],

  // Playground and social play scenarios
  'playground-games': [
    'playground-games_variant1_senior-infants',
    'playground-games_variant2_first-class',
    'playground-games_variant3_second-class'
  ],
  'playing-playground-games': [
    'playground-join_variant1_junior-infants',
    'playground-games_variant1_senior-infants',
    'playground-games_variant2_first-class'
  ],
  'inviting-to-play': [
    'inviting-play_variant1_first-class'
  ],
  'making-new-friends': [
    'making-friends_variant1_senior-infants',
    'playground-games_variant2_first-class',
    'playground-games_variant3_second-class'
  ],
  'resolving-playground-conflict': [
    'playground-conflict_variant1_second-class'
  ],
  'sharing-playground-equipment': [
    'playground-games_variant1_senior-infants',
    'playground-games_variant2_first-class',
    'playground-games_variant3_second-class'
  ],
  'expressing-feelings-playground': [
    'playground-feelings_variant1_second-class'
  ],
  'organizing-group-game': [
    'organizing-games_variant1_second-class'
  ],
  'comforting-upset-friend': [
    'comforting-friend_variant1_first-class'
  ],
  'sibling-play-interaction': [
    'playground-games_variant1_senior-infants',
    'playground-games_variant2_first-class',
    'playground-games_variant3_second-class'
  ],
  'sports-day-activities': [
    'sports-day_variant1_second-class'
  ],

  // Classroom learning scenarios
  'classroom-participation': [
    'classroom-participation_variant1_first-class',
    'classroom-participation_variant2_second-class',
    'classroom-participation_variant3_third-class'
  ],
  'participating-discussion': [
    'class-discussion_variant1_third-class'
  ],
  'group-work-collaboration': [
    'classroom-participation_variant1_first-class',
    'classroom-participation_variant2_second-class',
    'classroom-participation_variant3_third-class',
    'group-work-collaboration_variant1_junior-infants'
  ],
  'answering-in-class': [
    'answering-class_variant1_first-class'
  ],
  'explaining-homework-problem': [
    'homework-help_variant1_second-class'
  ],
  'sharing-learning-materials': [
    'sharing-materials_variant1_first-class'
  ],
  'reading-aloud-class': [
    'reading-aloud_variant1_second-class'
  ],
  'showing-understanding': [
    'showing-understanding_variant1_first-class'
  ],
  'school-assembly-participation': [
    'school-assembly_variant1_second-class'
  ],

  // New high-priority scenarios
  'working-together-groups': [
    'group-work-collaboration_variant1_junior-infants'
  ],
  'class-presentation': [
    'class-presentation_variant1_junior-infants',
    'class-presentation_variant1_senior-infants',
    'class-presentation_variant1_first-class'
  ],
  'giving-class-presentation': [
    'class-presentation_variant1_junior-infants',
    'class-presentation_variant1_senior-infants',
    'class-presentation_variant1_first-class'
  ],
  'talking-about-lunch': [
    'lunch-food-conversation_variant1_junior-infants'
  ],
  'sharing-chinese-culture': [
    'sharing-chinese-culture_variant1_junior-infants',
    'irish-culture_variant1_second-class',
    'irish-culture_variant2_third-class',
    'irish-culture_variant3_fourth-class'
  ],

  // Cultural scenarios
  'irish-culture': [
    'irish-culture_variant1_second-class',
    'irish-culture_variant2_third-class',
    'irish-culture_variant3_fourth-class'
  ],
  'st-patricks-day-celebration': [
    'irish-culture_variant1_second-class',
    'irish-culture_variant2_third-class',
    'irish-culture_variant3_fourth-class'
  ],
  'gaa-match-watching': [
    'irish-culture_variant1_second-class',
    'irish-culture_variant2_third-class',
    'irish-culture_variant3_fourth-class'
  ],
  'irish-traditional-music-event': [
    'irish-traditions_variant1_third-class',
    'irish-culture_variant2_third-class',
    'irish-culture_variant3_fourth-class'
  ],
  'irish-dancing-participation': [
    'irish-culture_variant1_second-class',
    'irish-culture_variant2_third-class',
    'irish-culture_variant3_fourth-class'
  ],
  'dublin-heritage-visit': [
    'irish-culture_variant1_second-class',
    'irish-culture_variant2_third-class',
    'irish-culture_variant3_fourth-class'
  ],
  'explaining-chinese-holiday': [
    'irish-culture_variant1_second-class',
    'irish-culture_variant2_third-class',
    'irish-culture_variant3_fourth-class'
  ],
  'local-community-event': [
    'irish-culture_variant1_second-class',
    'irish-culture_variant2_third-class',
    'irish-culture_variant3_fourth-class'
  ],
  'community-gathering-participation': [
    'irish-culture_variant1_second-class',
    'irish-culture_variant2_third-class',
    'irish-culture_variant3_fourth-class'
  ],

  // Emergency and safety scenarios
  'emergency-situations': [
    'emergency-situations_variant1_junior-infants',
    'emergency-situations_variant2_senior-infants',
    'emergency-situations_variant3_first-class',
    'emergency-situations_variant4_second-class'
  ],

  // Shopping and daily life scenarios
  'grocery-shopping-help': [
    'grocery-shopping_variant1_third-class'
  ],
  'clothes-shopping-preferences': [
    'clothes-shopping_variant1_third-class'
  ],
  'asking-store-directions': [
    'store-directions_variant1_second-class'
  ],
  'paying-at-checkout': [
    'checkout-payment_variant1_third-class'
  ],
  'comparing-prices': [
    'price-comparison_variant1_fourth-class'
  ],
  'asking-product-location': [
    'ask-help_variant1_junior-infants',
    'ask-help_variant2_senior-infants',
    'ask-help_variant3_first-class'
  ],
  'expressing-shopping-needs': [
    'express-hunger_variant1_junior-infants',
    'express-hunger_variant2_senior-infants'
  ],
  'polite-shop-interaction': [
    'intro-yourself_variant1_junior-infants',
    'intro-yourself_variant2_senior-infants', 
    'intro-yourself_variant3_first-class'
  ],

  // Transportation scenarios
  'bus-conversation': [
    'bus-travel_variant1_third-class'
  ],
  'dart-ticket-purchase': [
    'ask-help_variant1_junior-infants',
    'ask-help_variant2_senior-infants',
    'ask-help_variant3_first-class'
  ],
  'asking-walking-directions': [
    'ask-help_variant1_junior-infants',
    'ask-help_variant2_senior-infants',
    'ask-help_variant3_first-class'
  ],
  'transport-politeness': [
    'intro-yourself_variant1_junior-infants',
    'intro-yourself_variant2_senior-infants', 
    'intro-yourself_variant3_first-class'
  ],

  // Home and family scenarios  
  'home-dinner-conversation': [
    'home-dinner_variant1_second-class'
  ],
  'family-outing-planning': [
    'family-outing_variant1_second-class'
  ],
  'birthday-party-conversation': [
    'playground-games_variant1_senior-infants',
    'playground-games_variant2_first-class',
    'playground-games_variant3_second-class'
  ],
  'inviting-friend-over': [
    'playground-games_variant1_senior-infants',
    'playground-games_variant2_first-class',
    'playground-games_variant3_second-class'
  ],
  'sharing-interests': [
    'intro-yourself_variant1_junior-infants',
    'intro-yourself_variant2_senior-infants', 
    'intro-yourself_variant3_first-class'
  ],

  // Social skills scenarios
  'apologizing-appropriately': [
    'saying-goodbye_variant1_junior-infants',
    'saying-goodbye_variant2_senior-infants',
    'saying-goodbye_variant3_first-class'
  ],
  'expressing-disagreement-politely': [
    'classroom-participation_variant1_first-class',
    'classroom-participation_variant2_second-class',
    'classroom-participation_variant3_third-class'
  ],
  'meeting-new-neighbor': [
    'intro-yourself_variant1_junior-infants',
    'intro-yourself_variant2_senior-infants', 
    'intro-yourself_variant3_first-class'
  ]
};

/**
 * Transform a ConversationTurn object to a format compatible with Transcript.js
 * @param {Object} turn - ConversationTurn object from transcript data
 * @returns {Object} Message object for Transcript.js component
 */
export function transformTurnToMessage(turn) {
  return {
    id: `${turn.speaker}-${turn.timestamp}`,
    role: turn.speaker === 'xiao_mei' ? 'assistant' : 'user',
    content: turn.content,
    timestamp: turn.timestamp * 1000, // Convert to milliseconds for JavaScript Date
    language: turn.language,
    phase: turn.phase,
    encouragement_level: turn.encouragement_level
  };
}

/**
 * Transform a complete transcript to messages format for Transcript.js
 * @param {Object} transcriptData - Complete transcript data with metadata and transcript array
 * @returns {Object} Transformed transcript with messages array
 */
export function transformTranscriptToMessages(transcriptData) {
  return {
    metadata: transcriptData.metadata,
    messages: transcriptData.transcript.map(transformTurnToMessage)
  };
}

/**
 * Get available transcripts for a scenario
 * @param {string} scenarioId - The scenario ID
 * @returns {Array} Array of transcript IDs available for the scenario
 */
export function getAvailableTranscripts(scenarioId) {
  return TRANSCRIPT_MAP[scenarioId] || [];
}

/**
 * Get transcript metadata for a scenario
 * @param {string} scenarioId - The scenario ID
 * @returns {Array} Array of transcript metadata objects
 */
export function getTranscriptMetadata(scenarioId) {
  const transcriptIds = getAvailableTranscripts(scenarioId);
  
  return transcriptIds.map(transcriptId => {
    const parts = transcriptId.split('_');
    const variant = parts[1];
    const ageGroup = parts[2];
    
    return {
      transcriptId,
      scenarioId,
      variant,
      ageGroup,
      displayName: `${variant.replace('variant', 'Variant ')} (${ageGroup.replace('-', ' ')})`
    };
  });
}

/**
 * Load a specific transcript by ID
 * @param {string} transcriptId - The transcript ID to load
 * @returns {Promise<Object>} Promise that resolves to the transcript data
 */
export async function loadTranscript(transcriptId) {
  try {
    // In a real application, you would fetch this from a server or use dynamic imports
    // For now, we'll simulate loading by returning a placeholder
    // This would need to be implemented based on your build system
    
    const response = await fetch(`/data/transcripts/${transcriptId}.json`);
    if (!response.ok) {
      throw new Error(`Failed to load transcript: ${transcriptId}`);
    }
    
    const transcriptData = await response.json();
    return transformTranscriptToMessages(transcriptData);
  } catch (error) {
    console.error(`Error loading transcript ${transcriptId}:`, error);
    throw error;
  }
}

/**
 * Load all transcripts for a scenario
 * @param {string} scenarioId - The scenario ID
 * @returns {Promise<Array>} Promise that resolves to an array of transcript data
 */
export async function loadScenarioTranscripts(scenarioId) {
  const transcriptIds = getAvailableTranscripts(scenarioId);
  const transcripts = [];
  
  for (const transcriptId of transcriptIds) {
    try {
      const transcript = await loadTranscript(transcriptId);
      transcripts.push(transcript);
    } catch (error) {
      console.warn(`Failed to load transcript ${transcriptId}:`, error);
      // Continue loading other transcripts even if one fails
    }
  }
  
  return transcripts;
}

/**
 * Get a random transcript for a scenario
 * @param {string} scenarioId - The scenario ID
 * @returns {Promise<Object>} Promise that resolves to a random transcript
 */
export async function getRandomTranscript(scenarioId) {
  const transcriptIds = getAvailableTranscripts(scenarioId);
  
  if (transcriptIds.length === 0) {
    throw new Error(`No transcripts available for scenario: ${scenarioId}`);
  }
  
  const randomIndex = Math.floor(Math.random() * transcriptIds.length);
  const randomTranscriptId = transcriptIds[randomIndex];
  
  return await loadTranscript(randomTranscriptId);
}

/**
 * Filter transcripts by age group
 * @param {Array} transcripts - Array of transcript data
 * @param {string} ageGroup - The age group to filter by
 * @returns {Array} Filtered transcripts
 */
export function filterTranscriptsByAgeGroup(transcripts, ageGroup) {
  return transcripts.filter(transcript => 
    transcript.metadata.age_group === ageGroup
  );
}

/**
 * Filter transcripts by difficulty variant
 * @param {Array} transcripts - Array of transcript data
 * @param {string} variant - The variant to filter by
 * @returns {Array} Filtered transcripts
 */
export function filterTranscriptsByVariant(transcripts, variant) {
  return transcripts.filter(transcript => 
    transcript.metadata.difficulty_variant === variant
  );
}

/**
 * Get transcript statistics for a scenario
 * @param {string} scenarioId - The scenario ID
 * @returns {Object} Statistics about available transcripts
 */
export function getTranscriptStats(scenarioId) {
  const transcriptIds = getAvailableTranscripts(scenarioId);
  const ageGroups = new Set();
  const variants = new Set();
  
  transcriptIds.forEach(transcriptId => {
    const parts = transcriptId.split('_');
    if (parts.length >= 3) {
      variants.add(parts[1]);
      ageGroups.add(parts[2]);
    }
  });
  
  return {
    totalTranscripts: transcriptIds.length,
    ageGroups: Array.from(ageGroups),
    variants: Array.from(variants),
    scenarioId
  };
}

/**
 * Validate transcript data structure
 * @param {Object} transcriptData - Transcript data to validate
 * @returns {Object} Validation result with isValid boolean and issues array
 */
export function validateTranscript(transcriptData) {
  const issues = [];
  
  // Check required fields
  if (!transcriptData.metadata) {
    issues.push('Missing metadata');
  } else {
    if (!transcriptData.metadata.scenario_id) {
      issues.push('Missing scenario_id in metadata');
    }
    if (!transcriptData.metadata.age_group) {
      issues.push('Missing age_group in metadata');
    }
  }
  
  if (!transcriptData.transcript || !Array.isArray(transcriptData.transcript)) {
    issues.push('Missing or invalid transcript array');
  } else if (transcriptData.transcript.length === 0) {
    issues.push('Empty transcript');
  } else {
    // Validate each turn
    transcriptData.transcript.forEach((turn, index) => {
      if (!turn.phase) {
        issues.push(`Turn ${index}: Missing phase`);
      }
      if (!turn.speaker) {
        issues.push(`Turn ${index}: Missing speaker`);
      }
      if (!turn.content) {
        issues.push(`Turn ${index}: Missing content`);
      }
      if (!turn.language) {
        issues.push(`Turn ${index}: Missing language`);
      }
      if (typeof turn.timestamp !== 'number') {
        issues.push(`Turn ${index}: Invalid timestamp`);
      }
    });
  }
  
  return {
    isValid: issues.length === 0,
    issues
  };
}
