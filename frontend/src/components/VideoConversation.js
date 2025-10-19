import React, { useEffect, useMemo, useRef, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { RTVIEvent } from '@pipecat-ai/client-js';
import { WebRTCClient } from '../webrtc-client';
import { mockScenarios } from '../data/scenarios';
import { getTranscriptMetadata, getRandomTranscript, loadTranscript } from '../data/transcriptLoader';
import hybridTTS from '../services/hybridTTS';
import { childFriendlyAnimations, triggerSuccessCelebration } from '../design-system/animations';
import FriendlyLoader from '../design-system/components/FriendlyLoader';
import './VideoConversation.css';
import '../pages/pages.css';

// Age-appropriate sample sentences generator for ALL 60 scenarios
function getAgeAppropriateSentences(ageGroup, scenarioId) {
  // Comprehensive content library with automatic content generation
  return generateAgeAppropriateContent(ageGroup, scenarioId);
}

// Generate age-appropriate content based on scenario patterns and context
function generateAgeAppropriateContent(ageGroup, scenarioId) {
  // Define age-appropriate complexity levels
  const complexityLevels = {
    'junior-infants': { 
      formality: 'simple', 
      vocabulary: 'basic', 
      structure: 'short',
      politeness: 'direct'
    },
    'senior-infants': { 
      formality: 'casual', 
      vocabulary: 'simple', 
      structure: 'medium',
      politeness: 'polite'
    },
    'first-class': { 
      formality: 'polite', 
      vocabulary: 'moderate', 
      structure: 'medium',
      politeness: 'courteous'
    },
    'second-class': { 
      formality: 'courteous', 
      vocabulary: 'good', 
      structure: 'longer',
      politeness: 'respectful'
    },
    'third-class': { 
      formality: 'respectful', 
      vocabulary: 'advanced', 
      structure: 'complex',
      politeness: 'formal'
    },
    'fourth-class': { 
      formality: 'formal', 
      vocabulary: 'sophisticated', 
      structure: 'complex',
      politeness: 'very_formal'
    }
  };

  // Map all 60 scenarios to content templates
  const scenarioTemplates = {
    // INTRODUCTION SCENARIOS
    'introducing-yourself': () => generateIntroductionContent(ageGroup),
    'intro-yourself': () => generateIntroductionContent(ageGroup),
    
    // HELP & ASSISTANCE SCENARIOS
    'asking-for-help': () => generateHelpContent(ageGroup),
    'ask-help': () => generateHelpContent(ageGroup),
    'asking-teacher-question': () => generateTeacherQuestionContent(ageGroup),
    'asking-classmate-help': () => generateClassmateHelpContent(ageGroup),
    'asking-lunch-help': () => generateLunchHelpContent(ageGroup),
    
    // TOILET & BASIC NEEDS
    'asking-for-toilet': () => generateToiletContent(ageGroup),
    'ask-toilet': () => generateToiletContent(ageGroup),
    'expressing-hunger': () => generateHungerContent(ageGroup),
    'express-hunger': () => generateHungerContent(ageGroup),
    
    // CLASSROOM SCENARIOS
    'class-presentation': () => generatePresentationContent(ageGroup),
    'answering-in-class': () => generateAnsweringContent(ageGroup),
    'group-work-collaboration': () => generateGroupWorkContent(ageGroup),
    'participating-discussion': () => generateDiscussionContent(ageGroup),
    'classroom-participation': () => generateParticipationContent(ageGroup),
    'explaining-homework-problem': () => generateHomeworkHelpContent(ageGroup),
    'sharing-learning-materials': () => generateSharingMaterialsContent(ageGroup),
    'reading-aloud-class': () => generateReadingAloudContent(ageGroup),
    'showing-understanding': () => generateUnderstandingContent(ageGroup),
    
    // SOCIAL & FRIENDSHIP SCENARIOS
    'making-new-friends': () => generateFriendshipContent(ageGroup),
    'making-friends': () => generateFriendshipContent(ageGroup),
    'saying-goodbye': () => generateGoodbyeContent(ageGroup),
    'inviting-to-play': () => generateInvitationContent(ageGroup),
    'inviting-friend-over': () => generateFriendInvitationContent(ageGroup),
    'sharing-interests': () => generateSharingInterestsContent(ageGroup),
    'comforting-upset-friend': () => generateComfortingContent(ageGroup),
    'meeting-new-neighbor': () => generateMeetingNeighborContent(ageGroup),
    
    // PLAYGROUND SCENARIOS
    'playground-games': () => generatePlaygroundContent(ageGroup),
    'resolving-playground-conflict': () => generateConflictResolutionContent(ageGroup),
    'sharing-playground-equipment': () => generateSharingEquipmentContent(ageGroup),
    'expressing-feelings-playground': () => generateExpressingFeelingsContent(ageGroup),
    'organizing-group-game': () => generateOrganizingGameContent(ageGroup),
    
    // FOOD & DINING SCENARIOS
    'lunch-food-conversation': () => generateLunchConversationContent(ageGroup),
    'sharing-cultural-food': () => generateCulturalFoodContent(ageGroup),
    'describing-food-preferences': () => generateFoodPreferencesContent(ageGroup),
    'canteen-politeness': () => generateCanteenPolitenessContent(ageGroup),
    
    // SCHOOL EVENTS & ACTIVITIES
    'school-assembly-participation': () => generateAssemblyContent(ageGroup),
    'sports-day-activities': () => generateSportsContent(ageGroup),
    
    // SHOPPING & DAILY LIFE
    'grocery-shopping-help': () => generateGroceryShoppingContent(ageGroup),
    'clothes-shopping-preferences': () => generateClothesShoppingContent(ageGroup),
    'asking-store-directions': () => generateStoreDirectionsContent(ageGroup),
    'paying-at-checkout': () => generateCheckoutContent(ageGroup),
    'comparing-prices': () => generatePriceComparisonContent(ageGroup),
    'asking-product-location': () => generateProductLocationContent(ageGroup),
    'expressing-shopping-needs': () => generateShoppingNeedsContent(ageGroup),
    'polite-shop-interaction': () => generatePoliteShoppingContent(ageGroup),
    
    // TRANSPORT & DIRECTIONS
    'bus-conversation': () => generateBusConversationContent(ageGroup),
    'dart-ticket-purchase': () => generateTicketPurchaseContent(ageGroup),
    'asking-walking-directions': () => generateWalkingDirectionsContent(ageGroup),
    'transport-politeness': () => generateTransportPolitenessContent(ageGroup),
    
    // FAMILY & HOME
    'home-dinner-conversation': () => generateDinnerConversationContent(ageGroup),
    'sibling-play-interaction': () => generateSiblingPlayContent(ageGroup),
    'family-outing-planning': () => generateFamilyOutingContent(ageGroup),
    'birthday-party-conversation': () => generateBirthdayPartyContent(ageGroup),
    
    // CONFLICT RESOLUTION & EMOTIONS
    'apologizing-appropriately': () => generateApologyContent(ageGroup),
    'expressing-disagreement-politely': () => generateDisagreementContent(ageGroup),
    
    // COMMUNITY & CULTURAL
    'community-gathering-participation': () => generateCommunityGatheringContent(ageGroup),
    'local-community-event': () => generateCommunityEventContent(ageGroup),
    'st-patricks-day-celebration': () => generateStPatricksDayContent(ageGroup),
    'gaa-match-watching': () => generateGAAMatchContent(ageGroup),
    'irish-traditional-music-event': () => generateIrishMusicContent(ageGroup),
    'irish-dancing-participation': () => generateIrishDancingContent(ageGroup),
    'dublin-heritage-visit': () => generateDublinHeritageContent(ageGroup),
    'sharing-chinese-culture': () => generateChineseCultureContent(ageGroup),
    'explaining-chinese-holiday': () => generateChineseHolidayContent(ageGroup)
  };

  // Get specific content generator or use generic fallback
  const contentGenerator = scenarioTemplates[scenarioId];
  
  if (contentGenerator) {
    return contentGenerator();
  }
  
  // Generic fallback for any missing scenarios
  return generateGenericContent(ageGroup, scenarioId);
}

// Content generators for different scenario types
function generateIntroductionContent(ageGroup) {
  const templates = {
    'junior-infants': [
      "Hello, I am Emma. I am 4 years old.",
      "Hi, my name is Tom. I am 5 years old.",
      "Hello, I am Sarah.",
      "Hi, I am Ben. I like to play."
    ],
    'senior-infants': [
      "Hello, I am Lucy. I am 5 years old.",
      "Hi, my name is Jack. I am 6 years old.", 
      "Hello, I am Amy. I am in Senior Infants.",
      "Hi, I am Mark. I like school."
    ],
    'first-class': [
      "Hello, I am Sophie. I am 6 years old.",
      "Hi, my name is Ryan. I am 7 years old.",
      "Hello, I am Katie. I am in First Class.",
      "Hi, I am David. I like reading books."
    ],
    'second-class': [
      "Hello, I am Grace. I am 7 years old.",
      "Hi, my name is Alex. I am 8 years old.",
      "Hello, I am Ella. I am in Second Class.",
      "Hi, I am Luke. I enjoy mathematics."
    ],
    'third-class': [
      "Hello, I am Olivia. I am 8 years old.",
      "Hi, my name is James. I am 9 years old.",
      "Hello, I am Chloe. I am in Third Class.",
      "Hi, I am Noah. I like science experiments."
    ],
    'fourth-class': [
      "Hello, I am Isabella. I am 9 years old.",
      "Hi, my name is William. I am 10 years old.",
      "Hello, I am Ava. I am in Fourth Class.",
      "Hi, I am Liam. I enjoy creative writing."
    ]
  };
  return templates[ageGroup] || templates['junior-infants'];
}

function generateHelpContent(ageGroup) {
  const templates = {
    'junior-infants': ["Help me please.", "I need help.", "Can you help?", "Please help me."],
    'senior-infants': ["Can you help me please?", "I need help with this.", "Could you help me?", "I don't understand this."],
    'first-class': ["Could you help me with this problem?", "I need assistance, please.", "Can you explain this to me?", "I'm having trouble with this."],
    'second-class': ["Would you be able to help me?", "Could you assist me with this task?", "I'm finding this challenging.", "May I ask for your help?"],
    'third-class': ["I would appreciate your guidance.", "Could you provide some assistance?", "I'm encountering some difficulties.", "Would you mind helping me out?"],
    'fourth-class': ["I would be grateful for your help.", "Could you offer me some support?", "I'm struggling to understand this.", "Would it be possible to get assistance?"]
  };
  return templates[ageGroup] || templates['junior-infants'];
}

function generateTeacherQuestionContent(ageGroup) {
  const templates = {
    'junior-infants': ["Teacher, I don't understand.", "Can you help me?", "What does this mean?", "I need help, please."],
    'senior-infants': ["Excuse me, teacher.", "Can you explain this please?", "I don't understand this part.", "Could you help me with this?"],
    'first-class': ["Excuse me, teacher, may I ask a question?", "Could you explain that again, please?", "I'm not sure I understand this.", "May I ask for clarification?"],
    'second-class': ["Teacher, could you please help me?", "I have a question about this.", "Could you explain this concept?", "May I ask about this problem?"],
    'third-class': ["Excuse me, I have a question.", "Could you clarify this for me?", "I'm having difficulty understanding.", "May I request some assistance?"],
    'fourth-class': ["Teacher, may I pose a question?", "Could you provide clarification?", "I would appreciate your guidance.", "May I seek your assistance with this?"]
  };
  return templates[ageGroup] || templates['junior-infants'];
}

function generateToiletContent(ageGroup) {
  const templates = {
    'junior-infants': ["I need the toilet.", "Toilet please.", "Can I go toilet?", "I need to go."],
    'senior-infants': ["Can I go to the toilet please?", "May I use the bathroom?", "I need to use the toilet.", "Could I go to the toilet?"],
    'first-class': ["May I please go to the bathroom?", "Could I be excused to use the toilet?", "May I have permission to go to the toilet?", "Could I please use the facilities?"],
    'second-class': ["Could I please be excused for a moment?", "May I have permission to visit the bathroom?", "Would it be possible to use the toilet?", "Could I please step out briefly?"],
    'third-class': ["Excuse me, may I please use the restroom?", "Could I have permission to step out?", "May I be excused to use the facilities?", "Would it be alright if I visited the bathroom?"],
    'fourth-class': ["Excuse me, could I please be excused?", "May I have permission to leave momentarily?", "Could I please step out for a moment?", "Would it be possible to be excused briefly?"]
  };
  return templates[ageGroup] || templates['junior-infants'];
}

function generatePlaygroundContent(ageGroup) {
  const templates = {
    'junior-infants': ["Can I play?", "Let's play!", "I want to play.", "Play with me?"],
    'senior-infants': ["Can I join the game?", "May I play with you?", "Could I join in?", "Can we play together?"],
    'first-class': ["Could I join your game please?", "May I participate in this game?", "Would it be okay if I played too?", "Can I be part of your team?"],
    'second-class': ["Would you mind if I joined your game?", "Could I possibly join in your activity?", "May I participate in what you're doing?", "Would there be room for one more player?"],
    'third-class': ["Would it be possible for me to join?", "Could I participate in your activity?", "May I be included in what you're doing?", "Would you consider letting me play?"],
    'fourth-class': ["Would you be open to including me?", "Could I potentially join your group?", "May I have the opportunity to participate?", "Would you mind if I became involved?"]
  };
  return templates[ageGroup] || templates['junior-infants'];
}

function generateFriendshipContent(ageGroup) {
  const templates = {
    'junior-infants': ["Hi! I'm Anna.", "Do you want to play?", "Let's be friends!", "What's your name?"],
    'senior-infants': ["Hello, would you like to be friends?", "What do you like to do?", "Do you want to play together?", "I'm new here. Can we be friends?"],
    'first-class': ["Hi, I'm wondering if we could be friends?", "Would you like to spend break time together?", "I'd love to get to know you better.", "Do you have similar interests to me?"],
    'second-class': ["I was hoping we might become friends.", "Would you be interested in hanging out?", "I think we have a lot in common.", "I'd really like to be your friend."],
    'third-class': ["I'd love the opportunity to be your friend.", "Would you be interested in spending time together?", "I feel like we could be great friends.", "I'd really enjoy getting to know you better."],
    'fourth-class': ["I would appreciate the chance to be friends.", "Would you consider developing a friendship?", "I believe we could have a wonderful friendship.", "I'd be honored to call you my friend."]
  };
  return templates[ageGroup] || templates['junior-infants'];
}

function generateGoodbyeContent(ageGroup) {
  const templates = {
    'junior-infants': ["Bye bye!", "See you later!", "Goodbye!", "See you soon!"],
    'senior-infants': ["Goodbye, see you tomorrow!", "Have a nice day!", "See you later!", "Take care!"],
    'first-class': ["Have a lovely rest of your day!", "See you tomorrow at school!", "Take care and have fun!", "Looking forward to seeing you again!"],
    'second-class': ["Have a wonderful evening!", "See you bright and early tomorrow!", "Take care of yourself!", "Have a fantastic rest of your day!"],
    'third-class': ["Have an absolutely wonderful day!", "I look forward to seeing you again soon!", "Take good care of yourself!", "Have a truly fantastic time!"],
    'fourth-class': ["Have a marvelous rest of your day!", "I hope to see you again very soon!", "Please take excellent care of yourself!", "Have a truly spectacular time ahead!"]
  };
  return templates[ageGroup] || templates['junior-infants'];
}

// Helper functions for other scenario types (simplified for brevity)
function generateClassmateHelpContent(ageGroup) {
  return adaptContentForAge([
    "Can you help me?", "Will you help me please?", "Could you assist me with this?", 
    "Would you mind helping me?", "I would appreciate your assistance.", "Could you possibly help me out?"
  ], ageGroup);
}

function generateLunchHelpContent(ageGroup) {
  return adaptContentForAge([
    "Help me with lunch.", "Can you help me eat?", "Could you help me with my lunch?",
    "Would you mind helping me with this?", "I would appreciate help with my meal.", "Could you assist me with lunch please?"
  ], ageGroup);
}

function generateHungerContent(ageGroup) {
  return adaptContentForAge([
    "I'm hungry.", "I'm feeling hungry.", "I'm quite hungry now.", 
    "I'm feeling rather hungry.", "I'm experiencing some hunger.", "I'm feeling quite peckish at the moment."
  ], ageGroup);
}

function generatePresentationContent(ageGroup) {
  return adaptContentForAge([
    "I want to show.", "I'd like to present.", "I would like to share my work.",
    "I'd like to present my project.", "I would appreciate the opportunity to present.", "I would be honored to share my presentation."
  ], ageGroup);
}

function generateAnsweringContent(ageGroup) {
  return adaptContentForAge([
    "I know!", "I'd like to answer.", "I would like to respond.",
    "I'd like to contribute my answer.", "I would appreciate the chance to answer.", "I would be delighted to provide an answer."
  ], ageGroup);
}

function generateGroupWorkContent(ageGroup) {
  return adaptContentForAge([
    "Let's work together.", "Shall we work as a team?", "Could we collaborate on this?",
    "Would you like to work together?", "I believe we could work well together.", "I would appreciate collaborating with you."
  ], ageGroup);
}

function generateDiscussionContent(ageGroup) {
  return adaptContentForAge([
    "I want to talk.", "I'd like to share.", "I would like to contribute.",
    "I'd like to participate in this discussion.", "I would appreciate joining this conversation.", "I would be honored to contribute to this discussion."
  ], ageGroup);
}

function generateParticipationContent(ageGroup) {
  return adaptContentForAge([
    "Can I join?", "May I participate?", "Could I take part?",
    "Would it be possible to participate?", "I would appreciate the opportunity to join.", "I would be grateful for the chance to participate."
  ], ageGroup);
}

// Generic content generators for any remaining scenarios
function generateGenericContent(ageGroup, scenarioId) {
  // Extract scenario context from ID and generate appropriate content
  if (scenarioId.includes('help') || scenarioId.includes('ask')) {
    return generateHelpContent(ageGroup);
  }
  if (scenarioId.includes('play') || scenarioId.includes('game')) {
    return generatePlaygroundContent(ageGroup);
  }
  if (scenarioId.includes('friend') || scenarioId.includes('social')) {
    return generateFriendshipContent(ageGroup);
  }
  if (scenarioId.includes('goodbye') || scenarioId.includes('farewell')) {
    return generateGoodbyeContent(ageGroup);
  }
  if (scenarioId.includes('food') || scenarioId.includes('lunch') || scenarioId.includes('hungry')) {
    return generateHungerContent(ageGroup);
  }
  
  // Default generic sentences
  return adaptContentForAge([
    "Hello!", "Can you help me?", "Thank you!", "Please help me.",
    "I need help.", "Could you help me please?", "I would appreciate your help.",
    "May I ask for assistance?", "I would be grateful for guidance.", "Could you provide some support?"
  ], ageGroup);
}

// Utility function to adapt content complexity for age groups
function adaptContentForAge(baseContent, ageGroup) {
  const ageIndex = ['junior-infants', 'senior-infants', 'first-class', 'second-class', 'third-class', 'fourth-class'].indexOf(ageGroup);
  const maxIndex = Math.min(ageIndex + 1, baseContent.length - 1);
  
  // Return age-appropriate subset of content
  return baseContent.slice(0, Math.max(4, maxIndex + 3));
}

// Stub functions for all remaining scenarios - will use generic content generation
const generateHomeworkHelpContent = (ageGroup) => generateHelpContent(ageGroup);
const generateSharingMaterialsContent = (ageGroup) => adaptContentForAge(["Can I share this?", "Would you like to use this?", "We can share materials.", "Let's share our things.", "I'd like to share resources.", "Shall we share our materials?"], ageGroup);
const generateReadingAloudContent = (ageGroup) => adaptContentForAge(["I want to read.", "Can I read this?", "I'd like to read aloud.", "May I read this passage?", "I would like to read this.", "Could I read this section?"], ageGroup);
const generateUnderstandingContent = (ageGroup) => adaptContentForAge(["I understand.", "I get it now.", "That makes sense.", "I understand this concept.", "I comprehend this material.", "I have a clear understanding."], ageGroup);
const generateInvitationContent = (ageGroup) => adaptContentForAge(["Come and play!", "Do you want to play?", "Would you like to join?", "Would you like to play together?", "I'd like to invite you to play.", "Would you be interested in joining us?"], ageGroup);
const generateFriendInvitationContent = (ageGroup) => adaptContentForAge(["Come to my house!", "Want to come over?", "Would you like to visit?", "Would you like to come to my home?", "I'd like to invite you over.", "Would you be interested in visiting?"], ageGroup);
const generateSharingInterestsContent = (ageGroup) => adaptContentForAge(["I like this.", "I enjoy this too.", "I'm interested in this.", "I have similar interests.", "I share your enthusiasm.", "I have a passion for this."], ageGroup);
const generateComfortingContent = (ageGroup) => adaptContentForAge(["Are you okay?", "Don't be sad.", "I'm here to help you.", "Is there anything I can do?", "I'd like to help you feel better.", "I'm here to support you."], ageGroup);
const generateMeetingNeighborContent = (ageGroup) => adaptContentForAge(["Hello neighbor!", "Hi, I live nearby.", "Nice to meet you.", "I'm your new neighbor.", "I'd like to introduce myself.", "I'm pleased to make your acquaintance."], ageGroup);
const generateConflictResolutionContent = (ageGroup) => adaptContentForAge(["Sorry about that.", "Let's be friends.", "Can we work this out?", "I'd like to resolve this.", "Let's find a solution together.", "I believe we can work through this."], ageGroup);
const generateSharingEquipmentContent = (ageGroup) => adaptContentForAge(["Can I use this?", "Let's take turns.", "We can share this equipment.", "Would you like to take turns?", "I'd like to share this with you.", "Shall we use this together?"], ageGroup);
const generateExpressingFeelingsContent = (ageGroup) => adaptContentForAge(["I feel happy.", "I'm excited about this.", "I'm feeling a bit sad.", "I'm experiencing some emotions.", "I'd like to express my feelings.", "I'm feeling quite overwhelmed."], ageGroup);
const generateOrganizingGameContent = (ageGroup) => adaptContentForAge(["Let's play a game!", "Who wants to play?", "Shall we organize a game?", "Would you like to start a game?", "I'd like to organize an activity.", "Shall we coordinate a group activity?"], ageGroup);
const generateLunchConversationContent = (ageGroup) => adaptContentForAge(["What's for lunch?", "I like this food.", "What are you eating?", "That looks delicious.", "I'm enjoying my meal.", "What's your favorite food?"], ageGroup);
const generateCulturalFoodContent = (ageGroup) => adaptContentForAge(["This is Chinese food.", "Try this dish.", "This is from my culture.", "This is a traditional dish.", "I'd like to share my culture.", "This represents my heritage."], ageGroup);
const generateFoodPreferencesContent = (ageGroup) => adaptContentForAge(["I like apples.", "I don't like this.", "I prefer this food.", "This is my favorite dish.", "I have dietary preferences.", "I particularly enjoy this cuisine."], ageGroup);
const generateCanteenPolitenessContent = (ageGroup) => adaptContentForAge(["Please and thank you.", "Excuse me, please.", "May I have this please?", "Could I have this meal?", "I would appreciate this dish.", "May I respectfully request this?"], ageGroup);
const generateAssemblyContent = (ageGroup) => adaptContentForAge(["Sit quietly.", "Listen carefully.", "I want to participate.", "May I contribute to assembly?", "I'd like to participate respectfully.", "I would appreciate contributing."], ageGroup);
const generateSportsContent = (ageGroup) => adaptContentForAge(["Let's play sports!", "I want to run.", "Can I join the team?", "Would you like to play together?", "I'd like to participate in sports.", "May I join the athletic activity?"], ageGroup);

// Add stubs for all remaining functions referenced in scenarioTemplates
const generateGroceryShoppingContent = (ageGroup) => adaptContentForAge(["I need milk.", "Where is the bread?", "Can you help me find this?", "Where would I find this item?", "I'm looking for specific products.", "Could you direct me to this section?"], ageGroup);
const generateClothesShoppingContent = (ageGroup) => adaptContentForAge(["I like this shirt.", "Can I try this on?", "Does this fit me?", "May I try this garment?", "I'd like to try this clothing.", "Could I possibly try this on?"], ageGroup);
const generateStoreDirectionsContent = (ageGroup) => adaptContentForAge(["Where is the shop?", "How do I get there?", "Can you show me the way?", "Could you provide directions?", "I would appreciate directions.", "Could you guide me to the location?"], ageGroup);
const generateCheckoutContent = (ageGroup) => adaptContentForAge(["I want to pay.", "How much is this?", "Here's my money.", "I'd like to purchase this.", "I would like to pay for this.", "I'd like to complete this transaction."], ageGroup);
const generatePriceComparisonContent = (ageGroup) => adaptContentForAge(["This costs more.", "Which is cheaper?", "I'm comparing prices.", "Which option is more affordable?", "I'm evaluating the costs.", "I'm considering the price differences."], ageGroup);
const generateProductLocationContent = (ageGroup) => adaptContentForAge(["Where is this?", "I can't find this.", "Can you help me find this?", "Where would this item be located?", "I'm searching for this product.", "Could you direct me to this item?"], ageGroup);
const generateShoppingNeedsContent = (ageGroup) => adaptContentForAge(["I need this.", "I want to buy this.", "I'm looking for this.", "I require this particular item.", "I'm seeking this specific product.", "I would like to acquire this."], ageGroup);
const generatePoliteShoppingContent = (ageGroup) => adaptContentForAge(["Excuse me, please.", "Thank you very much.", "May I ask for help?", "Could you assist me please?", "I would appreciate your help.", "May I respectfully request assistance?"], ageGroup);
const generateBusConversationContent = (ageGroup) => adaptContentForAge(["Where does this go?", "Is this the right bus?", "How much is the ticket?", "Does this bus go to the city?", "I'd like to confirm the destination.", "Could you verify this route for me?"], ageGroup);
const generateTicketPurchaseContent = (ageGroup) => adaptContentForAge(["I need a ticket.", "One ticket please.", "How much is a ticket?", "I'd like to purchase a ticket.", "I would like to buy passage.", "Could I acquire a ticket please?"], ageGroup);
const generateWalkingDirectionsContent = (ageGroup) => adaptContentForAge(["Which way to go?", "How do I get there?", "Can you show me the way?", "Could you provide directions?", "I would appreciate guidance.", "Could you direct me to the location?"], ageGroup);
const generateTransportPolitenessContent = (ageGroup) => adaptContentForAge(["Excuse me.", "Thank you for your help.", "May I pass please?", "Could I get through please?", "I would appreciate passage.", "May I respectfully pass by?"], ageGroup);
const generateDinnerConversationContent = (ageGroup) => adaptContentForAge(["This tastes good.", "What's for dinner?", "I enjoyed this meal.", "This dinner is delicious.", "I appreciate this wonderful meal.", "This culinary experience is delightful."], ageGroup);
const generateSiblingPlayContent = (ageGroup) => adaptContentForAge(["Let's play together.", "Share with me.", "Can we play this game?", "Would you like to play together?", "I'd enjoy playing with you.", "Shall we engage in this activity?"], ageGroup);
const generateFamilyOutingContent = (ageGroup) => adaptContentForAge(["Where are we going?", "This is fun!", "I'm excited for our trip.", "I'm looking forward to this.", "I'm enthusiastic about our outing.", "I'm anticipating this family excursion."], ageGroup);
const generateBirthdayPartyContent = (ageGroup) => adaptContentForAge(["Happy birthday!", "This party is fun!", "I like the cake.", "This celebration is wonderful.", "I'm enjoying this birthday party.", "This festive occasion is delightful."], ageGroup);
const generateApologyContent = (ageGroup) => adaptContentForAge(["I'm sorry.", "I didn't mean to.", "Please forgive me.", "I apologize for my actions.", "I sincerely regret this.", "I offer my heartfelt apologies."], ageGroup);
const generateDisagreementContent = (ageGroup) => adaptContentForAge(["I don't think so.", "I have a different idea.", "I respectfully disagree.", "I have an alternative perspective.", "I hold a different viewpoint.", "I respectfully maintain a different opinion."], ageGroup);
const generateCommunityGatheringContent = (ageGroup) => adaptContentForAge(["Hello everyone!", "Nice to meet you all.", "I'm happy to be here.", "I'm pleased to join this gathering.", "I appreciate this community event.", "I'm honored to participate in this occasion."], ageGroup);
const generateCommunityEventContent = (ageGroup) => adaptContentForAge(["This is exciting!", "I like this event.", "This community event is great.", "I'm enjoying this local gathering.", "This civic occasion is wonderful.", "This community celebration is remarkable."], ageGroup);
const generateStPatricksDayContent = (ageGroup) => adaptContentForAge(["Happy St. Patrick's Day!", "I like the green.", "This celebration is fun.", "This Irish holiday is wonderful.", "I appreciate this cultural celebration.", "This traditional Irish festivity is magnificent."], ageGroup);
const generateGAAMatchContent = (ageGroup) => adaptContentForAge(["Go team!", "This game is exciting!", "I support this team.", "This match is thrilling.", "I'm enthusiastic about this game.", "This athletic competition is exhilarating."], ageGroup);
const generateIrishMusicContent = (ageGroup) => adaptContentForAge(["I like this music.", "The music sounds nice.", "This traditional music is beautiful.", "These Irish melodies are lovely.", "I appreciate this cultural music.", "This traditional Irish music is enchanting."], ageGroup);
const generateIrishDancingContent = (ageGroup) => adaptContentForAge(["Can I try dancing?", "I want to learn this.", "This dancing looks fun.", "I'd like to learn Irish dancing.", "I'm interested in this cultural dance.", "I would appreciate learning this traditional art."], ageGroup);
const generateDublinHeritageContent = (ageGroup) => adaptContentForAge(["This place is old.", "I like the buildings.", "This heritage site is interesting.", "This historical location is fascinating.", "I appreciate Dublin's rich heritage.", "This cultural landmark is truly remarkable."], ageGroup);
const generateChineseCultureContent = (ageGroup) => adaptContentForAge(["This is from China.", "I want to share my culture.", "This is a Chinese tradition.", "I'd like to share my heritage.", "I appreciate sharing my cultural background.", "I would like to present my ancestral traditions."], ageGroup);
const generateChineseHolidayContent = (ageGroup) => adaptContentForAge(["We celebrate this.", "This is Chinese New Year.", "This is an important holiday.", "This is a significant celebration.", "This represents our cultural observance.", "This embodies our traditional festivities."], ageGroup);

function VideoConversation() {
  const [searchParams, setSearchParams] = useSearchParams();
  const [hasStarted, setHasStarted] = useState(false); // Track if user has clicked connect
  const [connectionState, setConnectionState] = useState('idle'); // idle, connecting, connected, error
  const [error, setError] = useState('');
  const [isMicEnabled, setIsMicEnabled] = useState(true);
  const [remoteAudioStream, setRemoteAudioStream] = useState(null);
  const remoteAudioStreamRef = useRef(null);
  const [isCameraEnabled, setIsCameraEnabled] = useState(false); // Default to camera disabled for audio-only mode
  const [preferAudioOnly, setPreferAudioOnly] = useState(true); // Default to audio-only mode
  const [sampleSentencesByAge, setSampleSentencesByAge] = useState({});
  const [selectedAge, setSelectedAge] = useState('');
  const [selectedVariant, setSelectedVariant] = useState('');
  const [isLoadingSamples, setIsLoadingSamples] = useState(false);
  const [illustrationUrl, setIllustrationUrl] = useState('');
  const [isGeneratingImage, setIsGeneratingImage] = useState(false);
  const [isCheckingExisting, setIsCheckingExisting] = useState(false);
  const [subtitles, setSubtitles] = useState('');
  const [subtitleHistory, setSubtitleHistory] = useState([]);
  const [currentLlmResponse, setCurrentLlmResponse] = useState('');
  const [isStreaming, setIsStreaming] = useState(false);
  const [subtitlesEnabled, setSubtitlesEnabled] = useState(true);
  const [playingAudio, setPlayingAudio] = useState(null); // Track which audio is currently playing
  const [ttsServiceStatus, setTtsServiceStatus] = useState(null); // Track TTS service availability
  
  const webrtcClient = useRef(null);
  const remoteVideoRef = useRef(null);
  const localVideoRef = useRef(null);
  const isIntentionalDisconnect = useRef(false); // Track if disconnect is intentional
  const subtitleTimeoutRef = useRef(null);
  const debounceTimeoutRef = useRef(null);

  // Get scenario from URL parameters
  const scenarioId = searchParams.get('scenario');
  const scenario = scenarioId ? mockScenarios.find(s => s.id === scenarioId) : null;
  const transcriptChoices = useMemo(() => scenarioId ? getTranscriptMetadata(scenarioId) : [], [scenarioId]);
  const availableAges = useMemo(() => {
    const setAges = new Set();
    transcriptChoices.forEach(t => setAges.add(t.ageGroup));
    return Array.from(setAges);
  }, [transcriptChoices]);
  const availableVariants = useMemo(() => {
    const setVars = new Set();
    transcriptChoices.forEach(t => setVars.add(t.variant));
    return Array.from(setVars);
  }, [transcriptChoices]);

  // Debounced subtitle update for performance
  const debouncedSubtitleUpdate = useMemo(() => {
    return (text, delay = 100) => {
      if (debounceTimeoutRef.current) {
        clearTimeout(debounceTimeoutRef.current);
      }
      debounceTimeoutRef.current = setTimeout(() => {
        setSubtitles(text);
      }, delay);
    };
  }, []);
  
  // Log warning if scenario ID was provided but not found
  useEffect(() => {
    if (scenarioId && !scenario) {
      console.warn(`Scenario '${scenarioId}' not found in scenarios data. Using default configuration.`);
    }
    if (scenario) {
      console.log(`Using scenario: ${scenario.title} (${scenario.id})`);
    }
  }, [scenarioId, scenario]);

  // Initialize pickers from URL on first load and when scenario changes
  useEffect(() => {
    if (!scenarioId) return;
    const urlAge = searchParams.get('age') || '';
    const urlVariant = searchParams.get('variant') || '';
    setSelectedAge(urlAge);
    setSelectedVariant(urlVariant);
  }, [scenarioId, searchParams]);

  // Keep URL in sync when user changes pickers
  useEffect(() => {
    const next = new URLSearchParams(searchParams);
    if (selectedAge) next.set('age', selectedAge); else next.delete('age');
    if (selectedVariant) next.set('variant', selectedVariant); else next.delete('variant');
    setSearchParams(next, { replace: true });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedAge, selectedVariant]);

  // Load all transcripts for the scenario and extract sample sentences grouped by age
  useEffect(() => {
    let cancelled = false;
    async function loadAllSamples() {
      try {
        if (!scenarioId) {
          setSampleSentencesByAge({});
          return;
        }
        setIsLoadingSamples(true);
        
        // Load all available transcripts for this scenario
        const samplesByAge = {};
        const loadPromises = transcriptChoices.map(async (choice) => {
          try {
            const transcript = await loadTranscript(choice.transcriptId);
            // Extract sentences specifically from child_practice phases
            const candidates = [];
            transcript.messages.forEach(m => {
              const text = (m?.content || '').toString();
              if (!text) return;
              // Only include messages from child_practice phase with reasonable length
              if (m.phase === 'child_practice' && text.length <= 120) {
                candidates.push(text);
              }
            });
            
            if (candidates.length > 0) {
              const ageGroup = choice.ageGroup;
              if (!samplesByAge[ageGroup]) {
                samplesByAge[ageGroup] = [];
              }
              // Only add sentences that aren't already in the array to prevent duplicates
              candidates.forEach(sentence => {
                if (!samplesByAge[ageGroup].includes(sentence)) {
                  samplesByAge[ageGroup].push(sentence);
                }
              });
            }
          } catch (error) {
            console.warn(`Failed to load transcript ${choice.transcriptId}:`, error);
          }
        });
        
        await Promise.all(loadPromises);
        
        if (cancelled) return;
        
        // Add age-appropriate sample sentences to ensure diversity and educational relevance
        const ageAppropriateExamples = {
          'junior-infants': getAgeAppropriateSentences('junior-infants', scenarioId),
          'senior-infants': getAgeAppropriateSentences('senior-infants', scenarioId),
          'first-class': getAgeAppropriateSentences('first-class', scenarioId),
          'second-class': getAgeAppropriateSentences('second-class', scenarioId),
          'third-class': getAgeAppropriateSentences('third-class', scenarioId),
          'fourth-class': getAgeAppropriateSentences('fourth-class', scenarioId)
        };
        
        // Enhance each age group with appropriate examples, avoiding duplicates
        Object.keys(ageAppropriateExamples).forEach(ageGroup => {
          if (!samplesByAge[ageGroup]) {
            samplesByAge[ageGroup] = [];
          }
          
          // Add age-appropriate examples that aren't already present
          ageAppropriateExamples[ageGroup].forEach(example => {
            if (!samplesByAge[ageGroup].includes(example)) {
              samplesByAge[ageGroup].push(example);
            }
          });
          
          // Remove sentences that mention ages inappropriate for the age group
          samplesByAge[ageGroup] = samplesByAge[ageGroup].filter(sentence => {
            // Extract age mentions from sentences
            const ageMatch = sentence.match(/I am (\d+) years old/);
            if (!ageMatch) return true; // Keep sentences without age mentions
            
            const mentionedAge = parseInt(ageMatch[1]);
            
            // Filter based on age group appropriateness
            switch (ageGroup) {
              case 'junior-infants':
                return mentionedAge >= 4 && mentionedAge <= 5;
              case 'senior-infants':
                return mentionedAge >= 5 && mentionedAge <= 6;
              case 'first-class':
                return mentionedAge >= 6 && mentionedAge <= 7;
              case 'second-class':
                return mentionedAge >= 7 && mentionedAge <= 8;
              case 'third-class':
                return mentionedAge >= 8 && mentionedAge <= 9;
              case 'fourth-class':
                return mentionedAge >= 9 && mentionedAge <= 10;
              default:
                return true;
            }
          });
        });
        
        setSampleSentencesByAge(samplesByAge);
        
        // Preload audio for the first sample sentence
        const firstAgeGroup = Object.keys(samplesByAge)[0];
        if (firstAgeGroup && samplesByAge[firstAgeGroup].length > 0 && hybridTTS.isAvailable()) {
          try {
            await hybridTTS.preloadAudio(samplesByAge[firstAgeGroup][0], 'en-IE');
          } catch (error) {
            console.warn('Failed to preload audio:', error);
          }
        }
      } catch (e) {
        console.warn('Failed to load transcripts for samples:', e);
        setSampleSentencesByAge({});
      } finally {
        if (!cancelled) setIsLoadingSamples(false);
      }
    }
    loadAllSamples();
    return () => { cancelled = true; };
  }, [scenarioId, transcriptChoices]);

  // Check TTS service status on component mount
  useEffect(() => {
    const checkServices = async () => {
      const status = hybridTTS.getStatus();
      // Check Pipecat availability dynamically
      await hybridTTS.checkPipecatAvailability();
      const updatedStatus = hybridTTS.getStatus();
      setTtsServiceStatus(updatedStatus);
      console.log('TTS Service Status:', updatedStatus);
    };
    checkServices();
  }, []);

  // Check for existing illustrations for the current scenario
  const checkExistingIllustration = async () => {
    if (!scenarioId) return;
    try {
      setIsCheckingExisting(true);
      const res = await fetch(`http://localhost:8081/api/v1/illustrations/list/${scenarioId}`);
      if (res.ok) {
        const data = await res.json();
        if (data.illustrations && data.illustrations.length > 0) {
          // Get the most recent illustration
          const latest = data.illustrations[0];
          setIllustrationUrl(latest.file);
          return true; // Found existing illustration
        }
      }
    } catch (e) {
      console.warn('Failed to check existing illustrations:', e);
    } finally {
      setIsCheckingExisting(false);
    }
    return false; // No existing illustration found
  };

  // Generate an illustration aligned to the scenario using backend API (google-genai)
  const generateIllustration = async () => {
    if (!scenarioId) return;
    try {
      setIsGeneratingImage(true);
      const agePart = selectedAge ? ` Age group: ${selectedAge.replace('-', ' ')}.` : '';
      const variantPart = selectedVariant ? ` Difficulty: ${selectedVariant.replace('variant', 'Variant ')}.` : '';
      const prompt = `An educational, friendly illustration for scenario '${scenarioId}' in an Irish primary school context.
${agePart}${variantPart} Child-safe, simple, warm colors.
IMPORTANT: If the illustration contains any Irish text (Gaeilge), signs, labels, or written content, always include clear English translations or captions alongside the Irish text to help Chinese students understand.`;
      const res = await fetch('http://localhost:8081/api/v1/illustrations/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, scenario: scenarioId })
      });
      if (!res.ok) {
        throw new Error(`Image API error: ${res.status}`);
      }
      const data = await res.json();
      // Prefer persisted URL if available, otherwise data URL fallback
      setIllustrationUrl(data?.image_url || data?.image_data_url || '');
    } catch (e) {
      console.warn('Illustration generation failed:', e);
      setIllustrationUrl('');
    } finally {
      setIsGeneratingImage(false);
    }
  };

  // Auto-check for existing illustrations when scenario changes
  useEffect(() => {
    if (scenarioId) {
      checkExistingIllustration();
    }
  }, [scenarioId]);

  useEffect(() => {
    // Cleanup on unmount
    return () => {
      if (webrtcClient.current) {
        webrtcClient.current.disconnect();
      }
    };
  }, []);

  // Auto-clear subtitles after a period of inactivity
  useEffect(() => {
    if (subtitles && connectionState === 'connected') {
      // Clear any existing timeout
      if (subtitleTimeoutRef.current) {
        clearTimeout(subtitleTimeoutRef.current);
      }
      
      // Set a new timeout to clear subtitles after 8 seconds
      subtitleTimeoutRef.current = setTimeout(() => {
        setSubtitles('');
      }, 8000);
    }
    
    return () => {
      if (subtitleTimeoutRef.current) {
        clearTimeout(subtitleTimeoutRef.current);
      }
    };
  }, [subtitles, connectionState]);

  // Cleanup subtitle history periodically to prevent memory issues
  useEffect(() => {
    if (subtitleHistory.length > 10) {
      setSubtitleHistory(prev => prev.slice(-5));
    }
  }, [subtitleHistory]);

  const handleConnect = async () => {
    // Reset the intentional disconnect flag when starting a new connection
    isIntentionalDisconnect.current = false;
    setHasStarted(true);
    setConnectionState('connecting');
    await startConversation();
  };

  const startConversation = async () => {
    try {
      // Initialize WebRTC client with RTVI (use port 8082 where backend server is running)
      webrtcClient.current = new WebRTCClient('http://localhost:8080');
      
      // Set up callbacks
      webrtcClient.current.on('track', (remoteStream) => {
        console.log('Track received:', remoteStream);
        console.log('Audio tracks:', remoteStream?.getAudioTracks());
        console.log('Video tracks:', remoteStream?.getVideoTracks());
        
        // Store the remote audio stream for later use (both state and ref)
        if (remoteStream && remoteStream.getAudioTracks().length > 0) {
          setRemoteAudioStream(remoteStream);
          remoteAudioStreamRef.current = remoteStream;
          console.log('Stored remote audio stream');
          
          // Use the same approach as the working test page - create a separate Audio element
          console.log('Setting up audio playback using Audio element (like test page)');
          const audio = new Audio();
          audio.srcObject = remoteStream;
          audio.play().then(() => {
            console.log('✅ Audio playback started (Audio element)');
          }).catch(err => {
            console.warn('❌ Audio playback failed (Audio element):', err);
          });
        }
        
        // Handle video display separately
        if (remoteVideoRef.current && remoteVideoRef.current.srcObject !== remoteStream) {
          remoteVideoRef.current.srcObject = remoteStream;
        }
      });

      webrtcClient.current.on('botReady', () => {
        console.log('Bot ready event triggered');
        
        // Update local video (only if camera is enabled)
        if (localVideoRef.current) {
          const localStream = webrtcClient.current.getLocalStream();
          if (localStream && !preferAudioOnly) {
            localVideoRef.current.srcObject = localStream;
          } else {
            // Clear local video if camera is disabled
            localVideoRef.current.srcObject = null;
          }
        }
        
        // Use stored remote audio stream if available, otherwise try to get from client
        const streamToUse = remoteAudioStreamRef.current || remoteAudioStream || webrtcClient.current.getRemoteStream();
        console.log('Bot ready - using stream:', streamToUse);
        console.log('Bot ready - stored remote audio stream (ref):', remoteAudioStreamRef.current);
        console.log('Bot ready - stored remote audio stream (state):', remoteAudioStream);
        console.log('Bot ready - client remote stream:', webrtcClient.current.getRemoteStream());
        
        if (streamToUse) {
          // Handle video display
          if (remoteVideoRef.current) {
            if (remoteVideoRef.current.srcObject !== streamToUse) {
              remoteVideoRef.current.srcObject = streamToUse;
            }
          }
          
          // Handle audio playback using Audio element (like test page)
          if (streamToUse.getAudioTracks().length > 0) {
            console.log('Setting up audio playback from bot ready event using Audio element');
            const audio = new Audio();
            audio.srcObject = streamToUse;
            audio.play().then(() => {
              console.log('✅ Audio play successful from bot ready event (Audio element)');
            }).catch(err => {
              console.warn('❌ Bot ready audio play failed (Audio element):', err);
            });
          }
        } else {
          console.warn('No remote stream available for bot ready event');
        }
      });

      webrtcClient.current.on('connected', () => {
        setConnectionState('connected');
        
        // Trigger success celebration for child-friendly feedback
        triggerSuccessCelebration('confetti');
        
        // Update local video after connection (only if camera is enabled)
        setTimeout(() => {
          if (localVideoRef.current) {
            const localStream = webrtcClient.current.getLocalStream();
            if (localStream && !preferAudioOnly) {
              localVideoRef.current.srcObject = localStream;
            } else {
              // Clear local video if camera is disabled
              localVideoRef.current.srcObject = null;
            }
          }
        }, 500);
      });

      webrtcClient.current.on('connectionStateChange', (state) => {
        if (state === 'connected') {
          setConnectionState('connected');
        } else if (state === 'failed' || state === 'disconnected') {
          // Only show error if this wasn't an intentional disconnect
          if (!isIntentionalDisconnect.current) {
            setError('Connection lost');
            setConnectionState('error');
          }
        }
      });

      webrtcClient.current.on('error', (err) => {
        console.error('WebRTC error:', err);
        const msg = (err?.message || '').toLowerCase();
        const looksLikeServerDown = (
          msg.includes('failed to fetch') ||
          msg.includes('network') ||
          msg.includes('/api/offer') ||
          msg.includes('404') ||
          msg.includes('502') ||
          msg.includes('ecconnrefused')
        );
        if (looksLikeServerDown) {
          console.warn('[dev] Pipecat server might be down. Start it on port 8080 and backend proxy on 8081.');
          setError('System is under maintenance right now. Please try again shortly.');
        } else {
          setError(err?.message || (err ? String(err) : 'Connection error'));
        }
        setConnectionState('error');
      });

      // Add event listeners for text/transcript data using proper RTVI events
      if (webrtcClient.current.pcClient) {
        try {
          // Listen for user transcription (speech-to-text)
          webrtcClient.current.pcClient.on(RTVIEvent.UserTranscript, (data) => {
            try {
              console.log('User transcript received:', data);
              if (data?.final && data?.text?.trim()) {
                setSubtitles(data.text);
                setSubtitleHistory(prev => [...prev.slice(-4), { 
                  text: data.text, 
                  timestamp: Date.now(),
                  type: 'user'
                }]);
              }
            } catch (error) {
              console.warn('Error handling user transcript:', error);
            }
          });

          // Listen for bot transcription (final aggregated bot responses)
          webrtcClient.current.pcClient.on(RTVIEvent.BotTranscript, (data) => {
            try {
              console.log('Bot transcript received:', data);
              if (data?.text?.trim()) {
                setSubtitles(data.text);
                setSubtitleHistory(prev => [...prev.slice(-4), { 
                  text: data.text, 
                  timestamp: Date.now(),
                  type: 'bot'
                }]);
              }
            } catch (error) {
              console.warn('Error handling bot transcript:', error);
            }
          });

          // Listen for LLM streaming tokens (for real-time display)
          webrtcClient.current.pcClient.on(RTVIEvent.BotLlmText, (data) => {
            try {
              console.log('LLM token received:', data);
              if (data?.text) {
                setIsStreaming(true);
                // Check if this is the start of a new response (first token)
                if (data.text.trim() && !currentLlmResponse) {
                  setCurrentLlmResponse(data.text);
                  setSubtitles(data.text);
                } else {
                  // Accumulate subsequent tokens
                  setCurrentLlmResponse(prev => prev + data.text);
                  setSubtitles(prev => prev + data.text);
                }
              }
            } catch (error) {
              console.warn('Error handling LLM token:', error);
            }
          });

          // Listen for TTS text (text being sent to speech synthesis)
          webrtcClient.current.pcClient.on(RTVIEvent.BotTtsText, (data) => {
            try {
              console.log('TTS text received:', data);
              if (data?.text?.trim()) {
                // Reset LLM accumulator and use final TTS text
                setIsStreaming(false);
                setCurrentLlmResponse('');
                setSubtitles(data.text);
                setSubtitleHistory(prev => [...prev.slice(-4), { 
                  text: data.text, 
                  timestamp: Date.now(),
                  type: 'bot'
                }]);
              }
            } catch (error) {
              console.warn('Error handling TTS text:', error);
            }
          });

          // Fallback: Listen for generic RTVI messages in case specific events don't work
          webrtcClient.current.pcClient.on('message', (message) => {
            try {
              console.log('Generic RTVI message received:', message);
              // Check for text content in various message formats
              const text = message?.data?.text || message?.text || message?.content;
              if (text?.trim()) {
                const messageType = message?.type || message?.event || 'unknown';
                
                // Handle different types of text messages
                if (messageType.includes('transcript') || messageType.includes('text')) {
                  setSubtitles(text);
                  setSubtitleHistory(prev => [...prev.slice(-4), { 
                    text: text, 
                    timestamp: Date.now(),
                    type: messageType.includes('user') ? 'user' : 'bot'
                  }]);
                }
              }
            } catch (error) {
              console.warn('Error handling generic RTVI message:', error);
            }
          });
        } catch (error) {
          console.error('Error setting up RTVI event listeners:', error);
        }
      }

      // Connect using RTVI (it will handle media initialization)
      // Pass scenario parameter if available
      const connectOptions = scenario ? {
        scenario: scenario.id,
        scenarioDetails: {
          title: scenario.title,
          description: scenario.description,
          objectives: Array.isArray(scenario.objectives) ? scenario.objectives.slice(0, 5) : [],
          tags: Array.isArray(scenario.tags) ? scenario.tags : [],
          ageGroups: Array.isArray(scenario.ageGroups) ? scenario.ageGroups : [],
          difficulty: scenario.difficulty,
        },
        enableCam: !preferAudioOnly,
      } : { enableCam: !preferAudioOnly };
      
      console.log('VideoConversation: preferAudioOnly =', preferAudioOnly);
      console.log('VideoConversation: enableCam =', !preferAudioOnly);
      console.log('VideoConversation: connectOptions =', connectOptions);
      
      await webrtcClient.current.connect(connectOptions);
      
    } catch (err) {
      console.error('Failed to start conversation:', err);
      const msg = (err?.message || '').toLowerCase();
      const looksLikeServerDown = (
        msg.includes('failed to fetch') ||
        msg.includes('network') ||
        msg.includes('/api/offer') ||
        msg.includes('404') ||
        msg.includes('502') ||
        msg.includes('ecconnrefused')
      );
      if (looksLikeServerDown) {
        console.warn('[dev] Pipecat server might be down. Start it on port 8080 and backend proxy on 8081.');
        setError('System is under maintenance right now. Please try again shortly.');
      } else {
        setError(err?.message || 'Failed to start conversation');
      }
      setConnectionState('error');
    }
  };
  const toggleMode = () => {
    // Switch preference; if connected, also toggle camera accordingly
    const next = !preferAudioOnly;
    setPreferAudioOnly(next);
    if (webrtcClient.current && connectionState === 'connected') {
      webrtcClient.current.toggleCamera(!next);
      setIsCameraEnabled(!next);
      
      // Update local video display based on new mode
      if (localVideoRef.current) {
        if (next) {
          // Audio-only mode: clear local video
          localVideoRef.current.srcObject = null;
        } else {
          // Video mode: restore local video
          const localStream = webrtcClient.current.getLocalStream();
          if (localStream) {
            localVideoRef.current.srcObject = localStream;
          }
        }
      }
    }
  };

  const handleDisconnect = () => {
    // Set flag to indicate this is an intentional disconnect
    isIntentionalDisconnect.current = true;
    
    if (webrtcClient.current) {
      webrtcClient.current.disconnect();
    }
    
    // Clean up video elements
    if (remoteVideoRef.current) {
      remoteVideoRef.current.srcObject = null;
    }
    if (localVideoRef.current) {
      localVideoRef.current.srcObject = null;
    }
    
    setHasStarted(false);
    setConnectionState('idle');
    setError('');
    
    // Clear subtitle state and timeouts
    setSubtitles('');
    setSubtitleHistory([]);
    setCurrentLlmResponse('');
    setIsStreaming(false);
    if (subtitleTimeoutRef.current) {
      clearTimeout(subtitleTimeoutRef.current);
      subtitleTimeoutRef.current = null;
    }
    if (debounceTimeoutRef.current) {
      clearTimeout(debounceTimeoutRef.current);
      debounceTimeoutRef.current = null;
    }
    
    // Reset the flag after a short delay
    setTimeout(() => {
      isIntentionalDisconnect.current = false;
    }, 500);
  };

  const toggleMic = async () => {
    if (webrtcClient.current) {
      const newState = !isMicEnabled;
      await webrtcClient.current.toggleMicrophone(newState);
      setIsMicEnabled(newState);
    }
  };

  const toggleCamera = async () => {
    if (webrtcClient.current) {
      const newState = !isCameraEnabled;
      await webrtcClient.current.toggleCamera(newState);
      setIsCameraEnabled(newState);
    }
  };

  const toggleSubtitles = () => {
    setSubtitlesEnabled(!subtitlesEnabled);
  };

  // Function to play audio for sample sentences using Hybrid TTS (Cartesia + fallback)
  const playSampleAudio = async (text, index) => {
    try {
      // Stop any currently playing audio
      if (playingAudio !== null) {
        await hybridTTS.stop();
      }
      
      // Set playing state
      setPlayingAudio(index);
      
      // Use Hybrid TTS service (Cartesia with Web Speech API fallback)
      await hybridTTS.speak(text, 'en-IE', {
        // Force Web Speech API if needed for testing
        // forceWebSpeech: true
      });
      
      // Clear playing state when done
      setPlayingAudio(null);
      
    } catch (error) {
      console.warn('TTS playback error:', error);
      setPlayingAudio(null);
      
      // Show user-friendly error message
      if (error.message.includes('No TTS service available')) {
        console.warn('No TTS service available. Please check your internet connection and API keys.');
      }
    }
  };

  return (
    <div className="min-h-screen px-4 sm:px-6 lg:px-8 py-6 max-w-7xl mx-auto">
      <div className="text-center mb-8 lg:mb-12">
        <div className="max-w-4xl mx-auto">
          <h1 className="page-title">Conversation with Xiao Mei</h1>
          <p className="page-description">
            Practice your English conversation skills with AI-powered Xiao Mei (小美). 
            She's here to help you learn and have fun!
          </p>
        </div>
      </div>
      
      <div className="home-box">
        {/* <div className="support-design">
          <div className="support-design-box">
            <div className="os_line_wrap">
              <div className="os_line"></div>
              <div className="os_line"></div>
              <div className="os_line"></div>
              <div className="os_line"></div>
              <div className="os_line"></div>
              <div className="os_line"></div>
              <div className="os_line"></div>
            </div>
            <p className="text-size-tiny text-type-raster hero-type">CVI Portal</p>
            <div className="os_line_wrap">
              <div className="os_line"></div>
              <div className="os_line"></div>
              <div className="os_line"></div>
              <div className="os_line"></div>
              <div className="os_line"></div>
              <div className="os_line"></div>
              <div className="os_line"></div>
            </div>
          </div>
        </div> */}

        <div className="hero-support-wrap">
          <div className="hero_video-wrap">
            <div className="video-container">
              <video 
                ref={remoteVideoRef}
                autoPlay 
                playsInline
                className="video-stream"
              />
              
              {/* Local video preview in corner */}
              {hasStarted && (
                <div className="local-video-preview">
                  <video 
                    ref={localVideoRef}
                    autoPlay 
                    muted 
                    playsInline
                    className="local-video"
                  />
                  <span className="local-video-label">You</span>
                </div>
              )}
              
              {connectionState === 'idle' && (
                <div className="video-overlay initial">
                  <div className="connect-prompt">
                    <svg className="phone-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                      <path d="M23 7l-7 5 7 5V7z" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                      <rect x="1" y="5" width="15" height="14" rx="2" ry="2" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                    </svg>
                    <h3>Ready to Connect</h3>
                    <p>
                      {scenario 
                        ? `Start your ${scenario.title} learning session`
                        : scenarioId 
                          ? `Start your learning session (scenario '${scenarioId}' not found)`
                          : 'Start your Conversation with Pipecat and Tavus'
                      }
                    </p>
                    <button 
                      onClick={handleConnect} 
                      className="connect-btn child-friendly-button"
                      onMouseEnter={(e) => childFriendlyAnimations.gentleHover(e.target)}
                      onMouseLeave={(e) => childFriendlyAnimations.resetHover(e.target)}
                    >
                      <svg viewBox="0 0 24 24" fill="currentColor">
                        <path d="M23 7l-7 5 7 5V7z"/>
                        <rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>
                      </svg>
                      Connect
                    </button>
                  </div>
                </div>
              )}

              {connectionState === 'connecting' && (
                <div className="video-overlay">
                  <FriendlyLoader 
                    messages={[
                      'Connecting to your AI learning buddy...',
                      'Getting ready for our conversation...',
                      'Almost there...',
                      'Preparing your learning session...'
                    ]}
                    showProgressiveMessages={true}
                    size="large"
                  />
                </div>
              )}

              {connectionState === 'error' && (
                <div className="video-overlay error">
                  <svg className="error-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                    <circle cx="12" cy="12" r="10" strokeWidth="2"/>
                    <line x1="12" y1="8" x2="12" y2="12" strokeWidth="2" strokeLinecap="round"/>
                    <line x1="12" y1="16" x2="12.01" y2="16" strokeWidth="2" strokeLinecap="round"/>
                  </svg>
                  <p>{error || 'Connection failed'}</p>
                  <button 
                    onClick={handleConnect} 
                    className="retry-btn child-friendly-button"
                    onMouseEnter={(e) => childFriendlyAnimations.gentleHover(e.target)}
                    onMouseLeave={(e) => childFriendlyAnimations.resetHover(e.target)}
                  >
                    Retry Connection
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
      
      {/* Subtitle Display - Only show when connected and enabled */}
      {connectionState === 'connected' && subtitlesEnabled && (
        <div className="subtitle-container" data-testid="subtitle-container">
          <div className="subtitle-display" data-testid="subtitle-display" role="region" aria-live="polite" aria-label="AI assistant subtitles">
            {subtitles && (
              <div className={`current-subtitle ${isStreaming ? 'streaming' : ''}`}>
                <span className="subtitle-text">
                  {subtitles}
                  {isStreaming && <span className="typing-indicator">▌</span>}
                </span>
              </div>
            )}
          </div>
          
          {/* Optional: Show subtitle history */}
          {subtitleHistory.length > 0 && (
            <div className="subtitle-history" data-testid="subtitle-history">
              {subtitleHistory.slice(-3).map((item, index) => (
                <div key={`${item.timestamp}-${index}`} className={`subtitle-history-item ${item.type}`}>
                  <span className="subtitle-history-text">{item.text}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
      
      {/* Status and Controls Bar - Only show when started */}
      {hasStarted && (
        <div className="video-controls-bar">
          <div className="status-indicator">
            <span className={`status-dot ${connectionState}`}></span>
            <span className="status-text">
              {connectionState === 'connecting' && 'Connecting...'}
              {connectionState === 'connected' && 'Connected'}
              {connectionState === 'error' && 'Disconnected'}
            </span>
          </div>

          <div className="video-controls">
            <button 
              className={`control-button child-friendly-button`}
              onClick={toggleMode}
              onMouseEnter={(e) => childFriendlyAnimations.gentleHover(e.target)}
              onMouseLeave={(e) => childFriendlyAnimations.resetHover(e.target)}
              title={preferAudioOnly ? 'Switch to video mode' : 'Switch to audio-only mode'}
            >
              {preferAudioOnly ? (
                <span role="img" aria-label="video-off">🎤</span>
              ) : (
                <span role="img" aria-label="video-on">🎥</span>
              )}
            </button>
            <button 
              className={`control-button child-friendly-button ${!isMicEnabled ? 'disabled' : ''}`}
              onClick={toggleMic}
              onMouseEnter={(e) => childFriendlyAnimations.gentleHover(e.target)}
              onMouseLeave={(e) => childFriendlyAnimations.resetHover(e.target)}
              title={isMicEnabled ? 'Mute' : 'Unmute'}
              disabled={connectionState !== 'connected'}
            >
              {isMicEnabled ? (
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3z"/>
                  <path d="M17 11c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/>
                </svg>
              ) : (
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19 11h-1.7c0 .74-.16 1.43-.43 2.05l1.23 1.23c.56-.98.9-2.09.9-3.28zm-4.02.17c0-.06.02-.11.02-.17V5c0-1.66-1.34-3-3-3S9 3.34 9 5v.18l5.98 5.99zM4.27 3L3 4.27l6.01 6.01V11c0 1.66 1.33 3 2.99 3 .22 0 .44-.03.65-.08l1.66 1.66c-.71.33-1.5.52-2.31.52-2.76 0-5.3-2.1-5.3-5.1H5c0 3.41 2.72 6.23 6 6.72V21h2v-3.28c.91-.13 1.77-.45 2.54-.9L19.73 21 21 19.73 4.27 3z"/>
                </svg>
              )}
            </button>

            <button 
              className={`control-button child-friendly-button ${!isCameraEnabled ? 'disabled' : ''}`}
              onClick={toggleCamera}
              onMouseEnter={(e) => childFriendlyAnimations.gentleHover(e.target)}
              onMouseLeave={(e) => childFriendlyAnimations.resetHover(e.target)}
              title={isCameraEnabled ? 'Turn off camera' : 'Turn on camera'}
              disabled={connectionState !== 'connected'}
            >
              {isCameraEnabled ? (
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path d="M17 10.5V7c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1v-3.5l4 4v-11l-4 4z"/>
                </svg>
              ) : (
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path d="M21 6.5l-4 4V7c0-.55-.45-1-1-1H9.82L21 17.18V6.5zM3.27 2L2 3.27 4.73 6H4c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.21 0 .39-.08.54-.18L19.73 21 21 19.73 3.27 2z"/>
                </svg>
              )}
            </button>

            <button 
              className={`control-button child-friendly-button ${!subtitlesEnabled ? 'disabled' : ''}`}
              onClick={toggleSubtitles}
              onMouseEnter={(e) => childFriendlyAnimations.gentleHover(e.target)}
              onMouseLeave={(e) => childFriendlyAnimations.resetHover(e.target)}
              title={subtitlesEnabled ? 'Hide subtitles' : 'Show subtitles'}
            >
              {subtitlesEnabled ? (
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zM4 12h4v2H4v-2zm10 6H4v-2h10v2zm6 0h-4v-2h4v2zm0-4H10v-2h10v2z"/>
                </svg>
              ) : (
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zM4 12h4v2H4v-2zm10 6H4v-2h10v2zm6 0h-4v-2h4v2zm0-4H10v-2h10v2z"/>
                  <path d="M3 17l18-18" stroke="currentColor" strokeWidth="2"/>
                </svg>
              )}
            </button>

            <button 
              className="control-button child-friendly-button disconnect"
              onClick={handleDisconnect}
              onMouseEnter={(e) => childFriendlyAnimations.gentleHover(e.target)}
              onMouseLeave={(e) => childFriendlyAnimations.resetHover(e.target)}
              title="Disconnect"
            >
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 9c-1.6 0-3.15.25-4.6.72v3.1c0 .39-.23.74-.56.9-.98.49-1.87 1.12-2.66 1.85-.18.18-.43.28-.7.28-.28 0-.53-.11-.71-.29L.29 13.08c-.18-.17-.29-.42-.29-.7 0-.28.11-.53.29-.71C3.34 8.78 7.46 7 12 7s8.66 1.78 11.71 4.67c.18.18.29.43.29.71 0 .28-.11.53-.29.71l-2.48 2.48c-.18.18-.43.29-.71.29-.27 0-.52-.11-.7-.28-.79-.74-1.68-1.36-2.66-1.85-.33-.16-.56-.5-.56-.9v-3.1C15.15 9.25 13.6 9 12 9z"/>
              </svg>
            </button>
          </div>
        </div>
      )}
      <div className="illustration-block">
        <div className="illustration-header">
          <strong>Scenario illustration</strong>
          <button className="small" onClick={generateIllustration} disabled={isGeneratingImage || isCheckingExisting}>
            {isGeneratingImage ? 'Generating…' : 
             isCheckingExisting ? 'Loading…' : 
             (illustrationUrl ? 'Regenerate' : 'Generate')}
          </button>
        </div>
        {illustrationUrl ? (
          <img alt="Scenario illustration" src={illustrationUrl} className="illustration" />
        ) : (
          <div className="illustration-placeholder">No image yet</div>
        )}
      </div>

      {/* Scenario side panel */}
      <div className="conversation-side-panel" data-testid="conversation-side-panel">
        <div className="scenario-info">
          <h3>{scenario ? scenario.title : 'Conversation'}</h3>
          {scenario && (
            <p className="scenario-desc">{scenario.description}</p>
          )}
          {scenario && scenario.objectives?.length > 0 && (
            <div className="scenario-objectives">
              <strong>Objectives</strong>
              <ul>
                {scenario.objectives.slice(0, 4).map((obj, idx) => (
                  <li key={idx}>{obj}</li>
                ))}
              </ul>
            </div>
          )}
        </div>

        <div className="sample-sentences">
          <div className="sample-sentences-header">
            <strong>Try saying</strong>
            {ttsServiceStatus && (
              <div className="tts-service-indicator">
                <span className={`service-dot ${
                  ttsServiceStatus.cartesiaAvailable ? 'cartesia' : 
                  ttsServiceStatus.pipecatAvailable ? 'pipecat' : 
                  'web-speech'
                }`}></span>
                <span className="service-name">
                  {ttsServiceStatus.cartesiaAvailable ? 'High-Quality TTS' : 
                   ttsServiceStatus.pipecatAvailable ? 'Pipecat TTS' : 
                   'Web Speech'}
                </span>
              </div>
            )}
          </div>
          {isLoadingSamples ? (
            <FriendlyLoader 
              message="Loading helpful examples..."
              size="small"
              className="compact"
            />
          ) : Object.keys(sampleSentencesByAge).length === 0 ? (
            <p className="muted">No examples available</p>
          ) : (
            <div>
              {Object.entries(sampleSentencesByAge)
                .sort(([a], [b]) => {
                  // Sort age groups in progression: junior-infants, senior-infants, first-class, etc.
                  const order = ['junior-infants', 'senior-infants', 'first-class', 'second-class', 'third-class', 'fourth-class'];
                  return order.indexOf(a) - order.indexOf(b);
                })
                .map(([ageGroup, sentences]) => (
                  <div key={ageGroup} className="age-group-section">
                    <h4 className="age-group-header">
                      {ageGroup.replace('-', ' ').replace(/\b\w/g, l => l.toUpperCase())}
                    </h4>
                    <ul>
                      {sentences.map((s, i) => {
                        const globalIndex = `${ageGroup}-${i}`;
                        return (
                          <li key={globalIndex} className="sample-sentence-item">
                            <span className="sample-text">"{s}"</span>
                            <button 
                              className={`speaker-button ${playingAudio === globalIndex ? 'playing' : ''}`}
                              onClick={() => playSampleAudio(s, globalIndex)}
                              title={playingAudio === globalIndex ? "Playing..." : "Click to hear pronunciation"}
                              aria-label={`Play audio for: ${s}`}
                              disabled={playingAudio !== null && playingAudio !== globalIndex}
                            >
                              {playingAudio === globalIndex ? (
                                <svg viewBox="0 0 24 24" fill="currentColor" className="speaker-icon">
                                  <path d="M6 6h4v12H6V6zm8 0h4v12h-4V6z"/>
                                </svg>
                              ) : (
                                <svg viewBox="0 0 24 24" fill="currentColor" className="speaker-icon">
                                  <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
                                </svg>
                              )}
                            </button>
                          </li>
                        );
                      })}
                    </ul>
                  </div>
                ))}
            </div>
          )}
        </div>
      </div>

      
    </div>
  );
}

export default VideoConversation;