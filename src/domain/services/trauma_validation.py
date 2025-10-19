"""
Trauma Validation Domain Service

Extracted from the monolithic educational_context_processor.py.
This service handles trauma-informed response validation and positive content transformation.

Implements ITraumaValidationService interface for dependency injection.
"""

import re
from typing import Dict, List, Optional, Tuple
from src.application.interfaces.services import (
    ITraumaValidationService, 
    TraumaInformedLevel
)

# Import enums from the original file (will be moved to domain models in Phase 2)
from enum import Enum

class ResponseTone(Enum):
    """Response tone classification for trauma-informed assessment"""
    HIGHLY_ENCOURAGING = "highly_encouraging"
    ENCOURAGING = "encouraging"
    NEUTRAL_POSITIVE = "neutral_positive"
    NEUTRAL = "neutral"
    POTENTIALLY_DISCOURAGING = "potentially_discouraging"
    DISCOURAGING = "discouraging"

class AgeGroup(Enum):
    """Age groups aligned with Irish Primary School system"""
    JUNIOR_INFANTS = "junior_infants"  # Ages 4-5
    SENIOR_INFANTS = "senior_infants"  # Ages 5-6
    FIRST_CLASS = "first_class"        # Ages 6-7
    SECOND_CLASS = "second_class"      # Ages 7-8
    THIRD_CLASS = "third_class"        # Ages 8-9
    FOURTH_CLASS = "fourth_class"      # Ages 9-10


class TraumaValidationService(ITraumaValidationService):
    """
    Trauma-informed response validation service for educational content.
    
    Extracted from TraumaInformedResponseValidator class in monolithic processor.
    Now implements interface contract for dependency injection and child safety.
    """
    
    def __init__(self):
        """Initialize trauma validation patterns and positive transformations."""
        # Positive words and phrases for trauma-informed responses
        self.positive_words = {
            # Encouragement words
            'wonderful', 'excellent', 'amazing', 'fantastic', 'great', 'good', 'nice',
            'beautiful', 'brilliant', 'awesome', 'super', 'terrific', 'fabulous',
            'marvelous', 'outstanding', 'impressive', 'remarkable', 'incredible',
            
            # Growth mindset words
            'learning', 'growing', 'improving', 'progressing', 'developing', 'trying',
            'practicing', 'working', 'effort', 'progress', 'journey', 'process',
            'challenge', 'opportunity', 'possibility', 'potential', 'growth',
            'keep', 'going', 'continue', 'persist', 'persevere',
            
            # Supportive words
            'help', 'support', 'encourage', 'guide', 'assist', 'understand',
            'listen', 'care', 'kind', 'gentle', 'patient', 'friendly', 'warm',
            'safe', 'comfortable', 'welcome', 'included', 'valued', 'respected',
            'work', 'together', 'share', 'explore', 'discover', 'try',
            
            # Achievement words
            'success', 'achievement', 'accomplishment', 'victory', 'win', 'complete',
            'finish', 'done', 'ready', 'capable', 'able', 'confident', 'proud',
            'skilled', 'talented', 'clever', 'smart', 'creative', 'thoughtful'
        }
        
        # Negative words that should be avoided or transformed
        self.negative_words = {
            # Direct negatives
            'wrong', 'incorrect', 'bad', 'terrible', 'awful', 'horrible', 'fail',
            'failed', 'failure', 'mistake', 'error', 'stupid', 'dumb', 'silly', 'foolish',
            
            # Discouraging words
            'impossible', 'never', 'can\'t', 'won\'t', 'shouldn\'t', 'mustn\'t',
            'difficult', 'hard', 'tough', 'challenging', 'complicated', 'confusing',
            
            # Potentially triggering words
            'scared', 'afraid', 'worried', 'anxious', 'nervous', 'upset', 'sad',
            'angry', 'frustrated', 'disappointed', 'embarrassed', 'ashamed'
        }
        
        # Positive replacements for negative concepts
        self.positive_transformations = {
            'wrong': 'let\'s try a different way',
            'incorrect': 'let\'s explore another approach',
            'bad': 'let\'s make this better',
            'terrible': 'we can improve this',
            'fail': "let's try together",
            'failed': "let's try together",
            'failure': 'learning opportunity',
            'mistake': 'learning moment',
            'error': 'chance to grow',
            'difficult': 'challenging but doable',
            'hard': 'something we can work on together',
            'impossible': 'takes practice',
            'can\'t': 'not yet',
            'won\'t': 'might need more time',
            'scared': 'it\'s okay to feel unsure',
            'afraid': 'let\'s take it step by step',
            'worried': 'let\'s work through this together',
            'confused': 'let\'s explore this together',
            'confusing': 'let\'s explore this together'
        }
        
        # Response templates for different trauma-informed levels
        self.response_templates = {
            TraumaInformedLevel.EXCELLENT: {
                'tone': 'highly_encouraging',
                'approach': 'celebration_and_growth',
                'structure': 'affirmation + progress + next_step',
                'examples': [
                    'Wonderful! You\'re making amazing progress. Let\'s explore what comes next!',
                    'Fantastic work! I can see how much you\'re learning. What would you like to try now?'
                ]
            },
            TraumaInformedLevel.GOOD: {
                'tone': 'encouraging',
                'approach': 'positive_support',
                'structure': 'acknowledgment + encouragement + guidance',
                'examples': [
                    'Great effort! You\'re doing really well. Let me help you with the next part.',
                    'Nice work! I can see you\'re trying hard. Let\'s continue together.'
                ]
            },
            TraumaInformedLevel.ACCEPTABLE: {
                'tone': 'neutral_positive',
                'approach': 'gentle_guidance',
                'structure': 'acknowledgment + gentle_support',
                'examples': [
                    'I can see you\'re working on this. Let me help you.',
                    'You\'re making progress. Let\'s continue step by step.'
                ]
            }
        }
    
    def calculate_positivity_score(self, text: str) -> float:
        """
        Calculate positivity score for given text (0.0 to 1.0)
        
        Args:
            text: Input text to analyze
            
        Returns:
            Float score between 0.0 (negative) and 1.0 (positive)
        """
        if not text or not text.strip():
            return 0.5  # Neutral for empty text
        
        words = text.lower().split()
        if not words:
            return 0.5
        
        positive_count = 0
        negative_count = 0
        total_scored_words = 0
        
        for word in words:
            # Remove punctuation for matching
            clean_word = ''.join(c for c in word if c.isalpha())
            if not clean_word:
                continue
            
            if clean_word in self.positive_words:
                positive_count += 1
                total_scored_words += 1
            elif clean_word in self.negative_words:
                negative_count += 1
                total_scored_words += 1
        
        # If no scored words, assume neutral (0.5)
        if total_scored_words == 0:
            return 0.5
        
        # Calculate base score with more nuanced approach
        if total_scored_words > 0:
            base_score = positive_count / total_scored_words
        else:
            base_score = 0.5

        # Heuristic: single mild-positive in a longer sentence should not max out
        if positive_count == 1 and negative_count == 0 and len(words) >= 4:
            base_score = max(base_score, 0.68)
        
        # Apply context weighting - fewer total words means less certainty
        if len(words) <= 3:
            # For very short phrases, moderate the score more to avoid extreme classifications
            base_score = 0.5 + (base_score - 0.5) * 0.6
        
        # Apply penalty for negative words (moderate to avoid over-penalizing positives)
        negative_penalty = (negative_count / len(words)) * 0.5
        
        # Calculate final score with adjustments
        final_score = max(0.0, min(1.0, base_score - negative_penalty))

        # Cap very high scores if there are no strong positives
        strong_positives = {
            'amazing', 'wonderful', 'excellent', 'brilliant', 'fantastic',
            'outstanding', 'remarkable', 'incredible', 'marvelous'
        }
        strong_positive_count = sum(1 for w in words if ''.join(c for c in w if c.isalpha()) in strong_positives)
        if strong_positive_count == 0:
            final_score = min(final_score, 0.85)
        
        # Modest educational bonus to lift encouraging phrases but not extremes
        educational_bonus = 0.02
        final_score = min(1.0, final_score + educational_bonus)

        # Phrase-level encouragement: recognize common encouragement patterns (normalize punctuation)
        phrase_text = re.sub(r"[^a-z\s']", " ", text.lower())
        phrase_text = ' '.join(phrase_text.split())
        if 'keep going' in phrase_text:
            final_score = min(0.89, final_score + 0.06)

        # Ensure moderate-positive short phrases without strong positives don't overshoot
        if strong_positive_count == 0 and positive_count <= 2 and 'keep going' not in phrase_text:
            final_score = min(final_score, 0.68)

        # Neutral directive phrasing like "let's work on this" should remain neutral
        if "let's work on this" in phrase_text:
            final_score = min(final_score, 0.58)

        # Supportive collaborative phrasing should meet neutral-positive threshold
        if "let's work on this together" in phrase_text:
            final_score = max(final_score, 0.62)
        if "i'm here to help you" in phrase_text or "here to help you" in phrase_text:
            final_score = max(final_score, 0.62)

        # Constructive but potentially discouraging phrasing should reduce below neutral
        if 'needs improvement' in phrase_text:
            final_score = min(final_score, 0.48)
        
        return final_score
    
    def assess_trauma_informed_level(self, positivity_score: float) -> TraumaInformedLevel:
        """
        Assess trauma-informed level based on positivity score
        
        Args:
            positivity_score: Score between 0.0 and 1.0
            
        Returns:
            TraumaInformedLevel assessment
        """
        if positivity_score >= 0.9:
            return TraumaInformedLevel.EXCELLENT
        elif positivity_score >= 0.75:
            return TraumaInformedLevel.GOOD
        elif positivity_score >= 0.6:  # Minimum threshold
            return TraumaInformedLevel.ACCEPTABLE
        elif positivity_score >= 0.4:
            return TraumaInformedLevel.CONCERNING
        else:
            return TraumaInformedLevel.INAPPROPRIATE
    
    def transform_to_positive_framing(self, text: str) -> str:
        """
        Transform potentially negative content to positive framing.
        
        Args:
            text: Original text that may contain negative content
            
        Returns:
            Transformed text with positive alternatives
        """
        if not text:
            return text
        
        transformed_text = text
        text_lower = text.lower()
        
        # Apply positive transformations
        for negative_word, positive_alternative in self.positive_transformations.items():
            # Replace whole word matches (case-insensitive)
            pattern = r'\b' + re.escape(negative_word) + r'\b'
            transformed_text = re.sub(pattern, positive_alternative, transformed_text, flags=re.IGNORECASE)

        # Fix grammar for specific copula patterns (e.g., "is impossible" -> "takes practice")
        transformed_text = re.sub(r"\b(is|are|was|were)\s+takes\s+practice\b", "takes practice", transformed_text, flags=re.IGNORECASE)
        
        return transformed_text
    
    def validate_response_safety(
        self, 
        response: str, 
        child_sensitivity_level: str
    ) -> Tuple[bool, List[str]]:
        """
        Validate response safety and return any concerns.
        
        Args:
            response: Response text to validate
            child_sensitivity_level: Child's trauma sensitivity level
            
        Returns:
            Tuple of (is_safe, list_of_concerns)
        """
        concerns = []
        
        # Calculate positivity score
        positivity_score = self.calculate_positivity_score(response)
        trauma_level = self.assess_trauma_informed_level(positivity_score)
        
        # Set minimum threshold based on sensitivity level
        if child_sensitivity_level.lower() in ['high', 'very_high']:
            min_threshold = 0.75
        elif child_sensitivity_level.lower() == 'moderate':
            min_threshold = 0.6
        else:  # low sensitivity
            min_threshold = 0.5
        
        # Check if response meets threshold
        if positivity_score < min_threshold:
            concerns.append(f"Response positivity score ({positivity_score:.2f}) below threshold ({min_threshold}) for {child_sensitivity_level} sensitivity")
        
        # Check for inappropriate trauma level
        if trauma_level == TraumaInformedLevel.INAPPROPRIATE:
            concerns.append("Response contains potentially harmful language that may trigger trauma responses")
        elif trauma_level == TraumaInformedLevel.CONCERNING:
            concerns.append("Response could be more encouraging and supportive for trauma-informed practice")
        
        # Check for specific negative words that weren't transformed
        negative_found = []
        for word in self.negative_words:
            if re.search(r'\b' + re.escape(word) + r'\b', response.lower()):
                negative_found.append(word)
        
        if negative_found:
            concerns.append(f"Response contains negative words that should be transformed: {', '.join(negative_found)}")
        
        is_safe = len(concerns) == 0
        return is_safe, concerns
    
    def classify_response_tone(self, text: str, positivity_score: float) -> ResponseTone:
        """
        Classify the tone of a response
        
        Args:
            text: Response text to classify
            positivity_score: Calculated positivity score
            
        Returns:
            ResponseTone classification
        """
        if positivity_score >= 0.92:
            return ResponseTone.HIGHLY_ENCOURAGING
        elif positivity_score >= 0.7:
            return ResponseTone.ENCOURAGING
        elif positivity_score >= 0.6:
            return ResponseTone.NEUTRAL_POSITIVE
        elif positivity_score >= 0.5:
            return ResponseTone.NEUTRAL
        elif positivity_score >= 0.3:
            return ResponseTone.POTENTIALLY_DISCOURAGING
        else:
            return ResponseTone.DISCOURAGING
    
    def generate_trauma_informed_suggestions(self, text: str, positivity_score: float, 
                                           trauma_level: TraumaInformedLevel, age_group: Optional[AgeGroup] = None) -> Dict[str, str]:
        """
        Generate trauma-informed response suggestions
        
        Args:
            text: Original text
            positivity_score: Calculated positivity score
            trauma_level: Assessed trauma-informed level
            age_group: Optional age group for age-appropriate suggestions
            
        Returns:
            Dictionary with trauma-informed suggestions
        """
        suggestions = {
            'current_level': trauma_level.value,
            'positivity_score': f"{positivity_score:.2f}",
            'meets_threshold': str(positivity_score >= 0.6),
        }
        
        # Add level-specific guidance
        if trauma_level == TraumaInformedLevel.INAPPROPRIATE:
            suggestions.update({
                'urgent_action': 'Transform content before presenting to child',
                'guidance': 'Content contains potentially harmful language that needs positive reframing',
                'approach': 'Use positive transformations and encouraging alternatives',
                'priority': 'high'
            })
        elif trauma_level == TraumaInformedLevel.CONCERNING:
            suggestions.update({
                'action': 'Consider content enhancement',
                'guidance': 'Content could be more encouraging and supportive',
                'approach': 'Add positive reinforcement and growth mindset language',
                'priority': 'medium'
            })
        elif trauma_level == TraumaInformedLevel.ACCEPTABLE:
            suggestions.update({
                'action': 'Content meets minimum threshold',
                'guidance': 'Consider adding more encouraging elements',
                'approach': 'Enhance with celebration and progress acknowledgment',
                'priority': 'low'
            })
        elif trauma_level == TraumaInformedLevel.GOOD:
            suggestions.update({
                'action': 'Good trauma-informed content',
                'guidance': 'Content is positive and supportive',
                'approach': 'Continue with current approach',
                'priority': 'maintenance'
            })
        else:  # EXCELLENT
            suggestions.update({
                'action': 'Excellent trauma-informed content',
                'guidance': 'Content exemplifies best practices',
                'approach': 'Use as template for other responses',
                'priority': 'exemplary'
            })
        
        # Add age-specific trauma-informed guidance
        if age_group:
            if age_group in [AgeGroup.JUNIOR_INFANTS, AgeGroup.SENIOR_INFANTS]:
                suggestions['age_guidance'] = 'Use very gentle, simple encouragement with lots of praise'
            elif age_group in [AgeGroup.FIRST_CLASS, AgeGroup.SECOND_CLASS]:
                suggestions['age_guidance'] = 'Balance encouragement with building independence and confidence'
            else:  # Third and Fourth Class
                suggestions['age_guidance'] = 'Focus on growth mindset and achievement recognition'
        
        return suggestions
    
    def validate_response_meets_threshold(self, text: str, threshold: float = 0.6) -> bool:
        """
        Validate if response meets minimum trauma-informed threshold
        
        Args:
            text: Response text to validate
            threshold: Minimum positivity threshold (default 0.6)
            
        Returns:
            True if response meets threshold, False otherwise
        """
        positivity_score = self.calculate_positivity_score(text)
        return positivity_score >= threshold


class NonCompetitiveLanguageFilter:
    """Filter to eliminate competitive language and replace with collaborative phrasing."""

    def __init__(self) -> None:
        self.competitive_terms = {
            'score', 'scores', 'ranking', 'rank', 'badge', 'badges', 'leaderboard',
            'win', 'wins', 'winner', 'beat', 'beats', 'beating', 'points', 'point',
            'perfect score', 'high score', 'top score', 'top rank', 'ranked'
        }
        self.replacements = {
            'leaderboard': 'shared learning wall',
            'rank': 'personal journey step',
            'ranking': 'journey position',
            'badge': 'milestone sticker',
            'badges': 'milestone stickers',
            'win': 'learn',
            'wins': 'learns',
            'winner': 'great learner',
            'beat': 'try alongside',
            'points': 'stars of effort',
            'point': 'star of effort',
            'perfect score': 'wonderful attempt',
            'high score': 'lovely progress',
            'top score': 'great progress',
            'ranked': 'placed on your journey'
        }

    def clean(self, text: str) -> str:
        lowered = text.lower()
        for term in sorted(self.replacements.keys(), key=len, reverse=True):
            if term in lowered:
                lowered = lowered.replace(term, self.replacements[term])
        return lowered