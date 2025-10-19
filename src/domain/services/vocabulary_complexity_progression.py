"""
Vocabulary and Complexity Progression System for Expanded Scenario Library

Implements curriculum-aligned progression system that works with Irish curriculum stages
and provides sophisticated vocabulary complexity analysis for 50+ scenarios.

Integrates with Irish Curriculum Mapping System (Story 2.1) and supports
formal vs informal Irish English language pattern recognition.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Set, Tuple
from enum import Enum
import re
from .curriculum_integration import (
    CurriculumIntegrationService, AgeGroup, VocabularyComplexity, 
    IrishCurriculumStage, DevelopmentalAppropriateness
)
from .expanded_scenario_library import ExpandedScenarioType, ExpandedScenarioContent


class LanguagePatternType(str, Enum):
    """Types of Irish English language patterns"""
    FORMAL = "formal"
    INFORMAL = "informal"
    MIXED = "mixed"


class ProgressionLevel(str, Enum):
    """Progression levels for vocabulary development"""
    FOUNDATION = "foundation"      # Basic survival vocabulary
    DEVELOPING = "developing"      # Building conversational skills
    EXPANDING = "expanding"        # Broadening vocabulary range
    SOPHISTICATED = "sophisticated"  # Complex language use
    MASTERY = "mastery"           # Near-native fluency


@dataclass
class IrishEnglishPattern:
    """Irish English language pattern specification"""
    pattern_type: LanguagePatternType
    vocabulary: List[str]
    phrases: List[str]
    usage_context: str
    age_appropriateness: List[AgeGroup]
    examples: List[str] = field(default_factory=list)


@dataclass
class VocabularyProgression:
    """Vocabulary progression assessment for a scenario"""
    current_level: ProgressionLevel
    complexity_score: float  # 0.0-1.0
    vocabulary_coverage: Dict[VocabularyComplexity, int]
    irish_pattern_usage: Dict[LanguagePatternType, int]
    progression_recommendations: List[str]
    next_level_requirements: List[str]


@dataclass
class ScenarioComplexityAnalysis:
    """Comprehensive complexity analysis for a scenario"""
    scenario_type: ExpandedScenarioType
    age_group_suitability: Dict[AgeGroup, DevelopmentalAppropriateness]
    vocabulary_progression: VocabularyProgression
    sentence_complexity_score: float
    cultural_integration_complexity: float
    overall_complexity_rating: int  # 1-5 scale
    enhancement_suggestions: List[str]


class VocabularyComplexityProgressionService:
    """Advanced vocabulary and complexity progression system"""

    def __init__(self, curriculum_mapper: Optional[CurriculumIntegrationService] = None):
        self.curriculum_mapper = curriculum_mapper or CurriculumIntegrationService()
        
        # Initialize Irish English patterns
        self.irish_patterns = self._initialize_irish_patterns()
        
        # Initialize progression level mappings
        self.progression_mappings = self._initialize_progression_mappings()
        
        # Initialize vocabulary complexity analyzers
        self.complexity_analyzers = self._initialize_complexity_analyzers()
        
        # Cache for performance
        self._analysis_cache: Dict[str, ScenarioComplexityAnalysis] = {}

    def _initialize_irish_patterns(self) -> Dict[LanguagePatternType, List[IrishEnglishPattern]]:
        """Initialize comprehensive Irish English language patterns"""
        
        formal_patterns = [
            IrishEnglishPattern(
                pattern_type=LanguagePatternType.FORMAL,
                vocabulary=["toilet", "lift", "queue", "rubber", "jumper", "brilliant"],
                phrases=[
                    "Good morning",
                    "How do you do?",
                    "Could you please...",
                    "Would it be possible to...",
                    "I wonder if...",
                    "Thank you very much",
                    "You're most welcome",
                    "I beg your pardon"
                ],
                usage_context="Formal settings: school, official interactions, first meetings",
                age_appropriateness=[AgeGroup.SECOND_CLASS, AgeGroup.THIRD_CLASS, AgeGroup.FOURTH_CLASS],
                examples=[
                    "Could you please direct me to the toilet?",
                    "I wonder if you might help me with this problem?",
                    "You're most welcome to join our group."
                ]
            ),
            IrishEnglishPattern(
                pattern_type=LanguagePatternType.FORMAL,
                vocabulary=["lovely", "grand", "delighted", "pleased", "certainly"],
                phrases=[
                    "I'm delighted to meet you",
                    "That would be lovely",
                    "Certainly, I'd be pleased to help",
                    "How lovely to see you"
                ],
                usage_context="Polite social interactions, greeting adults, formal invitations",
                age_appropriateness=[AgeGroup.FIRST_CLASS, AgeGroup.SECOND_CLASS, AgeGroup.THIRD_CLASS, AgeGroup.FOURTH_CLASS],
                examples=[
                    "I'm delighted to make your acquaintance",
                    "That would be lovely, thank you very much"
                ]
            )
        ]
        
        informal_patterns = [
            IrishEnglishPattern(
                pattern_type=LanguagePatternType.INFORMAL,
                vocabulary=["craic", "gas", "deadly", "sound", "fair play"],
                phrases=[
                    "How's the form?",
                    "What's the story?",
                    "How are you keeping?",
                    "Grand altogether",
                    "Not too bad",
                    "Can't complain",
                    "That's gas",
                    "Sound out",
                    "Fair play to you"
                ],
                usage_context="Casual conversations with peers, playground interactions, informal settings",
                age_appropriateness=[AgeGroup.SENIOR_INFANTS, AgeGroup.FIRST_CLASS, AgeGroup.SECOND_CLASS, AgeGroup.THIRD_CLASS, AgeGroup.FOURTH_CLASS],
                examples=[
                    "How's the form? Are you having great craic?",
                    "That's gas! Fair play to you for trying!",
                    "Sound out, see you later!"
                ]
            ),
            IrishEnglishPattern(
                pattern_type=LanguagePatternType.INFORMAL,
                vocabulary=["mam", "da", "gaff", "mental", "savage"],
                phrases=[
                    "I'm grand",
                    "See you later",
                    "That's class",
                    "What's the craic?",
                    "I'm only messing",
                    "Take it handy"
                ],
                usage_context="Family conversations, friend interactions, relaxed social settings",
                age_appropriateness=[AgeGroup.FIRST_CLASS, AgeGroup.SECOND_CLASS, AgeGroup.THIRD_CLASS, AgeGroup.FOURTH_CLASS],
                examples=[
                    "I'm going to me mam's gaff later",
                    "That's mental! What's the craic with that?",
                    "Take it handy, see you tomorrow!"
                ]
            )
        ]
        
        mixed_patterns = [
            IrishEnglishPattern(
                pattern_type=LanguagePatternType.MIXED,
                vocabulary=["grand", "lovely", "brilliant", "nice", "good"],
                phrases=[
                    "That's grand, thanks",
                    "Lovely to meet you",
                    "That's brilliant!",
                    "Thanks a million",
                    "No bother at all"
                ],
                usage_context="Versatile expressions suitable for most social contexts",
                age_appropriateness=list(AgeGroup),
                examples=[
                    "That's grand, thanks a million!",
                    "Lovely to meet you! No bother at all.",
                    "That's brilliant! Thanks for helping."
                ]
            )
        ]
        
        return {
            LanguagePatternType.FORMAL: formal_patterns,
            LanguagePatternType.INFORMAL: informal_patterns,
            LanguagePatternType.MIXED: mixed_patterns
        }

    def _initialize_progression_mappings(self) -> Dict[ProgressionLevel, Dict[str, Any]]:
        """Initialize progression level mappings with curriculum alignment"""
        
        return {
            ProgressionLevel.FOUNDATION: {
                "age_groups": [AgeGroup.JUNIOR_INFANTS, AgeGroup.SENIOR_INFANTS],
                "vocabulary_complexity": [VocabularyComplexity.VERY_SIMPLE],
                "sentence_length": (2, 4),  # word count range
                "pattern_types": [LanguagePatternType.MIXED],
                "key_skills": [
                    "Basic greeting and farewell",
                    "Simple needs expression",
                    "Yes/no responses",
                    "Basic politeness words"
                ],
                "scenario_categories": ["basic_school_life", "essential_needs"]
            },
            ProgressionLevel.DEVELOPING: {
                "age_groups": [AgeGroup.SENIOR_INFANTS, AgeGroup.FIRST_CLASS],
                "vocabulary_complexity": [VocabularyComplexity.VERY_SIMPLE, VocabularyComplexity.SIMPLE],
                "sentence_length": (3, 6),
                "pattern_types": [LanguagePatternType.MIXED, LanguagePatternType.INFORMAL],
                "key_skills": [
                    "Simple conversation initiation",
                    "Basic question asking",
                    "Simple opinion expression",
                    "Playground interaction"
                ],
                "scenario_categories": ["school_interaction", "basic_social"]
            },
            ProgressionLevel.EXPANDING: {
                "age_groups": [AgeGroup.FIRST_CLASS, AgeGroup.SECOND_CLASS],
                "vocabulary_complexity": [VocabularyComplexity.SIMPLE, VocabularyComplexity.MODERATE],
                "sentence_length": (5, 8),
                "pattern_types": [LanguagePatternType.MIXED, LanguagePatternType.INFORMAL, LanguagePatternType.FORMAL],
                "key_skills": [
                    "Extended conversation",
                    "Cultural sharing",
                    "Problem description",
                    "Help seeking and offering"
                ],
                "scenario_categories": ["daily_activities", "social_interaction", "cultural_sharing"]
            },
            ProgressionLevel.SOPHISTICATED: {
                "age_groups": [AgeGroup.SECOND_CLASS, AgeGroup.THIRD_CLASS],
                "vocabulary_complexity": [VocabularyComplexity.MODERATE, VocabularyComplexity.COMPLEX],
                "sentence_length": (7, 12),
                "pattern_types": [LanguagePatternType.FORMAL, LanguagePatternType.MIXED],
                "key_skills": [
                    "Complex reasoning expression",
                    "Cultural comparison",
                    "Formal presentation",
                    "Conflict resolution"
                ],
                "scenario_categories": ["cultural_events", "advanced_social", "academic_presentation"]
            },
            ProgressionLevel.MASTERY: {
                "age_groups": [AgeGroup.THIRD_CLASS, AgeGroup.FOURTH_CLASS],
                "vocabulary_complexity": [VocabularyComplexity.COMPLEX],
                "sentence_length": (10, 20),
                "pattern_types": [LanguagePatternType.FORMAL, LanguagePatternType.INFORMAL, LanguagePatternType.MIXED],
                "key_skills": [
                    "Nuanced cultural discussion",
                    "Abstract concept explanation",
                    "Leadership communication",
                    "Advanced problem solving"
                ],
                "scenario_categories": ["advanced_cultural", "leadership", "complex_academic"]
            }
        }

    def _initialize_complexity_analyzers(self) -> Dict[str, Any]:
        """Initialize complexity analysis tools"""
        return {
            "sentence_complexity": {
                "simple_markers": ["and", "but", "so"],
                "complex_markers": ["because", "although", "however", "therefore", "meanwhile"],
                "advanced_markers": ["nevertheless", "furthermore", "consequently", "nonetheless"]
            },
            "vocabulary_sophistication": {
                "basic_connectors": ["and", "but", "so", "then"],
                "intermediate_connectors": ["because", "when", "if", "while"],
                "advanced_connectors": ["although", "however", "therefore", "nevertheless"]
            },
            "irish_cultural_markers": {
                "basic": ["please", "thank you", "lovely", "grand"],
                "intermediate": ["brilliant", "fair play", "sound", "craic"],
                "advanced": ["delighted", "how's the form", "take it handy", "no bother"]
            }
        }

    def analyze_scenario_complexity(self, scenario: ExpandedScenarioContent) -> ScenarioComplexityAnalysis:
        """Perform comprehensive complexity analysis of a scenario"""
        
        cache_key = f"{scenario.scenario_type.value}_complexity"
        if cache_key in self._analysis_cache:
            return self._analysis_cache[cache_key]
        
        # Analyze age group suitability
        age_suitability = self._analyze_age_group_suitability(scenario)
        
        # Analyze vocabulary progression
        vocab_progression = self._analyze_vocabulary_progression(scenario)
        
        # Analyze sentence complexity
        sentence_complexity = self._analyze_sentence_complexity(scenario)
        
        # Analyze cultural integration complexity
        cultural_complexity = self._analyze_cultural_integration_complexity(scenario)
        
        # Calculate overall complexity rating
        overall_rating = self._calculate_overall_complexity_rating(
            vocab_progression, sentence_complexity, cultural_complexity
        )
        
        # Generate enhancement suggestions
        enhancements = self._generate_enhancement_suggestions(scenario, vocab_progression)
        
        analysis = ScenarioComplexityAnalysis(
            scenario_type=scenario.scenario_type,
            age_group_suitability=age_suitability,
            vocabulary_progression=vocab_progression,
            sentence_complexity_score=sentence_complexity,
            cultural_integration_complexity=cultural_complexity,
            overall_complexity_rating=overall_rating,
            enhancement_suggestions=enhancements
        )
        
        self._analysis_cache[cache_key] = analysis
        return analysis

    def _analyze_age_group_suitability(self, scenario: ExpandedScenarioContent) -> Dict[AgeGroup, DevelopmentalAppropriateness]:
        """Analyze suitability of scenario for different age groups"""
        suitability = {}
        
        for age_group in AgeGroup:
            # Use curriculum mapper to assess appropriateness
            appropriateness = self.curriculum_mapper.assess_developmental_appropriateness(
                scenario.english_demonstration, age_group
            )
            suitability[age_group] = appropriateness
        
        return suitability

    def _analyze_vocabulary_progression(self, scenario: ExpandedScenarioContent) -> VocabularyProgression:
        """Analyze vocabulary progression characteristics of scenario"""
        
        # Combine all text for analysis
        full_text = f"{scenario.english_demonstration} {' '.join(scenario.irish_vocabulary_notes)}"
        
        # Analyze vocabulary complexity
        complexity = self.curriculum_mapper.analyze_vocabulary_complexity(full_text)
        
        # Calculate complexity score
        complexity_score = self._calculate_complexity_score(full_text)
        
        # Analyze vocabulary coverage
        vocab_coverage = self._analyze_vocabulary_coverage(full_text)
        
        # Analyze Irish pattern usage
        pattern_usage = self._analyze_irish_pattern_usage(full_text)
        
        # Determine current progression level
        current_level = self._determine_progression_level(complexity_score, complexity)
        
        # Generate recommendations
        recommendations = self._generate_progression_recommendations(scenario, current_level)
        
        # Determine next level requirements
        next_requirements = self._get_next_level_requirements(current_level)
        
        return VocabularyProgression(
            current_level=current_level,
            complexity_score=complexity_score,
            vocabulary_coverage=vocab_coverage,
            irish_pattern_usage=pattern_usage,
            progression_recommendations=recommendations,
            next_level_requirements=next_requirements
        )

    def _analyze_sentence_complexity(self, scenario: ExpandedScenarioContent) -> float:
        """Analyze sentence complexity score (0.0-1.0)"""
        text = scenario.english_demonstration
        
        if not text:
            return 0.0
        
        sentences = re.split(r'[.!?]+', text)
        total_complexity = 0.0
        
        for sentence in sentences:
            if not sentence.strip():
                continue
                
            # Count words
            words = sentence.split()
            word_count = len(words)
            
            # Analyze complexity markers
            complexity_markers = self.complexity_analyzers["sentence_complexity"]
            
            simple_count = sum(1 for marker in complexity_markers["simple_markers"] if marker in sentence.lower())
            complex_count = sum(1 for marker in complexity_markers["complex_markers"] if marker in sentence.lower())
            advanced_count = sum(1 for marker in complexity_markers["advanced_markers"] if marker in sentence.lower())
            
            # Calculate sentence complexity (length + structure)
            length_score = min(word_count / 20.0, 1.0)  # Normalize to 20 words max
            structure_score = (simple_count * 0.3 + complex_count * 0.6 + advanced_count * 1.0) / max(1, word_count / 5)
            
            sentence_complexity = (length_score + structure_score) / 2.0
            total_complexity += sentence_complexity
        
        return min(total_complexity / max(1, len([s for s in sentences if s.strip()])), 1.0)

    def _analyze_cultural_integration_complexity(self, scenario: ExpandedScenarioContent) -> float:
        """Analyze cultural integration complexity score (0.0-1.0)"""
        
        # Count cultural integration points
        cultural_points = len(scenario.cultural_integration_points)
        dublin_connections = len(scenario.dublin_location_connections)
        
        # Analyze vocabulary for cultural markers
        full_text = f"{scenario.english_demonstration} {' '.join(scenario.irish_vocabulary_notes)}"
        cultural_vocab_score = self._count_cultural_vocabulary(full_text)
        
        # Calculate weighted score
        integration_score = (
            (cultural_points / 5.0) * 0.4 +  # Max 5 cultural points
            (dublin_connections / 3.0) * 0.3 +  # Max 3 Dublin connections
            cultural_vocab_score * 0.3
        )
        
        return min(integration_score, 1.0)

    def _calculate_complexity_score(self, text: str) -> float:
        """Calculate overall complexity score for text (0.0-1.0)"""
        if not text:
            return 0.0
        
        words = text.split()
        if not words:
            return 0.0
        
        # Analyze different complexity factors
        word_length_score = sum(len(word) for word in words) / (len(words) * 10.0)  # Normalize to 10 chars avg
        vocabulary_diversity = len(set(word.lower() for word in words)) / len(words)
        sentence_variety = self._analyze_sentence_variety(text)
        
        # Combine scores
        complexity_score = (word_length_score + vocabulary_diversity + sentence_variety) / 3.0
        return min(complexity_score, 1.0)

    def _analyze_vocabulary_coverage(self, text: str) -> Dict[VocabularyComplexity, int]:
        """Analyze vocabulary coverage across complexity levels"""
        coverage = {level: 0 for level in VocabularyComplexity}
        
        words = [word.lower().strip('.,!?') for word in text.split()]
        
        for word in words:
            # Check against curriculum mapper vocabulary sets
            for complexity, vocab_set in self.curriculum_mapper.vocabulary_by_complexity.items():
                if word in vocab_set:
                    coverage[complexity] += 1
                    break
        
        return coverage

    def _analyze_irish_pattern_usage(self, text: str) -> Dict[LanguagePatternType, int]:
        """Analyze usage of Irish English patterns"""
        usage = {pattern_type: 0 for pattern_type in LanguagePatternType}
        text_lower = text.lower()
        
        for pattern_type, patterns in self.irish_patterns.items():
            for pattern in patterns:
                # Check vocabulary usage
                for vocab_word in pattern.vocabulary:
                    if vocab_word.lower() in text_lower:
                        usage[pattern_type] += 1
                
                # Check phrase usage
                for phrase in pattern.phrases:
                    if phrase.lower() in text_lower:
                        usage[pattern_type] += 2  # Phrases weighted higher
        
        return usage

    def _determine_progression_level(self, complexity_score: float, vocabulary_complexity: VocabularyComplexity) -> ProgressionLevel:
        """Determine current progression level based on analysis"""
        
        # Map vocabulary complexity to progression level
        complexity_mapping = {
            VocabularyComplexity.VERY_SIMPLE: ProgressionLevel.FOUNDATION,
            VocabularyComplexity.SIMPLE: ProgressionLevel.DEVELOPING,
            VocabularyComplexity.MODERATE: ProgressionLevel.EXPANDING,
            VocabularyComplexity.COMPLEX: ProgressionLevel.SOPHISTICATED
        }
        
        base_level = complexity_mapping.get(vocabulary_complexity, ProgressionLevel.DEVELOPING)
        
        # Adjust based on complexity score
        if complexity_score >= 0.8:
            if base_level == ProgressionLevel.SOPHISTICATED:
                return ProgressionLevel.MASTERY
            elif base_level == ProgressionLevel.EXPANDING:
                return ProgressionLevel.SOPHISTICATED
            elif base_level == ProgressionLevel.DEVELOPING:
                return ProgressionLevel.EXPANDING
        elif complexity_score <= 0.3:
            if base_level == ProgressionLevel.DEVELOPING:
                return ProgressionLevel.FOUNDATION
        
        return base_level

    def _generate_progression_recommendations(self, scenario: ExpandedScenarioContent, current_level: ProgressionLevel) -> List[str]:
        """Generate progression recommendations for scenario"""
        recommendations = []
        
        level_mapping = self.progression_mappings[current_level]
        
        # General recommendations based on level
        if current_level == ProgressionLevel.FOUNDATION:
            recommendations.extend([
                "Focus on simple, clear vocabulary",
                "Use short, direct sentences",
                "Emphasize essential survival phrases",
                "Include lots of repetition and practice"
            ])
        elif current_level == ProgressionLevel.DEVELOPING:
            recommendations.extend([
                "Introduce more varied vocabulary gradually",
                "Practice simple conversation patterns",
                "Add basic Irish English expressions",
                "Encourage longer responses"
            ])
        elif current_level == ProgressionLevel.EXPANDING:
            recommendations.extend([
                "Include cultural context explanations",
                "Practice both formal and informal patterns",
                "Develop storytelling abilities",
                "Introduce problem-solving scenarios"
            ])
        elif current_level == ProgressionLevel.SOPHISTICATED:
            recommendations.extend([
                "Focus on nuanced language use",
                "Practice complex reasoning expression",
                "Develop cultural comparison skills",
                "Encourage creative language use"
            ])
        else:  # MASTERY
            recommendations.extend([
                "Challenge with advanced concepts",
                "Practice leadership communication",
                "Develop abstract thinking expression",
                "Encourage teaching others"
            ])
        
        # Scenario-specific recommendations
        if scenario.category.value == "school_life":
            recommendations.append("Practice classroom-specific vocabulary and etiquette")
        elif scenario.category.value == "cultural_events":
            recommendations.append("Develop cultural appreciation and comparison skills")
        
        return recommendations

    def _get_next_level_requirements(self, current_level: ProgressionLevel) -> List[str]:
        """Get requirements for advancing to next progression level"""
        
        next_level_map = {
            ProgressionLevel.FOUNDATION: ProgressionLevel.DEVELOPING,
            ProgressionLevel.DEVELOPING: ProgressionLevel.EXPANDING,
            ProgressionLevel.EXPANDING: ProgressionLevel.SOPHISTICATED,
            ProgressionLevel.SOPHISTICATED: ProgressionLevel.MASTERY,
            ProgressionLevel.MASTERY: ProgressionLevel.MASTERY  # Already at top
        }
        
        next_level = next_level_map[current_level]
        
        if next_level == current_level:  # Already at mastery
            return ["Continue practicing advanced skills", "Focus on helping others learn"]
        
        next_mapping = self.progression_mappings[next_level]
        return next_mapping["key_skills"]

    def _calculate_overall_complexity_rating(self, vocab_progression: VocabularyProgression, 
                                           sentence_complexity: float, 
                                           cultural_complexity: float) -> int:
        """Calculate overall complexity rating (1-5 scale)"""
        
        # Convert progression level to numeric score
        level_scores = {
            ProgressionLevel.FOUNDATION: 1,
            ProgressionLevel.DEVELOPING: 2,
            ProgressionLevel.EXPANDING: 3,
            ProgressionLevel.SOPHISTICATED: 4,
            ProgressionLevel.MASTERY: 5
        }
        
        level_score = level_scores[vocab_progression.current_level]
        
        # Weighted average of all factors
        overall_score = (
            level_score * 0.4 +
            (sentence_complexity * 5) * 0.3 +
            (cultural_complexity * 5) * 0.3
        )
        
        return max(1, min(5, round(overall_score)))

    def _generate_enhancement_suggestions(self, scenario: ExpandedScenarioContent, 
                                        vocab_progression: VocabularyProgression) -> List[str]:
        """Generate enhancement suggestions for scenario"""
        suggestions = []
        
        # Based on vocabulary progression recommendations
        suggestions.extend(vocab_progression.progression_recommendations[:3])
        
        # Based on Irish pattern usage
        pattern_usage = vocab_progression.irish_pattern_usage
        if pattern_usage[LanguagePatternType.FORMAL] < 2:
            suggestions.append("Add more formal Irish English expressions")
        if pattern_usage[LanguagePatternType.INFORMAL] < 2:
            suggestions.append("Include casual Irish expressions for peer interaction")
        
        # Based on cultural integration
        if len(scenario.cultural_integration_points) < 3:
            suggestions.append("Enhance cultural context and background information")
        
        # Based on Dublin connections
        if len(scenario.dublin_location_connections) < 2:
            suggestions.append("Add specific Dublin location references")
        
        return suggestions[:5]  # Limit to top 5 suggestions

    def _analyze_sentence_variety(self, text: str) -> float:
        """Analyze sentence variety and structure (0.0-1.0)"""
        sentences = re.split(r'[.!?]+', text)
        if len(sentences) <= 1:
            return 0.3  # Low variety for single sentence
        
        # Analyze sentence lengths
        lengths = [len(sentence.split()) for sentence in sentences if sentence.strip()]
        if not lengths:
            return 0.0
        
        # Calculate variety (standard deviation normalized)
        avg_length = sum(lengths) / len(lengths)
        variance = sum((length - avg_length) ** 2 for length in lengths) / len(lengths)
        variety_score = min(variance / 10.0, 1.0)  # Normalize
        
        return variety_score

    def _count_cultural_vocabulary(self, text: str) -> float:
        """Count cultural vocabulary markers (0.0-1.0)"""
        text_lower = text.lower()
        cultural_markers = self.complexity_analyzers["irish_cultural_markers"]
        
        total_markers = 0
        for level, markers in cultural_markers.items():
            for marker in markers:
                if marker in text_lower:
                    total_markers += 1
        
        # Normalize based on text length
        words = text.split()
        if not words:
            return 0.0
        
        return min(total_markers / (len(words) / 10.0), 1.0)

    def get_progression_summary(self, scenarios: List[ExpandedScenarioContent]) -> Dict[str, Any]:
        """Get progression summary across multiple scenarios"""
        
        level_distribution = {level: 0 for level in ProgressionLevel}
        complexity_distribution = {i: 0 for i in range(1, 6)}
        pattern_usage_summary = {pattern: 0 for pattern in LanguagePatternType}
        
        for scenario in scenarios:
            analysis = self.analyze_scenario_complexity(scenario)
            
            level_distribution[analysis.vocabulary_progression.current_level] += 1
            complexity_distribution[analysis.overall_complexity_rating] += 1
            
            for pattern, count in analysis.vocabulary_progression.irish_pattern_usage.items():
                pattern_usage_summary[pattern] += count
        
        return {
            "total_scenarios": len(scenarios),
            "progression_level_distribution": {k.value: v for k, v in level_distribution.items()},
            "complexity_rating_distribution": complexity_distribution,
            "irish_pattern_usage_summary": {k.value: v for k, v in pattern_usage_summary.items()},
            "average_complexity": sum(i * count for i, count in complexity_distribution.items()) / len(scenarios) if scenarios else 0,
            "progression_coverage": {
                "foundation_to_developing": level_distribution[ProgressionLevel.FOUNDATION] + level_distribution[ProgressionLevel.DEVELOPING],
                "expanding_to_sophisticated": level_distribution[ProgressionLevel.EXPANDING] + level_distribution[ProgressionLevel.SOPHISTICATED],
                "mastery_level": level_distribution[ProgressionLevel.MASTERY]
            }
        }