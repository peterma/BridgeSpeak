"""
Bilingual Context Domain Service

Extracted from the monolithic educational_context_processor.py.
This service handles bilingual context management and Chinese → English progression.

Implements IBilingualContextService interface for dependency injection.
"""

from typing import Dict, List, Optional, Tuple, Any
from src.application.interfaces.services import (
    IBilingualContextService, 
    DetectedLanguage,
    BilingualContext,
    TransitionStrategy,
    ConfidenceLevel
)

# Import enums from the original file (will be moved to domain models in Phase 2)
from enum import Enum

class AgeGroup(Enum):
    """Age groups aligned with Irish Primary School system"""
    JUNIOR_INFANTS = "junior_infants"  # Ages 4-5
    SENIOR_INFANTS = "senior_infants"  # Ages 5-6
    FIRST_CLASS = "first_class"        # Ages 6-7
    SECOND_CLASS = "second_class"      # Ages 7-8
    THIRD_CLASS = "third_class"        # Ages 8-9
    FOURTH_CLASS = "fourth_class"      # Ages 9-10


class BilingualContextService(IBilingualContextService):
    """
    Bilingual context management service for Chinese → English progression.
    
    Combines functionality from BilingualContextManager and AdvancedBilingualContextManager
    classes from the monolithic processor. Now implements interface contract for dependency injection.
    """
    
    def __init__(self):
        """Initialize bilingual context management."""
        # Core state tracking
        self.current_context = BilingualContext.CHINESE_COMFORT
        self.confidence_level = ConfidenceLevel.VERY_LOW
        self.transition_strategy = TransitionStrategy.MAINTAIN_COMFORT
        
        # Basic manager compatibility
        self.language_switch_count = 0
        self.english_confidence_level = 0.0
        
        # Advanced tracking metrics
        self.english_confidence_score = 0.0  # 0.0 to 1.0
        self.chinese_usage_count = 0
        self.english_usage_count = 0
        self.mixed_usage_count = 0
        self.successful_transitions = 0
        self.total_interactions = 0
        
        # Context history for pattern analysis
        self.context_history = []
        self.confidence_history = []
        
        # Transition thresholds
        self.transition_thresholds = {
            ConfidenceLevel.VERY_LOW: 0.15,    # Very cautious transitions
            ConfidenceLevel.LOW: 0.25,         # Gentle encouragement  
            ConfidenceLevel.MODERATE: 0.35,    # More active transitions
            ConfidenceLevel.HIGH: 0.5,         # Confident progression
            ConfidenceLevel.VERY_HIGH: 0.7     # Natural switching
        }
    
    def determine_context(
        self, 
        detected_language: DetectedLanguage, 
        confidence_level: float,
        child_profile: Dict[str, Any]
    ) -> BilingualContext:
        """
        Determine appropriate bilingual context for response.
        
        Args:
            detected_language: Detected language from input
            confidence_level: Child's confidence level (0.0 to 1.0)
            child_profile: Child's profile information
            
        Returns:
            Appropriate bilingual context
        """
        self.total_interactions += 1
        self.english_confidence_score = confidence_level
        
        # Update confidence level classification
        old_confidence = self.confidence_level
        self.confidence_level = self._classify_confidence_level(confidence_level)
        
        # Track language usage patterns
        if detected_language == DetectedLanguage.CHINESE:
            self.chinese_usage_count += 1
        elif detected_language == DetectedLanguage.ENGLISH:
            self.english_usage_count += 1
        elif detected_language == DetectedLanguage.MIXED:
            self.mixed_usage_count += 1
        
        # Determine new context based on sophisticated analysis
        new_context = self._analyze_optimal_context(detected_language, old_confidence)
        
        # Update state
        self.current_context = new_context
        
        # Track history
        self.context_history.append(new_context)
        self.confidence_history.append(confidence_level)
        
        # Limit history size
        if len(self.context_history) > 10:
            self.context_history.pop(0)
            self.confidence_history.pop(0)
        
        return new_context
    
    def get_transition_strategy(
        self, 
        current_context: BilingualContext,
        child_progress: Dict[str, Any]
    ) -> TransitionStrategy:
        """
        Get recommended transition strategy.
        
        Args:
            current_context: Current bilingual context
            child_progress: Child's progress information
            
        Returns:
            Recommended transition strategy
        """
        # Extract detected language from child progress if available
        detected_language = child_progress.get('detected_language', DetectedLanguage.UNKNOWN)
        
        # Determine strategy based on context and patterns
        strategy = self._determine_transition_strategy(current_context, detected_language)
        self.transition_strategy = strategy
        return strategy
    
    def generate_bilingual_response_structure(
        self, 
        context: BilingualContext,
        english_content: str,
        chinese_support: Optional[str] = None
    ) -> Dict[str, str]:
        """
        Generate bilingual response structure based on context.
        
        Args:
            context: Current bilingual context
            english_content: English content to present
            chinese_support: Optional Chinese support text
            
        Returns:
            Dictionary with bilingual response structure
        """
        response_structure = {
            'context': context.value,
            'primary_language': self._get_primary_language_for_context(context),
            'english_content': english_content,
            'chinese_support': chinese_support or "",
            'presentation_style': self._get_presentation_style(context),
        }
        
        # Add context-specific guidance
        if context == BilingualContext.CHINESE_COMFORT:
            response_structure.update({
                'approach': 'Chinese-first with gentle English introduction',
                'structure': 'chinese_explanation + simple_english_word',
                'confidence_support': 'maximum',
                'encouragement_level': 'gentle'
            })
        elif context == BilingualContext.GENTLE_TRANSITION:
            response_structure.update({
                'approach': 'Gradual introduction with Chinese scaffolding',
                'structure': 'chinese_context + english_target + chinese_reinforcement',
                'confidence_support': 'high',
                'encouragement_level': 'encouraging'
            })
        elif context == BilingualContext.BRIDGE_BUILDING:
            response_structure.update({
                'approach': 'Connect Chinese and English concepts explicitly',
                'structure': 'concept_in_chinese + equivalent_in_english + connection',
                'confidence_support': 'balanced',
                'encouragement_level': 'positive'
            })
        elif context == BilingualContext.CONFIDENCE_BUILDING:
            response_structure.update({
                'approach': 'Celebrate English attempts with support',
                'structure': 'praise_english_attempt + gentle_correction + encouragement',
                'confidence_support': 'encouraging',
                'encouragement_level': 'enthusiastic'
            })
        elif context == BilingualContext.ENGLISH_DEMONSTRATION:
            response_structure.update({
                'approach': 'Primary English with Chinese backup available',
                'structure': 'english_primary + optional_chinese_clarification',
                'confidence_support': 'minimal',
                'encouragement_level': 'natural'
            })
        elif context == BilingualContext.NATURAL_SWITCHING:
            response_structure.update({
                'approach': 'Follow child\'s natural language preferences',
                'structure': 'adaptive_based_on_child_input',
                'confidence_support': 'responsive',
                'encouragement_level': 'natural'
            })
        elif context == BilingualContext.MIXED_SUPPORT:
            response_structure.update({
                'approach': 'Support mixed language usage patterns',
                'structure': 'flexible_mixing + positive_reinforcement',
                'confidence_support': 'adaptive',
                'encouragement_level': 'supportive'
            })
        
        return response_structure
    
    def _classify_confidence_level(self, score: float) -> ConfidenceLevel:
        """Classify numerical confidence into confidence level."""
        if score >= 0.8:
            return ConfidenceLevel.VERY_HIGH
        elif score >= 0.6:
            return ConfidenceLevel.HIGH
        elif score >= 0.4:
            return ConfidenceLevel.MODERATE
        elif score >= 0.2:
            return ConfidenceLevel.LOW
        else:
            return ConfidenceLevel.VERY_LOW
    
    def _analyze_optimal_context(
        self, 
        detected_language: DetectedLanguage, 
        previous_confidence: ConfidenceLevel
    ) -> BilingualContext:
        """
        Analyze optimal bilingual context using sophisticated patterns.
        
        Args:
            detected_language: Language detected in child's input
            previous_confidence: Previous confidence level
            
        Returns:
            Optimal bilingual context
        """
        # Check for confidence improvements
        confidence_improving = (
            self.confidence_level.value > previous_confidence.value 
            if hasattr(previous_confidence, 'value') else False
        )
        
        # Analyze recent context patterns
        recent_contexts = (
            self.context_history[-3:] 
            if len(self.context_history) >= 3 
            else self.context_history
        )
        
        # Sophisticated context determination
        if detected_language == DetectedLanguage.CHINESE:
            # Child using Chinese - determine comfort vs. transition context
            if self.confidence_level in [ConfidenceLevel.VERY_LOW, ConfidenceLevel.LOW]:
                return BilingualContext.CHINESE_COMFORT
            elif self.confidence_level == ConfidenceLevel.MODERATE:
                if confidence_improving:
                    return BilingualContext.GENTLE_TRANSITION
                else:
                    return BilingualContext.CHINESE_COMFORT
            else:  # HIGH or VERY_HIGH confidence
                return BilingualContext.BRIDGE_BUILDING
                
        elif detected_language == DetectedLanguage.ENGLISH:
            # Child attempting English - encourage and build confidence
            if self.confidence_level in [ConfidenceLevel.VERY_LOW, ConfidenceLevel.LOW]:
                return BilingualContext.CONFIDENCE_BUILDING
            elif self.confidence_level == ConfidenceLevel.MODERATE:
                return BilingualContext.CONFIDENCE_BUILDING
            else:  # HIGH or VERY_HIGH confidence
                return BilingualContext.NATURAL_SWITCHING
                
        elif detected_language == DetectedLanguage.MIXED:
            # Child mixing languages - bridge building opportunity
            if self.confidence_level in [ConfidenceLevel.VERY_LOW, ConfidenceLevel.LOW]:
                return BilingualContext.GENTLE_TRANSITION
            elif self.confidence_level == ConfidenceLevel.MODERATE:
                return BilingualContext.GENTLE_TRANSITION
            else:
                return BilingualContext.NATURAL_SWITCHING
                
        else:  # UNKNOWN
            # Default to current context or safe fallback
            if len(recent_contexts) > 0:
                return recent_contexts[-1]
            else:
                return BilingualContext.CHINESE_COMFORT
    
    def _determine_transition_strategy(
        self, 
        new_context: BilingualContext, 
        detected_language: DetectedLanguage
    ) -> TransitionStrategy:
        """
        Determine optimal transition strategy based on context and patterns.
        
        Args:
            new_context: Target bilingual context
            detected_language: Detected language from input
            
        Returns:
            Recommended transition strategy
        """
        # Consider recent success patterns
        recent_successes = self._calculate_recent_success_rate()
        
        if new_context == BilingualContext.CHINESE_COMFORT:
            return TransitionStrategy.MAINTAIN_COMFORT
            
        elif new_context == BilingualContext.GENTLE_TRANSITION:
            # For mixed usage patterns at low confidence, take step-by-step approach
            if (detected_language == DetectedLanguage.MIXED and 
                self.confidence_level in [ConfidenceLevel.VERY_LOW, ConfidenceLevel.LOW]):
                return TransitionStrategy.STEP_BY_STEP
            return TransitionStrategy.GENTLE_INTRODUCTION
                
        elif new_context == BilingualContext.BRIDGE_BUILDING:
            # If confidence trend is improving at moderate or higher, focus on building confidence
            if (self.confidence_level in [ConfidenceLevel.MODERATE, ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH] 
                and recent_successes >= 0.6):
                return TransitionStrategy.CONFIDENCE_BUILDING
            return TransitionStrategy.GRADUAL_INCREASE
            
        elif new_context == BilingualContext.CONFIDENCE_BUILDING:
            return TransitionStrategy.CONFIDENCE_BOOST
            
        elif new_context in [BilingualContext.ENGLISH_DEMONSTRATION, BilingualContext.NATURAL_SWITCHING]:
            if self.confidence_level in [ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH]:
                return TransitionStrategy.NATURAL_FLOW
            else:
                return TransitionStrategy.GRADUAL_INCREASE
                
        else:  # Default fallback
            return TransitionStrategy.GENTLE_INTRODUCTION
    
    def _calculate_recent_success_rate(self) -> float:
        """Calculate success rate of recent transitions."""
        if len(self.confidence_history) < 2:
            return 0.5  # Neutral assumption
        
        improvements = 0
        comparisons = min(5, len(self.confidence_history) - 1)
        
        for i in range(1, comparisons + 1):
            if self.confidence_history[-i] >= self.confidence_history[-i-1]:
                improvements += 1
        
        return improvements / comparisons if comparisons > 0 else 0.5
    
    def _get_primary_language_for_context(self, context: BilingualContext) -> str:
        """Get primary language for given context."""
        if context in [BilingualContext.CHINESE_COMFORT]:
            return "chinese"
        elif context in [BilingualContext.ENGLISH_DEMONSTRATION, BilingualContext.NATURAL_SWITCHING]:
            return "english"
        else:
            return "bilingual"
    
    def _get_presentation_style(self, context: BilingualContext) -> str:
        """Get presentation style for given context."""
        style_mapping = {
            BilingualContext.CHINESE_COMFORT: "chinese_primary_gentle_english",
            BilingualContext.GENTLE_TRANSITION: "scaffolded_introduction",
            BilingualContext.BRIDGE_BUILDING: "explicit_connections",
            BilingualContext.CONFIDENCE_BUILDING: "encouraging_english_focus",
            BilingualContext.ENGLISH_DEMONSTRATION: "english_primary_chinese_support",
            BilingualContext.NATURAL_SWITCHING: "adaptive_natural",
            BilingualContext.MIXED_SUPPORT: "flexible_mixed"
        }
        return style_mapping.get(context, "balanced_bilingual")
    
    # Additional methods for compatibility with original classes
    def get_current_context(self) -> BilingualContext:
        """Get current bilingual context."""
        return self.current_context
    
    def get_language_context(self) -> str:
        """Get current language context for backward compatibility."""
        if self.current_context == BilingualContext.CHINESE_COMFORT:
            return "chinese"
        elif self.current_context == BilingualContext.ENGLISH_DEMONSTRATION:
            return "english"
        else:
            return "mixed"
    
    def switch_to_english(self):
        """Switch context to English demonstration."""
        self.current_context = BilingualContext.ENGLISH_DEMONSTRATION
        self.language_switch_count += 1
        self.english_confidence_level = min(1.0, self.english_confidence_level + 0.1)
    
    def reset_to_chinese(self):
        """Reset to Chinese comfort phase."""
        self.current_context = BilingualContext.CHINESE_COMFORT
    
    def set_mixed_support(self):
        """Set context to mixed language support."""
        self.current_context = BilingualContext.MIXED_SUPPORT
        self.english_confidence_level = min(1.0, self.english_confidence_level + 0.05)
    
    def get_switch_count(self) -> int:
        """Get number of language context switches."""
        return self.language_switch_count
    
    def get_english_confidence(self) -> float:
        """Get estimated English confidence level (0.0 to 1.0)."""
        return max(self.english_confidence_level, self.english_confidence_score)
    
    def should_encourage_english(self) -> bool:
        """Determine if English should be gently encouraged."""
        return self.get_english_confidence() > 0.3
    
    def get_confidence_trend(self) -> str:
        """Get confidence trend analysis."""
        if len(self.confidence_history) < 3:
            return "insufficient_data"
        
        recent = self.confidence_history[-3:]
        if recent[-1] > recent[0] + 0.1:
            return "improving"
        elif recent[-1] < recent[0] - 0.1:
            return "declining"
        else:
            return "stable"
    
    def should_attempt_transition(self) -> bool:
        """Determine if a language transition should be attempted."""
        # Very low confidence should rarely attempt transitions
        if self.confidence_level == ConfidenceLevel.VERY_LOW:
            return self.english_confidence_score > 0.2 and len(self.confidence_history) > 2
        
        threshold = self.transition_thresholds.get(self.confidence_level, 0.3)
        recent_success = self._calculate_recent_success_rate()
        return recent_success >= threshold
    
    def get_transition_readiness_score(self) -> float:
        """Get a score indicating readiness for language transition (0.0-1.0)."""
        base_confidence = self.english_confidence_score
        recent_success = self._calculate_recent_success_rate()
        pattern_bonus = 0.1 if self.get_confidence_trend() == "improving" else 0.0
        
        return min(1.0, (base_confidence * 0.6) + (recent_success * 0.3) + pattern_bonus)
    
    def generate_advanced_bilingual_suggestions(self, age_group: Optional[AgeGroup] = None) -> Dict[str, str]:
        """
        Generate sophisticated bilingual response suggestions.
        
        Args:
            age_group: Optional age group for age-specific guidance
            
        Returns:
            Dictionary with advanced bilingual suggestions
        """
        suggestions = {
            'current_context': self.current_context.value,
            'confidence_level': self.confidence_level.value,
            'transition_strategy': self.transition_strategy.value,
            'confidence_score': f"{self.english_confidence_score:.2f}",
        }
        
        # Context-specific guidance
        if self.current_context == BilingualContext.CHINESE_COMFORT:
            suggestions.update({
                'approach': 'Maintain Chinese comfort while preparing gentle introduction',
                'next_step': 'Look for natural opportunities to introduce English words',
                'pace': 'very_slow',
                'support_level': 'maximum'
            })
        elif self.current_context == BilingualContext.GENTLE_TRANSITION:
            suggestions.update({
                'approach': 'Encouraging gentle introduction of English with Chinese support',
                'next_step': 'Use familiar concepts to bridge languages',
                'pace': 'slow',
                'support_level': 'high'
            })
        elif self.current_context == BilingualContext.BRIDGE_BUILDING:
            suggestions.update({
                'approach': 'Encouraging bridge: connect Chinese and English concepts',
                'next_step': 'Show equivalencies and build connections',
                'pace': 'moderate',
                'support_level': 'balanced'
            })
        elif self.current_context == BilingualContext.CONFIDENCE_BUILDING:
            suggestions.update({
                'approach': 'Celebrate English attempts and build confidence',
                'next_step': 'Encourage continued English usage with praise',
                'pace': 'moderate',
                'support_level': 'encouraging'
            })
        elif self.current_context == BilingualContext.NATURAL_SWITCHING:
            suggestions.update({
                'approach': 'Support natural language switching patterns',
                'next_step': 'Follow child\'s lead in language choice',
                'pace': 'natural',
                'support_level': 'minimal'
            })
        
        # Add age-specific guidance
        if age_group:
            if age_group in [AgeGroup.JUNIOR_INFANTS, AgeGroup.SENIOR_INFANTS]:
                suggestions['age_guidance'] = 'Use very simple words and lots of visual/physical cues'
            elif age_group in [AgeGroup.FIRST_CLASS, AgeGroup.SECOND_CLASS]:
                suggestions['age_guidance'] = 'Balance explanation with practice opportunities'
            else:
                suggestions['age_guidance'] = 'Encourage explicit language analysis and comparison'
        
        # Add usage statistics
        total_usage = self.chinese_usage_count + self.english_usage_count + self.mixed_usage_count
        if total_usage > 0:
            suggestions.update({
                'chinese_percentage': f"{(self.chinese_usage_count / total_usage) * 100:.1f}%",
                'english_percentage': f"{(self.english_usage_count / total_usage) * 100:.1f}%",
                'mixed_percentage': f"{(self.mixed_usage_count / total_usage) * 100:.1f}%"
            })
        
        return suggestions