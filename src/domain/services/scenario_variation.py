"""
Scenario Variation Service

Provides multiple conversation paths and variations for each scenario to prevent monotony
and allow repeated practice with different contexts and complexity levels.
"""

import random
import time
from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum

from .conversation_types import ScenarioType, ScenarioContent


class VariationType(str, Enum):
    """Types of scenario variations"""
    CONTEXT_CHANGE = "context_change"
    COMPLEXITY_LEVEL = "complexity_level"
    DIALOGUE_PARTNER = "dialogue_partner"
    SITUATIONAL_MODIFIER = "situational_modifier"


class ComplexityLevel(str, Enum):
    """Complexity levels for progressive learning"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


@dataclass
class ScenarioVariation:
    """A specific variation of a scenario"""
    variation_id: str
    base_scenario: ScenarioType
    variation_type: VariationType
    complexity_level: ComplexityLevel
    chinese_comfort: str
    english_demonstration: str
    context_description: str
    dialogue_partner: str = "teacher"  # teacher, friend, adult, etc.


@dataclass
class ConversationPath:
    """A complete conversation path with multiple variations"""
    path_id: str
    scenario_type: ScenarioType
    variations: List[ScenarioVariation]
    recommended_sequence: List[str]  # Order of variation_ids
    total_practice_time_minutes: int


class ScenarioVariationService:
    """Service for managing scenario variations and conversation paths"""

    def __init__(self):
        self.variation_library = self._initialize_variations()
        self.conversation_paths = self._initialize_conversation_paths()
        self.child_progress_tracker: Dict[str, Dict[str, Any]] = {}

    def _initialize_variations(self) -> Dict[ScenarioType, List[ScenarioVariation]]:
        """Initialize library of scenario variations"""
        return {
            ScenarioType.INTRODUCING_YOURSELF: [
                ScenarioVariation(
                    variation_id="intro_classroom",
                    base_scenario=ScenarioType.INTRODUCING_YOURSELF,
                    variation_type=VariationType.CONTEXT_CHANGE,
                    complexity_level=ComplexityLevel.BEGINNER,
                    chinese_comfort="在教室里，我们来练习自我介绍。新朋友想认识你！",
                    english_demonstration="Hello! My name is [name]. Nice to meet you!",
                    context_description="Meeting new classmates in school",
                    dialogue_partner="classmate"
                ),
                ScenarioVariation(
                    variation_id="intro_playground",
                    base_scenario=ScenarioType.INTRODUCING_YOURSELF,
                    variation_type=VariationType.CONTEXT_CHANGE,
                    complexity_level=ComplexityLevel.BEGINNER,
                    chinese_comfort="在操场上，有个孩子想和你一起玩。我们来自我介绍吧！",
                    english_demonstration="Hi there! I'm [name]. Would you like to play together?",
                    context_description="Meeting children on the playground",
                    dialogue_partner="potential_friend"
                ),
                ScenarioVariation(
                    variation_id="intro_detailed",
                    base_scenario=ScenarioType.INTRODUCING_YOURSELF,
                    variation_type=VariationType.COMPLEXITY_LEVEL,
                    complexity_level=ComplexityLevel.INTERMEDIATE,
                    chinese_comfort="现在我们练习更详细的自我介绍，包括年龄和兴趣。",
                    english_demonstration="Hello! My name is [name]. I'm [age] years old and I'm from China. I like [hobby].",
                    context_description="Detailed introduction with age and interests",
                    dialogue_partner="teacher"
                )
            ],
            ScenarioType.ASKING_FOR_TOILET: [
                ScenarioVariation(
                    variation_id="toilet_urgent",
                    base_scenario=ScenarioType.ASKING_FOR_TOILET,
                    variation_type=VariationType.SITUATIONAL_MODIFIER,
                    complexity_level=ComplexityLevel.BEGINNER,
                    chinese_comfort="有时候我们很急需要上厕所。这时候要礼貌但快速地问。",
                    english_demonstration="Excuse me, I really need the toilet, please!",
                    context_description="Urgent bathroom need situation",
                    dialogue_partner="teacher"
                ),
                ScenarioVariation(
                    variation_id="toilet_polite",
                    base_scenario=ScenarioType.ASKING_FOR_TOILET,
                    variation_type=VariationType.COMPLEXITY_LEVEL,
                    complexity_level=ComplexityLevel.INTERMEDIATE,
                    chinese_comfort="我们学习更礼貌地问厕所在哪里，也解释原因。",
                    english_demonstration="Excuse me, teacher. May I please use the toilet? I need to go.",
                    context_description="Very polite request with explanation",
                    dialogue_partner="teacher"
                ),
                ScenarioVariation(
                    variation_id="toilet_friend",
                    base_scenario=ScenarioType.ASKING_FOR_TOILET,
                    variation_type=VariationType.DIALOGUE_PARTNER,
                    complexity_level=ComplexityLevel.BEGINNER,
                    chinese_comfort="有时候我们问朋友厕所在哪里。这样说会更自然。",
                    english_demonstration="Hey, do you know where the toilet is?",
                    context_description="Asking a friend for directions",
                    dialogue_partner="friend"
                )
            ],
            ScenarioType.ASKING_FOR_HELP: [
                ScenarioVariation(
                    variation_id="help_homework",
                    base_scenario=ScenarioType.ASKING_FOR_HELP,
                    variation_type=VariationType.CONTEXT_CHANGE,
                    complexity_level=ComplexityLevel.BEGINNER,
                    chinese_comfort="做作业时遇到困难，我们来学习怎么请求帮助。",
                    english_demonstration="Can you help me with this, please? I don't understand.",
                    context_description="Asking for help with schoolwork",
                    dialogue_partner="teacher"
                ),
                ScenarioVariation(
                    variation_id="help_lost",
                    base_scenario=ScenarioType.ASKING_FOR_HELP,
                    variation_type=VariationType.SITUATIONAL_MODIFIER,
                    complexity_level=ComplexityLevel.INTERMEDIATE,
                    chinese_comfort="如果你迷路了，要勇敢地向大人求助。",
                    english_demonstration="Excuse me, I'm lost. Can you help me find my classroom, please?",
                    context_description="Getting lost and asking for directions",
                    dialogue_partner="adult"
                ),
                ScenarioVariation(
                    variation_id="help_hurt",
                    base_scenario=ScenarioType.ASKING_FOR_HELP,
                    variation_type=VariationType.SITUATIONAL_MODIFIER,
                    complexity_level=ComplexityLevel.ADVANCED,
                    chinese_comfort="如果受伤了，要马上告诉大人。这很重要！",
                    english_demonstration="Help, please! I hurt myself. Can you get a teacher?",
                    context_description="Asking for help when injured",
                    dialogue_partner="adult"
                )
            ],
            ScenarioType.EXPRESSING_HUNGER: [
                ScenarioVariation(
                    variation_id="hunger_lunch",
                    base_scenario=ScenarioType.EXPRESSING_HUNGER,
                    variation_type=VariationType.CONTEXT_CHANGE,
                    complexity_level=ComplexityLevel.BEGINNER,
                    chinese_comfort="午餐时间到了！我们学习在食堂怎么说饿了。",
                    english_demonstration="I'm hungry. What's for lunch today?",
                    context_description="Lunch time in school canteen",
                    dialogue_partner="lunch_staff"
                ),
                ScenarioVariation(
                    variation_id="hunger_snack",
                    base_scenario=ScenarioType.EXPRESSING_HUNGER,
                    variation_type=VariationType.COMPLEXITY_LEVEL,
                    complexity_level=ComplexityLevel.INTERMEDIATE,
                    chinese_comfort="课间饿了，我们学习礼貌地问能不能吃点心。",
                    english_demonstration="I'm feeling a bit hungry. May I have a snack, please?",
                    context_description="Asking for snack during break time",
                    dialogue_partner="teacher"
                ),
                ScenarioVariation(
                    variation_id="hunger_home",
                    base_scenario=ScenarioType.EXPRESSING_HUNGER,
                    variation_type=VariationType.CONTEXT_CHANGE,
                    complexity_level=ComplexityLevel.BEGINNER,
                    chinese_comfort="回到家，我们告诉家人我们饿了。",
                    english_demonstration="Mum, I'm hungry. What's for dinner?",
                    context_description="Expressing hunger at home",
                    dialogue_partner="parent"
                )
            ],
            ScenarioType.SAYING_GOODBYE: [
                ScenarioVariation(
                    variation_id="goodbye_end_day",
                    base_scenario=ScenarioType.SAYING_GOODBYE,
                    variation_type=VariationType.CONTEXT_CHANGE,
                    complexity_level=ComplexityLevel.BEGINNER,
                    chinese_comfort="放学了，我们和老师同学说再见。",
                    english_demonstration="Goodbye, teacher! See you tomorrow!",
                    context_description="End of school day farewell",
                    dialogue_partner="teacher"
                ),
                ScenarioVariation(
                    variation_id="goodbye_friend",
                    base_scenario=ScenarioType.SAYING_GOODBYE,
                    variation_type=VariationType.DIALOGUE_PARTNER,
                    complexity_level=ComplexityLevel.BEGINNER,
                    chinese_comfort="和朋友说再见时，我们可以说得更随意一些。",
                    english_demonstration="See you later! Have a great day!",
                    context_description="Casual goodbye to friends",
                    dialogue_partner="friend"
                ),
                ScenarioVariation(
                    variation_id="goodbye_weekend",
                    base_scenario=ScenarioType.SAYING_GOODBYE,
                    variation_type=VariationType.SITUATIONAL_MODIFIER,
                    complexity_level=ComplexityLevel.INTERMEDIATE,
                    chinese_comfort="周五放学，我们要说'周末愉快'。",
                    english_demonstration="Goodbye! Have a lovely weekend! See you on Monday!",
                    context_description="Friday afternoon farewell",
                    dialogue_partner="teacher"
                )
            ]
        }

    def _initialize_conversation_paths(self) -> Dict[ScenarioType, List[ConversationPath]]:
        """Initialize conversation paths with recommended sequences"""
        paths = {}
        
        for scenario_type, variations in self.variation_library.items():
            # Create beginner path
            beginner_variations = [v for v in variations if v.complexity_level == ComplexityLevel.BEGINNER]
            beginner_path = ConversationPath(
                path_id=f"{scenario_type.value}_beginner_path",
                scenario_type=scenario_type,
                variations=beginner_variations,
                recommended_sequence=[v.variation_id for v in beginner_variations],
                total_practice_time_minutes=5
            )
            
            # Create progressive path (all levels)
            all_variations = sorted(variations, key=lambda x: 
                                  ['beginner', 'intermediate', 'advanced'].index(x.complexity_level.value))
            progressive_path = ConversationPath(
                path_id=f"{scenario_type.value}_progressive_path",
                scenario_type=scenario_type,
                variations=all_variations,
                recommended_sequence=[v.variation_id for v in all_variations],
                total_practice_time_minutes=10
            )
            
            paths[scenario_type] = [beginner_path, progressive_path]
        
        return paths

    def get_scenario_variations(self, scenario_type: ScenarioType) -> List[ScenarioVariation]:
        """Get all variations for a scenario type"""
        return self.variation_library.get(scenario_type, [])

    def get_conversation_paths(self, scenario_type: ScenarioType) -> List[ConversationPath]:
        """Get conversation paths for a scenario type"""
        return self.conversation_paths.get(scenario_type, [])

    def select_variation_for_child(self, 
                                 scenario_type: ScenarioType, 
                                 child_id: str,
                                 preferred_complexity: Optional[ComplexityLevel] = None) -> Optional[ScenarioVariation]:
        """Select appropriate variation based on child's progress and preferences"""
        variations = self.get_scenario_variations(scenario_type)
        if not variations:
            return None
        
        # Track child's practice history
        if child_id not in self.child_progress_tracker:
            self.child_progress_tracker[child_id] = {
                "practiced_variations": set(),
                "complexity_progress": ComplexityLevel.BEGINNER,
                "session_count": 0
            }
        
        child_progress = self.child_progress_tracker[child_id]
        
        # Filter out recently practiced variations
        available_variations = [
            v for v in variations 
            if v.variation_id not in child_progress["practiced_variations"]
        ]
        
        # If all practiced, reset and use all
        if not available_variations:
            available_variations = variations
            child_progress["practiced_variations"].clear()
        
        # Filter by complexity if specified
        if preferred_complexity:
            complexity_variations = [
                v for v in available_variations 
                if v.complexity_level == preferred_complexity
            ]
            if complexity_variations:
                available_variations = complexity_variations
            else:
                # If no variations at preferred complexity, don't change available_variations
                # This ensures we return None if the specific complexity isn't available
                if not any(v.complexity_level == preferred_complexity for v in variations):
                    return None
        
        # Select variation
        selected = random.choice(available_variations)
        
        # Record practice
        child_progress["practiced_variations"].add(selected.variation_id)
        child_progress["session_count"] += 1
        
        return selected

    def create_varied_conversation_sequence(self, 
                                          scenario_type: ScenarioType, 
                                          child_id: str,
                                          session_length_minutes: int = 5) -> List[ScenarioVariation]:
        """Create a sequence of varied conversations for practice session"""
        target_variations = max(1, session_length_minutes // 2)  # ~2 minutes per variation
        
        sequence = []
        for _ in range(target_variations):
            variation = self.select_variation_for_child(scenario_type, child_id)
            if variation:
                sequence.append(variation)
        
        return sequence

    def get_recommended_next_variation(self, 
                                     scenario_type: ScenarioType, 
                                     child_id: str) -> Optional[ScenarioVariation]:
        """Get recommended next variation based on progression logic"""
        if child_id not in self.child_progress_tracker:
            # Start with beginner variation
            return self.select_variation_for_child(scenario_type, child_id, ComplexityLevel.BEGINNER)
        
        child_progress = self.child_progress_tracker[child_id]
        current_complexity = child_progress["complexity_progress"]
        session_count = child_progress["session_count"]
        
        # Progress complexity after several successful sessions
        if session_count >= 3 and current_complexity == ComplexityLevel.BEGINNER:
            child_progress["complexity_progress"] = ComplexityLevel.INTERMEDIATE
            return self.select_variation_for_child(scenario_type, child_id, ComplexityLevel.INTERMEDIATE)
        elif session_count >= 6 and current_complexity == ComplexityLevel.INTERMEDIATE:
            child_progress["complexity_progress"] = ComplexityLevel.ADVANCED
            return self.select_variation_for_child(scenario_type, child_id, ComplexityLevel.ADVANCED)
        
        # Continue with current complexity level
        return self.select_variation_for_child(scenario_type, child_id, current_complexity)

    def adjust_difficulty_based_on_performance(self, 
                                             child_id: str, 
                                             scenario_type: ScenarioType,
                                             performance_indicator: str) -> ComplexityLevel:
        """Adaptively adjust difficulty based on child's performance"""
        if child_id not in self.child_progress_tracker:
            return ComplexityLevel.BEGINNER
        
        child_progress = self.child_progress_tracker[child_id]
        current_complexity = child_progress["complexity_progress"]
        
        # Performance-based adjustment
        if performance_indicator == "struggling":
            # Move back one level if struggling
            if current_complexity == ComplexityLevel.ADVANCED:
                child_progress["complexity_progress"] = ComplexityLevel.INTERMEDIATE
                return ComplexityLevel.INTERMEDIATE
            elif current_complexity == ComplexityLevel.INTERMEDIATE:
                child_progress["complexity_progress"] = ComplexityLevel.BEGINNER
                return ComplexityLevel.BEGINNER
            else:
                return ComplexityLevel.BEGINNER
        
        elif performance_indicator == "excelling":
            # Move up one level if excelling
            if current_complexity == ComplexityLevel.BEGINNER:
                child_progress["complexity_progress"] = ComplexityLevel.INTERMEDIATE
                return ComplexityLevel.INTERMEDIATE
            elif current_complexity == ComplexityLevel.INTERMEDIATE:
                child_progress["complexity_progress"] = ComplexityLevel.ADVANCED
                return ComplexityLevel.ADVANCED
            else:
                return ComplexityLevel.ADVANCED
        
        # Default: maintain current level
        return current_complexity

    def get_difficulty_recommendation(self, 
                                    child_id: str,
                                    scenario_type: ScenarioType,
                                    recent_interactions: List[str]) -> Dict[str, Any]:
        """Analyze recent interactions and recommend difficulty adjustments"""
        if child_id not in self.child_progress_tracker:
            return {
                "current_level": ComplexityLevel.BEGINNER,
                "recommended_action": "start_beginner",
                "confidence": 1.0,
                "reasoning": "New learner - starting with beginner level"
            }
        
        child_progress = self.child_progress_tracker[child_id]
        current_complexity = child_progress["complexity_progress"]
        session_count = child_progress["session_count"]
        
        # Analyze performance patterns
        if len(recent_interactions) >= 3:
            successful_attempts = sum(1 for interaction in recent_interactions if len(interaction) > 0)
            success_rate = successful_attempts / len(recent_interactions)
            
            if success_rate >= 0.8 and session_count >= 2:
                return {
                    "current_level": current_complexity,
                    "recommended_action": "increase_difficulty",
                    "confidence": success_rate,
                    "reasoning": f"High success rate ({success_rate:.1%}) indicates readiness for advancement"
                }
            elif success_rate <= 0.4:
                return {
                    "current_level": current_complexity,
                    "recommended_action": "decrease_difficulty",
                    "confidence": 1.0 - success_rate,
                    "reasoning": f"Low success rate ({success_rate:.1%}) suggests need for simpler variations"
                }
        
        return {
            "current_level": current_complexity,
            "recommended_action": "maintain_level",
            "confidence": 0.7,
            "reasoning": "Insufficient data or stable performance - maintaining current level"
        }

    def apply_contextual_changes(self, base_content: str, variation: ScenarioVariation) -> str:
        """Apply contextual changes to prevent monotony"""
        context_modifiers = {
            "classroom": ["in class", "at school", "with classmates"],
            "playground": ["outside", "during break", "while playing"],
            "canteen": ["at lunch", "in the dining room", "with lunch staff"],
            "home": ["at home", "with family", "after school"]
        }
        
        # Simple context injection (in real implementation, this would be more sophisticated)
        if variation.context_description:
            return f"{base_content} ({variation.context_description})"
        
        return base_content

    def get_child_progress_summary(self, child_id: str) -> Dict[str, Any]:
        """Get progress summary for a child across all scenarios"""
        if child_id not in self.child_progress_tracker:
            return {
                "total_sessions": 0,
                "current_complexity": ComplexityLevel.BEGINNER,
                "practiced_variations": 0,
                "ready_for_next_level": False
            }
        
        progress = self.child_progress_tracker[child_id]
        return {
            "total_sessions": progress["session_count"],
            "current_complexity": progress["complexity_progress"],
            "practiced_variations": len(progress["practiced_variations"]),
            "ready_for_next_level": progress["session_count"] % 3 == 0 and progress["session_count"] > 0
        }

    def reset_child_progress(self, child_id: str) -> None:
        """Reset child's progress (new learning period)"""
        if child_id in self.child_progress_tracker:
            del self.child_progress_tracker[child_id]

    def get_variation_statistics(self) -> Dict[str, Any]:
        """Get statistics about available variations"""
        stats = {
            "total_scenarios": len(self.variation_library),
            "total_variations": 0,
            "variations_by_complexity": {level.value: 0 for level in ComplexityLevel},
            "variations_by_type": {vtype.value: 0 for vtype in VariationType}
        }
        
        for variations in self.variation_library.values():
            stats["total_variations"] += len(variations)
            for variation in variations:
                stats["variations_by_complexity"][variation.complexity_level.value] += 1
                stats["variations_by_type"][variation.variation_type.value] += 1
        
        return stats