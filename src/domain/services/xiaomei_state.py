from enum import Enum
from typing import Optional, Dict, List
from dataclasses import dataclass


class XiaoMeiState(str, Enum):
    WAITING = "waiting"
    SPEAKING = "speaking"
    LISTENING = "listening"
    CELEBRATING = "celebrating"


@dataclass
class FacialExpression:
    """Defines facial expression characteristics for each emotional state"""
    primary_expression: str
    mouth_shape: str
    eye_expression: str
    body_language: str
    animation_type: str
    
    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary for easy integration with video services"""
        return {
            "expression": self.primary_expression,
            "mouth": self.mouth_shape,
            "eyes": self.eye_expression,
            "body": self.body_language,
            "animation": self.animation_type
        }


class XiaoMeiStateManager:
    """Enhanced state manager for Xiao Mei emotional/interaction states with facial expressions."""

    def __init__(self, initial_state: Optional[XiaoMeiState] = None) -> None:
        self._state: XiaoMeiState = initial_state or XiaoMeiState.WAITING
        self._facial_expressions = self._initialize_facial_expressions()
        self._state_transition_rules = self._initialize_transition_rules()
        self._body_language_system = None  # Will be set externally to avoid circular imports

    def _initialize_facial_expressions(self) -> Dict[XiaoMeiState, FacialExpression]:
        """Initialize facial expression mapping for each state"""
        return {
            XiaoMeiState.WAITING: FacialExpression(
                primary_expression="gentle smile",
                mouth_shape="slight smile",
                eye_expression="bright, welcoming eyes with gentle blink",
                body_language="relaxed posture, welcoming stance",
                animation_type="gentle breathing, occasional head tilt"
            ),
            XiaoMeiState.SPEAKING: FacialExpression(
                primary_expression="animated conversation",
                mouth_shape="natural speech movement",
                eye_expression="focused eye contact with expressive eyebrows",
                body_language="engaged forward lean, hand gestures",
                animation_type="mouth movement sync, expressive gestures"
            ),
            XiaoMeiState.LISTENING: FacialExpression(
                primary_expression="attentive focus",
                mouth_shape="closed, slight smile",
                eye_expression="focused attention, encouraging nods",
                body_language="slight forward lean, open posture",
                animation_type="slow nods, attentive head movements"
            ),
            XiaoMeiState.CELEBRATING: FacialExpression(
                primary_expression="joyful celebration",
                mouth_shape="wide smile",
                eye_expression="sparkling eyes, raised eyebrows",
                body_language="celebratory gestures, clapping hands",
                animation_type="sparkle effects, celebratory movements"
            )
        }

    def _initialize_transition_rules(self) -> Dict[XiaoMeiState, List[XiaoMeiState]]:
        """Initialize valid state transitions for natural flow"""
        return {
            XiaoMeiState.WAITING: [XiaoMeiState.SPEAKING, XiaoMeiState.LISTENING],
            XiaoMeiState.SPEAKING: [XiaoMeiState.LISTENING, XiaoMeiState.CELEBRATING],
            XiaoMeiState.LISTENING: [XiaoMeiState.SPEAKING, XiaoMeiState.CELEBRATING, XiaoMeiState.WAITING],
            XiaoMeiState.CELEBRATING: [XiaoMeiState.WAITING, XiaoMeiState.SPEAKING]
        }

    @property
    def state(self) -> XiaoMeiState:
        return self._state

    def get_current_facial_expression(self) -> FacialExpression:
        """Get the facial expression for the current state"""
        return self._facial_expressions[self._state]

    def get_facial_expression_dict(self) -> Dict[str, str]:
        """Get current facial expression as dictionary for integration"""
        return self.get_current_facial_expression().to_dict()

    def can_transition_to(self, target_state: XiaoMeiState) -> bool:
        """Check if transition to target state is valid"""
        return target_state in self._state_transition_rules.get(self._state, [])

    def transition_to(self, target_state: XiaoMeiState) -> bool:
        """Attempt to transition to target state, returns success status"""
        if self.can_transition_to(target_state):
            self._state = target_state
            return True
        return False

    def set_waiting(self) -> bool:
        """Transition to waiting state"""
        return self.transition_to(XiaoMeiState.WAITING)

    def set_speaking(self) -> bool:
        """Transition to speaking state"""
        return self.transition_to(XiaoMeiState.SPEAKING)

    def set_listening(self) -> bool:
        """Transition to listening state"""
        return self.transition_to(XiaoMeiState.LISTENING)

    def set_celebrating(self) -> bool:
        """Transition to celebrating state"""
        return self.transition_to(XiaoMeiState.CELEBRATING)

    def get_valid_transitions(self) -> List[XiaoMeiState]:
        """Get list of valid states that can be transitioned to from current state"""
        return self._state_transition_rules.get(self._state, [])

    def get_state_description(self) -> str:
        """Get human-readable description of current state and expression"""
        expression = self.get_current_facial_expression()
        return f"State: {self._state.value.title()} - {expression.primary_expression}"

    def set_body_language_system(self, body_language_system) -> None:
        """Set the body language system for advanced interactions"""
        self._body_language_system = body_language_system

    def process_child_interaction(self, interaction_trigger: str, **context) -> Dict[str, any]:
        """Process child interaction and determine appropriate responses"""
        if not self._body_language_system:
            return {"state_changed": False, "body_language": None}

        # Import here to avoid circular dependency
        from .body_language_system import InteractionTrigger

        try:
            trigger = InteractionTrigger(interaction_trigger)
        except ValueError:
            return {"state_changed": False, "body_language": None, "error": f"Unknown trigger: {interaction_trigger}"}

        # Update interaction context
        self._body_language_system.update_interaction_context(
            trigger, 
            confidence_level=context.get("confidence_level"),
            lesson_topic=context.get("lesson_topic")
        )

        # Check if state transition is needed
        suggested_state = self._body_language_system.should_trigger_state_transition(trigger, self._state)
        state_changed = False
        
        if suggested_state and self.can_transition_to(suggested_state):
            old_state = self._state
            self._state = suggested_state
            state_changed = True
        else:
            suggested_state = self._state

        # Get appropriate body language response
        body_language_response = self._body_language_system.select_appropriate_response(trigger, self._state)

        return {
            "state_changed": state_changed,
            "old_state": old_state.value if state_changed else self._state.value,
            "new_state": self._state.value,
            "body_language": body_language_response.to_animation_config() if body_language_response else None,
            "interaction_summary": self._body_language_system.get_interaction_summary()
        }

    def get_sophisticated_transition_logic(self, child_context: Dict[str, any]) -> Dict[str, any]:
        """Get sophisticated state transition recommendations based on child context"""
        confidence_level = child_context.get("confidence_level", "moderate")
        recent_interactions = child_context.get("recent_interactions", [])
        silence_duration = child_context.get("silence_duration_ms", 0)
        
        recommendations = {
            "maintain_current": False,
            "suggested_state": None,
            "reasoning": "",
            "body_language_intensity": "moderate"
        }

        # Analysis based on confidence level
        if confidence_level == "low":
            if self._state == XiaoMeiState.CELEBRATING:
                recommendations["maintain_current"] = True
                recommendations["reasoning"] = "Maintaining celebration for low-confidence child"
                recommendations["body_language_intensity"] = "gentle"
            elif self._state == XiaoMeiState.SPEAKING:
                recommendations["suggested_state"] = XiaoMeiState.LISTENING
                recommendations["reasoning"] = "Transitioning to listening to avoid overwhelming low-confidence child"
        
        elif confidence_level == "high":
            if self._state == XiaoMeiState.WAITING and silence_duration > 3000:
                recommendations["suggested_state"] = XiaoMeiState.SPEAKING
                recommendations["reasoning"] = "Confident child may need more engagement"
                recommendations["body_language_intensity"] = "expressive"

        # Analysis based on recent interactions
        success_count = sum(1 for interaction in recent_interactions if "success" in interaction)
        struggle_count = sum(1 for interaction in recent_interactions if "struggle" in interaction)
        
        if success_count >= 2 and self._state != XiaoMeiState.CELEBRATING:
            recommendations["suggested_state"] = XiaoMeiState.CELEBRATING
            recommendations["reasoning"] = "Multiple successes warrant celebration"
            recommendations["body_language_intensity"] = "enthusiastic"
        elif struggle_count >= 2 and self._state == XiaoMeiState.CELEBRATING:
            recommendations["suggested_state"] = XiaoMeiState.SPEAKING
            recommendations["reasoning"] = "Recent struggles suggest need for guidance"
            recommendations["body_language_intensity"] = "supportive"

        return recommendations


