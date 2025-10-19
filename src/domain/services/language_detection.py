"""
Language Detection Domain Service

Extracted from the monolithic educational_context_processor.py.
This service handles language detection and confidence assessment for child speech input.

Implements ILanguageDetectionService interface for dependency injection.
"""

import re
from typing import Dict
from src.application.interfaces.services import (
    ILanguageDetectionService, 
    DetectedLanguage
)


class LanguageDetectionService(ILanguageDetectionService):
    """
    Language detection service for Chinese/English classification.
    
    Extracted from LanguageDetector class in monolithic processor.
    Now implements interface contract for dependency injection.
    """
    
    def __init__(self):
        """Initialize language detection patterns and indicators."""
        # Simple Chinese character ranges (basic implementation)
        # Using main CJK Unified Ideographs block which covers most common Chinese characters
        self.chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
        
        # Common English words for basic detection
        self.english_indicators = {
            'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one',
            'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'its', 'may', 'new', 'now', 'old',
            'see', 'two', 'way', 'who', 'boy', 'did', 'man', 'end', 'few', 'got', 'let', 'put', 'say',
            'she', 'too', 'use', 'hello', 'help', 'please', 'thank', 'thanks', 'sorry', 'yes', 'good'
        }
    
    def detect_language(self, text: str) -> DetectedLanguage:
        """
        Detect primary language in text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            DetectedLanguage enum value
        """
        if not text or not text.strip():
            return DetectedLanguage.UNKNOWN
        
        # Check for Chinese characters
        chinese_chars = len(self.chinese_pattern.findall(text))
        
        # Check for English indicators (words in our English indicator set)
        words = text.lower().split()
        english_indicators_found = sum(1 for word in words if word in self.english_indicators)
        
        # Check if text has alphabetic characters (potential English)
        has_alphabetic = any(c.isalpha() and ord(c) < 128 for c in text)
        total_words = len(words)
        
        # Improved classification logic
        if chinese_chars > 0 and english_indicators_found > 0:
            # Has both Chinese characters AND English indicators - definitely mixed
            return DetectedLanguage.MIXED
        elif chinese_chars > 0 and has_alphabetic and total_words > 1:
            # Has Chinese characters AND multiple words with English letters - likely mixed
            return DetectedLanguage.MIXED
        elif chinese_chars > 0:
            # Has Chinese characters, no significant English
            return DetectedLanguage.CHINESE
        elif english_indicators_found > 0:
            # Has known English words
            return DetectedLanguage.ENGLISH
        elif has_alphabetic and total_words > 0:
            # Has alphabetic characters that could be English
            # Additional check: if it's mostly ASCII letters, assume English
            alpha_chars = [c for c in text if c.isalpha()]
            if len(alpha_chars) > 0 and all(ord(c) < 128 for c in alpha_chars):
                return DetectedLanguage.ENGLISH
            else:
                return DetectedLanguage.UNKNOWN
        else:
            return DetectedLanguage.UNKNOWN
    
    def assess_confidence_level(self, text: str, detected_language: DetectedLanguage) -> float:
        """
        Assess child's confidence level based on language use.
        
        Args:
            text: Input text to analyze
            detected_language: Previously detected language
            
        Returns:
            Confidence score between 0.0 and 1.0
        """
        if not text or not text.strip():
            return 0.0
        
        words = text.lower().split()
        word_count = len(words)
        
        # Base confidence assessment
        base_confidence = 0.3  # Neutral starting point
        
        if detected_language == DetectedLanguage.CHINESE:
            # Child is comfortable in native language
            base_confidence = 0.8
            
            # Longer responses in Chinese indicate comfort
            if word_count > 3:
                base_confidence = min(0.9, base_confidence + 0.1)
                
        elif detected_language == DetectedLanguage.ENGLISH:
            # Attempting English shows some confidence
            base_confidence = 0.5
            
            # Check for complexity indicators
            english_indicators_found = sum(1 for word in words if word in self.english_indicators)
            if english_indicators_found > 0:
                # Using known English words shows higher confidence
                confidence_boost = min(0.3, english_indicators_found * 0.1)
                base_confidence += confidence_boost
                
            # Longer English responses indicate growing confidence
            if word_count > 2:
                base_confidence = min(0.8, base_confidence + 0.1)
                
        elif detected_language == DetectedLanguage.MIXED:
            # Code-switching shows transitional confidence
            base_confidence = 0.4
            
            # Balanced mixing might indicate bilingual comfort
            chinese_chars = len(self.chinese_pattern.findall(text))
            if chinese_chars > 0 and word_count > chinese_chars:
                base_confidence = 0.6
                
        # Cap confidence scores appropriately
        return max(0.0, min(1.0, base_confidence))
    
    def analyze_language_mixing(self, text: str) -> Dict[str, float]:
        """
        Analyze the ratio of different languages in mixed text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary with language ratios
        """
        if not text or not text.strip():
            return {"chinese": 0.0, "english": 0.0, "unknown": 1.0}
        
        # Count Chinese characters
        chinese_chars = len(self.chinese_pattern.findall(text))
        
        # Count English indicators
        words = text.lower().split()
        english_indicators_found = sum(1 for word in words if word in self.english_indicators)
        
        # Count alphabetic characters (potential English)
        alpha_chars = [c for c in text if c.isalpha() and ord(c) < 128]
        
        total_chars = len(text)
        if total_chars == 0:
            return {"chinese": 0.0, "english": 0.0, "unknown": 1.0}
        
        # Calculate rough ratios
        chinese_ratio = chinese_chars / total_chars
        english_ratio = len(alpha_chars) / total_chars
        
        # Adjust based on word-level indicators
        if english_indicators_found > 0:
            word_boost = min(0.3, english_indicators_found * 0.1)
            english_ratio = min(1.0, english_ratio + word_boost)
        
        # Normalize ratios
        total_ratio = chinese_ratio + english_ratio
        if total_ratio > 1.0:
            chinese_ratio = chinese_ratio / total_ratio
            english_ratio = english_ratio / total_ratio
        
        unknown_ratio = max(0.0, 1.0 - chinese_ratio - english_ratio)
        
        return {
            "chinese": round(chinese_ratio, 2),
            "english": round(english_ratio, 2), 
            "unknown": round(unknown_ratio, 2)
        }