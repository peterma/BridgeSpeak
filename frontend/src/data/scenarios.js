// Expanded scenario library with 60 scenarios
// Generated from backend ExpandedScenarioLibraryService

import { getTranscriptStats } from './transcriptLoader';

export const SCENARIO_CATEGORIES = {
  ESSENTIAL: 'essential',
  SCHOOL: 'school',
  SOCIAL: 'social',
  DAILY_LIFE: 'daily-life',
  CULTURAL: 'cultural'
};

export const AGE_GROUPS = {
  JUNIOR_INFANTS: 'junior-infants',
  SENIOR_INFANTS: 'senior-infants',
  FIRST_CLASS: 'first-class',
  SECOND_CLASS: 'second-class',
  THIRD_CLASS: 'third-class',
  FOURTH_CLASS: 'fourth-class'
};

export const DIFFICULTY_LEVELS = {
  BEGINNER: 'beginner',
  INTERMEDIATE: 'intermediate',
  ADVANCED: 'advanced'
};

export const mockScenarios = [
  {
    "id": "introducing-yourself",
    "title": "Introducing Yourself",
    "icon": "👋",
    "description": "Learn to introduce yourself in various social situations",
    "category": "social",
    "ageGroups": [
      "junior-infants",
      "senior-infants",
      "first-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "basic-communication",
      "friendship",
      "social"
    ],
    "chineseContext": "\u81ea\u6211\u4ecb\u7ecd\u662f\u793e\u4ea4\u7684\u7b2c\u4e00\u6b65\u3002\u5728\u7231\u5c14\u5170\uff0c\u4eba\u4eec\u559c\u6b22\u53cb\u597d\u7684\u95ee\u5019\uff01",
    "objectives": [
      "Practice introducing yourself",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/introducing-yourself.svg",
    "isPopular": true
  },
  {
    "id": "asking-for-toilet",
    "title": "Asking for the Toilet",
    "icon": "🚻",
    "description": "Learn to politely ask for toilet permission in school",
    "category": "classroom",
    "ageGroups": [
      "junior-infants",
      "senior-infants",
      "first-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "help-seeking",
      "classroom"
    ],
    "chineseContext": "\u5728\u5b66\u6821\u9700\u8981\u4e0a\u5395\u6240\u65f6\uff0c\u8981\u793c\u8c8c\u5730\u95ee\u8001\u5e08\u3002\u8fd9\u5f88\u6b63\u5e38\uff0c\u4e0d\u8981\u5bb3\u7f9e\uff01",
    "objectives": [
      "Practice asking for the toilet",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/asking-for-toilet.svg",
    "isPopular": true
  },
  {
    "id": "asking-for-help",
    "title": "Asking for Help",
    "icon": "🙋",
    "description": "Learn to ask for help when you need support",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "help-seeking",
      "classroom"
    ],
    "chineseContext": "\u9700\u8981\u5e2e\u52a9\u65f6\u4e3b\u52a8\u5bfb\u6c42\u662f\u597d\u4e60\u60ef\u3002\u7231\u5c14\u5170\u4eba\u5f88\u4e50\u610f\u5e2e\u52a9\u522b\u4eba\uff01",
    "objectives": [
      "Practice asking for help",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/asking-for-help.svg",
    "isPopular": true
  },
  {
    "id": "expressing-hunger",
    "title": "Expressing Hunger",
    "icon": "🍽️",
    "description": "Learn to express hunger and food needs appropriately",
    "category": "daily-life",
    "ageGroups": [
      "junior-infants",
      "senior-infants",
      "first-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "basic-communication",
      "food-lunch",
      "daily-life"
    ],
    "chineseContext": "\u8868\u8fbe\u9965\u997f\u5f88\u6b63\u5e38\u3002\u5728\u7231\u5c14\u5170\uff0c\u53ca\u65f6\u8868\u8fbe\u9700\u6c42\u662f\u91cd\u8981\u7684\uff01",
    "objectives": [
      "Practice expressing hunger",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/expressing-hunger.svg",
    "isPopular": false
  },
  {
    "id": "saying-goodbye",
    "title": "Saying Goodbye",
    "icon": "👋",
    "description": "Learn various ways to say goodbye appropriately",
    "category": "social",
    "ageGroups": [
      "junior-infants",
      "senior-infants",
      "first-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "basic-communication",
      "friendship",
      "social"
    ],
    "chineseContext": "\u597d\u7684\u544a\u522b\u8ba9\u4eba\u611f\u89c9\u6e29\u6696\u3002\u7231\u5c14\u5170\u4eba\u91cd\u89c6\u53cb\u597d\u7684\u7ed3\u675f\u8bed\uff01",
    "objectives": [
      "Practice saying goodbye",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/saying-goodbye.svg",
    "isPopular": false
  },
  {
    "id": "asking-teacher-question",
    "title": "Asking Teacher a Question",
    "icon": "❓",
    "description": "Learn to ask your teacher questions politely in Irish classroom setting",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "classroom",
      "learning",
      "basic-communication",
      "polite-behavior"
    ],
    "chineseContext": "\u5728\u7231\u5c14\u5170\u8bfe\u5802\u4e0a\uff0c\u8001\u5e08\u5f88\u6b22\u8fce\u5b66\u751f\u63d0\u95ee\u3002\u8fd9\u662f\u5b66\u4e60\u7684\u597d\u65b9\u6cd5\uff01",
    "objectives": [
      "Practice asking teacher a question",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/asking-teacher-question.svg",
    "isPopular": false
  },
  {
    "id": "group-work-collaboration",
    "title": "Working Together in Groups",
    "icon": "👥",
    "description": "Learn to collaborate effectively in group work activities",
    "category": "classroom",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "classroom",
      "basic-communication",
      "learning"
    ],
    "chineseContext": "\u5728\u7231\u5c14\u5170\u5b66\u6821\uff0c\u5c0f\u7ec4\u5408\u4f5c\u662f\u5f88\u5e38\u89c1\u7684\u3002\u5927\u5bb6\u4e00\u8d77\u5de5\u4f5c\uff0c\u76f8\u4e92\u5e2e\u52a9\uff01",
    "objectives": [
      "Practice working together in groups",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/group-work-collaboration.svg",
    "isPopular": false
  },
  {
    "id": "class-presentation",
    "title": "Giving a Class Presentation",
    "icon": "🎤",
    "description": "Learn to present to your class with confidence",
    "category": "classroom",
    "ageGroups": [
      "second-class",
      "third-class",
      "fourth-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "classroom",
      "learning",
      "basic-communication"
    ],
    "chineseContext": "\u5728\u7231\u5c14\u5170\u5b66\u6821\u505a\u6f14\u8bb2\u53ef\u4ee5\u63d0\u9ad8\u81ea\u4fe1\u5fc3\u3002\u540c\u5b66\u4eec\u90fd\u4f1a\u8ba4\u771f\u542c\uff01",
    "objectives": [
      "Practice giving a class presentation",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/class-presentation.svg",
    "isPopular": false
  },
  {
    "id": "answering-in-class",
    "title": "Answering Questions in Class",
    "icon": "✋",
    "description": "Learn to answer teacher questions confidently",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "classroom",
      "learning",
      "basic-communication"
    ],
    "chineseContext": "\u5728\u8bfe\u5802\u4e0a\u56de\u7b54\u95ee\u9898\u662f\u5b66\u4e60\u7684\u91cd\u8981\u90e8\u5206\u3002\u4e0d\u8981\u62c5\u5fc3\u51fa\u9519\uff01",
    "objectives": [
      "Practice answering questions in class",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/answering-in-class.svg",
    "isPopular": false
  },
  {
    "id": "explaining-homework-problem",
    "title": "Explaining Homework Difficulties",
    "icon": "📝",
    "description": "Learn to discuss homework challenges with teacher",
    "category": "classroom",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "classroom",
      "basic-communication",
      "learning"
    ],
    "chineseContext": "\u5982\u679c\u4f5c\u4e1a\u6709\u56f0\u96be\uff0c\u544a\u8bc9\u8001\u5e08\u662f\u5f88\u6b63\u5e38\u7684\u3002\u8001\u5e08\u4f1a\u5e2e\u52a9\u4f60\uff01",
    "objectives": [
      "Practice explaining homework difficulties",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/explaining-homework-problem.svg",
    "isPopular": false
  },
  {
    "id": "sharing-learning-materials",
    "title": "Sharing School Materials",
    "icon": "✏️",
    "description": "Learn to share and borrow school supplies politely",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "classroom",
      "sharing",
      "learning",
      "polite-behavior"
    ],
    "chineseContext": "\u5728\u7231\u5c14\u5170\u5b66\u6821\uff0c\u540c\u5b66\u4eec\u7ecf\u5e38\u5206\u4eab\u5b66\u4e60\u7528\u54c1\u3002\u8fd9\u662f\u53cb\u5584\u7684\u8868\u73b0\uff01",
    "objectives": [
      "Practice sharing school materials",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/sharing-learning-materials.svg",
    "isPopular": false
  },
  {
    "id": "participating-discussion",
    "title": "Joining Class Discussions",
    "icon": "💬",
    "description": "Learn to contribute to classroom discussions",
    "category": "classroom",
    "ageGroups": [
      "second-class",
      "third-class",
      "fourth-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "classroom",
      "learning",
      "basic-communication"
    ],
    "chineseContext": "\u53c2\u4e0e\u8bfe\u5802\u8ba8\u8bba\u53ef\u4ee5\u63d0\u9ad8\u82f1\u8bed\u6c34\u5e73\u3002\u5206\u4eab\u4f60\u7684\u60f3\u6cd5\u5f88\u91cd\u8981\uff01",
    "objectives": [
      "Practice joining class discussions",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/participating-discussion.svg",
    "isPopular": false
  },
  {
    "id": "asking-classmate-help",
    "title": "Asking Classmates for Help",
    "icon": "🤝",
    "description": "Learn to ask peers for help with schoolwork",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "classroom",
      "help-seeking",
      "learning",
      "basic-communication"
    ],
    "chineseContext": "\u5411\u540c\u5b66\u6c42\u52a9\u662f\u5f88\u6b63\u5e38\u7684\u3002\u7231\u5c14\u5170\u5b66\u751f\u5f88\u4e50\u610f\u4e92\u76f8\u5e2e\u52a9\uff01",
    "objectives": [
      "Practice asking classmates for help",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/asking-classmate-help.svg",
    "isPopular": false
  },
  {
    "id": "reading-aloud-class",
    "title": "Reading Aloud in Class",
    "icon": "📖",
    "description": "Learn to read confidently in front of the class",
    "category": "classroom",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "classroom",
      "learning"
    ],
    "chineseContext": "\u5728\u73ed\u4e0a\u5927\u58f0\u6717\u8bfb\u53ef\u4ee5\u7ec3\u4e60\u53d1\u97f3\u3002\u6162\u6162\u6765\uff0c\u4e0d\u8981\u7d27\u5f20\uff01",
    "objectives": [
      "Practice reading aloud in class",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/reading-aloud-class.svg",
    "isPopular": false
  },
  {
    "id": "showing-understanding",
    "title": "Showing You Understand",
    "icon": "💡",
    "description": "Learn to demonstrate comprehension in class",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "classroom",
      "learning",
      "basic-communication"
    ],
    "chineseContext": "\u8868\u73b0\u51fa\u4f60\u7406\u89e3\u4e86\u5f88\u91cd\u8981\u3002\u8fd9\u6837\u8001\u5e08\u77e5\u9053\u4f60\u5728\u8ba4\u771f\u542c\uff01",
    "objectives": [
      "Practice showing you understand",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/showing-understanding.svg",
    "isPopular": false
  },
  {
    "id": "making-new-friends",
    "title": "Making New Friends",
    "icon": "🤗",
    "description": "Learn to make friends in the school playground",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "friendship",
      "classroom",
      "basic-communication",
      "playground",
      "learning"
    ],
    "chineseContext": "\u5728\u7231\u5c14\u5170\u5b66\u6821\u4ea4\u670b\u53cb\u5f88\u5bb9\u6613\u3002\u7231\u5c14\u5170\u5b69\u5b50\u4eec\u5f88\u53cb\u597d\uff0c\u559c\u6b22\u8ba4\u8bc6\u65b0\u670b\u53cb\uff01",
    "objectives": [
      "Practice making new friends",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/making-new-friends.svg",
    "isPopular": false
  },
  {
    "id": "playground-games",
    "title": "Playing Playground Games",
    "icon": "⚽",
    "description": "Learn to join and organize playground games",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "classroom",
      "playground",
      "learning"
    ],
    "chineseContext": "\u7231\u5c14\u5170\u64cd\u573a\u4e0a\u6709\u5f88\u591a\u6709\u8da3\u7684\u6e38\u620f\u3002\u52a0\u5165\u6e38\u620f\u662f\u4ea4\u670b\u53cb\u7684\u597d\u65b9\u6cd5\uff01",
    "objectives": [
      "Practice playing playground games",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/playground-games.svg",
    "isPopular": true
  },
  {
    "id": "resolving-playground-conflict",
    "title": "Solving Playground Problems",
    "icon": "🤝",
    "description": "Learn to resolve disagreements peacefully",
    "category": "classroom",
    "ageGroups": [
      "second-class",
      "third-class",
      "fourth-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "classroom",
      "playground",
      "learning"
    ],
    "chineseContext": "\u5982\u679c\u64cd\u573a\u4e0a\u6709\u95ee\u9898\uff0c\u548c\u5e73\u89e3\u51b3\u662f\u6700\u597d\u7684\u65b9\u6cd5\u3002\u7231\u5c14\u5170\u4eba\u91cd\u89c6\u53cb\u5584\uff01",
    "objectives": [
      "Practice solving playground problems",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/resolving-playground-conflict.svg",
    "isPopular": false
  },
  {
    "id": "inviting-to-play",
    "title": "Inviting Others to Play",
    "icon": "🎾",
    "description": "Learn to include others in playground activities",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "classroom",
      "basic-communication",
      "playground",
      "learning"
    ],
    "chineseContext": "\u9080\u8bf7\u522b\u4eba\u4e00\u8d77\u73a9\u662f\u5f88\u53cb\u5584\u7684\u884c\u4e3a\u3002\u8fd9\u6837\u53ef\u4ee5\u8ba9\u6bcf\u4e2a\u4eba\u90fd\u5f00\u5fc3\uff01",
    "objectives": [
      "Practice inviting others to play",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/inviting-to-play.svg",
    "isPopular": false
  },
  {
    "id": "sharing-playground-equipment",
    "title": "Sharing Playground Equipment",
    "icon": "🤲",
    "description": "Learn to share and take turns with playground equipment",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "classroom",
      "playground",
      "sharing",
      "learning"
    ],
    "chineseContext": "\u5728\u64cd\u573a\u4e0a\u5206\u4eab\u8bbe\u5907\u5f88\u91cd\u8981\u3002\u8f6e\u6d41\u4f7f\u7528\u8ba9\u6bcf\u4e2a\u4eba\u90fd\u80fd\u73a9\uff01",
    "objectives": [
      "Practice sharing playground equipment",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/sharing-playground-equipment.svg",
    "isPopular": false
  },
  {
    "id": "expressing-feelings-playground",
    "title": "Expressing Feelings on Playground",
    "icon": "😊",
    "description": "Learn to communicate emotions appropriately",
    "category": "classroom",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "classroom",
      "learning",
      "basic-communication",
      "playground"
    ],
    "chineseContext": "\u8868\u8fbe\u611f\u53d7\u5f88\u91cd\u8981\u3002\u5982\u679c\u4f60\u96be\u8fc7\u6216\u5f00\u5fc3\uff0c\u53ef\u4ee5\u544a\u8bc9\u670b\u53cb\uff01",
    "objectives": [
      "Practice expressing feelings on playground",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/expressing-feelings-playground.svg",
    "isPopular": false
  },
  {
    "id": "organizing-group-game",
    "title": "Organizing Group Games",
    "icon": "🎯",
    "description": "Learn to lead and organize playground activities",
    "category": "classroom",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "classroom",
      "basic-communication",
      "playground",
      "learning"
    ],
    "chineseContext": "\u7ec4\u7ec7\u6e38\u620f\u53ef\u4ee5\u953b\u70bc\u9886\u5bfc\u80fd\u529b\u3002\u8ba9\u6bcf\u4e2a\u4eba\u90fd\u53c2\u4e0e\u8fdb\u6765\uff01",
    "objectives": [
      "Practice organizing group games",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/organizing-group-game.svg",
    "isPopular": false
  },
  {
    "id": "comforting-upset-friend",
    "title": "Comforting an Upset Friend",
    "icon": "🫂",
    "description": "Learn to provide emotional support to classmates",
    "category": "classroom",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "friendship",
      "classroom",
      "learning",
      "playground",
      "basic-communication"
    ],
    "chineseContext": "\u5b89\u6170\u96be\u8fc7\u7684\u670b\u53cb\u662f\u5f88\u5584\u826f\u7684\u884c\u4e3a\u3002\u7231\u5c14\u5170\u4eba\u5f88\u91cd\u89c6\u5173\u5fc3\u4ed6\u4eba\uff01",
    "objectives": [
      "Practice comforting an upset friend",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/comforting-upset-friend.svg",
    "isPopular": false
  },
  {
    "id": "lunch-food-conversation",
    "title": "Talking About Lunch",
    "icon": "🥪",
    "description": "Learn to discuss food and meals in the school canteen",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "classroom",
      "food-lunch",
      "basic-communication",
      "learning"
    ],
    "chineseContext": "\u5728\u5b66\u6821\u98df\u5802\u8c08\u8bba\u98df\u7269\u662f\u5f88\u6709\u8da3\u7684\uff01\u4f60\u53ef\u4ee5\u5206\u4eab\u4f60\u559c\u6b22\u7684\u4e2d\u56fd\u98df\u7269\u3002",
    "objectives": [
      "Practice talking about lunch",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/lunch-food-conversation.svg",
    "isPopular": true
  },
  {
    "id": "sharing-cultural-food",
    "title": "Sharing Cultural Foods",
    "icon": "🥟",
    "description": "Learn to share Chinese foods with Irish classmates",
    "category": "classroom",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "classroom",
      "food-lunch",
      "chinese-culture",
      "sharing",
      "learning"
    ],
    "chineseContext": "\u5206\u4eab\u4e2d\u56fd\u98df\u7269\u662f\u5f88\u597d\u7684\u6587\u5316\u4ea4\u6d41\u65b9\u5f0f\u3002\u7231\u5c14\u5170\u670b\u53cb\u4f1a\u5f88\u597d\u5947\uff01",
    "objectives": [
      "Practice sharing cultural foods",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/sharing-cultural-food.svg",
    "isPopular": false
  },
  {
    "id": "asking-lunch-help",
    "title": "Getting Help at Lunch",
    "icon": "🍽️",
    "description": "Learn to ask for help in the school canteen",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "classroom",
      "help-seeking",
      "learning",
      "food-lunch"
    ],
    "chineseContext": "\u5728\u98df\u5802\u9700\u8981\u5e2e\u52a9\u65f6\uff0c\u5de5\u4f5c\u4eba\u5458\u5f88\u4e50\u610f\u534f\u52a9\u4f60\uff01",
    "objectives": [
      "Practice getting help at lunch",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/asking-lunch-help.svg",
    "isPopular": false
  },
  {
    "id": "describing-food-preferences",
    "title": "Describing Food Preferences",
    "icon": "😋",
    "description": "Learn to express likes and dislikes about food",
    "category": "classroom",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "classroom",
      "food-lunch",
      "learning",
      "shopping",
      "basic-communication"
    ],
    "chineseContext": "\u8868\u8fbe\u5bf9\u98df\u7269\u7684\u559c\u597d\u53ef\u4ee5\u5e2e\u52a9\u522b\u4eba\u4e86\u89e3\u4f60\u3002\u8fd9\u662f\u5f88\u81ea\u7136\u7684\uff01",
    "objectives": [
      "Practice describing food preferences",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/describing-food-preferences.svg",
    "isPopular": false
  },
  {
    "id": "canteen-politeness",
    "title": "Being Polite in the Canteen",
    "icon": "🍴",
    "description": "Learn proper manners and etiquette in school dining",
    "category": "classroom",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "classroom",
      "food-lunch",
      "learning",
      "polite-behavior"
    ],
    "chineseContext": "\u5728\u98df\u5802\u4fdd\u6301\u793c\u8c8c\u5f88\u91cd\u8981\u3002\u7231\u5c14\u5170\u4eba\u5f88\u91cd\u89c6\u9910\u684c\u793c\u4eea\uff01",
    "objectives": [
      "Practice being polite in the canteen",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/canteen-politeness.svg",
    "isPopular": false
  },
  {
    "id": "school-assembly-participation",
    "title": "Participating in School Assembly",
    "icon": "🏛️",
    "description": "Learn to participate appropriately in school assemblies",
    "category": "classroom",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "classroom",
      "basic-communication",
      "learning"
    ],
    "chineseContext": "\u5b66\u6821\u96c6\u4f1a\u662f\u91cd\u8981\u7684\u793e\u533a\u6d3b\u52a8\u3002\u542c\u4ece\u6307\u793a\uff0c\u79ef\u6781\u53c2\u4e0e\uff01",
    "objectives": [
      "Practice participating in school assembly",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/school-assembly-participation.svg",
    "isPopular": false
  },
  {
    "id": "sports-day-activities",
    "title": "Sports Day Participation",
    "icon": "🏃",
    "description": "Learn to participate in Irish school sports events",
    "category": "classroom",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "classroom",
      "learning"
    ],
    "chineseContext": "\u4f53\u80b2\u8282\u662f\u7231\u5c14\u5170\u5b66\u6821\u7684\u4f20\u7edf\u6d3b\u52a8\u3002\u5c3d\u529b\u800c\u4e3a\uff0c\u4eab\u53d7\u8fd0\u52a8\u7684\u4e50\u8da3\uff01",
    "objectives": [
      "Practice sports day participation",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/sports-day-activities.svg",
    "isPopular": false
  },
  {
    "id": "grocery-shopping-help",
    "title": "Getting Help While Shopping",
    "icon": "🛒",
    "description": "Learn to ask for help in Dublin shops and supermarkets",
    "category": "daily-life",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "shopping",
      "basic-communication",
      "help-seeking",
      "daily-life",
      "learning"
    ],
    "chineseContext": "\u5728\u90fd\u67cf\u6797\u8d2d\u7269\u65f6\uff0c\u5e97\u5458\u4eec\u90fd\u5f88\u4e50\u610f\u5e2e\u52a9\u4f60\u3002\u4e0d\u8981\u5bb3\u6015\u5f00\u53e3\u8be2\u95ee\uff01",
    "objectives": [
      "Practice getting help while shopping",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/grocery-shopping-help.svg",
    "isPopular": false
  },
  {
    "id": "clothes-shopping-preferences",
    "title": "Shopping for Clothes",
    "icon": "👗",
    "description": "Learn to express preferences when clothes shopping",
    "category": "daily-life",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "daily-life",
      "shopping"
    ],
    "chineseContext": "\u5728\u90fd\u67cf\u6797\u4e70\u8863\u670d\u65f6\uff0c\u53ef\u4ee5\u8868\u8fbe\u4f60\u7684\u559c\u597d\u3002\u5e97\u5458\u4f1a\u5e2e\u4f60\u627e\u5230\u5408\u9002\u7684\uff01",
    "objectives": [
      "Practice shopping for clothes",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/clothes-shopping-preferences.svg",
    "isPopular": false
  },
  {
    "id": "asking-store-directions",
    "title": "Finding Things in Stores",
    "icon": "🏪",
    "description": "Learn to ask for directions within large shops",
    "category": "daily-life",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "shopping",
      "basic-communication",
      "daily-life",
      "learning"
    ],
    "chineseContext": "\u5728\u5927\u5546\u5e97\u91cc\u8ff7\u8def\u5f88\u6b63\u5e38\u3002\u8be2\u95ee\u65b9\u5411\u53ef\u4ee5\u5feb\u901f\u627e\u5230\u4f60\u9700\u8981\u7684\u4e1c\u897f\uff01",
    "objectives": [
      "Practice finding things in stores",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/asking-store-directions.svg",
    "isPopular": false
  },
  {
    "id": "paying-at-checkout",
    "title": "Paying at the Checkout",
    "icon": "💳",
    "description": "Learn checkout interactions and payment processes",
    "category": "daily-life",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "basic-communication",
      "daily-life",
      "learning",
      "shopping"
    ],
    "chineseContext": "\u5728\u6536\u94f6\u53f0\u4ed8\u6b3e\u662f\u8d2d\u7269\u7684\u6700\u540e\u6b65\u9aa4\u3002\u793c\u8c8c\u5730\u4e0e\u6536\u94f6\u5458\u4ea4\u6d41\uff01",
    "objectives": [
      "Practice paying at the checkout",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/paying-at-checkout.svg",
    "isPopular": false
  },
  {
    "id": "comparing-prices",
    "title": "Comparing Prices",
    "icon": "💰",
    "description": "Learn to discuss and compare prices when shopping",
    "category": "daily-life",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "shopping",
      "basic-communication",
      "daily-life"
    ],
    "chineseContext": "\u6bd4\u8f83\u4ef7\u683c\u662f\u660e\u667a\u7684\u8d2d\u7269\u65b9\u5f0f\u3002\u5728\u7231\u5c14\u5170\uff0c\u8fd9\u662f\u5f88\u6b63\u5e38\u7684\uff01",
    "objectives": [
      "Practice comparing prices",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/comparing-prices.svg",
    "isPopular": false
  },
  {
    "id": "asking-product-location",
    "title": "Finding Specific Products",
    "icon": "🔍",
    "description": "Learn to ask about specific product locations",
    "category": "daily-life",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "shopping",
      "daily-life",
      "basic-communication"
    ],
    "chineseContext": "\u627e\u7279\u5b9a\u5546\u54c1\u65f6\uff0c\u76f4\u63a5\u8be2\u95ee\u662f\u6700\u6709\u6548\u7684\u65b9\u6cd5\uff01",
    "objectives": [
      "Practice finding specific products",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/asking-product-location.svg",
    "isPopular": false
  },
  {
    "id": "expressing-shopping-needs",
    "title": "Expressing Shopping Needs",
    "icon": "📝",
    "description": "Learn to communicate shopping requirements clearly",
    "category": "daily-life",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "shopping",
      "daily-life",
      "basic-communication"
    ],
    "chineseContext": "\u6e05\u695a\u8868\u8fbe\u8d2d\u7269\u9700\u6c42\u53ef\u4ee5\u5f97\u5230\u66f4\u597d\u7684\u5e2e\u52a9\uff01",
    "objectives": [
      "Practice expressing shopping needs",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/expressing-shopping-needs.svg",
    "isPopular": false
  },
  {
    "id": "polite-shop-interaction",
    "title": "Polite Shopping Interactions",
    "icon": "😊",
    "description": "Learn general courteous behavior in shops",
    "category": "daily-life",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "shopping",
      "daily-life",
      "learning",
      "polite-behavior"
    ],
    "chineseContext": "\u5728\u5546\u5e97\u91cc\u4fdd\u6301\u793c\u8c8c\u4f1a\u8ba9\u8d2d\u7269\u4f53\u9a8c\u66f4\u6109\u5feb\uff01",
    "objectives": [
      "Practice polite shopping interactions",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/polite-shop-interaction.svg",
    "isPopular": false
  },
  {
    "id": "bus-conversation",
    "title": "Talking on Dublin Bus",
    "icon": "🚌",
    "description": "Learn polite conversation on public transport in Dublin",
    "category": "daily-life",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "transport",
      "daily-life",
      "basic-communication",
      "family",
      "polite-behavior"
    ],
    "chineseContext": "\u5728\u90fd\u67cf\u6797\u516c\u4ea4\u8f66\u4e0a\uff0c\u4eba\u4eec\u7ecf\u5e38\u53cb\u597d\u5730\u4ea4\u8c08\u3002\u8fd9\u662f\u7ec3\u4e60\u82f1\u8bed\u7684\u597d\u673a\u4f1a\uff01",
    "objectives": [
      "Practice talking on dublin bus",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/bus-conversation.svg",
    "isPopular": false
  },
  {
    "id": "dart-ticket-purchase",
    "title": "Buying DART Tickets",
    "icon": "🎫",
    "description": "Learn to purchase tickets for Dublin's DART train system",
    "category": "daily-life",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "basic-communication",
      "transport",
      "daily-life"
    ],
    "chineseContext": "\u4e70DART\u7968\u5f88\u7b80\u5355\u3002\u5de5\u4f5c\u4eba\u5458\u4f1a\u5e2e\u52a9\u4f60\u9009\u62e9\u6b63\u786e\u7684\u7968\uff01",
    "objectives": [
      "Practice buying dart tickets",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/dart-ticket-purchase.svg",
    "isPopular": false
  },
  {
    "id": "asking-walking-directions",
    "title": "Asking for Walking Directions",
    "icon": "🗺️",
    "description": "Learn to ask for directions when walking in Dublin",
    "category": "daily-life",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "transport",
      "daily-life",
      "learning",
      "basic-communication"
    ],
    "chineseContext": "\u5728\u90fd\u67cf\u6797\u8ff7\u8def\u65f6\uff0c\u8def\u4eba\u5f88\u4e50\u610f\u7ed9\u4f60\u6307\u8def\u3002\u4e0d\u8981\u72b9\u8c6b\uff01",
    "objectives": [
      "Practice asking for walking directions",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/asking-walking-directions.svg",
    "isPopular": false
  },
  {
    "id": "transport-politeness",
    "title": "Being Polite on Transport",
    "icon": "🚇",
    "description": "Learn general courtesy on Dublin public transport",
    "category": "daily-life",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "transport",
      "daily-life",
      "learning",
      "polite-behavior"
    ],
    "chineseContext": "\u5728\u516c\u5171\u4ea4\u901a\u4e0a\u4fdd\u6301\u793c\u8c8c\u5f88\u91cd\u8981\u3002\u8ba9\u5ea7\u4f4d\u7ed9\u9700\u8981\u7684\u4eba\uff01",
    "objectives": [
      "Practice being polite on transport",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/transport-politeness.svg",
    "isPopular": false
  },
  {
    "id": "home-dinner-conversation",
    "title": "Family Dinner Conversations",
    "icon": "🍚",
    "description": "Learn to participate in family meal discussions",
    "category": "daily-life",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "family",
      "daily-life",
      "learning"
    ],
    "chineseContext": "\u5bb6\u5ead\u665a\u9910\u65f6\u95f4\u662f\u7ec3\u4e60\u82f1\u8bed\u7684\u597d\u673a\u4f1a\u3002\u5206\u4eab\u4f60\u5728\u5b66\u6821\u7684\u7ecf\u5386\uff01",
    "objectives": [
      "Practice family dinner conversations",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/home-dinner-conversation.svg",
    "isPopular": false
  },
  {
    "id": "sibling-play-interaction",
    "title": "Playing with Siblings",
    "icon": "👫",
    "description": "Learn to interact and play with brothers and sisters",
    "category": "daily-life",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "daily-life",
      "playground",
      "basic-communication",
      "learning",
      "family"
    ],
    "chineseContext": "\u548c\u5144\u5f1f\u59d0\u59b9\u4e00\u8d77\u73a9\u53ef\u4ee5\u63d0\u9ad8\u82f1\u8bed\u53e3\u8bed\u3002\u4e00\u8d77\u73a9\u6e38\u620f\u5f88\u6709\u8da3\uff01",
    "objectives": [
      "Practice playing with siblings",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/sibling-play-interaction.svg",
    "isPopular": false
  },
  {
    "id": "family-outing-planning",
    "title": "Planning Family Outings",
    "icon": "🚗",
    "description": "Learn to participate in family trip planning discussions",
    "category": "daily-life",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "family",
      "daily-life",
      "basic-communication"
    ],
    "chineseContext": "\u53c2\u4e0e\u5bb6\u5ead\u51fa\u6e38\u8ba1\u5212\u53ef\u4ee5\u7ec3\u4e60\u8868\u8fbe\u60f3\u6cd5\u3002\u5206\u4eab\u4f60\u60f3\u53bb\u7684\u5730\u65b9\uff01",
    "objectives": [
      "Practice planning family outings",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/family-outing-planning.svg",
    "isPopular": false
  },
  {
    "id": "birthday-party-conversation",
    "title": "Birthday Party Conversations",
    "icon": "🎂",
    "description": "Learn to participate in Irish birthday celebrations",
    "category": "social",
    "ageGroups": [
      "senior-infants",
      "first-class",
      "second-class"
    ],
    "difficulty": "beginner",
    "estimatedTime": "5-8 minutes",
    "tags": [
      "family",
      "friendship",
      "daily-life",
      "social",
      "learning"
    ],
    "chineseContext": "\u7231\u5c14\u5170\u7684\u751f\u65e5\u805a\u4f1a\u5f88\u6709\u8da3\uff01\u5b69\u5b50\u4eec\u559c\u6b22\u4e00\u8d77\u5e86\u795d\u548c\u73a9\u6e38\u620f\u3002",
    "objectives": [
      "Practice birthday party conversations",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/birthday-party-conversation.svg",
    "isPopular": false
  },
  {
    "id": "inviting-friend-over",
    "title": "Inviting Friends to Your Home",
    "icon": "🏠",
    "description": "Learn to invite Irish friends for home visits",
    "category": "social",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "friendship",
      "basic-communication",
      "social",
      "daily-life"
    ],
    "chineseContext": "\u9080\u8bf7\u7231\u5c14\u5170\u670b\u53cb\u5230\u5bb6\u91cc\u6765\u662f\u5f88\u597d\u7684\u53cb\u8c0a\u8868\u73b0\u3002\u4ed6\u4eec\u4f1a\u5f88\u9ad8\u5174\uff01",
    "objectives": [
      "Practice inviting friends to your home",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/inviting-friend-over.svg",
    "isPopular": false
  },
  {
    "id": "sharing-interests",
    "title": "Sharing Your Interests",
    "icon": "🎨",
    "description": "Learn to discuss hobbies and interests with friends",
    "category": "social",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "friendship",
      "social",
      "sharing",
      "basic-communication"
    ],
    "chineseContext": "\u5206\u4eab\u4f60\u7684\u5174\u8da3\u7231\u597d\u53ef\u4ee5\u627e\u5230\u6709\u76f8\u540c\u7231\u597d\u7684\u670b\u53cb\uff01",
    "objectives": [
      "Practice sharing your interests",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/sharing-interests.svg",
    "isPopular": false
  },
  {
    "id": "apologizing-appropriately",
    "title": "Making Appropriate Apologies",
    "icon": "🙏",
    "description": "Learn to apologize sincerely when you make mistakes",
    "category": "social",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "friendship",
      "basic-communication",
      "polite-behavior",
      "social"
    ],
    "chineseContext": "\u9053\u6b49\u662f\u89e3\u51b3\u95ee\u9898\u7684\u91cd\u8981\u65b9\u5f0f\u3002\u771f\u8bda\u7684\u9053\u6b49\u80fd\u4fee\u590d\u53cb\u8c0a\uff01",
    "objectives": [
      "Practice making appropriate apologies",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/apologizing-appropriately.svg",
    "isPopular": false
  },
  {
    "id": "expressing-disagreement-politely",
    "title": "Polite Disagreement",
    "icon": "🤔",
    "description": "Learn to disagree respectfully with friends",
    "category": "social",
    "ageGroups": [
      "second-class",
      "third-class",
      "fourth-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "friendship",
      "learning",
      "social",
      "polite-behavior"
    ],
    "chineseContext": "\u793c\u8c8c\u5730\u8868\u8fbe\u4e0d\u540c\u610f\u89c1\u662f\u6b63\u5e38\u7684\u3002\u670b\u53cb\u4e4b\u95f4\u53ef\u4ee5\u6709\u4e0d\u540c\u770b\u6cd5\uff01",
    "objectives": [
      "Practice polite disagreement",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/expressing-disagreement-politely.svg",
    "isPopular": false
  },
  {
    "id": "community-gathering-participation",
    "title": "Community Gathering Participation",
    "icon": "👥",
    "description": "Learn to participate in local community events",
    "category": "social",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "friendship",
      "social",
      "community",
      "classroom"
    ],
    "chineseContext": "\u53c2\u52a0\u793e\u533a\u6d3b\u52a8\u662f\u878d\u5165\u7231\u5c14\u5170\u793e\u4f1a\u7684\u597d\u65b9\u6cd5\u3002\u5927\u5bb6\u90fd\u5f88\u6b22\u8fce\uff01",
    "objectives": [
      "Practice community gathering participation",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/community-gathering-participation.svg",
    "isPopular": false
  },
  {
    "id": "meeting-new-neighbor",
    "title": "Meeting New Neighbors",
    "icon": "👋",
    "description": "Learn to introduce yourself to neighbors in Dublin",
    "category": "social",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "social",
      "community",
      "friendship",
      "basic-communication"
    ],
    "chineseContext": "\u8ba4\u8bc6\u65b0\u90bb\u5c45\u662f\u5efa\u7acb\u793e\u533a\u5173\u7cfb\u7684\u5f00\u59cb\u3002\u7231\u5c14\u5170\u90bb\u5c45\u5f88\u53cb\u597d\uff01",
    "objectives": [
      "Practice meeting new neighbors",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/meeting-new-neighbor.svg",
    "isPopular": false
  },
  {
    "id": "local-community-event",
    "title": "Local Community Events",
    "icon": "🎪",
    "description": "Learn to engage with local Dublin community activities",
    "category": "social",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "friendship",
      "social",
      "community"
    ],
    "chineseContext": "\u53c2\u52a0\u672c\u5730\u793e\u533a\u6d3b\u52a8\u80fd\u8ba9\u4f60\u66f4\u597d\u5730\u4e86\u89e3\u90fd\u67cf\u6797\u6587\u5316\uff01",
    "objectives": [
      "Practice local community events",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/local-community-event.svg",
    "isPopular": false
  },
  {
    "id": "st-patricks-day-celebration",
    "title": "St. Patrick's Day Celebration",
    "icon": "🍀",
    "description": "Learn to participate in Ireland's national holiday celebration",
    "category": "chinese-culture",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "irish-culture",
      "community"
    ],
    "chineseContext": "\u5723\u5e15\u7279\u91cc\u514b\u8282\u662f\u7231\u5c14\u5170\u6700\u91cd\u8981\u7684\u8282\u65e5\uff01\u4f60\u53ef\u4ee5\u53c2\u52a0\u6e38\u884c\uff0c\u611f\u53d7\u7231\u5c14\u5170\u6587\u5316\u3002",
    "objectives": [
      "Practice st. patrick's day celebration",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/st-patricks-day-celebration.svg",
    "isPopular": false
  },
  {
    "id": "gaa-match-watching",
    "title": "Watching GAA Matches",
    "icon": "🏈",
    "description": "Learn to enjoy Gaelic Athletic Association sports",
    "category": "chinese-culture",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "irish-culture",
      "basic-communication",
      "community"
    ],
    "chineseContext": "\u89c2\u770bGAA\u6bd4\u8d5b\u662f\u4f53\u9a8c\u7231\u5c14\u5170\u4f20\u7edf\u4f53\u80b2\u7684\u597d\u65b9\u5f0f\u3002\u8fd9\u662f\u7231\u5c14\u5170\u72ec\u6709\u7684\u8fd0\u52a8\uff01",
    "objectives": [
      "Practice watching gaa matches",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/gaa-match-watching.svg",
    "isPopular": false
  },
  {
    "id": "irish-traditional-music-event",
    "title": "Irish Traditional Music Events",
    "icon": "🎵",
    "description": "Learn to appreciate and discuss Irish traditional music",
    "category": "chinese-culture",
    "ageGroups": [
      "second-class",
      "third-class",
      "fourth-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "irish-culture",
      "learning",
      "community"
    ],
    "chineseContext": "\u7231\u5c14\u5170\u4f20\u7edf\u97f3\u4e50\u5f88\u7f8e\u5999\uff01\u542c\u8fd9\u4e9b\u97f3\u4e50\u53ef\u4ee5\u66f4\u597d\u5730\u7406\u89e3\u7231\u5c14\u5170\u6587\u5316\u3002",
    "objectives": [
      "Practice irish traditional music events",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/irish-traditional-music-event.svg",
    "isPopular": false
  },
  {
    "id": "irish-dancing-participation",
    "title": "Irish Dancing Participation",
    "icon": "💃",
    "description": "Learn to participate in or appreciate Irish dancing",
    "category": "chinese-culture",
    "ageGroups": [
      "first-class",
      "second-class",
      "third-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "irish-culture",
      "classroom",
      "community"
    ],
    "chineseContext": "\u7231\u5c14\u5170\u821e\u8e48\u5f88\u6709\u8da3\uff01\u5373\u4f7f\u4f60\u4e0d\u4f1a\u8df3\uff0c\u89c2\u770b\u4e5f\u5f88\u6709\u610f\u601d\u3002",
    "objectives": [
      "Practice irish dancing participation",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/irish-dancing-participation.svg",
    "isPopular": false
  },
  {
    "id": "dublin-heritage-visit",
    "title": "Visiting Dublin Heritage Sites",
    "icon": "🏰",
    "description": "Learn to appreciate Dublin's historical and cultural heritage",
    "category": "chinese-culture",
    "ageGroups": [
      "second-class",
      "third-class",
      "fourth-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "transport",
      "learning",
      "irish-culture",
      "chinese-culture",
      "basic-communication",
      "community"
    ],
    "chineseContext": "\u53c2\u89c2\u90fd\u67cf\u6797\u5386\u53f2\u9057\u8ff9\u53ef\u4ee5\u4e86\u89e3\u7231\u5c14\u5170\u7684\u5386\u53f2\u548c\u6587\u5316\uff01",
    "objectives": [
      "Practice visiting dublin heritage sites",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/dublin-heritage-visit.svg",
    "isPopular": false
  },
  {
    "id": "sharing-chinese-culture",
    "title": "Sharing Your Chinese Culture",
    "icon": "🏮",
    "description": "Learn to proudly share Chinese traditions with Irish friends",
    "category": "chinese-culture",
    "ageGroups": [
      "second-class",
      "third-class",
      "fourth-class"
    ],
    "difficulty": "intermediate",
    "estimatedTime": "8-12 minutes",
    "tags": [
      "friendship",
      "learning",
      "chinese-culture",
      "sharing",
      "irish-culture",
      "basic-communication",
      "community"
    ],
    "chineseContext": "\u5206\u4eab\u4e2d\u56fd\u6587\u5316\u662f\u5f88\u7f8e\u597d\u7684\u4e8b\u60c5\uff01\u7231\u5c14\u5170\u670b\u53cb\u4eec\u5f88\u60f3\u4e86\u89e3\u4e2d\u56fd\u7684\u4f20\u7edf\u3002",
    "objectives": [
      "Practice sharing your chinese culture",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/sharing-chinese-culture.svg",
    "isPopular": false
  },
  {
    "id": "explaining-chinese-holiday",
    "title": "Explaining Chinese Holidays",
    "icon": "🧧",
    "description": "Learn to explain Chinese festivals and traditions to Irish friends",
    "category": "chinese-culture",
    "ageGroups": [
      "third-class",
      "fourth-class"
    ],
    "difficulty": "learning",
    "estimatedTime": "12-20 minutes",
    "tags": [
      "friendship",
      "learning",
      "basic-communication",
      "chinese-culture",
      "irish-culture",
      "community"
    ],
    "chineseContext": "\u5411\u7231\u5c14\u5170\u670b\u53cb\u89e3\u91ca\u4e2d\u56fd\u8282\u65e5\u662f\u5f88\u597d\u7684\u6587\u5316\u4ea4\u6d41\u673a\u4f1a\uff01",
    "objectives": [
      "Practice explaining chinese holidays",
      "Use appropriate Irish English phrases",
      "Build confidence in social situations",
      "Learn cultural context"
    ],
    "thumbnail": "/images/scenarios/explaining-chinese-holiday.svg",
    "isPopular": false
  }
];

// Helper functions for filtering
export const getScenariosByCategory = (category) => {
  return mockScenarios.filter(scenario => scenario.category === category);
};

export const getScenariosByAgeGroup = (ageGroup) => {
  return mockScenarios.filter(scenario => scenario.ageGroups.includes(ageGroup));
};

export const getScenariosByDifficulty = (difficulty) => {
  return mockScenarios.filter(scenario => scenario.difficulty === difficulty);
};

export const getPopularScenarios = () => {
  return mockScenarios.filter(scenario => scenario.isPopular);
};

export const searchScenarios = (query) => {
  if (!query.trim()) return mockScenarios;
  
  const lowercaseQuery = query.toLowerCase();
  return mockScenarios.filter(scenario =>
    scenario.title.toLowerCase().includes(lowercaseQuery) ||
    scenario.description.toLowerCase().includes(lowercaseQuery) ||
    scenario.tags.some(tag => tag.toLowerCase().includes(lowercaseQuery))
  );
};

export const filterScenariosByTags = (tags) => {
  if (!tags.length) return mockScenarios;
  
  return mockScenarios.filter(scenario =>
    tags.some(tag => scenario.tags.includes(tag))
  );
};

// Get all unique tags for filter UI
export const getAllTags = () => {
  const allTags = mockScenarios.flatMap(scenario => scenario.tags);
  return [...new Set(allTags)].sort();
};

// Enhance scenarios with transcript information
export const enhanceScenariosWithTranscripts = (scenarios) => {
  return scenarios.map(scenario => {
    try {
      const transcriptStats = getTranscriptStats(scenario.id);
      return {
        ...scenario,
        transcriptStats,
        hasTranscripts: transcriptStats.totalTranscripts > 0
      };
    } catch (error) {
      console.warn(`Failed to get transcript stats for scenario ${scenario.id}:`, error);
      return {
        ...scenario,
        transcriptStats: { totalTranscripts: 0, ageGroups: [], variants: [] },
        hasTranscripts: false
      };
    }
  });
};

// Get scenarios with transcript information
export const getScenariosWithTranscripts = () => {
  return enhanceScenariosWithTranscripts(mockScenarios);
};
