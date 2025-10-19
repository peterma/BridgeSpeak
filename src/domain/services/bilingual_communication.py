"""
Bilingual Communication Pattern Service for Xiao Mei

Provides structured bilingual communication patterns that guide children
through Chinese comfort → English demonstration learning sequences.
"""

import asyncio
from dataclasses import dataclass
from typing import List, Dict, Optional, AsyncGenerator
from enum import Enum


class CommunicationPhase(str, Enum):
    """Phases of bilingual communication pattern"""
    CHINESE_COMFORT = "chinese_comfort"
    TRANSITION_PAUSE = "transition_pause"
    ENGLISH_DEMONSTRATION = "english_demonstration"
    PATIENT_WAITING = "patient_waiting"
    BILINGUAL_CELEBRATION = "bilingual_celebration"


@dataclass
class BilingualMessage:
    """A message in the bilingual communication pattern"""
    phase: CommunicationPhase
    content: str
    language: str
    pause_after_ms: int = 0
    emotional_state: str = "friendly_encouraging"
    
    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary for pipeline integration"""
        return {
            "phase": self.phase.value,
            "content": self.content,
            "language": self.language,
            "pause_after_ms": str(self.pause_after_ms),
            "emotional_state": self.emotional_state
        }


@dataclass
class LearningScenario:
    """A complete bilingual learning scenario"""
    scenario_id: str
    topic: str
    chinese_comfort_phrases: List[str]
    english_demonstrations: List[str]
    celebration_phrases: List[str]
    difficulty_level: str = "beginner"


class BilingualCommunicationService:
    """Service for managing bilingual communication patterns and scenarios"""

    def __init__(self):
        self.learning_scenarios = self._initialize_learning_scenarios()
        self.current_scenario: Optional[LearningScenario] = None

    def _initialize_learning_scenarios(self) -> Dict[str, LearningScenario]:
        """Initialize basic learning scenarios for common topics"""
        return {
            "greetings": LearningScenario(
                scenario_id="greetings",
                topic="Basic Greetings",
                chinese_comfort_phrases=[
                    "你好! (Nǐ hǎo!)",
                    "早上好! (Zǎoshang hǎo!)",
                    "晚上好! (Wǎnshang hǎo!)"
                ],
                english_demonstrations=[
                    "Hello!",
                    "Good morning!",
                    "Good evening!"
                ],
                celebration_phrases=[
                    "好棒! (Hǎo bàng!) That was great!",
                    "很好! (Hěn hǎo!) Well done!",
                    "太棒了! (Tài bàng le!) Fantastic!"
                ]
            ),
            "family": LearningScenario(
                scenario_id="family",
                topic="Family Members",
                chinese_comfort_phrases=[
                    "妈妈 (Māma)",
                    "爸爸 (Bàba)",
                    "姐姐 (Jiějie)"
                ],
                english_demonstrations=[
                    "Mummy",
                    "Daddy", 
                    "Sister"
                ],
                celebration_phrases=[
                    "好棒! (Hǎo bàng!) You know your family!",
                    "很好! (Hěn hǎo!) That's right!",
                    "太好了! (Tài hǎo le!) Excellent!"
                ]
            ),
            "colours": LearningScenario(
                scenario_id="colours",
                topic="Colours",
                chinese_comfort_phrases=[
                    "红色 (Hóngsè)",
                    "蓝色 (Lánsè)",
                    "绿色 (Lǜsè)"
                ],
                english_demonstrations=[
                    "Red",
                    "Blue",
                    "Green"
                ],
                celebration_phrases=[
                    "好棒! (Hǎo bàng!) Beautiful colours!",
                    "很好! (Hěn hǎo!) You know your colours!",
                    "太棒了! (Tài bàng le!) Amazing!"
                ]
            )
        }

    def set_learning_scenario(self, scenario_id: str) -> bool:
        """Set the current learning scenario"""
        if scenario_id in self.learning_scenarios:
            self.current_scenario = self.learning_scenarios[scenario_id]
            return True
        return False

    def create_bilingual_sequence(self, chinese_phrase: str, english_phrase: str) -> List[BilingualMessage]:
        """Create a complete bilingual communication sequence"""
        return [
            BilingualMessage(
                phase=CommunicationPhase.CHINESE_COMFORT,
                content=chinese_phrase,
                language="zh-CN",
                pause_after_ms=0,
                emotional_state="friendly_encouraging"
            ),
            BilingualMessage(
                phase=CommunicationPhase.TRANSITION_PAUSE,
                content="",  # Silent pause
                language="",
                pause_after_ms=1000,  # 1 second pause
                emotional_state="patient_waiting"
            ),
            BilingualMessage(
                phase=CommunicationPhase.ENGLISH_DEMONSTRATION,
                content=english_phrase,
                language="en-IE",
                pause_after_ms=500,
                emotional_state="encouraging"
            ),
            BilingualMessage(
                phase=CommunicationPhase.PATIENT_WAITING,
                content="",  # Waiting for child response
                language="",
                pause_after_ms=2000,  # 2 seconds for child to respond
                emotional_state="patient_listening"
            )
        ]

    def create_celebration_sequence(self, celebration_phrase: str) -> List[BilingualMessage]:
        """Create a celebration sequence for successful learning"""
        return [
            BilingualMessage(
                phase=CommunicationPhase.BILINGUAL_CELEBRATION,
                content=celebration_phrase,
                language="mixed",  # Chinese + English
                pause_after_ms=500,
                emotional_state="celebrating"
            )
        ]

    def get_scenario_learning_sequence(self, scenario_id: str, item_index: int = 0) -> List[BilingualMessage]:
        """Get a complete learning sequence for a specific scenario item"""
        if not self.set_learning_scenario(scenario_id):
            return []
        
        scenario = self.current_scenario
        if item_index >= len(scenario.chinese_comfort_phrases):
            return []

        chinese_phrase = scenario.chinese_comfort_phrases[item_index]
        english_phrase = scenario.english_demonstrations[item_index]
        celebration_phrase = scenario.celebration_phrases[item_index % len(scenario.celebration_phrases)]

        # Create the complete sequence
        sequence = self.create_bilingual_sequence(chinese_phrase, english_phrase)
        sequence.extend(self.create_celebration_sequence(celebration_phrase))
        
        return sequence

    async def execute_bilingual_sequence(self, sequence: List[BilingualMessage]) -> AsyncGenerator[BilingualMessage, None]:
        """Execute a bilingual sequence with proper timing"""
        for message in sequence:
            yield message
            
            # Handle pauses
            if message.pause_after_ms > 0:
                await asyncio.sleep(message.pause_after_ms / 1000.0)

    def get_available_scenarios(self) -> Dict[str, str]:
        """Get list of available learning scenarios"""
        return {
            scenario_id: scenario.topic 
            for scenario_id, scenario in self.learning_scenarios.items()
        }

    def validate_bilingual_pattern(self, sequence: List[BilingualMessage]) -> Dict[str, bool]:
        """Validate that a sequence follows proper bilingual patterns"""
        if not sequence:
            return {"valid": False, "reason": "Empty sequence"}

        validation = {
            "has_chinese_comfort": False,
            "has_transition_pause": False, 
            "has_english_demonstration": False,
            "proper_timing": True,
            "valid": True
        }

        phases_found = [msg.phase for msg in sequence]
        
        validation["has_chinese_comfort"] = CommunicationPhase.CHINESE_COMFORT in phases_found
        validation["has_transition_pause"] = CommunicationPhase.TRANSITION_PAUSE in phases_found
        validation["has_english_demonstration"] = CommunicationPhase.ENGLISH_DEMONSTRATION in phases_found

        # Check for proper timing (transition pause should be 1000ms)
        for msg in sequence:
            if msg.phase == CommunicationPhase.TRANSITION_PAUSE and msg.pause_after_ms != 1000:
                validation["proper_timing"] = False

        validation["valid"] = all([
            validation["has_chinese_comfort"],
            validation["has_english_demonstration"],
            validation["proper_timing"]
        ])

        return validation

    def create_adaptive_response(self, child_confidence_level: str, topic: str) -> List[BilingualMessage]:
        """Create adaptive bilingual response based on child's confidence level"""
        if child_confidence_level == "low":
            # More Chinese comfort, slower pace
            return [
                BilingualMessage(
                    phase=CommunicationPhase.CHINESE_COMFORT,
                    content="没关系 (Méi guānxì) - It's okay",
                    language="zh-CN",
                    pause_after_ms=500
                ),
                BilingualMessage(
                    phase=CommunicationPhase.CHINESE_COMFORT,
                    content="我们一起试试 (Wǒmen yīqǐ shìshì) - Let's try together",
                    language="zh-CN",
                    pause_after_ms=1500
                )
            ]
        elif child_confidence_level == "high":
            # More direct English, faster pace
            return [
                BilingualMessage(
                    phase=CommunicationPhase.ENGLISH_DEMONSTRATION,
                    content="You're doing great! Let's try the next one!",
                    language="en-IE",
                    pause_after_ms=500
                )
            ]
        else:
            # Balanced approach
            return self.create_bilingual_sequence(
                "很好! (Hěn hǎo!)",
                "Good job! Let's continue!"
            )

    def create_sophisticated_bilingual_pattern(self, 
                                             context: Dict[str, any]) -> List[BilingualMessage]:
        """Create sophisticated bilingual communication patterns based on context"""
        confidence_level = context.get("confidence_level", "moderate")
        cultural_context = context.get("cultural_context", "neutral")
        lesson_progress = context.get("lesson_progress", "beginning")
        interaction_history = context.get("interaction_history", [])
        
        # Analyze recent performance for pattern selection
        recent_successes = sum(1 for item in interaction_history[-5:] if "success" in str(item))
        recent_struggles = sum(1 for item in interaction_history[-5:] if "struggle" in str(item))
        
        if cultural_context == "chinese_cultural_moment":
            return self._create_chinese_cultural_pattern(confidence_level, lesson_progress)
        elif cultural_context == "irish_cultural_moment":
            return self._create_irish_cultural_pattern(confidence_level, lesson_progress)
        elif recent_struggles >= 3:
            return self._create_support_intensive_pattern(confidence_level)
        elif recent_successes >= 3:
            return self._create_confidence_building_pattern(confidence_level)
        else:
            return self._create_progressive_difficulty_pattern(confidence_level, lesson_progress)

    def _create_chinese_cultural_pattern(self, confidence_level: str, lesson_progress: str) -> List[BilingualMessage]:
        """Create pattern emphasizing Chinese cultural comfort"""
        return [
            BilingualMessage(
                phase=CommunicationPhase.CHINESE_COMFORT,
                content="我们中国人很聪明 (Wǒmen zhōngguó rén hěn cōngmíng) - We Chinese people are very smart",
                language="zh-CN",
                pause_after_ms=1000,
                emotional_state="cultural_pride"
            ),
            BilingualMessage(
                phase=CommunicationPhase.TRANSITION_PAUSE,
                content="",
                language="",
                pause_after_ms=1500,
                emotional_state="confident_transition"
            ),
            BilingualMessage(
                phase=CommunicationPhase.ENGLISH_DEMONSTRATION,
                content="And now we can show our Irish friends how well we speak English too!",
                language="en-IE",
                pause_after_ms=800,
                emotional_state="cultural_bridge"
            )
        ]

    def _create_irish_cultural_pattern(self, confidence_level: str, lesson_progress: str) -> List[BilingualMessage]:
        """Create pattern emphasizing Irish cultural integration"""
        return [
            BilingualMessage(
                phase=CommunicationPhase.CHINESE_COMFORT,
                content="在爱尔兰我们也很棒 (Zài àiěrlán wǒmen yě hěn bàng) - In Ireland we are also wonderful",
                language="zh-CN",
                pause_after_ms=1000,
                emotional_state="cultural_integration"
            ),
            BilingualMessage(
                phase=CommunicationPhase.TRANSITION_PAUSE,
                content="",
                language="",
                pause_after_ms=1000,
                emotional_state="bridging"
            ),
            BilingualMessage(
                phase=CommunicationPhase.ENGLISH_DEMONSTRATION,
                content="Brilliant! Just like our Irish friends say - we belong here too!",
                language="en-IE",
                pause_after_ms=600,
                emotional_state="belonging"
            )
        ]

    def _create_support_intensive_pattern(self, confidence_level: str) -> List[BilingualMessage]:
        """Create intensive support pattern for struggling children"""
        return [
            BilingualMessage(
                phase=CommunicationPhase.CHINESE_COMFORT,
                content="没关系，慢慢来 (Méi guānxì, màn màn lái) - It's okay, take your time",
                language="zh-CN",
                pause_after_ms=2000,
                emotional_state="patient_support"
            ),
            BilingualMessage(
                phase=CommunicationPhase.CHINESE_COMFORT,
                content="每个人都需要练习 (Měi gè rén dōu xūyào liànxí) - Everyone needs practice",
                language="zh-CN",
                pause_after_ms=2000,
                emotional_state="normalization"
            ),
            BilingualMessage(
                phase=CommunicationPhase.TRANSITION_PAUSE,
                content="",
                language="",
                pause_after_ms=2000,
                emotional_state="gentle_transition"
            ),
            BilingualMessage(
                phase=CommunicationPhase.ENGLISH_DEMONSTRATION,
                content="Let's try together, one small step at a time",
                language="en-IE",
                pause_after_ms=1500,
                emotional_state="collaborative_support"
            )
        ]

    def _create_confidence_building_pattern(self, confidence_level: str) -> List[BilingualMessage]:
        """Create confidence building pattern for successful children"""
        return [
            BilingualMessage(
                phase=CommunicationPhase.CHINESE_COMFORT,
                content="你真的很棒! (Nǐ zhēn de hěn bàng!) - You're really amazing!",
                language="zh-CN",
                pause_after_ms=800,
                emotional_state="enthusiastic_praise"
            ),
            BilingualMessage(
                phase=CommunicationPhase.TRANSITION_PAUSE,
                content="",
                language="",
                pause_after_ms=500,
                emotional_state="excited_transition"
            ),
            BilingualMessage(
                phase=CommunicationPhase.ENGLISH_DEMONSTRATION,
                content="You're ready for something more challenging - let's go!",
                language="en-IE",
                pause_after_ms=500,
                emotional_state="confidence_boosting"
            )
        ]

    def _create_progressive_difficulty_pattern(self, confidence_level: str, lesson_progress: str) -> List[BilingualMessage]:
        """Create progressive difficulty pattern based on lesson progress"""
        if lesson_progress == "beginning":
            return [
                BilingualMessage(
                    phase=CommunicationPhase.CHINESE_COMFORT,
                    content="我们开始学习吧 (Wǒmen kāishǐ xuéxí ba) - Let's start learning",
                    language="zh-CN",
                    pause_after_ms=1000,
                    emotional_state="gentle_start"
                ),
                BilingualMessage(
                    phase=CommunicationPhase.TRANSITION_PAUSE,
                    content="",
                    language="",
                    pause_after_ms=1000,
                    emotional_state="prepared_transition"
                ),
                BilingualMessage(
                    phase=CommunicationPhase.ENGLISH_DEMONSTRATION,
                    content="Let's begin with something easy and fun!",
                    language="en-IE",
                    pause_after_ms=800,
                    emotional_state="encouraging_start"
                )
            ]
        elif lesson_progress == "middle":
            return [
                BilingualMessage(
                    phase=CommunicationPhase.CHINESE_COMFORT,
                    content="你学得很快 (Nǐ xué de hěn kuài) - You're learning quickly",
                    language="zh-CN",
                    pause_after_ms=800,
                    emotional_state="progress_acknowledgment"
                ),
                BilingualMessage(
                    phase=CommunicationPhase.ENGLISH_DEMONSTRATION,
                    content="Now let's try something a bit more interesting!",
                    language="en-IE",
                    pause_after_ms=600,
                    emotional_state="progression_excitement"
                )
            ]
        else:  # advanced
            return [
                BilingualMessage(
                    phase=CommunicationPhase.ENGLISH_DEMONSTRATION,
                    content="You're doing brilliantly! Ready for the advanced level?",
                    language="en-IE",
                    pause_after_ms=500,
                    emotional_state="advanced_confidence"
                ),
                BilingualMessage(
                    phase=CommunicationPhase.CHINESE_COMFORT,
                    content="你已经很厉害了! (Nǐ yǐjīng hěn lìhài le!) - You're already very capable!",
                    language="zh-CN",
                    pause_after_ms=600,
                    emotional_state="advanced_validation"
                )
            ]

    def create_contextual_switching_logic(self, child_context: Dict[str, any]) -> Dict[str, any]:
        """Create sophisticated contextual switching logic based on comprehensive child context"""
        confidence_trend = child_context.get("confidence_trend", "stable")
        time_in_lesson = child_context.get("time_in_lesson_minutes", 0)
        attention_indicators = child_context.get("attention_indicators", "focused")
        energy_level = child_context.get("energy_level", "moderate")
        
        switching_strategy = {
            "primary_language_ratio": 0.5,  # 50% Chinese, 50% English by default
            "pause_duration_modifier": 1.0,  # Normal pause timing
            "complexity_level": "moderate",
            "cultural_emphasis": "balanced",
            "interaction_pace": "standard",
            "reasoning": ""
        }
        
        # Adjust based on confidence trend
        if confidence_trend == "declining":
            switching_strategy["primary_language_ratio"] = 0.7  # More Chinese comfort
            switching_strategy["pause_duration_modifier"] = 1.5  # Longer pauses
            switching_strategy["complexity_level"] = "simplified"
            switching_strategy["cultural_emphasis"] = "chinese_comfort"
            switching_strategy["reasoning"] = "Increasing Chinese comfort due to declining confidence"
            
        elif confidence_trend == "improving":
            switching_strategy["primary_language_ratio"] = 0.3  # More English challenge
            switching_strategy["pause_duration_modifier"] = 0.8  # Faster pace
            switching_strategy["complexity_level"] = "enhanced"
            switching_strategy["cultural_emphasis"] = "irish_integration"
            switching_strategy["reasoning"] = "Encouraging English growth due to improving confidence"
        
        # Adjust based on attention and energy
        if attention_indicators == "distracted" or energy_level == "low":
            switching_strategy["interaction_pace"] = "slow"
            switching_strategy["pause_duration_modifier"] *= 1.3
            switching_strategy["complexity_level"] = "simplified"
            switching_strategy["reasoning"] += " | Adapting to low attention/energy"
            
        elif energy_level == "high":
            switching_strategy["interaction_pace"] = "dynamic"
            switching_strategy["pause_duration_modifier"] *= 0.9
            switching_strategy["cultural_emphasis"] = "balanced_energetic"
            switching_strategy["reasoning"] += " | Matching high energy with dynamic interaction"
        
        # Adjust based on lesson duration
        if time_in_lesson > 15:  # After 15 minutes
            switching_strategy["primary_language_ratio"] = min(0.8, switching_strategy["primary_language_ratio"] + 0.2)
            switching_strategy["complexity_level"] = "simplified"
            switching_strategy["reasoning"] += " | Increasing comfort due to lesson duration"
        
        return switching_strategy

    def create_smooth_cultural_transitions(self, 
                                         from_context: str, 
                                         to_context: str) -> List[BilingualMessage]:
        """Create smooth transitions between cultural contexts"""
        transition_phrases = {
            ("chinese_cultural", "irish_cultural"): [
                BilingualMessage(
                    phase=CommunicationPhase.CHINESE_COMFORT,
                    content="我们中国人很特别 (Wǒmen zhōngguó rén hěn tèbié) - We Chinese people are special",
                    language="zh-CN",
                    pause_after_ms=1000,
                    emotional_state="cultural_pride"
                ),
                BilingualMessage(
                    phase=CommunicationPhase.TRANSITION_PAUSE,
                    content="",
                    language="",
                    pause_after_ms=1000,
                    emotional_state="bridging"
                ),
                BilingualMessage(
                    phase=CommunicationPhase.ENGLISH_DEMONSTRATION,
                    content="And Irish people have wonderful traditions too - we can appreciate both!",
                    language="en-IE",
                    pause_after_ms=800,
                    emotional_state="cultural_bridge"
                )
            ],
            ("irish_cultural", "chinese_cultural"): [
                BilingualMessage(
                    phase=CommunicationPhase.ENGLISH_DEMONSTRATION,
                    content="Irish culture is brilliant, and it makes our Chinese heritage even more special!",
                    language="en-IE",
                    pause_after_ms=1000,
                    emotional_state="cultural_appreciation"
                ),
                BilingualMessage(
                    phase=CommunicationPhase.TRANSITION_PAUSE,
                    content="",
                    language="",
                    pause_after_ms=1000,
                    emotional_state="thoughtful_transition"
                ),
                BilingualMessage(
                    phase=CommunicationPhase.CHINESE_COMFORT,
                    content="我们可以两种文化都爱 (Wǒmen kěyǐ liǎng zhǒng wénhuà dōu ài) - We can love both cultures",
                    language="zh-CN",
                    pause_after_ms=1200,
                    emotional_state="inclusive_love"
                )
            ]
        }
        
        return transition_phrases.get((from_context, to_context), [
            BilingualMessage(
                phase=CommunicationPhase.TRANSITION_PAUSE,
                content="",
                language="",
                pause_after_ms=1000,
                emotional_state="gentle_transition"
            )
        ])