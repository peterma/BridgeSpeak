"""
Service Interface Definitions

These interfaces define the contracts for domain services without coupling to implementations.
This enables dependency injection, testing with mocks, and service composition.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Tuple
from enum import Enum

# These enums will be moved to domain models in Phase 2
class DetectedLanguage(Enum):
    CHINESE = "chinese"
    ENGLISH = "english" 
    MIXED = "mixed"
    UNKNOWN = "unknown"

class TraumaInformedLevel(Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    ACCEPTABLE = "acceptable"
    CONCERNING = "concerning"
    INAPPROPRIATE = "inappropriate"

class BilingualContext(Enum):
    CHINESE_COMFORT = "chinese_comfort"
    GENTLE_TRANSITION = "gentle_transition"
    BRIDGE_BUILDING = "bridge_building"
    CONFIDENCE_BUILDING = "confidence_building"
    ENGLISH_DEMONSTRATION = "english_demonstration"
    NATURAL_SWITCHING = "natural_switching"
    MIXED_SUPPORT = "mixed_support"

class TransitionStrategy(Enum):
    MAINTAIN_COMFORT = "maintain_comfort"
    GENTLE_INTRODUCTION = "gentle_introduction"
    GRADUAL_INCREASE = "gradual_increase"
    CONFIDENCE_BOOST = "confidence_boost"
    NATURAL_FLOW = "natural_flow"
    STEP_BY_STEP = "step_by_step"
    CONFIDENCE_BUILDING = "confidence_building"

class ConfidenceLevel(Enum):
    VERY_LOW = "very_low"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    VERY_HIGH = "very_high"


class ILanguageDetectionService(ABC):
    """Interface for language detection and analysis."""
    
    @abstractmethod
    def detect_language(self, text: str) -> DetectedLanguage:
        """Detect the primary language of input text."""
        pass
    
    @abstractmethod
    def assess_confidence_level(self, text: str, detected_language: DetectedLanguage) -> float:
        """Assess child's confidence level based on language use (0.0 to 1.0)."""
        pass
    
    @abstractmethod
    def analyze_language_mixing(self, text: str) -> Dict[str, float]:
        """Analyze the ratio of different languages in mixed text."""
        pass


class IBilingualContextService(ABC):
    """Interface for bilingual context management and transition strategies."""
    
    @abstractmethod
    def determine_context(
        self, 
        detected_language: DetectedLanguage, 
        confidence_level: float,
        child_profile: Dict[str, Any]
    ) -> BilingualContext:
        """Determine appropriate bilingual context for response."""
        pass
    
    @abstractmethod
    def get_transition_strategy(
        self, 
        current_context: BilingualContext,
        child_progress: Dict[str, Any]
    ) -> TransitionStrategy:
        """Get recommended transition strategy."""
        pass
    
    @abstractmethod
    def generate_bilingual_response_structure(
        self, 
        context: BilingualContext,
        english_content: str,
        chinese_support: Optional[str] = None
    ) -> Dict[str, str]:
        """Generate bilingual response structure based on context."""
        pass


class ITraumaValidationService(ABC):
    """Interface for trauma-informed response validation."""
    
    @abstractmethod
    def calculate_positivity_score(self, text: str) -> float:
        """Calculate positivity score for trauma-informed validation (0.0 to 1.0)."""
        pass
    
    @abstractmethod
    def assess_trauma_informed_level(self, positivity_score: float) -> TraumaInformedLevel:
        """Assess trauma-informed appropriateness level."""
        pass
    
    @abstractmethod
    def transform_to_positive_framing(self, text: str) -> str:
        """Transform potentially negative content to positive framing."""
        pass
    
    @abstractmethod
    def validate_response_safety(
        self, 
        response: str, 
        child_sensitivity_level: str
    ) -> Tuple[bool, List[str]]:
        """Validate response safety and return any concerns."""
        pass


class ICurriculumIntegrationService(ABC):
    """Interface for Irish curriculum integration and age-appropriate content."""
    
    @abstractmethod
    def get_age_appropriate_vocabulary(
        self, 
        age_group: str, 
        scenario_type: str
    ) -> List[str]:
        """Get vocabulary appropriate for age group and scenario."""
        pass
    
    @abstractmethod
    def validate_curriculum_alignment(
        self, 
        content: str, 
        curriculum_stage: str
    ) -> Dict[str, Any]:
        """Validate content alignment with Irish curriculum standards."""
        pass
    
    @abstractmethod
    def suggest_educational_enhancements(
        self, 
        base_content: str,
        learning_objectives: List[str]
    ) -> Dict[str, str]:
        """Suggest educational enhancements aligned with curriculum."""
        pass


class ILearningAnalyticsService(ABC):
    """Interface for learning progress tracking and analytics."""
    
    @abstractmethod
    async def record_conversation_turn(
        self, 
        child_id: str,
        session_id: str, 
        turn_data: Dict[str, Any]
    ) -> None:
        """Record a conversation turn for analytics."""
        pass
    
    @abstractmethod
    async def analyze_vocabulary_progress(
        self, 
        child_id: str
    ) -> Dict[str, Any]:
        """Analyze vocabulary learning progress."""
        pass
    
    @abstractmethod
    async def generate_progress_insights(
        self, 
        child_id: str,
        time_period_days: int = 30
    ) -> Dict[str, Any]:
        """Generate learning progress insights."""
        pass
    
    @abstractmethod
    async def identify_learning_patterns(
        self, 
        child_id: str
    ) -> Dict[str, Any]:
        """Identify patterns in child's learning behavior."""
        pass