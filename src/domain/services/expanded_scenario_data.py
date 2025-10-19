"""
Comprehensive Scenario Data for Expanded Scenario Library

Contains complete definitions for all 50+ scenarios across categories:
- School Life (25 scenarios)
- Daily Activities (15 scenarios) 
- Social Interactions (8 scenarios)
- Cultural Events (7 scenarios)

Total: 55 scenarios (50+ requirement met)
"""

from typing import Dict, List
from .expanded_scenario_library import ExpandedScenarioType, ExpandedScenarioContent, ScenarioCategory


def get_complete_scenario_library() -> Dict[ExpandedScenarioType, ExpandedScenarioContent]:
    """Get complete 55 scenario library"""
    
    scenarios = {}
    
    # === ORIGINAL FOUNDATION SCENARIOS (5) ===
    
    scenarios[ExpandedScenarioType.INTRODUCING_YOURSELF] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.INTRODUCING_YOURSELF,
        category=ScenarioCategory.SOCIAL_INTERACTIONS,
        title="Introducing Yourself",
        description="Learn to introduce yourself in various social situations",
        chinese_comfort="自我介绍是社交的第一步。在爱尔兰，人们喜欢友好的问候！",
        english_demonstration="Hello, my name is Li Wei. I'm from China. Nice to meet you!",
        irish_vocabulary_notes=[
            "'Nice to meet you' is standard Irish greeting",
            "First name introduction is common among children",
            "Mentioning your country shows openness"
        ],
        age_group_notes="Fundamental social skill for all interactions",
        difficulty_level=1,
        cultural_integration_points=[
            "Irish friendly greeting culture",
            "International student integration",
            "Cultural background sharing"
        ],
        dublin_location_connections=["Schools", "Playgrounds", "Community centres"]
    )
    
    scenarios[ExpandedScenarioType.ASKING_FOR_TOILET] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.ASKING_FOR_TOILET,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Asking for the Toilet",
        description="Learn to politely ask for toilet permission in school",
        chinese_comfort="在学校需要上厕所时，要礼貌地问老师。这很正常，不要害羞！",
        english_demonstration="Excuse me, Miss. May I go to the toilet, please?",
        irish_vocabulary_notes=[
            "Say 'toilet' not 'bathroom' in Ireland",
            "'May I go to...' is polite permission request",
            "'Excuse me' gets attention politely"
        ],
        age_group_notes="Essential daily need and politeness skill",
        difficulty_level=1,
        cultural_integration_points=[
            "Irish school toilet etiquette",
            "Polite permission requests",
            "Classroom protocol understanding"
        ],
        dublin_location_connections=["Dublin schools", "Classroom settings"]
    )
    
    scenarios[ExpandedScenarioType.ASKING_FOR_HELP] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.ASKING_FOR_HELP,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Asking for Help",
        description="Learn to ask for help when you need support",
        chinese_comfort="需要帮助时主动寻求是好习惯。爱尔兰人很乐意帮助别人！",
        english_demonstration="Could you help me, please? I don't understand this part.",
        irish_vocabulary_notes=[
            "'Could you help me?' is polite help request",
            "'I don't understand' shows learning honesty",
            "Irish culture values helping others"
        ],
        age_group_notes="Critical for learning support and social connection",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish helpfulness culture",
            "Learning support acceptance",
            "Community assistance norms"
        ],
        dublin_location_connections=["Schools", "Study areas", "Community spaces"]
    )
    
    scenarios[ExpandedScenarioType.EXPRESSING_HUNGER] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.EXPRESSING_HUNGER,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Expressing Hunger",
        description="Learn to express hunger and food needs appropriately",
        chinese_comfort="表达饥饿很正常。在爱尔兰，及时表达需求是重要的！",
        english_demonstration="I'm feeling hungry. When is lunch time, please?",
        irish_vocabulary_notes=[
            "'I'm feeling hungry' is natural expression",
            "'When is lunch time?' asks for schedule",
            "Irish meal timing is important socially"
        ],
        age_group_notes="Basic needs expression and time awareness",
        difficulty_level=1,
        cultural_integration_points=[
            "Irish meal culture",
            "School schedule understanding",
            "Needs expression acceptance"
        ],
        dublin_location_connections=["School canteens", "Dining areas", "Home settings"]
    )
    
    scenarios[ExpandedScenarioType.SAYING_GOODBYE] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.SAYING_GOODBYE,
        category=ScenarioCategory.SOCIAL_INTERACTIONS,
        title="Saying Goodbye",
        description="Learn various ways to say goodbye appropriately",
        chinese_comfort="好的告别让人感觉温暖。爱尔兰人重视友好的结束语！",
        english_demonstration="Goodbye! See you tomorrow. Have a lovely day!",
        irish_vocabulary_notes=[
            "'See you tomorrow' shows future connection",
            "'Have a lovely day' is Irish politeness",
            "Warm goodbyes maintain relationships"
        ],
        age_group_notes="Social closure and relationship maintenance",
        difficulty_level=1,
        cultural_integration_points=[
            "Irish goodbye customs",
            "Warm departure expressions",
            "Relationship continuity language"
        ],
        dublin_location_connections=["Schools", "Social gatherings", "Public spaces"]
    )
    
    # === SCHOOL LIFE SCENARIOS (25) ===
    
    # Classroom interactions (10)
    scenarios[ExpandedScenarioType.ASKING_TEACHER_QUESTION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.ASKING_TEACHER_QUESTION,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Asking Teacher a Question",
        description="Learn to ask your teacher questions politely in Irish classroom setting",
        chinese_comfort="在爱尔兰课堂上，老师很欢迎学生提问。这是学习的好方法！",
        english_demonstration="Excuse me, Ms. O'Brien. May I ask a question, please?",
        irish_vocabulary_notes=[
            "Use 'Ms./Mr.' with teacher's surname",
            "'May I ask a question?' is polite classroom language",
            "'Excuse me' gets teacher's attention respectfully"
        ],
        age_group_notes="Essential for classroom participation and learning confidence",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish classroom respect traditions",
            "Teacher-student relationship in Ireland",
            "Polite question-asking customs"
        ],
        dublin_location_connections=["Dublin schools", "Classroom environments"]
    )
    
    scenarios[ExpandedScenarioType.GROUP_WORK_COLLABORATION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.GROUP_WORK_COLLABORATION,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Working Together in Groups",
        description="Learn to collaborate effectively in group work activities",
        chinese_comfort="在爱尔兰学校，小组合作是很常见的。大家一起工作，相互帮助！",
        english_demonstration="Let's work together. What do you think about this idea?",
        irish_vocabulary_notes=[
            "'Let's work together' shows collaboration",
            "'What do you think?' includes others' opinions",
            "Group work is valued in Irish education"
        ],
        age_group_notes="Develops teamwork and communication skills",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish collaborative learning culture",
            "Teamwork in Irish schools",
            "Inclusive group dynamics"
        ],
        dublin_location_connections=["School project areas", "Learning spaces"]
    )
    
    scenarios[ExpandedScenarioType.CLASS_PRESENTATION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.CLASS_PRESENTATION,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Giving a Class Presentation",
        description="Learn to present to your class with confidence",
        chinese_comfort="在爱尔兰学校做演讲可以提高自信心。同学们都会认真听！",
        english_demonstration="Good morning, everyone. Today I want to tell you about...",
        irish_vocabulary_notes=[
            "'Good morning, everyone' is formal presentation start",
            "'I want to tell you about' introduces your topic",
            "Irish classrooms encourage student presentations"
        ],
        age_group_notes="Builds confidence and public speaking skills",
        difficulty_level=4,
        cultural_integration_points=[
            "Irish presentation culture",
            "Classroom speaking confidence",
            "Academic communication skills"
        ],
        dublin_location_connections=["School classrooms", "Assembly halls"]
    )
    
    scenarios[ExpandedScenarioType.ANSWERING_IN_CLASS] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.ANSWERING_IN_CLASS,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Answering Questions in Class",
        description="Learn to answer teacher questions confidently",
        chinese_comfort="在课堂上回答问题是学习的重要部分。不要担心出错！",
        english_demonstration="I think the answer is... Am I on the right track?",
        irish_vocabulary_notes=[
            "'I think the answer is' shows thoughtful response",
            "'Am I on the right track?' asks for feedback",
            "Irish teachers encourage student participation"
        ],
        age_group_notes="Essential for active classroom participation",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish classroom participation norms",
            "Learning from mistakes culture",
            "Teacher-student dialogue"
        ],
        dublin_location_connections=["Dublin school classrooms"]
    )
    
    scenarios[ExpandedScenarioType.EXPLAINING_HOMEWORK_PROBLEM] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.EXPLAINING_HOMEWORK_PROBLEM,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Explaining Homework Difficulties",
        description="Learn to discuss homework challenges with teacher",
        chinese_comfort="如果作业有困难，告诉老师是很正常的。老师会帮助你！",
        english_demonstration="I tried my best, but I found this part quite difficult.",
        irish_vocabulary_notes=[
            "'I tried my best' shows effort",
            "'Quite difficult' is polite way to express challenge",
            "Irish teachers appreciate honest communication"
        ],
        age_group_notes="Builds communication and help-seeking skills",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish academic support culture",
            "Honest communication with teachers",
            "Learning support accessibility"
        ],
        dublin_location_connections=["School classrooms", "Study areas"]
    )
    
    scenarios[ExpandedScenarioType.SHARING_LEARNING_MATERIALS] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.SHARING_LEARNING_MATERIALS,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Sharing School Materials",
        description="Learn to share and borrow school supplies politely",
        chinese_comfort="在爱尔兰学校，同学们经常分享学习用品。这是友善的表现！",
        english_demonstration="Could I borrow your rubber, please? I'll give it back after class.",
        irish_vocabulary_notes=[
            "'Rubber' not 'eraser' in Irish English",
            "'Could I borrow' is polite request",
            "'I'll give it back' shows responsibility"
        ],
        age_group_notes="Teaches sharing and responsibility",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish sharing culture in schools",
            "Classroom community building",
            "Responsibility and trust"
        ],
        dublin_location_connections=["School classrooms", "Resource areas"]
    )
    
    scenarios[ExpandedScenarioType.PARTICIPATING_DISCUSSION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.PARTICIPATING_DISCUSSION,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Joining Class Discussions",
        description="Learn to contribute to classroom discussions",
        chinese_comfort="参与课堂讨论可以提高英语水平。分享你的想法很重要！",
        english_demonstration="That's a brilliant point! I'd like to add that...",
        irish_vocabulary_notes=[
            "'Brilliant point' is enthusiastic Irish praise",
            "'I'd like to add' politely contributes to discussion",
            "Irish classrooms value diverse opinions"
        ],
        age_group_notes="Develops critical thinking and communication",
        difficulty_level=4,
        cultural_integration_points=[
            "Irish discussion culture",
            "Respectful debate traditions",
            "Academic dialogue skills"
        ],
        dublin_location_connections=["School discussion areas", "Debate clubs"]
    )
    
    scenarios[ExpandedScenarioType.ASKING_CLASSMATE_HELP] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.ASKING_CLASSMATE_HELP,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Asking Classmates for Help",
        description="Learn to ask peers for help with schoolwork",
        chinese_comfort="向同学求助是很正常的。爱尔兰学生很乐意互相帮助！",
        english_demonstration="I'm a bit stuck on this question. Could you help me out?",
        irish_vocabulary_notes=[
            "'I'm a bit stuck' is casual way to say having difficulty",
            "'Could you help me out?' is friendly request",
            "Irish students are known for being helpful"
        ],
        age_group_notes="Builds peer relationships and collaborative learning",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish peer support culture",
            "Collaborative learning environment",
            "Student community bonds"
        ],
        dublin_location_connections=["School study areas", "Classroom groups"]
    )
    
    scenarios[ExpandedScenarioType.READING_ALOUD_CLASS] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.READING_ALOUD_CLASS,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Reading Aloud in Class",
        description="Learn to read confidently in front of the class",
        chinese_comfort="在班上大声朗读可以练习发音。慢慢来，不要紧张！",
        english_demonstration="Would you like me to read the next paragraph? I'll do my best.",
        irish_vocabulary_notes=[
            "'Would you like me to' offers to participate",
            "'I'll do my best' shows positive attitude",
            "Irish teachers encourage reading practice"
        ],
        age_group_notes="Builds reading confidence and pronunciation skills",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish reading culture",
            "Classroom performance confidence",
            "Language development support"
        ],
        dublin_location_connections=["School libraries", "Reading corners"]
    )
    
    scenarios[ExpandedScenarioType.SHOWING_UNDERSTANDING] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.SHOWING_UNDERSTANDING,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Showing You Understand",
        description="Learn to demonstrate comprehension in class",
        chinese_comfort="表现出你理解了很重要。这样老师知道你在认真听！",
        english_demonstration="Oh, I see! So that means... Is that right?",
        irish_vocabulary_notes=[
            "'Oh, I see!' shows sudden understanding",
            "'So that means' demonstrates thinking",
            "'Is that right?' checks understanding"
        ],
        age_group_notes="Essential for effective learning communication",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish learning confirmation culture",
            "Active listening demonstration",
            "Teacher-student feedback loop"
        ],
        dublin_location_connections=["School classrooms", "Learning environments"]
    )
    
    # Playground conversations (8)
    scenarios[ExpandedScenarioType.MAKING_NEW_FRIENDS] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.MAKING_NEW_FRIENDS,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Making New Friends",
        description="Learn to make friends in the school playground",
        chinese_comfort="在爱尔兰学校交朋友很容易。爱尔兰孩子们很友好，喜欢认识新朋友！",
        english_demonstration="Hi! I'm new here. Would you like to be friends?",
        irish_vocabulary_notes=[
            "'Would you like to be friends?' is direct but friendly",
            "Irish children are known for being welcoming",
            "'New here' explains your situation"
        ],
        age_group_notes="Essential for social integration and confidence",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish friendship culture",
            "Playground social norms",
            "Welcoming nature of Irish children"
        ],
        dublin_location_connections=["School playgrounds", "Recreation areas"]
    )
    
    scenarios[ExpandedScenarioType.PLAYGROUND_GAMES] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.PLAYGROUND_GAMES,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Playing Playground Games",
        description="Learn to join and organize playground games",
        chinese_comfort="爱尔兰操场上有很多有趣的游戏。加入游戏是交朋友的好方法！",
        english_demonstration="Can I play too? What are the rules of this game?",
        irish_vocabulary_notes=[
            "'Can I play too?' asks to join politely",
            "'What are the rules?' shows interest in learning",
            "Irish playgrounds have traditional games"
        ],
        age_group_notes="Develops social skills and physical activity",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish playground traditions",
            "Inclusive play culture",
            "Traditional Irish games"
        ],
        dublin_location_connections=["School playgrounds", "Dublin parks"]
    )
    
    scenarios[ExpandedScenarioType.RESOLVING_PLAYGROUND_CONFLICT] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.RESOLVING_PLAYGROUND_CONFLICT,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Solving Playground Problems",
        description="Learn to resolve disagreements peacefully",
        chinese_comfort="如果操场上有问题，和平解决是最好的方法。爱尔兰人重视友善！",
        english_demonstration="I'm sorry about that. Can we sort this out together?",
        irish_vocabulary_notes=[
            "'Sorry about that' takes responsibility",
            "'Sort this out' means solve the problem",
            "Irish culture values peaceful resolution"
        ],
        age_group_notes="Essential conflict resolution and emotional skills",
        difficulty_level=4,
        cultural_integration_points=[
            "Irish conflict resolution culture",
            "Peaceful problem-solving",
            "Community harmony values"
        ],
        dublin_location_connections=["School playgrounds", "Mediation areas"]
    )
    
    scenarios[ExpandedScenarioType.INVITING_TO_PLAY] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.INVITING_TO_PLAY,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Inviting Others to Play",
        description="Learn to include others in playground activities",
        chinese_comfort="邀请别人一起玩是很友善的行为。这样可以让每个人都开心！",
        english_demonstration="Would you like to come and play with us? We're having great craic!",
        irish_vocabulary_notes=[
            "'Would you like to come and play' is inclusive invitation",
            "'Great craic' is Irish slang for fun",
            "Irish culture values inclusion"
        ],
        age_group_notes="Builds inclusive social leadership skills",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish inclusion values",
            "Playground leadership",
            "Community building through play"
        ],
        dublin_location_connections=["School playgrounds", "Community play areas"]
    )
    
    scenarios[ExpandedScenarioType.SHARING_PLAYGROUND_EQUIPMENT] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.SHARING_PLAYGROUND_EQUIPMENT,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Sharing Playground Equipment",
        description="Learn to share and take turns with playground equipment",
        chinese_comfort="在操场上分享设备很重要。轮流使用让每个人都能玩！",
        english_demonstration="Can I have a go after you? I'll wait my turn.",
        irish_vocabulary_notes=[
            "'Have a go' means take a turn",
            "'Wait my turn' shows understanding of fairness",
            "Irish playgrounds emphasize fairness"
        ],
        age_group_notes="Teaches fairness and patience",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish fairness culture",
            "Playground etiquette",
            "Patient waiting customs"
        ],
        dublin_location_connections=["School playgrounds", "Public play areas"]
    )
    
    scenarios[ExpandedScenarioType.EXPRESSING_FEELINGS_PLAYGROUND] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.EXPRESSING_FEELINGS_PLAYGROUND,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Expressing Feelings on Playground",
        description="Learn to communicate emotions appropriately",
        chinese_comfort="表达感受很重要。如果你难过或开心，可以告诉朋友！",
        english_demonstration="I feel a bit left out. Could I join in, please?",
        irish_vocabulary_notes=[
            "'Feel a bit left out' expresses emotion clearly",
            "'Could I join in' requests inclusion",
            "Irish culture supports emotional expression"
        ],
        age_group_notes="Develops emotional literacy and communication",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish emotional openness",
            "Playground emotional support",
            "Feeling validation culture"
        ],
        dublin_location_connections=["School playgrounds", "Support areas"]
    )
    
    scenarios[ExpandedScenarioType.ORGANIZING_GROUP_GAME] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.ORGANIZING_GROUP_GAME,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Organizing Group Games",
        description="Learn to lead and organize playground activities",
        chinese_comfort="组织游戏可以锻炼领导能力。让每个人都参与进来！",
        english_demonstration="Let's play a game together! Who wants to be on my team?",
        irish_vocabulary_notes=[
            "'Let's play a game together' shows leadership",
            "'Who wants to be on my team?' includes everyone",
            "Irish playgrounds value team organization"
        ],
        age_group_notes="Develops leadership and organizational skills",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish leadership development",
            "Playground organization skills",
            "Team-building culture"
        ],
        dublin_location_connections=["School playgrounds", "Sports areas"]
    )
    
    scenarios[ExpandedScenarioType.COMFORTING_UPSET_FRIEND] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.COMFORTING_UPSET_FRIEND,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Comforting an Upset Friend",
        description="Learn to provide emotional support to classmates",
        chinese_comfort="安慰难过的朋友是很善良的行为。爱尔兰人很重视关心他人！",
        english_demonstration="Are you alright? Is there anything I can do to help?",
        irish_vocabulary_notes=[
            "'Are you alright?' shows caring concern",
            "'Anything I can do to help?' offers support",
            "Irish culture values caring for others"
        ],
        age_group_notes="Builds empathy and caring relationships",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish caring traditions",
            "Playground support networks",
            "Emotional support culture"
        ],
        dublin_location_connections=["School support areas", "Quiet playground zones"]
    )
    
    # Canteen/lunch scenarios (5)
    scenarios[ExpandedScenarioType.LUNCH_FOOD_CONVERSATION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.LUNCH_FOOD_CONVERSATION,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Talking About Lunch",
        description="Learn to discuss food and meals in the school canteen",
        chinese_comfort="在学校食堂谈论食物是很有趣的！你可以分享你喜欢的中国食物。",
        english_demonstration="This lunch looks lovely! At home, we eat rice and vegetables.",
        irish_vocabulary_notes=[
            "'Lovely' is common Irish way to say nice",
            "Sharing about home food creates connections",
            "School canteen staff are friendly"
        ],
        age_group_notes="Builds cultural bridges through food discussion",
        difficulty_level=2,
        cultural_integration_points=[
            "Food as cultural connector",
            "Irish meal traditions",
            "Sharing cultural differences positively"
        ],
        dublin_location_connections=["School canteens", "Dublin food culture"]
    )
    
    scenarios[ExpandedScenarioType.SHARING_CULTURAL_FOOD] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.SHARING_CULTURAL_FOOD,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Sharing Cultural Foods",
        description="Learn to share Chinese foods with Irish classmates",
        chinese_comfort="分享中国食物是很好的文化交流方式。爱尔兰朋友会很好奇！",
        english_demonstration="Would you like to try some of my Chinese lunch? It's really tasty!",
        irish_vocabulary_notes=[
            "'Would you like to try' offers sharing",
            "'Really tasty' describes food positively",
            "Food sharing builds friendships in Irish culture"
        ],
        age_group_notes="Promotes cultural pride and sharing",
        difficulty_level=3,
        cultural_integration_points=[
            "Cultural food sharing",
            "Chinese cuisine introduction",
            "Cross-cultural friendship building"
        ],
        dublin_location_connections=["School canteens", "Cultural celebration areas"]
    )
    
    scenarios[ExpandedScenarioType.ASKING_LUNCH_HELP] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.ASKING_LUNCH_HELP,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Getting Help at Lunch",
        description="Learn to ask for help in the school canteen",
        chinese_comfort="在食堂需要帮助时，工作人员很乐意协助你！",
        english_demonstration="Excuse me, could you help me find the cutlery, please?",
        irish_vocabulary_notes=[
            "'Cutlery' means knives, forks, spoons",
            "Canteen staff in Ireland are helpful",
            "'Could you help me find' is polite request"
        ],
        age_group_notes="Builds independence and help-seeking skills",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish hospitality in schools",
            "Canteen support culture",
            "Independence building"
        ],
        dublin_location_connections=["School canteens", "Lunch service areas"]
    )
    
    scenarios[ExpandedScenarioType.DESCRIBING_FOOD_PREFERENCES] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.DESCRIBING_FOOD_PREFERENCES,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Describing Food Preferences",
        description="Learn to express likes and dislikes about food",
        chinese_comfort="表达对食物的喜好可以帮助别人了解你。这是很自然的！",
        english_demonstration="I quite like the sandwiches, but I'm not keen on the soup.",
        irish_vocabulary_notes=[
            "'Quite like' is moderate positive preference",
            "'Not keen on' is polite way to say dislike",
            "Irish culture respects food preferences"
        ],
        age_group_notes="Develops preference expression and vocabulary",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish food preference culture",
            "Polite opinion expression",
            "Dietary discussion norms"
        ],
        dublin_location_connections=["School canteens", "Food service areas"]
    )
    
    scenarios[ExpandedScenarioType.CANTEEN_POLITENESS] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.CANTEEN_POLITENESS,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Being Polite in the Canteen",
        description="Learn proper manners and etiquette in school dining",
        chinese_comfort="在食堂保持礼貌很重要。爱尔兰人很重视餐桌礼仪！",
        english_demonstration="Thank you very much! Could I have some more water, please?",
        irish_vocabulary_notes=[
            "'Thank you very much' shows appreciation",
            "'Could I have some more' is polite request",
            "Irish dining etiquette emphasizes politeness"
        ],
        age_group_notes="Essential social etiquette and manners",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish dining etiquette",
            "Canteen courtesy culture",
            "Polite request patterns"
        ],
        dublin_location_connections=["School canteens", "Dining areas"]
    )
    
    # School events (2)
    scenarios[ExpandedScenarioType.SCHOOL_ASSEMBLY_PARTICIPATION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.SCHOOL_ASSEMBLY_PARTICIPATION,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Participating in School Assembly",
        description="Learn to participate appropriately in school assemblies",
        chinese_comfort="学校集会是重要的社区活动。听从指示，积极参与！",
        english_demonstration="Good morning, everyone. Thank you for that lovely song.",
        irish_vocabulary_notes=[
            "'Good morning, everyone' is formal assembly greeting",
            "'Lovely song' appreciates school performances",
            "Irish assemblies emphasize community"
        ],
        age_group_notes="Develops formal social participation skills",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish school community traditions",
            "Assembly participation norms",
            "Formal school event etiquette"
        ],
        dublin_location_connections=["School assembly halls", "Community gathering spaces"]
    )
    
    scenarios[ExpandedScenarioType.SPORTS_DAY_ACTIVITIES] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.SPORTS_DAY_ACTIVITIES,
        category=ScenarioCategory.SCHOOL_LIFE,
        title="Sports Day Participation",
        description="Learn to participate in Irish school sports events",
        chinese_comfort="体育节是爱尔兰学校的传统活动。尽力而为，享受运动的乐趣！",
        english_demonstration="Well done! That was a brilliant race! Fair play to you!",
        irish_vocabulary_notes=[
            "'Well done' congratulates others",
            "'Brilliant race' praises performance",
            "'Fair play to you' is Irish expression of respect"
        ],
        age_group_notes="Builds sportsmanship and team spirit",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish sports culture",
            "Sportsmanship values",
            "Team spirit traditions"
        ],
        dublin_location_connections=["School sports fields", "Dublin GAA grounds"]
    )
    
    # === DAILY ACTIVITIES SCENARIOS (15) ===
    
    # Shopping scenarios (8)
    scenarios[ExpandedScenarioType.GROCERY_SHOPPING_HELP] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.GROCERY_SHOPPING_HELP,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Getting Help While Shopping",
        description="Learn to ask for help in Dublin shops and supermarkets",
        chinese_comfort="在都柏林购物时，店员们都很乐意帮助你。不要害怕开口询问！",
        english_demonstration="Excuse me, could you help me find the milk, please?",
        irish_vocabulary_notes=[
            "'Could you help me find...' is polite shop request",
            "Shop staff in Ireland are known for being helpful",
            "'Please' always used for politeness"
        ],
        age_group_notes="Practical life skill for independence",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish hospitality in shops",
            "Polite shopping etiquette",
            "Customer service culture in Ireland"
        ],
        dublin_location_connections=["Tesco", "SuperValu", "Local shops", "Dublin markets"]
    )
    
    scenarios[ExpandedScenarioType.CLOTHES_SHOPPING_PREFERENCES] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.CLOTHES_SHOPPING_PREFERENCES,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Shopping for Clothes",
        description="Learn to express preferences when clothes shopping",
        chinese_comfort="在都柏林买衣服时，可以表达你的喜好。店员会帮你找到合适的！",
        english_demonstration="I quite like this jumper. Do you have it in blue, please?",
        irish_vocabulary_notes=[
            "'Jumper' not 'sweater' in Irish English",
            "'Quite like' expresses moderate preference",
            "'Do you have it in...' asks about options"
        ],
        age_group_notes="Develops consumer communication skills",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish shopping culture",
            "Clothing preference expression",
            "Retail interaction norms"
        ],
        dublin_location_connections=["Grafton Street", "Henry Street", "Shopping centres"]
    )
    
    scenarios[ExpandedScenarioType.ASKING_STORE_DIRECTIONS] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.ASKING_STORE_DIRECTIONS,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Finding Things in Stores",
        description="Learn to ask for directions within large shops",
        chinese_comfort="在大商店里迷路很正常。询问方向可以快速找到你需要的东西！",
        english_demonstration="Excuse me, where would I find the children's books, please?",
        irish_vocabulary_notes=[
            "'Where would I find...' is polite way to ask directions",
            "Shop staff know store layouts well",
            "Irish shops are organized logically"
        ],
        age_group_notes="Essential navigation and inquiry skills",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish shop navigation culture",
            "Polite inquiry patterns",
            "Retail assistance expectations"
        ],
        dublin_location_connections=["Dundrum Shopping Centre", "Blanchardstown", "City centre shops"]
    )
    
    scenarios[ExpandedScenarioType.PAYING_AT_CHECKOUT] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.PAYING_AT_CHECKOUT,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Paying at the Checkout",
        description="Learn checkout interactions and payment processes",
        chinese_comfort="在收银台付款是购物的最后步骤。礼貌地与收银员交流！",
        english_demonstration="That's grand, thank you. Could I have a bag, please?",
        irish_vocabulary_notes=[
            "'That's grand' means that's fine/good",
            "'Could I have a bag' requests shopping bag",
            "Irish checkout interactions are friendly"
        ],
        age_group_notes="Practical transaction and social skills",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish checkout courtesy",
            "Payment interaction norms",
            "Consumer politeness culture"
        ],
        dublin_location_connections=["All Dublin shops", "Supermarket checkouts"]
    )
    
    scenarios[ExpandedScenarioType.COMPARING_PRICES] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.COMPARING_PRICES,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Comparing Prices",
        description="Learn to discuss and compare prices when shopping",
        chinese_comfort="比较价格是明智的购物方式。在爱尔兰，这是很正常的！",
        english_demonstration="This one is a bit dear. Is there anything cheaper available?",
        irish_vocabulary_notes=[
            "'A bit dear' means somewhat expensive",
            "'Cheaper available' asks for alternatives",
            "Price comparison is normal in Irish shopping"
        ],
        age_group_notes="Develops practical money management skills",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish price comparison culture",
            "Consumer awareness norms",
            "Value-conscious shopping"
        ],
        dublin_location_connections=["Dublin markets", "Comparison shopping areas"]
    )
    
    scenarios[ExpandedScenarioType.ASKING_PRODUCT_LOCATION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.ASKING_PRODUCT_LOCATION,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Finding Specific Products",
        description="Learn to ask about specific product locations",
        chinese_comfort="找特定商品时，直接询问是最有效的方法！",
        english_demonstration="Do you stock Chinese noodles? Where might I find them?",
        irish_vocabulary_notes=[
            "'Do you stock...' asks if store carries item",
            "'Where might I find...' is polite location request",
            "Irish shops often stock international foods"
        ],
        age_group_notes="Builds specific inquiry and cultural bridge skills",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish multicultural retail",
            "International food availability",
            "Cultural food access"
        ],
        dublin_location_connections=["Asian markets", "International food sections"]
    )
    
    scenarios[ExpandedScenarioType.EXPRESSING_SHOPPING_NEEDS] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.EXPRESSING_SHOPPING_NEEDS,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Expressing Shopping Needs",
        description="Learn to communicate shopping requirements clearly",
        chinese_comfort="清楚表达购物需求可以得到更好的帮助！",
        english_demonstration="I'm looking for something special for my mam's birthday.",
        irish_vocabulary_notes=[
            "'Mam' is Irish term for mother",
            "'Looking for something special' explains purpose",
            "Irish staff enjoy helping with special occasions"
        ],
        age_group_notes="Develops specific communication and gift-giving awareness",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish gift-giving culture",
            "Family celebration traditions",
            "Special occasion shopping"
        ],
        dublin_location_connections=["Gift shops", "Dublin shopping districts"]
    )
    
    scenarios[ExpandedScenarioType.POLITE_SHOP_INTERACTION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.POLITE_SHOP_INTERACTION,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Polite Shopping Interactions",
        description="Learn general courteous behavior in shops",
        chinese_comfort="在商店里保持礼貌会让购物体验更愉快！",
        english_demonstration="Thank you for your help. You've been very kind.",
        irish_vocabulary_notes=[
            "'Thank you for your help' acknowledges assistance",
            "'Very kind' appreciates good service",
            "Irish retail culture values courtesy"
        ],
        age_group_notes="Essential social courtesy and appreciation skills",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish courtesy traditions",
            "Service appreciation culture",
            "Retail relationship building"
        ],
        dublin_location_connections=["All Dublin retail establishments"]
    )
    
    # Transportation scenarios (4)
    scenarios[ExpandedScenarioType.BUS_CONVERSATION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.BUS_CONVERSATION,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Talking on Dublin Bus",
        description="Learn polite conversation on public transport in Dublin",
        chinese_comfort="在都柏林公交车上，人们经常友好地交谈。这是练习英语的好机会！",
        english_demonstration="Is this seat taken? Thank you very much.",
        irish_vocabulary_notes=[
            "'Is this seat taken?' is polite way to ask about seats",
            "'Thank you very much' shows Irish politeness",
            "Dublin Bus has friendly atmosphere"
        ],
        age_group_notes="Essential for navigating Dublin independently",
        difficulty_level=3,
        cultural_integration_points=[
            "Dublin public transport culture",
            "Politeness on Irish public transport",
            "Social interaction norms"
        ],
        dublin_location_connections=["Dublin Bus routes", "Bus stops throughout Dublin"]
    )
    
    scenarios[ExpandedScenarioType.DART_TICKET_PURCHASE] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.DART_TICKET_PURCHASE,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Buying DART Tickets",
        description="Learn to purchase tickets for Dublin's DART train system",
        chinese_comfort="买DART票很简单。工作人员会帮助你选择正确的票！",
        english_demonstration="A return ticket to Howth, please. How much is that?",
        irish_vocabulary_notes=[
            "'Return ticket' means round trip",
            "'How much is that?' asks for price",
            "DART connects Dublin coast and city"
        ],
        age_group_notes="Essential Dublin transport independence",
        difficulty_level=3,
        cultural_integration_points=[
            "Dublin DART system culture",
            "Public transport ticketing",
            "Independent travel skills"
        ],
        dublin_location_connections=["DART stations", "Connolly Station", "Pearse Station"]
    )
    
    scenarios[ExpandedScenarioType.ASKING_WALKING_DIRECTIONS] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.ASKING_WALKING_DIRECTIONS,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Asking for Walking Directions",
        description="Learn to ask for directions when walking in Dublin",
        chinese_comfort="在都柏林迷路时，路人很乐意给你指路。不要犹豫！",
        english_demonstration="Excuse me, could you tell me the way to Trinity College, please?",
        irish_vocabulary_notes=[
            "'Could you tell me the way to...' is polite direction request",
            "Dublin people are known for being helpful with directions",
            "'Please' essential for politeness"
        ],
        age_group_notes="Essential Dublin navigation and social skills",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish helpfulness culture",
            "Dublin navigation norms",
            "Street interaction etiquette"
        ],
        dublin_location_connections=["Dublin city centre", "Trinity College", "Major landmarks"]
    )
    
    scenarios[ExpandedScenarioType.TRANSPORT_POLITENESS] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.TRANSPORT_POLITENESS,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Being Polite on Transport",
        description="Learn general courtesy on Dublin public transport",
        chinese_comfort="在公共交通上保持礼貌很重要。让座位给需要的人！",
        english_demonstration="Would you like my seat? I'm getting off soon anyway.",
        irish_vocabulary_notes=[
            "'Would you like my seat?' offers seat politely",
            "'Getting off soon anyway' explains reason",
            "Irish transport culture values courtesy"
        ],
        age_group_notes="Essential public space courtesy and empathy",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish public transport etiquette",
            "Courtesy to elderly and disabled",
            "Community consideration values"
        ],
        dublin_location_connections=["All Dublin public transport"]
    )
    
    # Family activities (3)
    scenarios[ExpandedScenarioType.HOME_DINNER_CONVERSATION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.HOME_DINNER_CONVERSATION,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Family Dinner Conversations",
        description="Learn to participate in family meal discussions",
        chinese_comfort="家庭晚餐时间是练习英语的好机会。分享你在学校的经历！",
        english_demonstration="School was brilliant today! We learned about Irish history.",
        irish_vocabulary_notes=[
            "'Brilliant' is enthusiastic Irish positive expression",
            "Family meals are important in Irish culture",
            "Sharing school experiences builds family bonds"
        ],
        age_group_notes="Builds family communication and daily sharing",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish family meal traditions",
            "Daily experience sharing",
            "Family bonding through conversation"
        ],
        dublin_location_connections=["Dublin homes", "Family environments"]
    )
    
    scenarios[ExpandedScenarioType.SIBLING_PLAY_INTERACTION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.SIBLING_PLAY_INTERACTION,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Playing with Siblings",
        description="Learn to interact and play with brothers and sisters",
        chinese_comfort="和兄弟姐妹一起玩可以提高英语口语。一起玩游戏很有趣！",
        english_demonstration="Come on, let's play this game together! You can go first.",
        irish_vocabulary_notes=[
            "'Come on' encourages participation",
            "'Let's play together' shows cooperation",
            "'You can go first' shows generosity"
        ],
        age_group_notes="Develops sibling cooperation and sharing",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish family play culture",
            "Sibling cooperation values",
            "Home entertainment traditions"
        ],
        dublin_location_connections=["Dublin homes", "Family play areas"]
    )
    
    scenarios[ExpandedScenarioType.FAMILY_OUTING_PLANNING] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.FAMILY_OUTING_PLANNING,
        category=ScenarioCategory.DAILY_ACTIVITIES,
        title="Planning Family Outings",
        description="Learn to participate in family trip planning discussions",
        chinese_comfort="参与家庭出游计划可以练习表达想法。分享你想去的地方！",
        english_demonstration="I'd love to visit the zoo! Could we go to Phoenix Park too?",
        irish_vocabulary_notes=[
            "'I'd love to visit' expresses enthusiasm",
            "'Could we go to...' suggests additional activities",
            "Phoenix Park is Dublin's famous large park"
        ],
        age_group_notes="Develops planning participation and Dublin geography",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish family outing traditions",
            "Dublin recreational culture",
            "Family decision-making inclusion"
        ],
        dublin_location_connections=["Phoenix Park", "Dublin Zoo", "Family attractions"]
    )
    
    # === SOCIAL INTERACTIONS SCENARIOS (8) ===
    
    scenarios[ExpandedScenarioType.BIRTHDAY_PARTY_CONVERSATION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.BIRTHDAY_PARTY_CONVERSATION,
        category=ScenarioCategory.SOCIAL_INTERACTIONS,
        title="Birthday Party Conversations",
        description="Learn to participate in Irish birthday celebrations",
        chinese_comfort="爱尔兰的生日聚会很有趣！孩子们喜欢一起庆祝和玩游戏。",
        english_demonstration="Happy birthday! I hope you have a brilliant day!",
        irish_vocabulary_notes=[
            "'Brilliant day' is Irish way to say wonderful day",
            "Birthday wishes are very important in Irish culture",
            "Party games are common at Irish children's parties"
        ],
        age_group_notes="Important for social participation and friendships",
        difficulty_level=2,
        cultural_integration_points=[
            "Irish birthday traditions",
            "Party etiquette in Ireland",
            "Gift-giving customs"
        ],
        dublin_location_connections=["Party venues", "Dublin parks", "Community centres"]
    )
    
    scenarios[ExpandedScenarioType.INVITING_FRIEND_OVER] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.INVITING_FRIEND_OVER,
        category=ScenarioCategory.SOCIAL_INTERACTIONS,
        title="Inviting Friends to Your Home",
        description="Learn to invite Irish friends for home visits",
        chinese_comfort="邀请爱尔兰朋友到家里来是很好的友谊表现。他们会很高兴！",
        english_demonstration="Would you like to come round for tea on Saturday?",
        irish_vocabulary_notes=[
            "'Come round' means visit your home",
            "'For tea' means for a meal/snack",
            "Irish children often visit friends' homes"
        ],
        age_group_notes="Builds deeper friendships and cultural exchange",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish home visiting culture",
            "Friendship deepening traditions",
            "Cultural hospitality exchange"
        ],
        dublin_location_connections=["Dublin homes", "Residential areas"]
    )
    
    scenarios[ExpandedScenarioType.SHARING_INTERESTS] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.SHARING_INTERESTS,
        category=ScenarioCategory.SOCIAL_INTERACTIONS,
        title="Sharing Your Interests",
        description="Learn to discuss hobbies and interests with friends",
        chinese_comfort="分享你的兴趣爱好可以找到有相同爱好的朋友！",
        english_demonstration="I really enjoy drawing. What do you like to do for fun?",
        irish_vocabulary_notes=[
            "'Really enjoy' expresses strong positive feeling",
            "'What do you like to do for fun?' asks about interests",
            "Irish children love sharing hobbies"
        ],
        age_group_notes="Develops friendship building and self-expression",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish hobby sharing culture",
            "Interest-based friendship building",
            "Personal expression values"
        ],
        dublin_location_connections=["Hobby clubs", "Community centres", "Recreation areas"]
    )
    
    scenarios[ExpandedScenarioType.APOLOGIZING_APPROPRIATELY] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.APOLOGIZING_APPROPRIATELY,
        category=ScenarioCategory.SOCIAL_INTERACTIONS,
        title="Making Appropriate Apologies",
        description="Learn to apologize sincerely when you make mistakes",
        chinese_comfort="道歉是解决问题的重要方式。真诚的道歉能修复友谊！",
        english_demonstration="I'm really sorry about that. I didn't mean to upset you.",
        irish_vocabulary_notes=[
            "'Really sorry' shows genuine regret",
            "'Didn't mean to' explains no bad intention",
            "Irish culture values sincere apologies"
        ],
        age_group_notes="Essential conflict resolution and relationship repair",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish apology culture",
            "Relationship repair traditions",
            "Sincere communication values"
        ],
        dublin_location_connections=["All social environments"]
    )
    
    scenarios[ExpandedScenarioType.EXPRESSING_DISAGREEMENT_POLITELY] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.EXPRESSING_DISAGREEMENT_POLITELY,
        category=ScenarioCategory.SOCIAL_INTERACTIONS,
        title="Polite Disagreement",
        description="Learn to disagree respectfully with friends",
        chinese_comfort="礼貌地表达不同意见是正常的。朋友之间可以有不同看法！",
        english_demonstration="I see your point, but I think differently about that.",
        irish_vocabulary_notes=[
            "'I see your point' acknowledges their view",
            "'Think differently' expresses disagreement politely",
            "Irish culture values respectful disagreement"
        ],
        age_group_notes="Develops respectful communication and critical thinking",
        difficulty_level=4,
        cultural_integration_points=[
            "Irish respectful disagreement culture",
            "Polite debate traditions",
            "Opinion diversity acceptance"
        ],
        dublin_location_connections=["Discussion environments", "Social gathering spaces"]
    )
    
    scenarios[ExpandedScenarioType.COMMUNITY_GATHERING_PARTICIPATION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.COMMUNITY_GATHERING_PARTICIPATION,
        category=ScenarioCategory.SOCIAL_INTERACTIONS,
        title="Community Gathering Participation",
        description="Learn to participate in local community events",
        chinese_comfort="参加社区活动是融入爱尔兰社会的好方法。大家都很欢迎！",
        english_demonstration="This is a lovely community event! Thank you for including us.",
        irish_vocabulary_notes=[
            "'Lovely community event' appreciates gathering",
            "'Thank you for including us' shows gratitude",
            "Irish communities are known for being inclusive"
        ],
        age_group_notes="Builds community connection and social integration",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish community inclusion culture",
            "Local participation traditions",
            "Social integration pathways"
        ],
        dublin_location_connections=["Community centres", "Local event venues", "Parish halls"]
    )
    
    scenarios[ExpandedScenarioType.MEETING_NEW_NEIGHBOR] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.MEETING_NEW_NEIGHBOR,
        category=ScenarioCategory.SOCIAL_INTERACTIONS,
        title="Meeting New Neighbors",
        description="Learn to introduce yourself to neighbors in Dublin",
        chinese_comfort="认识新邻居是建立社区关系的开始。爱尔兰邻居很友好！",
        english_demonstration="Hello! We're new to the area. I'm delighted to meet you!",
        irish_vocabulary_notes=[
            "'New to the area' explains recent arrival",
            "'Delighted to meet you' is enthusiastic Irish greeting",
            "Irish neighborhoods value friendly relations"
        ],
        age_group_notes="Builds community integration and social confidence",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish neighborhood culture",
            "Community introduction norms",
            "Local relationship building"
        ],
        dublin_location_connections=["Dublin residential areas", "Neighborhood environments"]
    )
    
    scenarios[ExpandedScenarioType.LOCAL_COMMUNITY_EVENT] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.LOCAL_COMMUNITY_EVENT,
        category=ScenarioCategory.SOCIAL_INTERACTIONS,
        title="Local Community Events",
        description="Learn to engage with local Dublin community activities",
        chinese_comfort="参加本地社区活动能让你更好地了解都柏林文化！",
        english_demonstration="What a fantastic turnout! The local community is brilliant.",
        irish_vocabulary_notes=[
            "'Fantastic turnout' praises good attendance",
            "'Local community is brilliant' appreciates community",
            "Irish communities take pride in local events"
        ],
        age_group_notes="Develops community appreciation and local engagement",
        difficulty_level=3,
        cultural_integration_points=[
            "Dublin local community culture",
            "Neighborhood event participation",
            "Local pride and engagement"
        ],
        dublin_location_connections=["Local venues", "Community spaces", "Neighborhood centres"]
    )
    
    # === CULTURAL EVENTS SCENARIOS (7) ===
    
    scenarios[ExpandedScenarioType.ST_PATRICKS_DAY_CELEBRATION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.ST_PATRICKS_DAY_CELEBRATION,
        category=ScenarioCategory.CULTURAL_EVENTS,
        title="St. Patrick's Day Celebration",
        description="Learn to participate in Ireland's national holiday celebration",
        chinese_comfort="圣帕特里克节是爱尔兰最重要的节日！你可以参加游行，感受爱尔兰文化。",
        english_demonstration="Look at the beautiful green decorations! The parade is brilliant!",
        irish_vocabulary_notes=[
            "'Brilliant' is enthusiastic Irish praise",
            "Green is the traditional St. Patrick's Day color",
            "Parades are central to the celebration"
        ],
        age_group_notes="Experience authentic Irish cultural celebration",
        difficulty_level=3,
        cultural_integration_points=[
            "Ireland's national identity",
            "St. Patrick's Day traditions",
            "Community celebration spirit"
        ],
        dublin_location_connections=["O'Connell Street parade", "Dublin city centre", "Trinity College"]
    )
    
    scenarios[ExpandedScenarioType.GAA_MATCH_WATCHING] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.GAA_MATCH_WATCHING,
        category=ScenarioCategory.CULTURAL_EVENTS,
        title="Watching GAA Matches",
        description="Learn to enjoy Gaelic Athletic Association sports",
        chinese_comfort="观看GAA比赛是体验爱尔兰传统体育的好方式。这是爱尔兰独有的运动！",
        english_demonstration="What an exciting match! Dublin are playing brilliantly today!",
        irish_vocabulary_notes=[
            "'Exciting match' shows enthusiasm for sport",
            "Dublin GAA teams represent the county",
            "'Playing brilliantly' praises team performance"
        ],
        age_group_notes="Experience authentic Irish sports culture",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish GAA sports traditions",
            "County pride and loyalty",
            "Community sports culture"
        ],
        dublin_location_connections=["Croke Park", "Local GAA clubs", "Dublin GAA venues"]
    )
    
    scenarios[ExpandedScenarioType.IRISH_TRADITIONAL_MUSIC_EVENT] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.IRISH_TRADITIONAL_MUSIC_EVENT,
        category=ScenarioCategory.CULTURAL_EVENTS,
        title="Irish Traditional Music Events",
        description="Learn to appreciate and discuss Irish traditional music",
        chinese_comfort="爱尔兰传统音乐很美妙！听这些音乐可以更好地理解爱尔兰文化。",
        english_demonstration="The fiddle music is absolutely lovely! Irish music is so beautiful.",
        irish_vocabulary_notes=[
            "'Absolutely lovely' is strong appreciation",
            "Fiddle is important in Irish traditional music",
            "Irish music has deep cultural significance"
        ],
        age_group_notes="Develops cultural appreciation and music vocabulary",
        difficulty_level=4,
        cultural_integration_points=[
            "Irish musical heritage",
            "Traditional art appreciation",
            "Cultural music traditions"
        ],
        dublin_location_connections=["Traditional music venues", "Cultural centres", "Dublin pubs"]
    )
    
    scenarios[ExpandedScenarioType.IRISH_DANCING_PARTICIPATION] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.IRISH_DANCING_PARTICIPATION,
        category=ScenarioCategory.CULTURAL_EVENTS,
        title="Irish Dancing Participation",
        description="Learn to participate in or appreciate Irish dancing",
        chinese_comfort="爱尔兰舞蹈很有趣！即使你不会跳，观看也很有意思。",
        english_demonstration="The Irish dancing is amazing! Could you show me some steps?",
        irish_vocabulary_notes=[
            "'Amazing' shows strong admiration",
            "'Show me some steps' requests learning",
            "Irish dancing is celebrated worldwide"
        ],
        age_group_notes="Experience kinesthetic cultural expression",
        difficulty_level=3,
        cultural_integration_points=[
            "Irish dancing traditions",
            "Physical cultural expression",
            "Performance art appreciation"
        ],
        dublin_location_connections=["Dance schools", "Cultural performance venues", "Community centres"]
    )
    
    scenarios[ExpandedScenarioType.DUBLIN_HERITAGE_VISIT] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.DUBLIN_HERITAGE_VISIT,
        category=ScenarioCategory.CULTURAL_EVENTS,
        title="Visiting Dublin Heritage Sites",
        description="Learn to appreciate Dublin's historical and cultural heritage",
        chinese_comfort="参观都柏林历史遗迹可以了解爱尔兰的历史和文化！",
        english_demonstration="Dublin Castle has such fascinating history! I'd love to learn more.",
        irish_vocabulary_notes=[
            "'Fascinating history' shows historical interest",
            "'I'd love to learn more' expresses curiosity",
            "Dublin has rich historical heritage"
        ],
        age_group_notes="Develops historical awareness and cultural knowledge",
        difficulty_level=4,
        cultural_integration_points=[
            "Dublin historical significance",
            "Irish heritage appreciation",
            "Cultural landmark understanding"
        ],
        dublin_location_connections=["Dublin Castle", "Trinity College", "Christ Church Cathedral", "Kilmainham Gaol"]
    )
    
    scenarios[ExpandedScenarioType.SHARING_CHINESE_CULTURE] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.SHARING_CHINESE_CULTURE,
        category=ScenarioCategory.CULTURAL_EVENTS,
        title="Sharing Your Chinese Culture",
        description="Learn to proudly share Chinese traditions with Irish friends",
        chinese_comfort="分享中国文化是很美好的事情！爱尔兰朋友们很想了解中国的传统。",
        english_demonstration="In China, we celebrate Chinese New Year with red decorations and dragon dances!",
        irish_vocabulary_notes=[
            "Sharing cultural traditions builds friendships",
            "Irish people are interested in other cultures",
            "Describing celebrations helps cultural understanding"
        ],
        age_group_notes="Builds cultural pride and cross-cultural understanding",
        difficulty_level=4,
        cultural_integration_points=[
            "Cultural bridge building",
            "Pride in Chinese heritage",
            "Irish appreciation for diversity"
        ],
        dublin_location_connections=["Cultural centres", "Schools", "Community events"]
    )
    
    scenarios[ExpandedScenarioType.EXPLAINING_CHINESE_HOLIDAY] = ExpandedScenarioContent(
        scenario_type=ExpandedScenarioType.EXPLAINING_CHINESE_HOLIDAY,
        category=ScenarioCategory.CULTURAL_EVENTS,
        title="Explaining Chinese Holidays",
        description="Learn to explain Chinese festivals and traditions to Irish friends",
        chinese_comfort="向爱尔兰朋友解释中国节日是很好的文化交流机会！",
        english_demonstration="Mid-Autumn Festival is when Chinese families gather to admire the moon and eat mooncakes.",
        irish_vocabulary_notes=[
            "Explaining traditions helps others understand your culture",
            "Irish people appreciate learning about other celebrations",
            "Cultural sharing builds deeper friendships"
        ],
        age_group_notes="Advanced cultural sharing and explanation skills",
        difficulty_level=5,
        cultural_integration_points=[
            "Chinese holiday education",
            "Cross-cultural celebration sharing",
            "Heritage pride and education"
        ],
        dublin_location_connections=["Schools", "Cultural events", "Community presentations"]
    )
    
    return scenarios


def get_scenario_categories_mapping() -> Dict[ScenarioCategory, List[ExpandedScenarioType]]:
    """Get mapping of categories to scenario types"""
    scenarios = get_complete_scenario_library()
    
    categories = {
        ScenarioCategory.SCHOOL_LIFE: [],
        ScenarioCategory.DAILY_ACTIVITIES: [],
        ScenarioCategory.SOCIAL_INTERACTIONS: [],
        ScenarioCategory.CULTURAL_EVENTS: []
    }
    
    for scenario_type, scenario_content in scenarios.items():
        categories[scenario_content.category].append(scenario_type)
    
    return categories