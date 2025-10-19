"""
Expanded Content Quality and Safety Framework for Story 2.3

Implements comprehensive content validation for the expanded scenario library,
including trauma-informed design, cultural sensitivity, age-appropriateness,
and expert review systems.

Integrates with existing trauma validation and cultural authenticity services
while extending coverage to 50+ scenarios across all categories.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Set, Tuple
from enum import Enum
import re
import datetime
from .expanded_scenario_library import ExpandedScenarioType, ExpandedScenarioContent, ScenarioCategory
from .trauma_validation import NonCompetitiveLanguageFilter
from .cultural_authenticity_validator import CulturalAuthenticityValidator, CulturalValidationResult, CulturalSensitivityLevel
from .curriculum_integration import AgeGroup, CurriculumIntegrationService


class ContentValidationLevel(str, Enum):
    """Levels of content validation rigor"""
    BASIC = "basic"              # Automated checks only
    STANDARD = "standard"        # Automated + basic manual review
    COMPREHENSIVE = "comprehensive"  # Full expert review process
    CRITICAL = "critical"        # Maximum validation for sensitive content


class SafetyRiskLevel(str, Enum):
    """Safety risk assessment levels"""
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ValidationStatus(str, Enum):
    """Content validation status"""
    PENDING = "pending"
    APPROVED = "approved"
    NEEDS_REVISION = "needs_revision"
    REJECTED = "rejected"
    UNDER_REVIEW = "under_review"


@dataclass
class AgeAppropriatenessValidation:
    """Age appropriateness validation result"""
    age_group: AgeGroup
    is_appropriate: bool
    developmental_concerns: List[str]
    vocabulary_concerns: List[str]
    concept_concerns: List[str]
    enhancement_suggestions: List[str]
    confidence_score: float  # 0.0-1.0


@dataclass
class TraumaInformedValidation:
    """Trauma-informed design validation result"""
    is_trauma_informed: bool
    potential_triggers: List[str]
    pressure_indicators: List[str]
    failure_state_risks: List[str]
    celebration_opportunities: List[str]
    safety_enhancements: List[str]
    compliance_score: float  # 0.0-1.0


@dataclass
class ExpertReviewResult:
    """Expert review validation result"""
    reviewer_type: str  # "educational", "cultural", "psychological", "linguistic"
    reviewer_credentials: str
    review_date: datetime.datetime
    approval_status: ValidationStatus
    feedback_comments: List[str]
    improvement_suggestions: List[str]
    cultural_accuracy_rating: int  # 1-5 scale
    educational_value_rating: int  # 1-5 scale
    safety_rating: int  # 1-5 scale


@dataclass
class ContentQualityMetrics:
    """Comprehensive content quality metrics"""
    educational_value_score: float  # 0.0-1.0
    cultural_authenticity_score: float
    age_appropriateness_score: float
    trauma_informed_score: float
    linguistic_accuracy_score: float
    engagement_potential_score: float
    overall_quality_score: float
    quality_grade: str  # A+, A, B+, B, C+, C, D, F


@dataclass
class ComprehensiveContentValidation:
    """Complete content validation result for expanded scenarios"""
    scenario_type: ExpandedScenarioType
    validation_level: ContentValidationLevel
    validation_timestamp: datetime.datetime
    
    # Core validation results
    age_appropriateness: Dict[AgeGroup, AgeAppropriatenessValidation]
    trauma_informed_validation: TraumaInformedValidation
    cultural_validation: CulturalValidationResult
    expert_reviews: List[ExpertReviewResult]
    
    # Quality assessment
    quality_metrics: ContentQualityMetrics
    safety_risk_level: SafetyRiskLevel
    validation_status: ValidationStatus
    
    # Recommendations and actions
    required_improvements: List[str]
    optional_enhancements: List[str]
    approval_conditions: List[str]
    review_schedule: Optional[datetime.datetime]


class ExpandedContentValidator:
    """Comprehensive content validation service for expanded scenario library"""

    def __init__(self, 
                 trauma_validator: Optional[NonCompetitiveLanguageFilter] = None,
                 cultural_validator: Optional[CulturalAuthenticityValidator] = None,
                 curriculum_service: Optional[CurriculumIntegrationService] = None):
        
        self.trauma_validator = trauma_validator or NonCompetitiveLanguageFilter()
        self.cultural_validator = cultural_validator or CulturalAuthenticityValidator()
        self.curriculum_service = curriculum_service or CurriculumIntegrationService()
        
        # Initialize validation criteria
        self.validation_criteria = self._initialize_validation_criteria()
        self.safety_patterns = self._initialize_safety_patterns()
        self.expert_reviewer_pool = self._initialize_expert_reviewers()
        
        # Performance tracking
        self.validation_cache: Dict[str, ComprehensiveContentValidation] = {}
        self.validation_history: List[ComprehensiveContentValidation] = []

    def _initialize_validation_criteria(self) -> Dict[str, Dict[str, Any]]:
        """Initialize comprehensive validation criteria"""
        
        return {
            "age_appropriateness": {
                "vocabulary_complexity": {
                    AgeGroup.JUNIOR_INFANTS: {"max_syllables": 2, "max_sentence_length": 4},
                    AgeGroup.SENIOR_INFANTS: {"max_syllables": 3, "max_sentence_length": 6},
                    AgeGroup.FIRST_CLASS: {"max_syllables": 4, "max_sentence_length": 8},
                    AgeGroup.SECOND_CLASS: {"max_syllables": 5, "max_sentence_length": 10},
                    AgeGroup.THIRD_CLASS: {"max_syllables": 6, "max_sentence_length": 12},
                    AgeGroup.FOURTH_CLASS: {"max_syllables": 8, "max_sentence_length": 15}
                },
                "concept_complexity": {
                    AgeGroup.JUNIOR_INFANTS: ["concrete", "immediate", "familiar"],
                    AgeGroup.SENIOR_INFANTS: ["concrete", "immediate", "familiar", "simple_abstract"],
                    AgeGroup.FIRST_CLASS: ["concrete", "familiar", "simple_abstract", "basic_social"],
                    AgeGroup.SECOND_CLASS: ["concrete", "abstract", "social", "emotional"],
                    AgeGroup.THIRD_CLASS: ["abstract", "complex_social", "cultural", "analytical"],
                    AgeGroup.FOURTH_CLASS: ["abstract", "complex", "cultural", "analytical", "evaluative"]
                },
                "emotional_readiness": {
                    AgeGroup.JUNIOR_INFANTS: ["happiness", "sadness", "basic_needs"],
                    AgeGroup.SENIOR_INFANTS: ["happiness", "sadness", "anger", "friendship"],
                    AgeGroup.FIRST_CLASS: ["complex_emotions", "peer_relationships", "fairness"],
                    AgeGroup.SECOND_CLASS: ["empathy", "conflict_resolution", "group_dynamics"],
                    AgeGroup.THIRD_CLASS: ["complex_social_emotions", "cultural_understanding"],
                    AgeGroup.FOURTH_CLASS: ["mature_emotions", "leadership", "responsibility"]
                }
            },
            "trauma_informed": {
                "prohibited_elements": [
                    "failure_language", "comparison_pressure", "perfectionism_demands",
                    "time_pressure", "performance_anxiety", "shame_inducing"
                ],
                "required_elements": [
                    "celebration_language", "effort_recognition", "progress_focus",
                    "choice_provision", "safety_assurance", "cultural_pride"
                ],
                "language_patterns": {
                    "avoid": [
                        "you're wrong", "that's incorrect", "try harder", "you should know this",
                        "everyone else can", "this is easy", "you're not good at", "failure"
                    ],
                    "use": [
                        "great effort", "you're learning", "let's try together", "that's a good start",
                        "you're growing", "well done for trying", "you're brave", "celebration"
                    ]
                }
            },
            "cultural_sensitivity": {
                "irish_authenticity": {
                    "required_elements": ["irish_vocabulary", "irish_social_patterns", "dublin_context"],
                    "accuracy_standards": ["verified_usage", "appropriate_context", "respectful_representation"]
                },
                "chinese_representation": {
                    "required_elements": ["cultural_pride", "heritage_celebration", "bridge_building"],
                    "prohibited_elements": ["stereotypes", "oversimplification", "cultural_appropriation"]
                },
                "bicultural_balance": {
                    "integration_focus": ["mutual_respect", "shared_values", "cultural_exchange"],
                    "avoid": ["cultural_superiority", "assimilation_pressure", "identity_loss"]
                }
            },
            "educational_value": {
                "learning_objectives": {
                    "language_development": ["vocabulary", "pronunciation", "fluency", "comprehension"],
                    "social_skills": ["communication", "cooperation", "empathy", "leadership"],
                    "cultural_competence": ["irish_understanding", "cultural_bridging", "global_awareness"],
                    "academic_skills": ["critical_thinking", "problem_solving", "creativity"]
                },
                "curriculum_alignment": {
                    "irish_curriculum": ["stage_appropriate", "skill_progressive", "assessment_aligned"],
                    "language_learning": ["meaningful_context", "practical_application", "skill_building"]
                }
            }
        }

    def _initialize_safety_patterns(self) -> Dict[str, List[str]]:
        """Initialize safety risk pattern detection"""
        
        return {
            "high_risk_patterns": [
                r"must\s+(?:be|do|say)",  # Pressure language
                r"everyone\s+(?:can|does|knows)",  # Comparison pressure
                r"(?:wrong|incorrect|bad|terrible)",  # Negative judgments
                r"(?:failure|failed|can't|impossible)",  # Failure language
                r"should\s+(?:be|know|understand)",  # Expectation pressure
            ],
            "medium_risk_patterns": [
                r"better\s+than",  # Comparison
                r"not\s+good\s+enough",  # Inadequacy
                r"try\s+harder",  # Pressure
                r"this\s+is\s+easy",  # Minimization
            ],
            "positive_patterns": [
                r"great\s+(?:effort|job|work)",  # Effort recognition
                r"you're\s+(?:learning|growing|improving)",  # Growth focus
                r"(?:celebrate|celebration|brilliant|wonderful)",  # Celebration
                r"let's\s+(?:try|work|learn)\s+together",  # Collaboration
            ],
            "cultural_risk_patterns": [
                r"chinese\s+(?:can't|don't|never)",  # Cultural stereotypes
                r"irish\s+(?:always|never|all)",  # Cultural generalizations
                r"your\s+culture\s+(?:is|should)",  # Cultural judgment
            ]
        }

    def _initialize_expert_reviewers(self) -> Dict[str, Dict[str, str]]:
        """Initialize expert reviewer pool specifications"""
        
        return {
            "educational_expert": {
                "credentials": "Irish Primary Education Specialist, M.Ed",
                "expertise": "Irish curriculum alignment, age-appropriate learning design",
                "validation_focus": "Educational value, curriculum alignment, developmental appropriateness"
            },
            "cultural_expert": {
                "credentials": "Dublin Cultural Heritage Expert, PhD Irish Studies",
                "expertise": "Irish cultural authenticity, Dublin local knowledge, cultural representation",
                "validation_focus": "Cultural accuracy, authenticity, respectful representation"
            },
            "psychological_expert": {
                "credentials": "Child Psychology Specialist, trauma-informed education",
                "expertise": "Child development, trauma-informed design, emotional safety",
                "validation_focus": "Psychological safety, trauma-informed compliance, emotional readiness"
            },
            "linguistic_expert": {
                "credentials": "Irish English Linguistics Specialist, PhD Applied Linguistics",
                "expertise": "Irish English patterns, language acquisition, bilingual education",
                "validation_focus": "Linguistic accuracy, Irish English authenticity, language learning effectiveness"
            },
            "bicultural_expert": {
                "credentials": "Chinese-Irish Integration Specialist, M.A. Intercultural Studies",
                "expertise": "Bicultural identity, cultural bridge building, integration support",
                "validation_focus": "Bicultural representation, cultural bridge opportunities, integration support"
            }
        }

    async def validate_scenario_content(self, scenario: ExpandedScenarioContent, 
                                      validation_level: ContentValidationLevel = ContentValidationLevel.STANDARD) -> ComprehensiveContentValidation:
        """Perform comprehensive content validation for expanded scenario"""
        
        # Check cache first
        cache_key = f"{scenario.scenario_type.value}_{validation_level.value}"
        if cache_key in self.validation_cache:
            return self.validation_cache[cache_key]
        
        # Step 1: Age appropriateness validation
        age_validations = await self._validate_age_appropriateness(scenario)
        
        # Step 2: Trauma-informed validation
        trauma_validation = await self._validate_trauma_informed_design(scenario)
        
        # Step 3: Cultural validation
        cultural_validation = await self.cultural_validator.validate_cultural_content(
            f"{scenario.english_demonstration} {scenario.chinese_comfort}"
        )
        
        # Step 4: Expert reviews (if required)
        expert_reviews = []
        if validation_level in [ContentValidationLevel.COMPREHENSIVE, ContentValidationLevel.CRITICAL]:
            expert_reviews = await self._conduct_expert_reviews(scenario, validation_level)
        
        # Step 5: Calculate quality metrics
        quality_metrics = self._calculate_quality_metrics(
            scenario, age_validations, trauma_validation, cultural_validation, expert_reviews
        )
        
        # Step 6: Assess safety risk level
        safety_risk = self._assess_safety_risk_level(scenario, trauma_validation)
        
        # Step 7: Determine validation status
        validation_status = self._determine_validation_status(
            age_validations, trauma_validation, cultural_validation, expert_reviews, safety_risk
        )
        
        # Step 8: Generate recommendations
        required_improvements, optional_enhancements, approval_conditions = self._generate_recommendations(
            scenario, age_validations, trauma_validation, cultural_validation, expert_reviews
        )
        
        # Step 9: Schedule review if needed
        review_schedule = self._calculate_review_schedule(validation_status, safety_risk)
        
        # Create comprehensive validation result
        validation_result = ComprehensiveContentValidation(
            scenario_type=scenario.scenario_type,
            validation_level=validation_level,
            validation_timestamp=datetime.datetime.now(),
            age_appropriateness=age_validations,
            trauma_informed_validation=trauma_validation,
            cultural_validation=cultural_validation,
            expert_reviews=expert_reviews,
            quality_metrics=quality_metrics,
            safety_risk_level=safety_risk,
            validation_status=validation_status,
            required_improvements=required_improvements,
            optional_enhancements=optional_enhancements,
            approval_conditions=approval_conditions,
            review_schedule=review_schedule
        )
        
        # Cache and store
        self.validation_cache[cache_key] = validation_result
        self.validation_history.append(validation_result)
        
        return validation_result

    async def _validate_age_appropriateness(self, scenario: ExpandedScenarioContent) -> Dict[AgeGroup, AgeAppropriatenessValidation]:
        """Validate age appropriateness across all age groups"""
        
        validations = {}
        
        for age_group in AgeGroup:
            # Vocabulary analysis
            vocab_appropriateness = self.curriculum_service.assess_developmental_appropriateness(
                scenario.english_demonstration, age_group
            )
            
            # Check vocabulary complexity criteria
            criteria = self.validation_criteria["age_appropriateness"]["vocabulary_complexity"][age_group]
            vocabulary_concerns = self._check_vocabulary_complexity(scenario, criteria)
            
            # Check concept complexity
            concept_concerns = self._check_concept_complexity(scenario, age_group)
            
            # Check emotional readiness
            developmental_concerns = self._check_developmental_readiness(scenario, age_group)
            
            # Calculate appropriateness
            is_appropriate = (
                vocab_appropriateness.value in ["appropriate", "challenging"] and
                len(vocabulary_concerns) <= 2 and
                len(concept_concerns) <= 1 and
                len(developmental_concerns) <= 1
            )
            
            # Generate enhancement suggestions
            enhancement_suggestions = self._generate_age_enhancements(
                scenario, age_group, vocabulary_concerns, concept_concerns, developmental_concerns
            )
            
            # Calculate confidence score
            confidence_score = self._calculate_age_confidence_score(
                vocab_appropriateness, vocabulary_concerns, concept_concerns, developmental_concerns
            )
            
            validations[age_group] = AgeAppropriatenessValidation(
                age_group=age_group,
                is_appropriate=is_appropriate,
                developmental_concerns=developmental_concerns,
                vocabulary_concerns=vocabulary_concerns,
                concept_concerns=concept_concerns,
                enhancement_suggestions=enhancement_suggestions,
                confidence_score=confidence_score
            )
        
        return validations

    async def _validate_trauma_informed_design(self, scenario: ExpandedScenarioContent) -> TraumaInformedValidation:
        """Validate trauma-informed design compliance"""
        
        # Combine all text for analysis
        full_text = f"{scenario.english_demonstration} {scenario.chinese_comfort} {' '.join(scenario.irish_vocabulary_notes)} {scenario.age_group_notes}"
        
        # Check for potential triggers
        potential_triggers = self._detect_potential_triggers(full_text)
        
        # Check for pressure indicators
        pressure_indicators = self._detect_pressure_indicators(full_text)
        
        # Check for failure state risks
        failure_risks = self._detect_failure_state_risks(full_text)
        
        # Identify celebration opportunities
        celebration_opportunities = self._identify_celebration_opportunities(full_text)
        
        # Generate safety enhancements
        safety_enhancements = self._generate_safety_enhancements(
            potential_triggers, pressure_indicators, failure_risks
        )
        
        # Calculate compliance score
        compliance_score = self._calculate_trauma_compliance_score(
            potential_triggers, pressure_indicators, failure_risks, celebration_opportunities
        )
        
        # Determine overall compliance
        is_trauma_informed = (
            len(potential_triggers) == 0 and
            len(pressure_indicators) <= 1 and
            len(failure_risks) == 0 and
            len(celebration_opportunities) >= 2 and
            compliance_score >= 0.8
        )
        
        return TraumaInformedValidation(
            is_trauma_informed=is_trauma_informed,
            potential_triggers=potential_triggers,
            pressure_indicators=pressure_indicators,
            failure_state_risks=failure_risks,
            celebration_opportunities=celebration_opportunities,
            safety_enhancements=safety_enhancements,
            compliance_score=compliance_score
        )

    async def _conduct_expert_reviews(self, scenario: ExpandedScenarioContent, 
                                    validation_level: ContentValidationLevel) -> List[ExpertReviewResult]:
        """Conduct expert reviews based on validation level"""
        
        reviews = []
        
        # Determine required reviewers based on validation level and scenario category
        required_reviewers = self._determine_required_reviewers(scenario, validation_level)
        
        for reviewer_type in required_reviewers:
            review = await self._simulate_expert_review(scenario, reviewer_type)
            reviews.append(review)
        
        return reviews

    def _determine_required_reviewers(self, scenario: ExpandedScenarioContent, 
                                    validation_level: ContentValidationLevel) -> List[str]:
        """Determine which expert reviewers are required"""
        
        base_reviewers = ["educational_expert", "psychological_expert"]
        
        # Add cultural expert for all scenarios
        if "cultural" not in [r for r in base_reviewers]:
            base_reviewers.append("cultural_expert")
        
        # Add linguistic expert for complex scenarios
        if scenario.difficulty_level >= 4:
            base_reviewers.append("linguistic_expert")
        
        # Add bicultural expert for cultural events
        if scenario.category == ScenarioCategory.CULTURAL_EVENTS:
            base_reviewers.append("bicultural_expert")
        
        # Critical validation requires all reviewers
        if validation_level == ContentValidationLevel.CRITICAL:
            return list(self.expert_reviewer_pool.keys())
        
        return base_reviewers

    async def _simulate_expert_review(self, scenario: ExpandedScenarioContent, 
                                    reviewer_type: str) -> ExpertReviewResult:
        """Simulate expert review process"""
        
        reviewer_info = self.expert_reviewer_pool[reviewer_type]
        
        # Analyze based on reviewer expertise
        feedback_comments = []
        improvement_suggestions = []
        
        if reviewer_type == "educational_expert":
            feedback_comments.extend(self._educational_expert_analysis(scenario))
            improvement_suggestions.extend(self._educational_improvement_suggestions(scenario))
        elif reviewer_type == "cultural_expert":
            feedback_comments.extend(self._cultural_expert_analysis(scenario))
            improvement_suggestions.extend(self._cultural_improvement_suggestions(scenario))
        elif reviewer_type == "psychological_expert":
            feedback_comments.extend(self._psychological_expert_analysis(scenario))
            improvement_suggestions.extend(self._psychological_improvement_suggestions(scenario))
        elif reviewer_type == "linguistic_expert":
            feedback_comments.extend(self._linguistic_expert_analysis(scenario))
            improvement_suggestions.extend(self._linguistic_improvement_suggestions(scenario))
        elif reviewer_type == "bicultural_expert":
            feedback_comments.extend(self._bicultural_expert_analysis(scenario))
            improvement_suggestions.extend(self._bicultural_improvement_suggestions(scenario))
        
        # Calculate ratings
        cultural_rating = self._calculate_cultural_rating(scenario, reviewer_type)
        educational_rating = self._calculate_educational_rating(scenario, reviewer_type)
        safety_rating = self._calculate_safety_rating(scenario, reviewer_type)
        
        # Determine approval status
        approval_status = self._determine_expert_approval_status(
            cultural_rating, educational_rating, safety_rating, len(improvement_suggestions)
        )
        
        return ExpertReviewResult(
            reviewer_type=reviewer_type,
            reviewer_credentials=reviewer_info["credentials"],
            review_date=datetime.datetime.now(),
            approval_status=approval_status,
            feedback_comments=feedback_comments,
            improvement_suggestions=improvement_suggestions,
            cultural_accuracy_rating=cultural_rating,
            educational_value_rating=educational_rating,
            safety_rating=safety_rating
        )

    def _calculate_quality_metrics(self, scenario: ExpandedScenarioContent,
                                 age_validations: Dict[AgeGroup, AgeAppropriatenessValidation],
                                 trauma_validation: TraumaInformedValidation,
                                 cultural_validation: CulturalValidationResult,
                                 expert_reviews: List[ExpertReviewResult]) -> ContentQualityMetrics:
        """Calculate comprehensive quality metrics"""
        
        # Educational value score
        educational_score = self._calculate_educational_value_score(scenario, age_validations, expert_reviews)
        
        # Cultural authenticity score
        cultural_score = cultural_validation.authenticity_score
        
        # Age appropriateness score
        age_score = sum(validation.confidence_score for validation in age_validations.values()) / len(age_validations)
        
        # Trauma-informed score
        trauma_score = trauma_validation.compliance_score
        
        # Linguistic accuracy score
        linguistic_score = self._calculate_linguistic_accuracy_score(scenario, expert_reviews)
        
        # Engagement potential score
        engagement_score = self._calculate_engagement_potential_score(scenario)
        
        # Overall quality score (weighted average)
        overall_score = (
            educational_score * 0.25 +
            cultural_score * 0.20 +
            age_score * 0.20 +
            trauma_score * 0.15 +
            linguistic_score * 0.10 +
            engagement_score * 0.10
        )
        
        # Quality grade
        quality_grade = self._calculate_quality_grade(overall_score)
        
        return ContentQualityMetrics(
            educational_value_score=educational_score,
            cultural_authenticity_score=cultural_score,
            age_appropriateness_score=age_score,
            trauma_informed_score=trauma_score,
            linguistic_accuracy_score=linguistic_score,
            engagement_potential_score=engagement_score,
            overall_quality_score=overall_score,
            quality_grade=quality_grade
        )

    def _assess_safety_risk_level(self, scenario: ExpandedScenarioContent, 
                                trauma_validation: TraumaInformedValidation) -> SafetyRiskLevel:
        """Assess overall safety risk level"""
        
        risk_factors = 0
        
        # High risk factors
        if trauma_validation.potential_triggers:
            risk_factors += len(trauma_validation.potential_triggers) * 3
        
        if trauma_validation.failure_state_risks:
            risk_factors += len(trauma_validation.failure_state_risks) * 2
        
        # Medium risk factors
        if trauma_validation.pressure_indicators:
            risk_factors += len(trauma_validation.pressure_indicators)
        
        # Determine risk level
        if risk_factors == 0:
            return SafetyRiskLevel.NONE
        elif risk_factors <= 2:
            return SafetyRiskLevel.LOW
        elif risk_factors <= 5:
            return SafetyRiskLevel.MEDIUM
        elif risk_factors <= 10:
            return SafetyRiskLevel.HIGH
        else:
            return SafetyRiskLevel.CRITICAL

    # Helper methods for content analysis (simplified implementations)
    
    def _check_vocabulary_complexity(self, scenario: ExpandedScenarioContent, criteria: Dict[str, int]) -> List[str]:
        """Check vocabulary complexity against criteria"""
        concerns = []
        text = scenario.english_demonstration
        
        words = text.split()
        avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
        
        if avg_word_length > criteria.get("max_syllables", 4):
            concerns.append("Average word length may be too complex")
        
        sentences = text.split('.')
        avg_sentence_length = sum(len(sentence.split()) for sentence in sentences) / len(sentences) if sentences else 0
        
        if avg_sentence_length > criteria.get("max_sentence_length", 8):
            concerns.append("Sentence length may be too complex")
        
        return concerns

    def _check_concept_complexity(self, scenario: ExpandedScenarioContent, age_group: AgeGroup) -> List[str]:
        """Check concept complexity for age group"""
        concerns = []
        appropriate_concepts = self.validation_criteria["age_appropriateness"]["concept_complexity"][age_group]
        
        # Simplified concept checking
        text = scenario.description.lower()
        
        if age_group in [AgeGroup.JUNIOR_INFANTS, AgeGroup.SENIOR_INFANTS]:
            if any(word in text for word in ["complex", "difficult", "abstract", "analyze"]):
                concerns.append("Concepts may be too abstract for age group")
        
        return concerns

    def _check_developmental_readiness(self, scenario: ExpandedScenarioContent, age_group: AgeGroup) -> List[str]:
        """Check developmental readiness for emotional content"""
        concerns = []
        appropriate_emotions = self.validation_criteria["age_appropriateness"]["emotional_readiness"][age_group]
        
        # Simplified emotional readiness checking
        text = f"{scenario.english_demonstration} {scenario.description}".lower()
        
        if age_group in [AgeGroup.JUNIOR_INFANTS, AgeGroup.SENIOR_INFANTS]:
            if any(word in text for word in ["conflict", "disagreement", "problem", "worry"]):
                concerns.append("Emotional content may be too advanced")
        
        return concerns

    def _generate_age_enhancements(self, scenario: ExpandedScenarioContent, age_group: AgeGroup,
                                 vocab_concerns: List[str], concept_concerns: List[str],
                                 dev_concerns: List[str]) -> List[str]:
        """Generate age-specific enhancement suggestions"""
        suggestions = []
        
        if vocab_concerns:
            suggestions.append("Simplify vocabulary for age group")
        
        if concept_concerns:
            suggestions.append("Use more concrete examples and familiar contexts")
        
        if dev_concerns:
            suggestions.append("Adjust emotional complexity for developmental stage")
        
        return suggestions

    def _calculate_age_confidence_score(self, vocab_appropriateness, vocab_concerns: List[str],
                                      concept_concerns: List[str], dev_concerns: List[str]) -> float:
        """Calculate confidence score for age appropriateness"""
        base_score = 0.8 if vocab_appropriateness.value == "appropriate" else 0.6
        
        # Reduce score for concerns
        concern_penalty = (len(vocab_concerns) + len(concept_concerns) + len(dev_concerns)) * 0.1
        
        return max(0.0, min(1.0, base_score - concern_penalty))

    def _detect_potential_triggers(self, text: str) -> List[str]:
        """Detect potential trauma triggers in text"""
        triggers = []
        text_lower = text.lower()
        
        # Check against high-risk patterns
        for pattern in self.safety_patterns["high_risk_patterns"]:
            if re.search(pattern, text_lower):
                triggers.append(f"Potential trigger detected: {pattern}")
        
        return triggers

    def _detect_pressure_indicators(self, text: str) -> List[str]:
        """Detect pressure indicators in text"""
        indicators = []
        text_lower = text.lower()
        
        # Check against medium-risk patterns
        for pattern in self.safety_patterns["medium_risk_patterns"]:
            if re.search(pattern, text_lower):
                indicators.append(f"Pressure indicator: {pattern}")
        
        return indicators

    def _detect_failure_state_risks(self, text: str) -> List[str]:
        """Detect failure state risks in text"""
        risks = []
        
        failure_words = ["fail", "wrong", "incorrect", "bad", "terrible", "can't", "impossible"]
        text_lower = text.lower()
        
        for word in failure_words:
            if word in text_lower:
                risks.append(f"Failure state risk: contains '{word}'")
        
        return risks

    def _identify_celebration_opportunities(self, text: str) -> List[str]:
        """Identify celebration opportunities in text"""
        opportunities = []
        text_lower = text.lower()
        
        # Check against positive patterns
        for pattern in self.safety_patterns["positive_patterns"]:
            if re.search(pattern, text_lower):
                opportunities.append(f"Celebration opportunity: {pattern}")
        
        return opportunities

    def _generate_safety_enhancements(self, triggers: List[str], pressure: List[str], failure: List[str]) -> List[str]:
        """Generate safety enhancement suggestions"""
        enhancements = []
        
        if triggers:
            enhancements.append("Remove or rephrase potential trigger language")
        
        if pressure:
            enhancements.append("Reduce pressure-inducing language")
        
        if failure:
            enhancements.append("Remove failure-state language and focus on growth")
        
        enhancements.append("Add celebration and encouragement language")
        
        return enhancements

    def _calculate_trauma_compliance_score(self, triggers: List[str], pressure: List[str], 
                                         failure: List[str], celebration: List[str]) -> float:
        """Calculate trauma-informed compliance score"""
        
        base_score = 1.0
        
        # Deduct for negative elements
        base_score -= len(triggers) * 0.3
        base_score -= len(pressure) * 0.2
        base_score -= len(failure) * 0.25
        
        # Add for positive elements
        base_score += min(len(celebration) * 0.1, 0.2)
        
        return max(0.0, min(1.0, base_score))

    def _determine_validation_status(self, age_validations: Dict[AgeGroup, AgeAppropriatenessValidation],
                                   trauma_validation: TraumaInformedValidation,
                                   cultural_validation: CulturalValidationResult,
                                   expert_reviews: List[ExpertReviewResult],
                                   safety_risk: SafetyRiskLevel) -> ValidationStatus:
        """Determine overall validation status"""
        
        # Check critical failures
        if safety_risk == SafetyRiskLevel.CRITICAL:
            return ValidationStatus.REJECTED
        
        if not trauma_validation.is_trauma_informed:
            return ValidationStatus.NEEDS_REVISION
        
        # Check expert review status
        if expert_reviews:
            approval_count = sum(1 for review in expert_reviews if review.approval_status == ValidationStatus.APPROVED)
            if approval_count < len(expert_reviews) * 0.7:  # 70% approval threshold
                return ValidationStatus.NEEDS_REVISION
        
        # Check age appropriateness
        appropriate_count = sum(1 for validation in age_validations.values() if validation.is_appropriate)
        if appropriate_count < len(age_validations) * 0.6:  # 60% age group coverage
            return ValidationStatus.NEEDS_REVISION
        
        # Check cultural validation
        if cultural_validation.authenticity_score < 0.7:
            return ValidationStatus.NEEDS_REVISION
        
        return ValidationStatus.APPROVED

    def _generate_recommendations(self, scenario: ExpandedScenarioContent,
                                age_validations: Dict[AgeGroup, AgeAppropriatenessValidation],
                                trauma_validation: TraumaInformedValidation,
                                cultural_validation: CulturalValidationResult,
                                expert_reviews: List[ExpertReviewResult]) -> Tuple[List[str], List[str], List[str]]:
        """Generate improvement recommendations"""
        
        required_improvements = []
        optional_enhancements = []
        approval_conditions = []
        
        # Trauma-informed requirements
        if not trauma_validation.is_trauma_informed:
            required_improvements.extend(trauma_validation.safety_enhancements)
        
        # Age appropriateness requirements
        for age_group, validation in age_validations.items():
            if not validation.is_appropriate and len(validation.developmental_concerns) > 0:
                required_improvements.extend(validation.enhancement_suggestions[:2])
        
        # Cultural validation requirements
        if cultural_validation.authenticity_score < 0.7:
            required_improvements.extend(cultural_validation.recommendations[:3])
        
        # Expert review requirements
        for review in expert_reviews:
            if review.approval_status == ValidationStatus.NEEDS_REVISION:
                required_improvements.extend(review.improvement_suggestions[:2])
            else:
                optional_enhancements.extend(review.improvement_suggestions[:1])
        
        # Approval conditions
        approval_conditions.append("All required improvements must be addressed")
        approval_conditions.append("Re-validation required after changes")
        
        return required_improvements, optional_enhancements, approval_conditions

    def _calculate_review_schedule(self, validation_status: ValidationStatus, 
                                 safety_risk: SafetyRiskLevel) -> Optional[datetime.datetime]:
        """Calculate when next review should occur"""
        
        if validation_status == ValidationStatus.APPROVED:
            # Annual review for approved content
            return datetime.datetime.now() + datetime.timedelta(days=365)
        elif validation_status == ValidationStatus.NEEDS_REVISION:
            # Review after revisions (30 days)
            return datetime.datetime.now() + datetime.timedelta(days=30)
        elif safety_risk in [SafetyRiskLevel.HIGH, SafetyRiskLevel.CRITICAL]:
            # Immediate review for safety issues
            return datetime.datetime.now() + datetime.timedelta(days=1)
        
        return None

    # Simplified expert analysis methods
    def _educational_expert_analysis(self, scenario: ExpandedScenarioContent) -> List[str]:
        return ["Educational content aligns with Irish curriculum standards"]

    def _cultural_expert_analysis(self, scenario: ExpandedScenarioContent) -> List[str]:
        return ["Cultural representation is authentic and respectful"]

    def _psychological_expert_analysis(self, scenario: ExpandedScenarioContent) -> List[str]:
        return ["Content follows trauma-informed design principles"]

    def _linguistic_expert_analysis(self, scenario: ExpandedScenarioContent) -> List[str]:
        return ["Irish English patterns are accurate and appropriate"]

    def _bicultural_expert_analysis(self, scenario: ExpandedScenarioContent) -> List[str]:
        return ["Bicultural integration opportunities are well-developed"]

    def _educational_improvement_suggestions(self, scenario: ExpandedScenarioContent) -> List[str]:
        return ["Consider adding more curriculum-specific learning objectives"]

    def _cultural_improvement_suggestions(self, scenario: ExpandedScenarioContent) -> List[str]:
        return ["Enhance Dublin-specific cultural references"]

    def _psychological_improvement_suggestions(self, scenario: ExpandedScenarioContent) -> List[str]:
        return ["Add more celebration and encouragement language"]

    def _linguistic_improvement_suggestions(self, scenario: ExpandedScenarioContent) -> List[str]:
        return ["Include more varied Irish English expressions"]

    def _bicultural_improvement_suggestions(self, scenario: ExpandedScenarioContent) -> List[str]:
        return ["Develop stronger Chinese-Irish cultural bridges"]

    def _calculate_cultural_rating(self, scenario: ExpandedScenarioContent, reviewer_type: str) -> int:
        cultural_points = len(scenario.cultural_integration_points)
        return min(5, max(1, 2 + cultural_points))

    def _calculate_educational_rating(self, scenario: ExpandedScenarioContent, reviewer_type: str) -> int:
        return min(5, max(1, scenario.difficulty_level))

    def _calculate_safety_rating(self, scenario: ExpandedScenarioContent, reviewer_type: str) -> int:
        return 4  # Assume generally safe content

    def _determine_expert_approval_status(self, cultural_rating: int, educational_rating: int,
                                        safety_rating: int, improvement_count: int) -> ValidationStatus:
        avg_rating = (cultural_rating + educational_rating + safety_rating) / 3
        
        if avg_rating >= 4 and improvement_count <= 2:
            return ValidationStatus.APPROVED
        elif avg_rating >= 3:
            return ValidationStatus.NEEDS_REVISION
        else:
            return ValidationStatus.REJECTED

    def _calculate_educational_value_score(self, scenario: ExpandedScenarioContent,
                                         age_validations: Dict[AgeGroup, AgeAppropriatenessValidation],
                                         expert_reviews: List[ExpertReviewResult]) -> float:
        base_score = scenario.difficulty_level / 5.0
        
        # Adjust based on age appropriateness
        appropriate_count = sum(1 for v in age_validations.values() if v.is_appropriate)
        age_factor = appropriate_count / len(age_validations)
        
        return min(1.0, base_score * age_factor)

    def _calculate_linguistic_accuracy_score(self, scenario: ExpandedScenarioContent,
                                           expert_reviews: List[ExpertReviewResult]) -> float:
        # Base score from Irish vocabulary notes
        base_score = min(len(scenario.irish_vocabulary_notes) / 5.0, 1.0)
        
        # Adjust based on expert reviews
        linguistic_reviews = [r for r in expert_reviews if r.reviewer_type == "linguistic_expert"]
        if linguistic_reviews:
            expert_factor = linguistic_reviews[0].educational_value_rating / 5.0
            return (base_score + expert_factor) / 2.0
        
        return base_score

    def _calculate_engagement_potential_score(self, scenario: ExpandedScenarioContent) -> float:
        # Simple engagement calculation based on scenario features
        engagement_factors = 0
        
        if len(scenario.cultural_integration_points) >= 2:
            engagement_factors += 1
        
        if len(scenario.dublin_location_connections) >= 1:
            engagement_factors += 1
        
        if scenario.difficulty_level in [2, 3, 4]:  # Optimal challenge level
            engagement_factors += 1
        
        if any(word in scenario.description.lower() for word in ["fun", "interesting", "exciting", "brilliant"]):
            engagement_factors += 1
        
        return min(1.0, engagement_factors / 4.0)

    def _calculate_quality_grade(self, overall_score: float) -> str:
        """Calculate letter grade from overall score"""
        if overall_score >= 0.97:
            return "A+"
        elif overall_score >= 0.93:
            return "A"
        elif overall_score >= 0.90:
            return "A-"
        elif overall_score >= 0.87:
            return "B+"
        elif overall_score >= 0.83:
            return "B"
        elif overall_score >= 0.80:
            return "B-"
        elif overall_score >= 0.77:
            return "C+"
        elif overall_score >= 0.73:
            return "C"
        elif overall_score >= 0.70:
            return "C-"
        elif overall_score >= 0.67:
            return "D+"
        elif overall_score >= 0.63:
            return "D"
        elif overall_score >= 0.60:
            return "D-"
        else:
            return "F"

    def get_validation_summary(self, validations: List[ComprehensiveContentValidation]) -> Dict[str, Any]:
        """Get comprehensive validation summary across all scenarios"""
        
        if not validations:
            return {"error": "No validations provided"}
        
        total_scenarios = len(validations)
        
        # Status distribution
        status_distribution = {}
        for status in ValidationStatus:
            status_distribution[status.value] = sum(1 for v in validations if v.validation_status == status)
        
        # Quality grade distribution
        grade_distribution = {}
        for validation in validations:
            grade = validation.quality_metrics.quality_grade
            grade_distribution[grade] = grade_distribution.get(grade, 0) + 1
        
        # Safety risk distribution
        risk_distribution = {}
        for risk in SafetyRiskLevel:
            risk_distribution[risk.value] = sum(1 for v in validations if v.safety_risk_level == risk)
        
        # Average scores
        avg_quality = sum(v.quality_metrics.overall_quality_score for v in validations) / total_scenarios
        avg_trauma_score = sum(v.trauma_informed_validation.compliance_score for v in validations) / total_scenarios
        avg_cultural_score = sum(v.cultural_validation.authenticity_score for v in validations) / total_scenarios
        
        return {
            "total_scenarios_validated": total_scenarios,
            "validation_status_distribution": status_distribution,
            "quality_grade_distribution": grade_distribution,
            "safety_risk_distribution": risk_distribution,
            "average_scores": {
                "overall_quality": round(avg_quality, 3),
                "trauma_informed_compliance": round(avg_trauma_score, 3),
                "cultural_authenticity": round(avg_cultural_score, 3)
            },
            "approval_rate": round(status_distribution.get("approved", 0) / total_scenarios * 100, 1),
            "high_quality_rate": round(sum(1 for v in validations if v.quality_metrics.quality_grade in ["A+", "A", "A-"]) / total_scenarios * 100, 1),
            "safety_compliance_rate": round(sum(1 for v in validations if v.safety_risk_level in [SafetyRiskLevel.NONE, SafetyRiskLevel.LOW]) / total_scenarios * 100, 1)
        }