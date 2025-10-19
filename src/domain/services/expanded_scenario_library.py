"""
Expanded Scenario Library Service for Story 2.3

Provides comprehensive conversation scenarios for Chinese children learning English in Ireland.
Expands from 5 foundational scenarios to 50+ scenarios across multiple categories:
school life, daily activities, social interactions, and cultural events.

Integrates with Irish Curriculum Mapping and Dublin Cultural Context services.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Set
from enum import Enum
import time
import random
from .conversation_types import ScenarioType, ConversationPhase, ScenarioContent, ConversationTurn, ScenarioSession
from .curriculum_integration import CurriculumIntegrationService, AgeGroup, VocabularyComplexity, IrishCurriculumStage
from .dublin_cultural_integration import DublinCulturalIntegrationService


class ExpandedScenarioType(str, Enum):
    """Extended scenario types for comprehensive library"""
    
    # Original scenarios (5)
    INTRODUCING_YOURSELF = "introducing_yourself"
    ASKING_FOR_TOILET = "asking_for_toilet"
    ASKING_FOR_HELP = "asking_for_help"
    EXPRESSING_HUNGER = "expressing_hunger"
    SAYING_GOODBYE = "saying_goodbye"
    
    # School Life Scenarios (25 scenarios)
    # Classroom interactions (10)
    ASKING_TEACHER_QUESTION = "asking_teacher_question"
    GROUP_WORK_COLLABORATION = "group_work_collaboration"
    CLASS_PRESENTATION = "class_presentation"
    ANSWERING_IN_CLASS = "answering_in_class"
    EXPLAINING_HOMEWORK_PROBLEM = "explaining_homework_problem"
    SHARING_LEARNING_MATERIALS = "sharing_learning_materials"
    PARTICIPATING_DISCUSSION = "participating_discussion"
    ASKING_CLASSMATE_HELP = "asking_classmate_help"
    READING_ALOUD_CLASS = "reading_aloud_class"
    SHOWING_UNDERSTANDING = "showing_understanding"
    
    # Playground conversations (8)
    MAKING_NEW_FRIENDS = "making_new_friends"
    PLAYGROUND_GAMES = "playground_games"
    RESOLVING_PLAYGROUND_CONFLICT = "resolving_playground_conflict"
    INVITING_TO_PLAY = "inviting_to_play"
    SHARING_PLAYGROUND_EQUIPMENT = "sharing_playground_equipment"
    EXPRESSING_FEELINGS_PLAYGROUND = "expressing_feelings_playground"
    ORGANIZING_GROUP_GAME = "organizing_group_game"
    COMFORTING_UPSET_FRIEND = "comforting_upset_friend"
    
    # Canteen/lunch scenarios (5)
    LUNCH_FOOD_CONVERSATION = "lunch_food_conversation"
    SHARING_CULTURAL_FOOD = "sharing_cultural_food"
    ASKING_LUNCH_HELP = "asking_lunch_help"
    DESCRIBING_FOOD_PREFERENCES = "describing_food_preferences"
    CANTEEN_POLITENESS = "canteen_politeness"
    
    # School events (2)
    SCHOOL_ASSEMBLY_PARTICIPATION = "school_assembly_participation"
    SPORTS_DAY_ACTIVITIES = "sports_day_activities"
    
    # Daily Life Scenarios (15 scenarios)
    # Shopping scenarios (8)
    GROCERY_SHOPPING_HELP = "grocery_shopping_help"
    CLOTHES_SHOPPING_PREFERENCES = "clothes_shopping_preferences"
    ASKING_STORE_DIRECTIONS = "asking_store_directions"
    PAYING_AT_CHECKOUT = "paying_at_checkout"
    COMPARING_PRICES = "comparing_prices"
    ASKING_PRODUCT_LOCATION = "asking_product_location"
    EXPRESSING_SHOPPING_NEEDS = "expressing_shopping_needs"
    POLITE_SHOP_INTERACTION = "polite_shop_interaction"
    
    # Transportation scenarios (4)
    BUS_CONVERSATION = "bus_conversation"
    DART_TICKET_PURCHASE = "dart_ticket_purchase"
    ASKING_WALKING_DIRECTIONS = "asking_walking_directions"
    TRANSPORT_POLITENESS = "transport_politeness"
    
    # Family activities (3)
    HOME_DINNER_CONVERSATION = "home_dinner_conversation"
    SIBLING_PLAY_INTERACTION = "sibling_play_interaction"
    FAMILY_OUTING_PLANNING = "family_outing_planning"
    
    # Social Interactions (8 scenarios)
    # Friend-making scenarios (6)
    BIRTHDAY_PARTY_CONVERSATION = "birthday_party_conversation"
    INVITING_FRIEND_OVER = "inviting_friend_over"
    SHARING_INTERESTS = "sharing_interests"
    APOLOGIZING_APPROPRIATELY = "apologizing_appropriately"
    EXPRESSING_DISAGREEMENT_POLITELY = "expressing_disagreement_politely"
    COMMUNITY_GATHERING_PARTICIPATION = "community_gathering_participation"
    
    # Neighborhood interactions (2)
    MEETING_NEW_NEIGHBOR = "meeting_new_neighbor"
    LOCAL_COMMUNITY_EVENT = "local_community_event"
    
    # Cultural Events (7 scenarios)
    # Irish cultural participation (5)
    ST_PATRICKS_DAY_CELEBRATION = "st_patricks_day_celebration"
    GAA_MATCH_WATCHING = "gaa_match_watching"
    IRISH_TRADITIONAL_MUSIC_EVENT = "irish_traditional_music_event"
    IRISH_DANCING_PARTICIPATION = "irish_dancing_participation"
    DUBLIN_HERITAGE_VISIT = "dublin_heritage_visit"
    
    # Bicultural sharing (2)
    SHARING_CHINESE_CULTURE = "sharing_chinese_culture"
    EXPLAINING_CHINESE_HOLIDAY = "explaining_chinese_holiday"


class ScenarioCategory(str, Enum):
    """Scenario category classification"""
    SCHOOL_LIFE = "school_life"
    DAILY_ACTIVITIES = "daily_activities" 
    SOCIAL_INTERACTIONS = "social_interactions"
    CULTURAL_EVENTS = "cultural_events"


class ConversationPathType(str, Enum):
    """Types of conversation paths for each scenario"""
    BEGINNER_PATH = "beginner_path"
    INTERMEDIATE_PATH = "intermediate_path"
    ADVANCED_PATH = "advanced_path"
    CULTURAL_BRIDGE_PATH = "cultural_bridge_path"
    SUPPORTIVE_PATH = "supportive_path"


@dataclass
class ConversationPath:
    """A single conversation path for a scenario"""
    path_type: ConversationPathType
    complexity_level: VocabularyComplexity
    conversation_turns: List[ConversationTurn]
    response_options: List[str]
    learning_objectives: List[str]
    cultural_elements: List[str] = field(default_factory=list)


@dataclass
class ScenarioRecommendation:
    """Recommendation for next scenario"""
    scenario: 'ExpandedScenarioContent'
    conversation_paths: List[ConversationPath]
    reasoning: str
    complexity_adjustment: str
    alternative_scenarios: List['ExpandedScenarioContent'] = field(default_factory=list)


@dataclass
class ExpandedScenarioContent:
    """Enhanced content structure for expanded scenarios"""
    scenario_type: ExpandedScenarioType
    category: ScenarioCategory
    title: str
    description: str
    chinese_comfort: str
    english_demonstration: str
    irish_vocabulary_notes: List[str]
    age_group_notes: str
    difficulty_level: int = 1  # 1-5 scale
    conversation_paths: Dict[ConversationPathType, ConversationPath] = field(default_factory=dict)
    cultural_integration_points: List[str] = field(default_factory=list)
    dublin_location_connections: List[str] = field(default_factory=list)
    curriculum_alignment: Dict[str, Any] = field(default_factory=dict)


class ExpandedScenarioLibraryService:
    """Comprehensive scenario management service with 50+ scenarios"""

    def __init__(self, 
                 curriculum_mapper: Optional[CurriculumIntegrationService] = None,
                 cultural_context: Optional[DublinCulturalIntegrationService] = None):
        
        self.curriculum_mapper = curriculum_mapper or CurriculumIntegrationService()
        self.cultural_context = cultural_context or DublinCulturalIntegrationService()
        
        # Initialize expanded scenario library
        self.scenarios = self._initialize_expanded_scenario_library()
        self.scenario_categories = self._initialize_scenario_categories()
        self.conversation_path_generator = ConversationPathGenerator(self.curriculum_mapper)
        self.scenario_recommendation_engine = ScenarioRecommendationEngine(
            self.curriculum_mapper, self.cultural_context
        )
        
        # Performance optimization
        self._scenario_cache: Dict[str, ExpandedScenarioContent] = {}
        self.active_sessions: Dict[str, ScenarioSession] = {}

    def _initialize_expanded_scenario_library(self) -> Dict[ExpandedScenarioType, ExpandedScenarioContent]:
        """Initialize comprehensive 50+ scenario library"""
        from .expanded_scenario_data import get_complete_scenario_library
        return get_complete_scenario_library()


    def _initialize_scenario_categories(self) -> Dict[ScenarioCategory, List[ExpandedScenarioType]]:
        """Initialize scenario categorization mapping"""
        from .expanded_scenario_data import get_scenario_categories_mapping
        return get_scenario_categories_mapping()

    async def get_scenario_recommendation(self, child_profile: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ScenarioRecommendation:
        """Get intelligent scenario recommendation based on child profile and progress"""
        return await self.scenario_recommendation_engine.recommend_next_scenario(child_profile, context)

    def get_scenarios_by_category(self, category: ScenarioCategory) -> List[ExpandedScenarioContent]:
        """Get all scenarios in a specific category"""
        scenario_types = self.scenario_categories.get(category, [])
        return [self.scenarios[scenario_type] for scenario_type in scenario_types]

    def get_scenario_content(self, scenario_type: ExpandedScenarioType) -> Optional[ExpandedScenarioContent]:
        """Get content for specific scenario"""
        return self.scenarios.get(scenario_type)

    async def generate_conversation_paths(self, scenario_type: ExpandedScenarioType, child_profile: Dict[str, Any]) -> List[ConversationPath]:
        """Generate multiple conversation paths for scenario"""
        scenario = self.scenarios.get(scenario_type)
        if not scenario:
            return []
        
        return await self.conversation_path_generator.generate_paths(scenario, child_profile)

    def get_library_summary(self) -> Dict[str, Any]:
        """Get comprehensive library summary"""
        return {
            "total_scenarios": len(self.scenarios),
            "scenarios_by_category": {
                category.value: len(scenario_types) 
                for category, scenario_types in self.scenario_categories.items()
            },
            "complexity_distribution": self._get_complexity_distribution(),
            "cultural_integration_coverage": self._get_cultural_coverage(),
            "curriculum_alignment_summary": self._get_curriculum_alignment_summary()
        }

    def _get_complexity_distribution(self) -> Dict[int, int]:
        """Get distribution of scenarios by difficulty level"""
        distribution = {}
        for scenario in self.scenarios.values():
            level = scenario.difficulty_level
            distribution[level] = distribution.get(level, 0) + 1
        return distribution

    def _get_cultural_coverage(self) -> Dict[str, int]:
        """Get cultural integration coverage statistics"""
        dublin_connections = sum(1 for s in self.scenarios.values() if s.dublin_location_connections)
        cultural_points = sum(1 for s in self.scenarios.values() if s.cultural_integration_points)
        
        return {
            "scenarios_with_dublin_connections": dublin_connections,
            "scenarios_with_cultural_integration": cultural_points,
            "total_cultural_coverage": (dublin_connections + cultural_points) / (len(self.scenarios) * 2)
        }

    def _get_curriculum_alignment_summary(self) -> Dict[str, Any]:
        """Get curriculum alignment summary"""
        aligned_scenarios = sum(1 for s in self.scenarios.values() if s.curriculum_alignment)
        
        return {
            "curriculum_aligned_scenarios": aligned_scenarios,
            "alignment_percentage": aligned_scenarios / len(self.scenarios) * 100,
            "age_group_coverage": "Junior Infants to 4th Class"
        }


class ConversationPathGenerator:
    """Generates multiple conversation paths for scenarios"""

    def __init__(self, curriculum_mapper: CurriculumIntegrationService):
        self.curriculum_mapper = curriculum_mapper

    async def generate_paths(self, scenario: ExpandedScenarioContent, child_profile: Dict[str, Any]) -> List[ConversationPath]:
        """Generate conversation paths for scenario"""
        paths = []
        
        age_group = self._get_age_group_from_profile(child_profile)
        
        # Generate beginner path
        beginner_path = await self._generate_beginner_path(scenario, age_group)
        if beginner_path:
            paths.append(beginner_path)
        
        # Generate intermediate path
        intermediate_path = await self._generate_intermediate_path(scenario, age_group)
        if intermediate_path:
            paths.append(intermediate_path)
        
        # Generate advanced path (if age appropriate)
        if age_group in [AgeGroup.THIRD_CLASS, AgeGroup.FOURTH_CLASS]:
            advanced_path = await self._generate_advanced_path(scenario, age_group)
            if advanced_path:
                paths.append(advanced_path)
        
        # Generate cultural bridge path
        cultural_path = await self._generate_cultural_bridge_path(scenario, child_profile)
        if cultural_path:
            paths.append(cultural_path)
        
        return paths

    async def _generate_beginner_path(self, scenario: ExpandedScenarioContent, age_group: AgeGroup) -> Optional[ConversationPath]:
        """Generate beginner-level conversation path"""
        complexity = VocabularyComplexity.VERY_SIMPLE if age_group == AgeGroup.JUNIOR_INFANTS else VocabularyComplexity.SIMPLE
        
        turns = [
            ConversationTurn(
                phase=ConversationPhase.CHINESE_COMFORT,
                speaker="xiao_mei",
                content=scenario.chinese_comfort,
                language="zh-CN",
                timestamp=time.time()
            ),
            ConversationTurn(
                phase=ConversationPhase.ENGLISH_DEMONSTRATION,
                speaker="xiao_mei",
                content=scenario.english_demonstration,
                language="en-IE",
                timestamp=time.time()
            )
        ]
        
        response_options = self._generate_simple_response_options(scenario)
        learning_objectives = ["Basic vocabulary", "Simple sentence structure", "Polite interaction"]
        
        return ConversationPath(
            path_type=ConversationPathType.BEGINNER_PATH,
            complexity_level=complexity,
            conversation_turns=turns,
            response_options=response_options,
            learning_objectives=learning_objectives,
            cultural_elements=scenario.cultural_integration_points[:1]
        )

    async def _generate_intermediate_path(self, scenario: ExpandedScenarioContent, age_group: AgeGroup) -> Optional[ConversationPath]:
        """Generate intermediate-level conversation path"""
        complexity = VocabularyComplexity.SIMPLE if age_group in [AgeGroup.SENIOR_INFANTS, AgeGroup.FIRST_CLASS] else VocabularyComplexity.MODERATE
        
        # Enhanced conversation with follow-up questions
        turns = [
            ConversationTurn(
                phase=ConversationPhase.CHINESE_COMFORT,
                speaker="xiao_mei",
                content=scenario.chinese_comfort + " 我们可以练习更多的对话。",
                language="zh-CN",
                timestamp=time.time()
            ),
            ConversationTurn(
                phase=ConversationPhase.ENGLISH_DEMONSTRATION,
                speaker="xiao_mei",
                content=f"{scenario.english_demonstration} How do you feel about that?",
                language="en-IE",
                timestamp=time.time()
            )
        ]
        
        response_options = self._generate_intermediate_response_options(scenario)
        learning_objectives = ["Extended conversation", "Expressing opinions", "Following conversation flow"]
        
        return ConversationPath(
            path_type=ConversationPathType.INTERMEDIATE_PATH,
            complexity_level=complexity,
            conversation_turns=turns,
            response_options=response_options,
            learning_objectives=learning_objectives,
            cultural_elements=scenario.cultural_integration_points[:2]
        )

    async def _generate_advanced_path(self, scenario: ExpandedScenarioContent, age_group: AgeGroup) -> Optional[ConversationPath]:
        """Generate advanced-level conversation path"""
        complexity = VocabularyComplexity.COMPLEX
        
        # Complex conversation with problem-solving
        turns = [
            ConversationTurn(
                phase=ConversationPhase.CHINESE_COMFORT,
                speaker="xiao_mei",
                content=scenario.chinese_comfort + " 今天我们挑战更复杂的对话，你准备好了吗？",
                language="zh-CN",
                timestamp=time.time()
            ),
            ConversationTurn(
                phase=ConversationPhase.ENGLISH_DEMONSTRATION,
                speaker="xiao_mei",
                content=f"{scenario.english_demonstration} What do you think would happen if...?",
                language="en-IE",
                timestamp=time.time()
            )
        ]
        
        response_options = self._generate_advanced_response_options(scenario)
        learning_objectives = ["Complex reasoning", "Hypothetical thinking", "Cultural analysis"]
        
        return ConversationPath(
            path_type=ConversationPathType.ADVANCED_PATH,
            complexity_level=complexity,
            conversation_turns=turns,
            response_options=response_options,
            learning_objectives=learning_objectives,
            cultural_elements=scenario.cultural_integration_points
        )

    async def _generate_cultural_bridge_path(self, scenario: ExpandedScenarioContent, child_profile: Dict[str, Any]) -> Optional[ConversationPath]:
        """Generate cultural bridge conversation path"""
        
        turns = [
            ConversationTurn(
                phase=ConversationPhase.CHINESE_COMFORT,
                speaker="xiao_mei",
                content=f"{scenario.chinese_comfort} 你觉得这与中国的情况有什么相似之处？",
                language="zh-CN",
                timestamp=time.time()
            ),
            ConversationTurn(
                phase=ConversationPhase.ENGLISH_DEMONSTRATION,
                speaker="xiao_mei",
                content=f"{scenario.english_demonstration} In your culture, how do you handle this situation?",
                language="en-IE",
                timestamp=time.time()
            )
        ]
        
        response_options = self._generate_cultural_response_options(scenario)
        learning_objectives = ["Cultural comparison", "Sharing heritage", "Building bridges"]
        
        return ConversationPath(
            path_type=ConversationPathType.CULTURAL_BRIDGE_PATH,
            complexity_level=VocabularyComplexity.MODERATE,
            conversation_turns=turns,
            response_options=response_options,
            learning_objectives=learning_objectives,
            cultural_elements=scenario.cultural_integration_points + ["Chinese cultural sharing"]
        )

    def _generate_simple_response_options(self, scenario: ExpandedScenarioContent) -> List[str]:
        """Generate simple response options"""
        return [
            "Yes, please",
            "No, thank you",
            "I understand",
            "Can you help me?",
            "Thank you very much"
        ]

    def _generate_intermediate_response_options(self, scenario: ExpandedScenarioContent) -> List[str]:
        """Generate intermediate response options"""
        return [
            "I think that's a good idea",
            "Could you explain that again, please?",
            "That's interesting, tell me more",
            "I agree with you",
            "I'm not sure about that"
        ]

    def _generate_advanced_response_options(self, scenario: ExpandedScenarioContent) -> List[str]:
        """Generate advanced response options"""
        return [
            "From my perspective, I believe...",
            "That's an interesting point, however...",
            "I wonder if we could consider...",
            "Based on my experience...",
            "What if we approached it differently?"
        ]

    def _generate_cultural_response_options(self, scenario: ExpandedScenarioContent) -> List[str]:
        """Generate cultural bridge response options"""
        return [
            "In China, we usually...",
            "My family does it like this...",
            "That's similar to Chinese culture because...",
            "The difference I notice is...",
            "I can share something from my culture..."
        ]

    def _get_age_group_from_profile(self, child_profile: Dict[str, Any]) -> AgeGroup:
        """Extract age group from child profile"""
        age = child_profile.get('age', 8)
        if age <= 5:
            return AgeGroup.JUNIOR_INFANTS
        elif age <= 6:
            return AgeGroup.SENIOR_INFANTS
        elif age <= 7:
            return AgeGroup.FIRST_CLASS
        elif age <= 8:
            return AgeGroup.SECOND_CLASS
        elif age <= 9:
            return AgeGroup.THIRD_CLASS
        else:
            return AgeGroup.FOURTH_CLASS


class ScenarioRecommendationEngine:
    """Intelligent scenario recommendation based on child progress"""

    def __init__(self, curriculum_mapper: CurriculumIntegrationService, cultural_context: DublinCulturalIntegrationService):
        self.curriculum_mapper = curriculum_mapper
        self.cultural_context = cultural_context

    async def recommend_next_scenario(self, child_profile: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ScenarioRecommendation:
        """Recommend next scenario based on child profile and session history"""
        
        age_group = self._get_age_group_from_profile(child_profile)
        progress_history = child_profile.get('progress_history', [])
        current_comfort_level = child_profile.get('comfort_level', 'beginner')
        
        # Get curriculum-appropriate scenarios
        appropriate_scenarios = await self._filter_age_appropriate_scenarios(age_group)
        
        # Filter based on progress history
        unvisited_scenarios = self._filter_unvisited_scenarios(appropriate_scenarios, progress_history)
        
        # Select scenario based on complexity progression
        selected_scenario = await self._select_optimal_scenario(unvisited_scenarios, child_profile)
        
        # Generate conversation paths
        conversation_paths = await self._generate_paths_for_recommendation(selected_scenario, child_profile)
        
        # Create recommendation reasoning
        reasoning = self._generate_recommendation_reasoning(selected_scenario, child_profile)
        
        # Suggest complexity adjustment
        complexity_adjustment = self._suggest_complexity_adjustment(child_profile, selected_scenario)
        
        # Generate alternatives
        alternatives = await self._generate_alternative_scenarios(unvisited_scenarios, selected_scenario)
        
        return ScenarioRecommendation(
            scenario=selected_scenario,
            conversation_paths=conversation_paths,
            reasoning=reasoning,
            complexity_adjustment=complexity_adjustment,
            alternative_scenarios=alternatives
        )

    async def _filter_age_appropriate_scenarios(self, age_group: AgeGroup) -> List[ExpandedScenarioContent]:
        """Filter scenarios appropriate for age group"""
        from .expanded_scenario_data import get_complete_scenario_library
        all_scenarios = get_complete_scenario_library()
        
        # Filter based on difficulty level appropriate for age group
        age_complexity_map = {
            AgeGroup.JUNIOR_INFANTS: [1, 2],
            AgeGroup.SENIOR_INFANTS: [1, 2, 3], 
            AgeGroup.FIRST_CLASS: [2, 3],
            AgeGroup.SECOND_CLASS: [2, 3, 4],
            AgeGroup.THIRD_CLASS: [3, 4, 5],
            AgeGroup.FOURTH_CLASS: [3, 4, 5]
        }
        
        appropriate_levels = age_complexity_map.get(age_group, [2, 3])
        return [s for s in all_scenarios.values() if s.difficulty_level in appropriate_levels]

    def _filter_unvisited_scenarios(self, scenarios: List[ExpandedScenarioContent], progress_history: List[str]) -> List[ExpandedScenarioContent]:
        """Filter out scenarios child has already completed"""
        visited_scenario_ids = set(progress_history)
        return [s for s in scenarios if s.scenario_type.value not in visited_scenario_ids]

    async def _select_optimal_scenario(self, scenarios: List[ExpandedScenarioContent], child_profile: Dict[str, Any]) -> ExpandedScenarioContent:
        """Select optimal scenario based on learning progression"""
        if not scenarios:
            # Return a default scenario from school life category
            from .expanded_scenario_data import get_complete_scenario_library
            all_scenarios = get_complete_scenario_library()
            school_scenarios = [s for s in all_scenarios.values() if s.category == ScenarioCategory.SCHOOL_LIFE]
            return school_scenarios[0] if school_scenarios else list(all_scenarios.values())[0]
        
        # Intelligent selection based on child's comfort level and category preference
        comfort_level = child_profile.get('comfort_level', 'beginner')
        
        if comfort_level == 'beginner':
            # Choose easiest available scenario
            return min(scenarios, key=lambda s: s.difficulty_level)
        elif comfort_level == 'advanced':
            # Choose more challenging scenario
            return max(scenarios, key=lambda s: s.difficulty_level)
        else:
            # Balanced selection - medium difficulty
            return min(scenarios, key=lambda s: abs(s.difficulty_level - 3))

    async def _generate_paths_for_recommendation(self, scenario: ExpandedScenarioContent, child_profile: Dict[str, Any]) -> List[ConversationPath]:
        """Generate conversation paths for recommended scenario"""
        conversation_path_generator = ConversationPathGenerator(self.curriculum_mapper)
        return await conversation_path_generator.generate_paths(scenario, child_profile)

    def _generate_recommendation_reasoning(self, scenario: ExpandedScenarioContent, child_profile: Dict[str, Any]) -> str:
        """Generate human-readable reasoning for recommendation"""
        age = child_profile.get('age', 8)
        return f"This scenario is perfect for age {age} and helps build {scenario.category.value} skills while practicing Irish English vocabulary."

    def _suggest_complexity_adjustment(self, child_profile: Dict[str, Any], scenario: ExpandedScenarioContent) -> str:
        """Suggest complexity level adjustment"""
        comfort_level = child_profile.get('comfort_level', 'beginner')
        
        if comfort_level == 'beginner':
            return "Start with simple vocabulary and short sentences"
        elif comfort_level == 'intermediate':
            return "Use varied vocabulary and encourage longer responses"
        else:
            return "Challenge with complex language and cultural discussions"

    async def _generate_alternative_scenarios(self, available_scenarios: List[ExpandedScenarioContent], selected_scenario: ExpandedScenarioContent) -> List[ExpandedScenarioContent]:
        """Generate alternative scenario options"""
        alternatives = [s for s in available_scenarios if s != selected_scenario]
        return alternatives[:3]  # Return top 3 alternatives

    def _get_age_group_from_profile(self, child_profile: Dict[str, Any]) -> AgeGroup:
        """Extract age group from child profile"""
        age = child_profile.get('age', 8)
        if age <= 5:
            return AgeGroup.JUNIOR_INFANTS
        elif age <= 6:
            return AgeGroup.SENIOR_INFANTS
        elif age <= 7:
            return AgeGroup.FIRST_CLASS
        elif age <= 8:
            return AgeGroup.SECOND_CLASS
        elif age <= 9:
            return AgeGroup.THIRD_CLASS
        else:
            return AgeGroup.FOURTH_CLASS