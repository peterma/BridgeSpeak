// Script to update scenario tags to streamlined system
const fs = require('fs');

// Read the scenarios file
const content = fs.readFileSync('src/data/scenarios.js', 'utf8');

// Define tag mappings
const tagMappings = {
  // Basic communication
  'introducing': 'basic-communication',
  'saying': 'basic-communication', 
  'asking': 'basic-communication',
  'answering': 'basic-communication',
  'explaining': 'basic-communication',
  'expressing': 'basic-communication',
  'talking': 'basic-communication',
  'yourself': 'basic-communication',
  'about': 'basic-communication',
  'showing': 'basic-communication',
  'understand': 'basic-communication',
  'giving': 'basic-communication',
  'making': 'basic-communication',
  'joining': 'basic-communication',
  'participating': 'basic-communication',
  'inviting': 'basic-communication',
  'organizing': 'basic-communication',
  'comforting': 'basic-communication',
  'describing': 'basic-communication',
  'comparing': 'basic-communication',
  'finding': 'basic-communication',
  'buying': 'basic-communication',
  'paying': 'basic-communication',
  'planning': 'basic-communication',
  'meeting': 'basic-communication',
  'visiting': 'basic-communication',
  'watching': 'basic-communication',
  'working': 'basic-communication',
  'together': 'basic-communication',
  'while': 'basic-communication',
  'with': 'basic-communication',
  'your': 'basic-communication',
  
  // Help seeking
  'help': 'help-seeking',
  'getting': 'help-seeking',
  
  // Sharing
  'sharing': 'sharing',
  'materials': 'sharing',
  'foods': 'sharing',
  'interests': 'sharing',
  
  // Polite behavior
  'polite': 'polite-behavior',
  'appropriate': 'polite-behavior',
  'being': 'polite-behavior',
  
  // Classroom
  'classroom': 'classroom',
  'teacher': 'classroom',
  'classmates': 'classroom',
  'school': 'classroom',
  'class': 'classroom',
  'question': 'classroom',
  'questions': 'classroom',
  'homework': 'classroom',
  'difficulties': 'classroom',
  'presentation': 'classroom',
  'discussions': 'classroom',
  'reading': 'classroom',
  'aloud': 'classroom',
  'assembly': 'classroom',
  'sports': 'classroom',
  'participation': 'classroom',
  
  // Learning
  'learning': 'learning',
  'basic': 'learning',
  'advanced': 'learning',
  'groups': 'learning',
  'group': 'learning',
  
  // Playground
  'playground': 'playground',
  'play': 'playground',
  'playing': 'playground',
  'games': 'playground',
  'equipment': 'playground',
  'solving': 'playground',
  'problems': 'playground',
  'others': 'playground',
  'feelings': 'playground',
  'upset': 'playground',
  
  // Food/Lunch
  'food': 'food-lunch',
  'lunch': 'food-lunch',
  'canteen': 'food-lunch',
  'hunger': 'food-lunch',
  
  // Friendship
  'friend': 'friendship',
  'friends': 'friendship',
  'friendship': 'friendship',
  'goodbye': 'friendship',
  'apologies': 'friendship',
  'disagreement': 'friendship',
  
  // Family
  'family': 'family',
  'siblings': 'family',
  'dinner': 'family',
  'outings': 'family',
  'conversations': 'family',
  'conversation': 'family',
  
  // Community
  'community': 'community',
  'neighbors': 'community',
  'local': 'community',
  'events': 'community',
  'gathering': 'community',
  
  // Shopping
  'shopping': 'shopping',
  'stores': 'shopping',
  'clothes': 'shopping',
  'prices': 'shopping',
  'products': 'shopping',
  'specific': 'shopping',
  'needs': 'shopping',
  'interactions': 'shopping',
  'checkout': 'shopping',
  'preferences': 'shopping',
  'things': 'shopping',
  
  // Transport
  'transport': 'transport',
  'bus': 'transport',
  'dart': 'transport',
  'walking': 'transport',
  'directions': 'transport',
  'tickets': 'transport',
  'dublin': 'transport',
  
  // Irish Culture
  'irish': 'irish-culture',
  'traditions': 'irish-culture',
  'traditional': 'irish-culture',
  'patrick\'s': 'irish-culture',
  'gaa': 'irish-culture',
  'matches': 'irish-culture',
  'music': 'irish-culture',
  'dancing': 'irish-culture',
  'heritage': 'irish-culture',
  'sites': 'irish-culture',
  'celebration': 'irish-culture',
  'culture': 'irish-culture',
  
  // Chinese Culture
  'chinese': 'chinese-culture',
  'cultural': 'chinese-culture',
  'holidays': 'chinese-culture',
  
  // Daily Life
  'daily-life': 'daily-life',
  'activities': 'daily-life',
  'party': 'daily-life',
  'birthday': 'daily-life',
  'home': 'daily-life',
  
  // Social
  'social': 'social'
};

// Apply tag mappings
let updatedContent = content;
for (const [oldTag, newTag] of Object.entries(tagMappings)) {
  const regex = new RegExp(`"${oldTag}"`, 'g');
  updatedContent = updatedContent.replace(regex, `"${newTag}"`);
}

// Write back to file
fs.writeFileSync('src/data/scenarios.js', updatedContent);

console.log('Tags updated successfully!');
