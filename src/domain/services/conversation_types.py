"""
Shared conversation types and enums

This module contains shared types used across conversation services to avoid circular imports.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
import time


class ScenarioType(str, Enum):
    """Available conversation scenarios"""
    INTRODUCING_YOURSELF = "introducing_yourself"
    ASKING_FOR_TOILET = "asking_for_toilet"
    ASKING_FOR_HELP = "asking_for_help"
    EXPRESSING_HUNGER = "expressing_hunger"
    SAYING_GOODBYE = "saying_goodbye"


class ConversationPhase(str, Enum):
    """Phases of conversation flow"""
    CHINESE_COMFORT = "chinese_comfort"
    ENGLISH_DEMONSTRATION = "english_demonstration"
    CHILD_PRACTICE = "child_practice"
    ENCOURAGING_FEEDBACK = "encouraging_feedback"


@dataclass
class ConversationTurn:
    """A single turn in the conversation"""
    phase: ConversationPhase
    speaker: str  # "xiao_mei" or "child"
    content: str
    language: str  # "zh-CN", "en-IE", or "mixed"
    timestamp: float
    encouragement_level: str = "standard"  # "gentle", "standard", "enthusiastic"


@dataclass
class ScenarioContent:
    """Content structure for a conversation scenario"""
    scenario_type: ScenarioType
    title: str
    description: str
    chinese_comfort: str
    english_demonstration: str
    irish_vocabulary_notes: List[str]
    age_group_notes: str
    difficulty_level: int = 1  # 1-5 scale


@dataclass
class ScenarioSession:
    """A complete scenario conversation session"""
    scenario_type: ScenarioType
    child_id: str
    session_id: str
    turns: List[ConversationTurn]
    started_at: float
    completed: bool = False
    success_indicators: List[str] = None

    def __post_init__(self):
        if self.success_indicators is None:
            self.success_indicators = []
