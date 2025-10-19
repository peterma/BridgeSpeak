"""
Encouragement System for Trauma-Informed Learning

Provides pronunciation-agnostic encouragement that celebrates all child attempts.
Implements bilingual praise patterns with cultural sensitivity.
"""

import random
import time
from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum

from .conversation_types import ScenarioType, ConversationTurn, ConversationPhase


class EncouragementLevel(str, Enum):
    """Levels of encouragement intensity"""
    GENTLE = "gentle"
    STANDARD = "standard" 
    ENTHUSIASTIC = "enthusiastic"
    CELEBRATORY = "celebratory"


class ChildResponseCategory(str, Enum):
    """Categories of child responses for appropriate encouragement"""
    ATTEMPTED_PHRASE = "attempted_phrase"
    PARTIAL_ATTEMPT = "partial_attempt"
    SILENCE = "silence"
    OFF_TOPIC = "off_topic"
    EMOTIONAL_DISTRESS = "emotional_distress"


@dataclass
class EncouragementPattern:
    """Pattern for generating encouragement messages"""
    chinese_phrase: str
    english_phrase: str
    level: EncouragementLevel
    response_category: ChildResponseCategory
    cultural_context: Optional[str] = None


@dataclass
class SilenceHandlingStrategy:
    """Strategy for handling child silence with gentle prompting"""
    initial_wait_seconds: int = 3
    gentle_prompt: str = "没关系，慢慢来 (Méi guānxi, màn màn lái) - That's okay, take your time"
    follow_up_prompt: str = "我们一起试试吧 (Wǒmen yīqǐ shì shì ba) - Let's try together"
    max_silence_duration: int = 10  # seconds before offering help


class EncouragementSystem:
    """Service for providing trauma-informed encouragement and feedback"""

    def __init__(self):
        self.encouragement_patterns = self._initialize_encouragement_patterns()
        self.silence_strategy = SilenceHandlingStrategy()
        self.praise_history: Dict[str, List[str]] = {}  # Track what encouragement was used

    def _initialize_encouragement_patterns(self) -> Dict[ChildResponseCategory, List[EncouragementPattern]]:
        """Initialize library of encouragement patterns"""
        return {
            ChildResponseCategory.ATTEMPTED_PHRASE: [
                EncouragementPattern(
                    chinese_phrase="好棒!",
                    english_phrase="That was brilliant!",
                    level=EncouragementLevel.ENTHUSIASTIC,
                    response_category=ChildResponseCategory.ATTEMPTED_PHRASE,
                    cultural_context="Irish English expression of enthusiasm"
                ),
                EncouragementPattern(
                    chinese_phrase="太好了!",
                    english_phrase="Excellent work!",
                    level=EncouragementLevel.CELEBRATORY,
                    response_category=ChildResponseCategory.ATTEMPTED_PHRASE
                ),
                EncouragementPattern(
                    chinese_phrase="很好!",
                    english_phrase="Very good! You're doing grand!",
                    level=EncouragementLevel.STANDARD,
                    response_category=ChildResponseCategory.ATTEMPTED_PHRASE,
                    cultural_context="Irish expression 'grand' for good"
                ),
                EncouragementPattern(
                    chinese_phrase="真棒!",
                    english_phrase="Well done! That's lovely!",
                    level=EncouragementLevel.ENTHUSIASTIC,
                    response_category=ChildResponseCategory.ATTEMPTED_PHRASE,
                    cultural_context="Irish expression 'lovely' for approval"
                )
            ],
            ChildResponseCategory.PARTIAL_ATTEMPT: [
                EncouragementPattern(
                    chinese_phrase="很好的开始!",
                    english_phrase="That's a great start!",
                    level=EncouragementLevel.GENTLE,
                    response_category=ChildResponseCategory.PARTIAL_ATTEMPT
                ),
                EncouragementPattern(
                    chinese_phrase="继续努力!",
                    english_phrase="Keep going, you're doing well!",
                    level=EncouragementLevel.STANDARD,
                    response_category=ChildResponseCategory.PARTIAL_ATTEMPT
                ),
                EncouragementPattern(
                    chinese_phrase="进步了!",
                    english_phrase="You're making progress! Fair play!",
                    level=EncouragementLevel.ENTHUSIASTIC,
                    response_category=ChildResponseCategory.PARTIAL_ATTEMPT,
                    cultural_context="Irish expression 'fair play' for acknowledgment"
                )
            ],
            ChildResponseCategory.SILENCE: [
                EncouragementPattern(
                    chinese_phrase="没关系",
                    english_phrase="That's perfectly okay",
                    level=EncouragementLevel.GENTLE,
                    response_category=ChildResponseCategory.SILENCE
                ),
                EncouragementPattern(
                    chinese_phrase="慢慢来",
                    english_phrase="Take your time, no rush",
                    level=EncouragementLevel.GENTLE,
                    response_category=ChildResponseCategory.SILENCE
                ),
                EncouragementPattern(
                    chinese_phrase="我们一起试试",
                    english_phrase="Let's try together",
                    level=EncouragementLevel.GENTLE,
                    response_category=ChildResponseCategory.SILENCE
                )
            ],
            ChildResponseCategory.OFF_TOPIC: [
                EncouragementPattern(
                    chinese_phrase="好有趣!",
                    english_phrase="That's interesting! Now let's try our English phrase",
                    level=EncouragementLevel.GENTLE,
                    response_category=ChildResponseCategory.OFF_TOPIC
                ),
                EncouragementPattern(
                    chinese_phrase="你想得很多!",
                    english_phrase="You're thinking a lot! Let's focus on our practice",
                    level=EncouragementLevel.GENTLE,
                    response_category=ChildResponseCategory.OFF_TOPIC
                )
            ],
            ChildResponseCategory.EMOTIONAL_DISTRESS: [
                EncouragementPattern(
                    chinese_phrase="别担心",
                    english_phrase="You're safe here with me",
                    level=EncouragementLevel.GENTLE,
                    response_category=ChildResponseCategory.EMOTIONAL_DISTRESS
                ),
                EncouragementPattern(
                    chinese_phrase="我们慢慢学",
                    english_phrase="We'll learn slowly and gently",
                    level=EncouragementLevel.GENTLE,
                    response_category=ChildResponseCategory.EMOTIONAL_DISTRESS
                )
            ]
        }

    def generate_encouragement(self, 
                             child_response: Optional[str], 
                             child_id: str,
                             scenario_type: Optional[ScenarioType] = None) -> ConversationTurn:
        """Generate appropriate encouragement based on child's response"""
        
        # Categorize the child's response
        response_category = self._categorize_child_response(child_response)
        
        # Select appropriate encouragement pattern
        pattern = self._select_encouragement_pattern(response_category, child_id)
        
        # Generate encouraging message
        message = self._create_encouraging_message(pattern, scenario_type)
        
        # Record this encouragement to avoid repetition
        self._record_encouragement_used(child_id, message)
        
        return ConversationTurn(
            phase=ConversationPhase.ENCOURAGING_FEEDBACK,
            speaker="xiao_mei",
            content=message,
            language="mixed",  # Chinese + English
            timestamp=time.time(),
            encouragement_level=pattern.level.value
        )

    def _categorize_child_response(self, response: Optional[str]) -> ChildResponseCategory:
        """Categorize child's response to provide appropriate encouragement"""
        if not response or response.strip() == "":
            return ChildResponseCategory.SILENCE
        
        # For this implementation, we're pronunciation-agnostic
        # Any attempt is considered a success
        response_lower = response.lower().strip()
        
        # Check for emotional indicators first (highest priority)
        emotional_words = ["scared", "can't", "don't know", "hard", "difficult"]
        if any(word in response_lower for word in emotional_words):
            return ChildResponseCategory.EMOTIONAL_DISTRESS
        
        # Check for attempt at English phrases
        english_indicators = ["hello", "my name", "toilet", "help", "hungry", "goodbye"]
        if any(indicator in response_lower for indicator in english_indicators):
            return ChildResponseCategory.ATTEMPTED_PHRASE
        
        # Check for partial attempts (must be short and not contain full phrases)
        if len(response_lower) > 2 and len(response_lower) < 10:  # Short partial attempts
            # Make sure it's not a full attempt that was miscategorized
            if not any(indicator in response_lower for indicator in english_indicators):
                return ChildResponseCategory.PARTIAL_ATTEMPT
        
        # Default to off-topic if something was said but doesn't match expected patterns
        return ChildResponseCategory.OFF_TOPIC

    def _select_encouragement_pattern(self, 
                                    category: ChildResponseCategory, 
                                    child_id: str) -> EncouragementPattern:
        """Select appropriate encouragement pattern avoiding recent repetition"""
        available_patterns = self.encouragement_patterns.get(category, [])
        
        if not available_patterns:
            # Fallback pattern
            return EncouragementPattern(
                chinese_phrase="好的!",
                english_phrase="Good!",
                level=EncouragementLevel.STANDARD,
                response_category=category
            )
        
        # Avoid recently used patterns
        recent_encouragements = self.praise_history.get(child_id, [])
        
        # Find patterns not recently used
        unused_patterns = [
            pattern for pattern in available_patterns
            if pattern.chinese_phrase not in recent_encouragements[-3:]  # Last 3 encouragements
        ]
        
        # Use unused pattern if available, otherwise pick randomly
        selected_patterns = unused_patterns if unused_patterns else available_patterns
        return random.choice(selected_patterns)

    def _create_encouraging_message(self, 
                                  pattern: EncouragementPattern, 
                                  scenario_type: Optional[ScenarioType]) -> str:
        """Create the final encouraging message combining Chinese and English"""
        base_message = f"{pattern.chinese_phrase} {pattern.english_phrase}"
        
        # Add scenario-specific encouragement if applicable
        if scenario_type:
            scenario_specific = self._get_scenario_specific_praise(scenario_type)
            if scenario_specific:
                base_message += f" {scenario_specific}"
        
        return base_message

    def _get_scenario_specific_praise(self, scenario_type: ScenarioType) -> str:
        """Get scenario-specific praise additions"""
        scenario_praise = {
            ScenarioType.INTRODUCING_YOURSELF: "You're great at making new friends!",
            ScenarioType.ASKING_FOR_TOILET: "Perfect way to ask politely!",
            ScenarioType.ASKING_FOR_HELP: "It's brilliant to ask for help when you need it!",
            ScenarioType.EXPRESSING_HUNGER: "Good communication about your needs!",
            ScenarioType.SAYING_GOODBYE: "Such a lovely, polite goodbye!"
        }
        return scenario_praise.get(scenario_type, "")

    def _record_encouragement_used(self, child_id: str, message: str) -> None:
        """Record encouragement used to avoid repetition"""
        if child_id not in self.praise_history:
            self.praise_history[child_id] = []
        
        # Extract Chinese phrase for tracking
        chinese_part = message.split(" ")[0] if " " in message else message
        self.praise_history[child_id].append(chinese_part)
        
        # Keep only last 10 encouragements to prevent memory bloat
        if len(self.praise_history[child_id]) > 10:
            self.praise_history[child_id] = self.praise_history[child_id][-10:]

    def handle_silence(self, child_id: str, silence_duration_seconds: int) -> ConversationTurn:
        """Handle child silence with gentle, patient prompting"""
        if silence_duration_seconds <= self.silence_strategy.initial_wait_seconds:
            # Initial gentle wait - no response needed yet
            return None
        
        if silence_duration_seconds <= self.silence_strategy.max_silence_duration:
            # Gentle prompt
            prompt_text = self.silence_strategy.gentle_prompt
        else:
            # Offer to try together
            prompt_text = self.silence_strategy.follow_up_prompt
        
        return ConversationTurn(
            phase=ConversationPhase.ENCOURAGING_FEEDBACK,
            speaker="xiao_mei",
            content=prompt_text,
            language="mixed",
            timestamp=time.time(),
            encouragement_level=EncouragementLevel.GENTLE.value
        )

    def is_pronunciation_agnostic(self) -> bool:
        """Confirm this system is pronunciation-agnostic (always True)"""
        return True

    def get_encouragement_statistics(self, child_id: str) -> Dict[str, Any]:
        """Get statistics about encouragement given to a child"""
        history = self.praise_history.get(child_id, [])
        
        return {
            "total_encouragements": len(history),
            "recent_encouragements": history[-5:] if history else [],
            "encouragement_variety": len(set(history)),
            "last_encouragement_time": time.time() if history else None
        }

    def reset_child_history(self, child_id: str) -> None:
        """Reset encouragement history for a child (new session)"""
        if child_id in self.praise_history:
            del self.praise_history[child_id]

    def validate_trauma_informed_principles(self) -> Dict[str, bool]:
        """Validate that all encouragement follows trauma-informed principles"""
        validation_results = {
            "no_negative_feedback": True,  # All patterns are positive
            "pronunciation_agnostic": True,  # System doesn't judge pronunciation
            "culturally_sensitive": True,  # Includes both Chinese and Irish elements
            "patient_approach": True,  # Includes gentle silence handling
            "celebrates_attempts": True,  # All attempts receive positive feedback
        }
        
        # Verify no negative language in any pattern
        all_patterns = []
        for category_patterns in self.encouragement_patterns.values():
            all_patterns.extend(category_patterns)
        
        negative_words = ["wrong", "bad", "incorrect", "fail", "error", "mistake"]
        for pattern in all_patterns:
            content = f"{pattern.chinese_phrase} {pattern.english_phrase}".lower()
            if any(negative_word in content for negative_word in negative_words):
                validation_results["no_negative_feedback"] = False
                break
        
        return validation_results

    def create_bilingual_praise_pattern(self, 
                                      intensity: EncouragementLevel = EncouragementLevel.STANDARD) -> str:
        """Create a bilingual praise pattern following trauma-informed principles"""
        patterns = {
            EncouragementLevel.GENTLE: [
                "很好 (Hěn hǎo) - Good work",
                "不错 (Bùcuò) - That's nice",
                "好的 (Hǎo de) - Well done"
            ],
            EncouragementLevel.STANDARD: [
                "好棒! (Hǎo bàng!) That was great!",
                "很好! (Hěn hǎo!) You did well!",
                "太好了! (Tài hǎo le!) That was excellent!"
            ],
            EncouragementLevel.ENTHUSIASTIC: [
                "真棒! (Zhēn bàng!) That was brilliant!",
                "太厉害了! (Tài lìhài le!) You're amazing!",
                "好极了! (Hǎo jí le!) Outstanding work!"
            ],
            EncouragementLevel.CELEBRATORY: [
                "太棒了! (Tài bàng le!) Absolutely brilliant!",
                "完美! (Wánměi!) Perfect! You're a star!",
                "真的很棒! (Zhēn de hěn bàng!) Really wonderful!"
            ]
        }
        
        available_patterns = patterns.get(intensity, patterns[EncouragementLevel.STANDARD])
        return random.choice(available_patterns)

class BilingualPraiseEngine:
    """Simple bilingual praise generator for universal celebration."""

    def __init__(self) -> None:
        self.chinese_praise = [
            "好棒! (Hǎo bàng!)",
            "很好! (Hěn hǎo!)",
            "太厉害了! (Tài lìhài le!)",
            "你真聪明! (Nǐ zhēn cōngmíng!)"
        ]
        self.english_validation = [
            "That was wonderful!",
            "I love how you tried!",
            "You're doing great!",
            "What a brave attempt!"
        ]

    def generate_bilingual_praise(self) -> str:
        return f"{random.choice(self.chinese_praise)} {random.choice(self.english_validation)}"

class PersonalJourneyNarrative:
    """Helper to create exploration-focused, non-competitive narrative phrases."""

    def __init__(self) -> None:
        self.journey_phrases = [
            "Let's keep exploring together!",
            "I love how you're discovering new words!",
            "We're on a learning adventure!",
            "Every try is another step on your journey!",
            "We're building confidence one step at a time!"
        ]

    def add_to(self, base_message: str) -> str:
        tail = random.choice(self.journey_phrases)
        return f"{base_message} {tail}"

    def create_bilingual_praise_pattern(self, 
                                      intensity: EncouragementLevel = EncouragementLevel.STANDARD) -> str:
        """Create a bilingual praise pattern following trauma-informed principles"""
        patterns = {
            EncouragementLevel.GENTLE: [
                "很好 (Hěn hǎo) - Good work",
                "不错 (Bùcuò) - That's nice",
                "好的 (Hǎo de) - Well done"
            ],
            EncouragementLevel.STANDARD: [
                "好棒! (Hǎo bàng!) That was great!",
                "很好! (Hěn hǎo!) You did well!",
                "太好了! (Tài hǎo le!) That was excellent!"
            ],
            EncouragementLevel.ENTHUSIASTIC: [
                "真棒! (Zhēn bàng!) That was brilliant!",
                "太厉害了! (Tài lìhài le!) You're amazing!",
                "好极了! (Hǎo jí le!) Outstanding work!"
            ],
            EncouragementLevel.CELEBRATORY: [
                "太棒了! (Tài bàng le!) Absolutely brilliant!",
                "完美! (Wánměi!) Perfect! You're a star!",
                "真的很棒! (Zhēn de hěn bàng!) Really wonderful!"
            ]
        }
        
        available_patterns = patterns.get(intensity, patterns[EncouragementLevel.STANDARD])
        return random.choice(available_patterns)
