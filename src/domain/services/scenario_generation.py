"""
Scenario Generation Service for Basic Conversation System

Provides foundational conversation scenarios for Chinese children learning English in Ireland.
Implements the 5 core scenarios with Irish English vocabulary and bilingual patterns.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
import time
from .conversation_types import ScenarioType, ConversationPhase, ScenarioContent, ConversationTurn, ScenarioSession


class ScenarioGenerationService:
    """Core service for generating and managing conversation scenarios"""

    def __init__(self):
        self.scenarios = self._initialize_scenario_library()
        self.irish_vocabulary_map = self._initialize_irish_vocabulary()
        self.active_sessions: Dict[str, ScenarioSession] = {}
        
        # Trauma-informed components (Story 1.4) - imported locally to avoid circular imports
        from .encouragement_system import BilingualPraiseEngine, PersonalJourneyNarrative
        from .trauma_validation import NonCompetitiveLanguageFilter
        self.praise_engine = BilingualPraiseEngine()
        self.journey_narrative = PersonalJourneyNarrative()
        self.non_competitive_filter = NonCompetitiveLanguageFilter()

    def _initialize_scenario_library(self) -> Dict[ScenarioType, ScenarioContent]:
        """Initialize the library of available scenarios"""
        return {
            ScenarioType.INTRODUCING_YOURSELF: ScenarioContent(
                scenario_type=ScenarioType.INTRODUCING_YOURSELF,
                title="Introducing Yourself",
                description="Learn to introduce yourself to new friends in English",
                chinese_comfort="现在我们练习自我介绍。在爱尔兰，孩子们喜欢认识新朋友！",
                english_demonstration="Hello! My name is [your name]. I'm from China. Nice to meet you!",
                irish_vocabulary_notes=[
                    "Use 'lovely to meet you' as common Irish greeting",
                    "'What's your name?' is standard introduction question",
                    "Irish children often ask 'Where are you from?'"
                ],
                age_group_notes="Perfect for ages 4-10, encourages social confidence"
            ),
            ScenarioType.ASKING_FOR_TOILET: ScenarioContent(
                scenario_type=ScenarioType.ASKING_FOR_TOILET,
                title="Asking for the Toilet",
                description="Learn to ask for the toilet using Irish English vocabulary",
                chinese_comfort="在学校里，我们需要知道怎么问厕所在哪里。在爱尔兰，我们说'toilet'不说'bathroom'。",
                english_demonstration="Excuse me, where is the toilet, please?",
                irish_vocabulary_notes=[
                    "Use 'toilet' not 'bathroom' - standard Irish English",
                    "'Excuse me' is polite way to get attention",
                    "Add 'please' at the end for Irish politeness"
                ],
                age_group_notes="Essential for school comfort and independence"
            ),
            ScenarioType.ASKING_FOR_HELP: ScenarioContent(
                scenario_type=ScenarioType.ASKING_FOR_HELP,
                title="Asking for Help",
                description="Learn to ask for help when you need it",
                chinese_comfort="有时候我们需要帮助，这完全没关系！在爱尔兰，人们很乐意帮助孩子。",
                english_demonstration="Can you help me, please? I don't understand.",
                irish_vocabulary_notes=[
                    "'Can you help me?' is direct and polite",
                    "'I don't understand' shows you want to learn",
                    "Irish people are known for being helpful"
                ],
                age_group_notes="Builds confidence to seek support when needed"
            ),
            ScenarioType.EXPRESSING_HUNGER: ScenarioContent(
                scenario_type=ScenarioType.EXPRESSING_HUNGER,
                title="Expressing Hunger",
                description="Learn to talk about being hungry, especially at school",
                chinese_comfort="在学校食堂，我们可以说我们饿了。爱尔兰学校的午餐很不错！",
                english_demonstration="I'm hungry. What's for lunch today?",
                irish_vocabulary_notes=[
                    "'What's for lunch?' is common school question",
                    "School canteen staff are friendly and helpful",
                    "'I'm hungry' is simple and clear"
                ],
                age_group_notes="Practical for daily school life and meal times"
            ),
            ScenarioType.SAYING_GOODBYE: ScenarioContent(
                scenario_type=ScenarioType.SAYING_GOODBYE,
                title="Saying Goodbye",
                description="Learn different ways to say goodbye in Irish English",
                chinese_comfort="学会说再见很重要。爱尔兰人有很多友好的说再见的方式！",
                english_demonstration="Goodbye! See you tomorrow! Take care!",
                irish_vocabulary_notes=[
                    "'See you tomorrow' is common school goodbye",
                    "'Take care' shows you care about the person",
                    "'Cheerio' is informal Irish goodbye"
                ],
                age_group_notes="Ends interactions on positive, caring note"
            )
        }

    def _initialize_irish_vocabulary(self) -> Dict[str, str]:
        """Initialize Irish English vocabulary mappings"""
        return {
            "bathroom": "toilet",
            "elevator": "lift",
            "candy": "sweets",
            "line": "queue",
            "soccer": "football",
            "eraser": "rubber",
            "great": "brilliant",
            "good": "grand",
            "nice": "lovely"
        }

    def get_available_scenarios(self) -> List[ScenarioType]:
        """Get list of available scenario types"""
        return list(self.scenarios.keys())

    def get_scenario_content(self, scenario_type: ScenarioType) -> Optional[ScenarioContent]:
        """Get content for a specific scenario"""
        return self.scenarios.get(scenario_type)

    def validate_age_appropriateness(self, scenario_type: ScenarioType, age: int) -> bool:
        """Validate if scenario is appropriate for child's age"""
        # All scenarios are designed for ages 4-10 (Irish primary school)
        if age < 4 or age > 10:
            return False
        
        scenario = self.scenarios.get(scenario_type)
        if not scenario:
            return False
            
        # All current scenarios are appropriate for the entire age range
        return True

    def create_scenario_session(self, 
                              scenario_type: ScenarioType, 
                              child_id: str) -> Optional[ScenarioSession]:
        """Create a new scenario conversation session"""
        if scenario_type not in self.scenarios:
            return None
            
        session_id = f"{child_id}_{scenario_type.value}_{int(time.time())}"
        
        session = ScenarioSession(
            scenario_type=scenario_type,
            child_id=child_id,
            session_id=session_id,
            turns=[],
            started_at=time.time()
        )
        
        self.active_sessions[session_id] = session
        return session

    def get_chinese_comfort_phase(self, scenario_type: ScenarioType) -> Optional[ConversationTurn]:
        """Generate Chinese comfort phase for scenario with trauma-informed design"""
        scenario = self.scenarios.get(scenario_type)
        if not scenario:
            return None
        
        # Apply trauma-informed processing to comfort content
        comfort_content = self.non_competitive_filter.clean(scenario.chinese_comfort)
        comfort_content = self.journey_narrative.add_to(comfort_content)
            
        return ConversationTurn(
            phase=ConversationPhase.CHINESE_COMFORT,
            speaker="xiao_mei",
            content=comfort_content,
            language="zh-CN",
            timestamp=time.time()
        )

    def get_english_demonstration_phase(self, scenario_type: ScenarioType) -> Optional[ConversationTurn]:
        """Generate English demonstration phase for scenario with trauma-informed design"""
        scenario = self.scenarios.get(scenario_type)
        if not scenario:
            return None
        
        # Apply trauma-informed processing to demonstration content
        demo_content = self.non_competitive_filter.clean(scenario.english_demonstration)
        demo_content = self.journey_narrative.add_to(demo_content)
            
        return ConversationTurn(
            phase=ConversationPhase.ENGLISH_DEMONSTRATION,
            speaker="xiao_mei",
            content=demo_content,
            language="en-IE",
            timestamp=time.time()
        )

    def apply_irish_vocabulary(self, text: str) -> str:
        """Apply Irish English vocabulary preferences to text"""
        irish_text = text
        for american_word, irish_word in self.irish_vocabulary_map.items():
            irish_text = irish_text.replace(american_word, irish_word)
        return irish_text

    def get_scenario_summary(self) -> Dict[str, Any]:
        """Get summary of all available scenarios"""
        return {
            "total_scenarios": len(self.scenarios),
            "scenario_types": [scenario_type.value for scenario_type in self.scenarios.keys()],
            "active_sessions": len(self.active_sessions),
            "irish_vocabulary_mappings": len(self.irish_vocabulary_map)
        }

    def get_session(self, session_id: str) -> Optional[ScenarioSession]:
        """Get an active session by ID"""
        return self.active_sessions.get(session_id)

    def add_turn_to_session(self, session_id: str, turn: ConversationTurn) -> bool:
        """Add a conversation turn to an active session"""
        session = self.active_sessions.get(session_id)
        if session:
            session.turns.append(turn)
            return True
        return False

    def complete_session(self, session_id: str) -> bool:
        """Mark a session as completed"""
        session = self.active_sessions.get(session_id)
        if session:
            session.completed = True
            return True
        return False