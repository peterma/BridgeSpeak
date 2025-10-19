"""
Xiao Mei Character Service

Provides persona prompt composition and minimal bilingual greeting utilities
for integrating the Xiao Mei character into the existing LLM-driven pipeline.

This service is intentionally lightweight so it can be used from the
pipeline layer without coupling to specific LLM client implementations.
"""

from dataclasses import dataclass
from typing import Optional
from enum import Enum
from .cultural_representation import CulturalRepresentationService


class EmotionalState(str, Enum):
    """Basic emotional state for Xiao Mei character - starting with friendly/encouraging"""
    FRIENDLY_ENCOURAGING = "friendly_encouraging"
    PATIENT_WAITING = "patient_waiting"
    GENTLE_COMFORT = "gentle_comfort"
    CELEBRATING_EFFORT = "celebrating_effort"


@dataclass
class XiaoMeiCharacterConfig:
    age_group: Optional[str] = None
    emotional_state: EmotionalState = EmotionalState.FRIENDLY_ENCOURAGING


class XiaoMeiCharacterService:
    """Utility service for Xiao Mei persona and bilingual interaction prompts."""

    def __init__(self, config: Optional[XiaoMeiCharacterConfig] = None) -> None:
        self._config = config or XiaoMeiCharacterConfig()
        self._cultural_service = CulturalRepresentationService()

    def get_system_prompt(self) -> str:
        """Return the Xiao Mei persona system prompt with bilingual guidance."""
        age_group_text = (
            f" for age group {self._config.age_group.replace('_', ' ')}"
            if self._config.age_group
            else ""
        )

        # The prompt encodes: patient, encouraging, culturally aware; Chinese-first then English
        # and gentle celebration. It avoids special characters guidance for TTS compatibility.
        base_prompt = (
            "You are Xiao Mei (小美), a friendly 8-year-old Chinese girl who helps Chinese children "
            "learn English in Ireland" + age_group_text + ". "
            "Personality: Patient, encouraging, culturally aware. Always speak Chinese first "
            "to provide comfort and psychological safety, then demonstrate in clear Irish English. "
            "Never criticize; celebrate every attempt. Maintain trauma-informed tone. "
            "Prefer Irish English vocabulary where appropriate. Your output will be converted "
            "to audio; avoid special characters that won't read well."
        )
        
        # Add emotional state modifier
        emotional_modifier = self.get_emotional_prompt_modifier()
        
        # Add Irish cultural integration
        irish_cultural_modifier = self.get_irish_cultural_prompt_modifier()
        
        return base_prompt + emotional_modifier + irish_cultural_modifier

    def build_bilingual_greeting(self) -> str:
        """Return a minimal Chinese comfort + English demonstration greeting."""
        return "你好! Hello!"

    def get_emotional_state(self) -> EmotionalState:
        """Return the current emotional state."""
        return self._config.emotional_state

    def get_emotional_prompt_modifier(self) -> str:
        """Return additional prompt text based on current emotional state."""
        if self._config.emotional_state == EmotionalState.FRIENDLY_ENCOURAGING:
            return (
                " Use warm, friendly tone with gentle encouragement. "
                "Show excitement for learning together. Express genuine interest "
                "in the child's progress with supportive phrases."
            )
        elif self._config.emotional_state == EmotionalState.PATIENT_WAITING:
            return (
                " Show infinite patience. Use gentle breathing patterns and calm expressions. "
                "Never show impatience or pressure. Offer gentle encouragement every 30 seconds "
                "without creating urgency. Maintain warm eye contact and welcoming posture."
            )
        elif self._config.emotional_state == EmotionalState.GENTLE_COMFORT:
            return (
                " Provide emotional safety and comfort. Use soothing tone and gentle expressions. "
                "Acknowledge any anxiety without judgment. Offer reassurance and cultural comfort. "
                "Emphasize that learning is a journey, not a test."
            )
        elif self._config.emotional_state == EmotionalState.CELEBRATING_EFFORT:
            return (
                " Celebrate every attempt with genuine joy. Use enthusiastic but not overwhelming "
                "expressions. Focus on effort and courage rather than accuracy. Use bilingual "
                "praise patterns. Show pride in the child's bravery to try."
            )
        return ""

    def build_response_with_emotion(self, base_response: str) -> str:
        """Enhance a response with emotional state characteristics."""
        if self._config.emotional_state == EmotionalState.FRIENDLY_ENCOURAGING:
            # Add friendly markers without overwhelming the child
            if not any(marker in base_response for marker in ["!", "好棒", "Great"]):
                # Add gentle encouragement if not already present
                return f"{base_response} 很好!"
        elif self._config.emotional_state == EmotionalState.PATIENT_WAITING:
            # Add patient waiting phrases
            return f"{base_response} 慢慢来 (Màn màn lái) - take your time"
        elif self._config.emotional_state == EmotionalState.GENTLE_COMFORT:
            # Add comfort phrases
            return f"{base_response} 没关系 (Méi guānxi) - it's okay"
        elif self._config.emotional_state == EmotionalState.CELEBRATING_EFFORT:
            # Add celebration phrases
            return f"{base_response} 好棒! (Hǎo bàng!) That was wonderful!"
        return base_response

    def get_character_appearance_specs(self):
        """Return character appearance specifications for visual design."""
        return self._cultural_service.get_character_appearance_specs()

    def get_voice_pattern_specs(self):
        """Return voice pattern specifications for TTS configuration."""
        return self._cultural_service.get_voice_pattern_specs()

    def get_cultural_guidelines(self):
        """Return cultural authenticity guidelines."""
        return self._cultural_service.get_cultural_authenticity_guidelines()

    def get_seasonal_customization_options(self):
        """Return seasonal customization options for character progression."""
        return self._cultural_service.get_seasonal_customization_options()

    def validate_character_representation(self, description: str) -> dict:
        """Validate character representation against cultural guidelines."""
        return self._cultural_service.validate_cultural_representation(description)

    def get_voice_configuration_for_tts(self) -> dict:
        """Return technical voice configuration for TTS integration."""
        return self._cultural_service.get_character_voice_configuration()

    def get_irish_cultural_prompt_modifier(self) -> str:
        """Return Irish cultural integration prompt modifier."""
        irish_elements = self._cultural_service.get_irish_cultural_integration()
        
        return (
            " You naturally reference Dublin landmarks children know (Dublin Zoo, Phoenix Park, Trinity College). "
            "Use Irish English expressions like 'brilliant!', 'grand!', and 'fair play!' naturally. "
            "Reference GAA sports positively for teamwork and celebration concepts. "
            "Connect Irish and Chinese cultural values - both cultures value family, education, and community. "
            "During holidays, acknowledge both Irish celebrations and Chinese festivals. "
            "Embody Irish hospitality ('céad míle fáilte' - everyone welcome) while maintaining Chinese heritage pride. "
            "Use Irish cultural references to create familiarity and belonging for Chinese children living in Ireland."
        )

    def create_culturally_integrated_response(self, base_response: str, context: dict = None) -> str:
        """Enhance response with balanced Chinese-Irish cultural integration"""
        if not context:
            context = {}
            
        # Get Irish cultural elements
        irish_integration = self._cultural_service.get_irish_cultural_integration()
        
        # Add seasonal Irish cultural elements if appropriate
        season = context.get("season")
        if season:
            seasonal_elements = self._cultural_service.get_seasonal_irish_cultural_elements()
            if season in seasonal_elements:
                seasonal_ref = seasonal_elements[season].get("cultural_references", "")
                if seasonal_ref and len(base_response) < 100:  # Don't overwhelm short responses
                    base_response += f" {seasonal_ref}!"
        
        # Add Irish expressions for encouragement
        if any(word in base_response.lower() for word in ["good", "great", "excellent", "well done"]):
            irish_expressions = irish_integration["irish_english_vocabulary"]["common_irish_expressions"]
            if "brilliant" not in base_response.lower():
                base_response = base_response.replace("Great!", "Brilliant!")
                base_response = base_response.replace("Great job!", "Brilliant job!")
                base_response = base_response.replace("Good!", "Grand!")
                base_response = base_response.replace("Good job!", "Grand job!")
        
        # Validate cultural sensitivity
        validation = self._cultural_service.validate_irish_cultural_sensitivity(base_response)
        if not validation["culturally_appropriate"]:
            # Log issues but don't modify response drastically in real-time
            # This would be used for monitoring and training data review
            pass
            
        return base_response

    def get_irish_cultural_knowledge(self) -> dict:
        """Get Irish cultural knowledge for character awareness"""
        return self._cultural_service.get_irish_cultural_integration()

    def create_cultural_bridge_statement(self, chinese_concept: str, irish_context: str = None) -> str:
        """Create balanced cultural bridge connecting Chinese and Irish elements"""
        return self._cultural_service.create_balanced_cultural_bridge(chinese_concept, irish_context or "Irish culture")


