"""
Body Language Response System for Xiao Mei

Provides sophisticated body language responses based on child interactions,
emotional states, and contextual triggers for more expressive character behavior.
"""

import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set
from enum import Enum

from .xiaomei_state import XiaoMeiState


class InteractionTrigger(str, Enum):
    """Triggers that cause body language responses"""
    CHILD_SUCCESS = "child_success"
    CHILD_STRUGGLE = "child_struggle"
    CHILD_SILENCE = "child_silence"
    CHILD_EXCITEMENT = "child_excitement"
    CHILD_CONFUSION = "child_confusion"
    LESSON_START = "lesson_start"
    LESSON_END = "lesson_end"
    ENCOURAGEMENT_NEEDED = "encouragement_needed"
    CELEBRATION_TIME = "celebration_time"


class BodyLanguageIntensity(str, Enum):
    """Intensity levels for body language responses"""
    SUBTLE = "subtle"
    MODERATE = "moderate"
    EXPRESSIVE = "expressive"
    ENTHUSIASTIC = "enthusiastic"


@dataclass
class BodyLanguageResponse:
    """A specific body language response configuration"""
    gesture_type: str
    intensity: BodyLanguageIntensity
    duration_ms: int
    facial_complement: str
    animation_sequence: List[str]
    audio_cues: List[str] = field(default_factory=list)
    
    def to_animation_config(self) -> Dict[str, any]:
        """Convert to animation configuration for video service"""
        return {
            "gesture": self.gesture_type,
            "intensity": self.intensity.value,
            "duration": self.duration_ms,
            "facial_expression": self.facial_complement,
            "sequence": self.animation_sequence,
            "audio_cues": self.audio_cues
        }


@dataclass
class InteractionContext:
    """Context about child interactions for body language decisions"""
    recent_success_count: int = 0
    recent_struggle_count: int = 0
    silence_duration_ms: int = 0
    confidence_level: str = "moderate"
    current_lesson_topic: str = "general"
    interaction_history: List[str] = field(default_factory=list)
    last_trigger_time: float = field(default_factory=time.time)


class BodyLanguageSystem:
    """Advanced body language response system for natural character behavior"""

    def __init__(self):
        self.response_library = self._initialize_response_library()
        self.trigger_mappings = self._initialize_trigger_mappings()
        self.context = InteractionContext()
        self.active_responses: List[BodyLanguageResponse] = []

    def _initialize_response_library(self) -> Dict[str, BodyLanguageResponse]:
        """Initialize library of body language responses"""
        return {
            # Success celebrations
            "gentle_clap": BodyLanguageResponse(
                gesture_type="clapping",
                intensity=BodyLanguageIntensity.MODERATE,
                duration_ms=2000,
                facial_complement="proud smile with sparkling eyes",
                animation_sequence=["raise_hands", "gentle_clap", "thumbs_up"],
                audio_cues=["clap_sound", "encouragement_chime"]
            ),
            "excited_bounce": BodyLanguageResponse(
                gesture_type="bouncing",
                intensity=BodyLanguageIntensity.ENTHUSIASTIC,
                duration_ms=3000,
                facial_complement="wide smile with raised eyebrows",
                animation_sequence=["slight_bounce", "hand_gesture", "settle"],
                audio_cues=["excitement_sound", "celebration_music"]
            ),
            
            # Encouragement gestures
            "supportive_lean": BodyLanguageResponse(
                gesture_type="leaning_forward",
                intensity=BodyLanguageIntensity.SUBTLE,
                duration_ms=1500,
                facial_complement="encouraging smile with attentive eyes",
                animation_sequence=["lean_forward", "nod", "open_hands"],
                audio_cues=["soft_chime"]
            ),
            "patient_wait": BodyLanguageResponse(
                gesture_type="waiting",
                intensity=BodyLanguageIntensity.SUBTLE,
                duration_ms=4000,
                facial_complement="patient smile with gentle breathing",
                animation_sequence=["settle_posture", "gentle_breathing", "occasional_blink"],
                audio_cues=["calm_ambient"]
            ),
            
            # Listening responses
            "active_listening": BodyLanguageResponse(
                gesture_type="nodding",
                intensity=BodyLanguageIntensity.MODERATE,
                duration_ms=2500,
                facial_complement="focused attention with encouraging nods",
                animation_sequence=["slight_forward_lean", "gentle_nods", "eye_contact"],
                audio_cues=["listening_hum"]
            ),
            
            # Confusion support
            "gentle_guidance": BodyLanguageResponse(
                gesture_type="guiding_gesture",
                intensity=BodyLanguageIntensity.MODERATE,
                duration_ms=3000,
                facial_complement="understanding smile with helpful expression",
                animation_sequence=["open_hands", "guiding_motion", "reassuring_gesture"],
                audio_cues=["gentle_guidance_chime"]
            ),
            
            # Lesson transitions
            "lesson_welcome": BodyLanguageResponse(
                gesture_type="welcoming",
                intensity=BodyLanguageIntensity.MODERATE,
                duration_ms=2000,
                facial_complement="bright welcoming smile",
                animation_sequence=["open_arms", "welcome_gesture", "settle"],
                audio_cues=["welcome_chime", "lesson_start_music"]
            ),
            "lesson_completion": BodyLanguageResponse(
                gesture_type="completion_celebration",
                intensity=BodyLanguageIntensity.EXPRESSIVE,
                duration_ms=4000,
                facial_complement="proud celebration with sparkling effects",
                animation_sequence=["celebration_pose", "sparkle_effects", "proud_stance"],
                audio_cues=["completion_fanfare", "achievement_sound"]
            )
        }

    def _initialize_trigger_mappings(self) -> Dict[InteractionTrigger, List[str]]:
        """Map interaction triggers to appropriate body language responses"""
        return {
            InteractionTrigger.CHILD_SUCCESS: ["gentle_clap", "excited_bounce"],
            InteractionTrigger.CHILD_STRUGGLE: ["gentle_guidance", "supportive_lean"],
            InteractionTrigger.CHILD_SILENCE: ["patient_wait", "active_listening"],
            InteractionTrigger.CHILD_EXCITEMENT: ["excited_bounce", "gentle_clap"],
            InteractionTrigger.CHILD_CONFUSION: ["gentle_guidance", "supportive_lean"],
            InteractionTrigger.LESSON_START: ["lesson_welcome"],
            InteractionTrigger.LESSON_END: ["lesson_completion"],
            InteractionTrigger.ENCOURAGEMENT_NEEDED: ["supportive_lean", "gentle_guidance"],
            InteractionTrigger.CELEBRATION_TIME: ["excited_bounce", "gentle_clap"]
        }

    def update_interaction_context(self, 
                                 trigger: InteractionTrigger, 
                                 confidence_level: Optional[str] = None,
                                 lesson_topic: Optional[str] = None) -> None:
        """Update context based on child interactions"""
        current_time = time.time()
        
        # Update context based on trigger
        if trigger == InteractionTrigger.CHILD_SUCCESS:
            self.context.recent_success_count += 1
            self.context.recent_struggle_count = max(0, self.context.recent_struggle_count - 1)
        elif trigger == InteractionTrigger.CHILD_STRUGGLE:
            self.context.recent_struggle_count += 1
            self.context.recent_success_count = max(0, self.context.recent_success_count - 1)
        elif trigger == InteractionTrigger.CHILD_SILENCE:
            self.context.silence_duration_ms = int((current_time - self.context.last_trigger_time) * 1000)
        
        # Update other context
        if confidence_level:
            self.context.confidence_level = confidence_level
        if lesson_topic:
            self.context.current_lesson_topic = lesson_topic
            
        # Track interaction history (keep last 10)
        self.context.interaction_history.append(trigger.value)
        if len(self.context.interaction_history) > 10:
            self.context.interaction_history.pop(0)
            
        self.context.last_trigger_time = current_time

    def select_appropriate_response(self, 
                                  trigger: InteractionTrigger,
                                  current_state: XiaoMeiState) -> Optional[BodyLanguageResponse]:
        """Select most appropriate body language response based on context"""
        available_responses = self.trigger_mappings.get(trigger, [])
        if not available_responses:
            return None

        # Apply contextual selection logic
        response_id = self._apply_contextual_selection(available_responses, trigger, current_state)
        return self.response_library.get(response_id)

    def _apply_contextual_selection(self, 
                                  responses: List[str], 
                                  trigger: InteractionTrigger,
                                  current_state: XiaoMeiState) -> str:
        """Apply contextual logic to select best response"""
        # Default to first response
        selected = responses[0]
        
        # Adjust based on child's confidence level
        if self.context.confidence_level == "low" and trigger == InteractionTrigger.CHILD_SUCCESS:
            # More subtle celebration for low confidence children
            if "gentle_clap" in responses:
                selected = "gentle_clap"
        elif self.context.confidence_level == "high" and trigger == InteractionTrigger.CHILD_SUCCESS:
            # More expressive celebration for confident children
            if "excited_bounce" in responses:
                selected = "excited_bounce"
        
        # Adjust based on recent interaction pattern
        if self.context.recent_struggle_count > 2:
            # More supportive responses after struggles
            if trigger == InteractionTrigger.ENCOURAGEMENT_NEEDED and "supportive_lean" in responses:
                selected = "supportive_lean"
        
        # Adjust based on silence duration
        if self.context.silence_duration_ms > 5000:  # 5 seconds of silence
            if trigger == InteractionTrigger.CHILD_SILENCE and "patient_wait" in responses:
                selected = "patient_wait"
        
        # State-based adjustments
        if current_state == XiaoMeiState.CELEBRATING:
            # Prefer more expressive responses during celebration state
            if "excited_bounce" in responses:
                selected = "excited_bounce"
        elif current_state == XiaoMeiState.LISTENING:
            # Prefer subtle responses during listening state
            if "active_listening" in responses:
                selected = "active_listening"
        
        return selected

    def get_state_transition_triggers(self) -> Dict[InteractionTrigger, XiaoMeiState]:
        """Get mapping of interaction triggers to recommended state transitions"""
        return {
            InteractionTrigger.CHILD_SUCCESS: XiaoMeiState.CELEBRATING,
            InteractionTrigger.CHILD_EXCITEMENT: XiaoMeiState.CELEBRATING,
            InteractionTrigger.CELEBRATION_TIME: XiaoMeiState.CELEBRATING,
            InteractionTrigger.CHILD_SILENCE: XiaoMeiState.LISTENING,
            InteractionTrigger.CHILD_STRUGGLE: XiaoMeiState.SPEAKING,  # Provide guidance
            InteractionTrigger.CHILD_CONFUSION: XiaoMeiState.SPEAKING,  # Provide explanation
            InteractionTrigger.LESSON_START: XiaoMeiState.SPEAKING,
            InteractionTrigger.LESSON_END: XiaoMeiState.CELEBRATING,
            InteractionTrigger.ENCOURAGEMENT_NEEDED: XiaoMeiState.SPEAKING
        }

    def should_trigger_state_transition(self, 
                                      trigger: InteractionTrigger,
                                      current_state: XiaoMeiState) -> Optional[XiaoMeiState]:
        """Determine if interaction should trigger a state transition"""
        suggested_state = self.get_state_transition_triggers().get(trigger)
        
        # Don't transition if already in the suggested state
        if suggested_state == current_state:
            return None
            
        # Apply additional logic based on context
        if trigger == InteractionTrigger.CHILD_SUCCESS:
            # Only transition to celebrating if we had recent struggles (makes celebration more meaningful)
            if self.context.recent_struggle_count > 0:
                return XiaoMeiState.CELEBRATING
            return None
        
        return suggested_state

    def get_interaction_summary(self) -> Dict[str, any]:
        """Get summary of recent interactions for debugging/monitoring"""
        return {
            "recent_successes": self.context.recent_success_count,
            "recent_struggles": self.context.recent_struggle_count,
            "silence_duration": self.context.silence_duration_ms,
            "confidence_level": self.context.confidence_level,
            "lesson_topic": self.context.current_lesson_topic,
            "recent_interactions": self.context.interaction_history[-5:],  # Last 5 interactions
            "last_trigger_time": self.context.last_trigger_time
        }

    def reset_context(self) -> None:
        """Reset interaction context (e.g., for new session)"""
        self.context = InteractionContext()
        self.active_responses.clear()