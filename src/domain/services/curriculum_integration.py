"""
Curriculum Integration Domain Service

Extracted from the monolithic educational_context_processor.py.
This service handles Irish curriculum integration and age-appropriate content analysis.

Implements ICurriculumIntegrationService interface for dependency injection.
"""

from typing import Dict, List, Any, Optional
from src.application.interfaces.services import ICurriculumIntegrationService

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

class VocabularyComplexity(Enum):
    """Vocabulary complexity levels for age-appropriate content"""
    VERY_SIMPLE = "very_simple"        # Ages 4-5: Single syllables, basic nouns
    SIMPLE = "simple"                  # Ages 5-7: Common words, simple sentences
    MODERATE = "moderate"              # Ages 7-8: More varied vocabulary
    COMPLEX = "complex"                # Ages 9-10: Advanced vocabulary, longer sentences

class IrishCurriculumStage(Enum):
    """Irish Primary School curriculum stages for educational alignment"""
    JUNIOR_INFANTS_STAGE = "junior_infants_stage"      # Ages 4-5: Foundation stage
    SENIOR_INFANTS_STAGE = "senior_infants_stage"      # Ages 5-6: Early learning stage  
    FIRST_CLASS_STAGE = "first_class_stage"            # Ages 6-7: Beginning formal learning
    SECOND_CLASS_STAGE = "second_class_stage"          # Ages 7-8: Developing skills stage
    THIRD_CLASS_STAGE = "third_class_stage"            # Ages 8-9: Intermediate skills stage
    FOURTH_CLASS_STAGE = "fourth_class_stage"          # Ages 9-10: Advanced primary stage

class CurriculumArea(Enum):
    """Irish Primary School curriculum areas"""
    ENGLISH = "english"                          # English language development
    MATHEMATICS = "mathematics"                  # Numeracy and problem solving
    SCIENCE = "science"                         # Science and technology
    HISTORY = "history"                         # History and heritage
    GEOGRAPHY = "geography"                     # Geography and environment
    SPHE = "sphe"                              # Social, Personal & Health Education
    ARTS = "arts"                              # Visual arts, music, drama
    PHYSICAL_EDUCATION = "physical_education"   # Physical education and wellbeing

class DevelopmentalMilestone(Enum):
    """Key developmental milestones for Irish primary education"""
    FOUNDATION_LITERACY = "foundation_literacy"         # Basic reading/writing readiness
    EMERGING_READER = "emerging_reader"                 # Beginning reading skills
    DEVELOPING_READER = "developing_reader"             # Growing reading fluency
    INDEPENDENT_READER = "independent_reader"           # Self-sufficient reading
    ADVANCED_READER = "advanced_reader"                 # Complex text comprehension
    CRITICAL_THINKER = "critical_thinker"              # Analysis and evaluation skills

class DevelopmentalAppropriateness(Enum):
    """Assessment of developmental appropriateness for content"""
    TOO_SIMPLE = "too_simple"          # Below child's developmental level
    APPROPRIATE = "appropriate"        # Perfect for child's developmental level
    CHALLENGING = "challenging"        # Slightly above but manageable
    TOO_COMPLEX = "too_complex"        # Above child's developmental level


class CurriculumIntegrationService(ICurriculumIntegrationService):
    """
    Curriculum integration service for Irish Primary School alignment.
    
    Combines functionality from AgeAppropriateContentAnalyzer and IrishCurriculumIntegrationManager
    classes from the monolithic processor. Now implements interface contract for dependency injection.
    """
    
    def __init__(self):
        """Initialize curriculum integration data and mappings."""
        # Age-appropriate vocabulary sets (basic implementation)
        self.vocabulary_by_complexity = {
            VocabularyComplexity.VERY_SIMPLE: {
                # Ages 4-5: Basic nouns, simple actions, common words
                'hello', 'hi', 'bye', 'yes', 'no', 'please', 'thank', 'good', 'bad',
                'big', 'small', 'red', 'blue', 'cat', 'dog', 'mom', 'dad', 'home',
                'eat', 'play', 'run', 'sit', 'go', 'come', 'look', 'see', 'happy',
                'sad', 'one', 'two', 'me', 'you', 'up', 'down', 'hot', 'cold'
            },
            VocabularyComplexity.SIMPLE: {
                # Ages 5-7: Common words, simple sentences
                'school', 'teacher', 'friend', 'book', 'color', 'number', 'story',
                'picture', 'family', 'house', 'animal', 'water', 'food', 'learn',
                'help', 'like', 'want', 'need', 'think', 'know', 'read', 'write',
                'draw', 'sing', 'dance', 'walk', 'talk', 'listen', 'watch', 'find',
                'this', 'that', 'nice', 'fun', 'learning', 'is', 'to', 'me', 'my',
                'answer', 'the', 'a', 'an'
            },
            VocabularyComplexity.MODERATE: {
                # Ages 7-8: More varied vocabulary
                'understand', 'remember', 'important', 'different', 'together',
                'language', 'question', 'explain', 'describe', 'compare',
                'because', 'although', 'however', 'wonderful', 'interesting',
                'difficult', 'easy', 'problem', 'solution', 'create', 'imagine'
            },
            VocabularyComplexity.COMPLEX: {
                # Ages 9-10: Advanced vocabulary
                'communicate', 'conversation', 'pronunciation', 'vocabulary',
                'appreciate', 'comprehend', 'demonstrate', 'participate',
                'investigate', 'experience', 'opportunity', 'responsibility',
                'independent', 'confident', 'enthusiastic', 'comfortable',
                'comprehensively'
            }
        }
        
        # Age group to complexity mapping
        self.age_group_complexity = {
            AgeGroup.JUNIOR_INFANTS: VocabularyComplexity.VERY_SIMPLE,
            AgeGroup.SENIOR_INFANTS: VocabularyComplexity.SIMPLE,
            AgeGroup.FIRST_CLASS: VocabularyComplexity.SIMPLE,
            AgeGroup.SECOND_CLASS: VocabularyComplexity.MODERATE,
            AgeGroup.THIRD_CLASS: VocabularyComplexity.MODERATE,
            AgeGroup.FOURTH_CLASS: VocabularyComplexity.COMPLEX,
        }
        
        # Irish curriculum stage mapping for age groups
        self.age_to_curriculum_stage = {
            AgeGroup.JUNIOR_INFANTS: IrishCurriculumStage.JUNIOR_INFANTS_STAGE,
            AgeGroup.SENIOR_INFANTS: IrishCurriculumStage.SENIOR_INFANTS_STAGE,
            AgeGroup.FIRST_CLASS: IrishCurriculumStage.FIRST_CLASS_STAGE,
            AgeGroup.SECOND_CLASS: IrishCurriculumStage.SECOND_CLASS_STAGE,
            AgeGroup.THIRD_CLASS: IrishCurriculumStage.THIRD_CLASS_STAGE,
            AgeGroup.FOURTH_CLASS: IrishCurriculumStage.FOURTH_CLASS_STAGE
        }
        
        # Developmental milestone mapping for curriculum stages
        self.stage_to_milestone = {
            IrishCurriculumStage.JUNIOR_INFANTS_STAGE: DevelopmentalMilestone.FOUNDATION_LITERACY,
            IrishCurriculumStage.SENIOR_INFANTS_STAGE: DevelopmentalMilestone.EMERGING_READER,
            IrishCurriculumStage.FIRST_CLASS_STAGE: DevelopmentalMilestone.DEVELOPING_READER,
            IrishCurriculumStage.SECOND_CLASS_STAGE: DevelopmentalMilestone.INDEPENDENT_READER,
            IrishCurriculumStage.THIRD_CLASS_STAGE: DevelopmentalMilestone.ADVANCED_READER,
            IrishCurriculumStage.FOURTH_CLASS_STAGE: DevelopmentalMilestone.CRITICAL_THINKER
        }
        
        # Curriculum area keywords for content classification
        self.curriculum_area_keywords = {
            CurriculumArea.ENGLISH: {
                'read', 'write', 'story', 'book', 'letter', 'word', 'sentence', 'poem', 'rhyme',
                'speak', 'listen', 'talk', 'say', 'tell', 'language', 'alphabet', 'spelling',
                'grammar', 'reading', 'writing', 'communication', 'vocabulary', 'literature'
            },
            CurriculumArea.MATHEMATICS: {
                'number', 'count', 'add', 'subtract', 'multiply', 'divide', 'math', 'maths',
                'calculate', 'solve', 'problem', 'shape', 'pattern', 'measure', 'size',
                'length', 'weight', 'time', 'money', 'graph', 'data', 'fraction', 'decimal'
            },
            CurriculumArea.SCIENCE: {
                'science', 'experiment', 'observe', 'discover', 'nature', 'animal', 'plant',
                'earth', 'space', 'weather', 'light', 'sound', 'water', 'air', 'energy',
                'material', 'living', 'environment', 'investigate', 'explore', 'hypothesis'
            },
            CurriculumArea.HISTORY: {
                'history', 'past', 'ago', 'old', 'ancient', 'before', 'timeline', 'story',
                'people', 'family', 'tradition', 'culture', 'heritage', 'ancestor',
                'events', 'change', 'time', 'ireland', 'irish', 'dublin', 'castle'
            },
            CurriculumArea.GEOGRAPHY: {
                'place', 'location', 'map', 'country', 'city', 'town', 'village', 'home',
                'travel', 'direction', 'geography', 'world', 'earth', 'land', 'sea',
                'mountain', 'river', 'forest', 'farm', 'ireland', 'dublin', 'environment'
            },
            CurriculumArea.SPHE: {
                'feel', 'emotion', 'happy', 'sad', 'friend', 'friendship', 'kind', 'help',
                'share', 'care', 'family', 'safe', 'healthy', 'exercise', 'food',
                'myself', 'others', 'community', 'respect', 'responsibility', 'decision'
            },
            CurriculumArea.ARTS: {
                'draw', 'paint', 'color', 'picture', 'art', 'create', 'make', 'music',
                'sing', 'dance', 'drama', 'play', 'creative', 'imagination', 'beautiful',
                'express', 'design', 'craft', 'instrument', 'song', 'performance'
            },
            CurriculumArea.PHYSICAL_EDUCATION: {
                'run', 'jump', 'play', 'game', 'sport', 'exercise', 'move', 'body',
                'healthy', 'strong', 'fit', 'team', 'ball', 'active', 'physical',
                'outdoor', 'balance', 'coordination', 'skills', 'competition', 'fun'
            }
        }
        
        # Curriculum-aligned learning objectives by stage
        self.stage_learning_objectives = {
            IrishCurriculumStage.JUNIOR_INFANTS_STAGE: {
                'oral_language': 'Develop basic speaking and listening skills',
                'early_literacy': 'Recognize letters and simple words',
                'social_skills': 'Learn to interact with peers and adults',
                'self_care': 'Develop independence in basic tasks'
            },
            IrishCurriculumStage.SENIOR_INFANTS_STAGE: {
                'reading_readiness': 'Begin to read simple texts',
                'writing_readiness': 'Form letters and write simple words',
                'numeracy': 'Understand basic number concepts',
                'confidence': 'Build confidence in learning'
            },
            IrishCurriculumStage.FIRST_CLASS_STAGE: {
                'reading_fluency': 'Read simple texts with understanding',
                'writing_skills': 'Write simple sentences clearly',
                'problem_solving': 'Solve basic mathematical problems',
                'curiosity': 'Develop curiosity about the world'
            },
            IrishCurriculumStage.SECOND_CLASS_STAGE: {
                'comprehension': 'Understand and discuss texts',
                'expression': 'Express ideas clearly in writing',
                'reasoning': 'Use logical thinking in problem solving',
                'collaboration': 'Work effectively with others'
            },
            IrishCurriculumStage.THIRD_CLASS_STAGE: {
                'analysis': 'Analyze and interpret information',
                'creativity': 'Express ideas creatively',
                'independence': 'Work independently on tasks',
                'research': 'Find and use information effectively'
            },
            IrishCurriculumStage.FOURTH_CLASS_STAGE: {
                'critical_thinking': 'Think critically about information',
                'synthesis': 'Combine ideas from different sources',
                'leadership': 'Show leadership in group activities',
                'preparation': 'Prepare for transition to post-primary'
            }
        }
    
    def get_age_appropriate_vocabulary(
        self, 
        age_group: str, 
        scenario_type: str
    ) -> List[str]:
        """
        Get vocabulary appropriate for age group and scenario.
        
        Args:
            age_group: Target age group (string representation)
            scenario_type: Type of learning scenario
            
        Returns:
            List of appropriate vocabulary words
        """
        # Convert string age group to enum
        try:
            age_enum = AgeGroup(age_group.lower())
        except ValueError:
            age_enum = AgeGroup.FIRST_CLASS  # Default fallback
        
        # Get appropriate complexity level
        complexity = self.age_group_complexity.get(age_enum, VocabularyComplexity.SIMPLE)
        vocabulary_set = self.vocabulary_by_complexity.get(complexity, set())
        
        # Filter by scenario type if specific vocabulary needed
        if scenario_type.lower() in ['greeting', 'introduction']:
            # Basic greeting vocabulary
            filtered_vocab = {word for word in vocabulary_set 
                            if word in ['hello', 'hi', 'bye', 'good', 'nice', 'please', 'thank']}
        elif scenario_type.lower() in ['learning', 'educational']:
            # Learning-focused vocabulary
            filtered_vocab = {word for word in vocabulary_set 
                            if word in ['learn', 'read', 'write', 'book', 'story', 'question', 'answer']}
        else:
            # Return all vocabulary for general scenarios
            filtered_vocab = vocabulary_set
        
        return list(filtered_vocab)
    
    def validate_curriculum_alignment(
        self, 
        content: str, 
        curriculum_stage: str
    ) -> Dict[str, Any]:
        """
        Validate content alignment with Irish curriculum standards.
        
        Args:
            content: Content to validate
            curriculum_stage: Target curriculum stage
            
        Returns:
            Dictionary with alignment validation results
        """
        # Convert string to enum
        try:
            stage_enum = IrishCurriculumStage(curriculum_stage.lower())
        except ValueError:
            stage_enum = IrishCurriculumStage.FIRST_CLASS_STAGE  # Default fallback
        
        return self.assess_curriculum_alignment(content, stage_enum)
    
    def suggest_educational_enhancements(
        self, 
        base_content: str,
        learning_objectives: List[str]
    ) -> Dict[str, str]:
        """
        Suggest educational enhancements aligned with curriculum.
        
        Args:
            base_content: Base content to enhance
            learning_objectives: Target learning objectives
            
        Returns:
            Dictionary with enhancement suggestions
        """
        # Analyze content complexity
        complexity = self.analyze_vocabulary_complexity(base_content)
        curriculum_areas = self.identify_curriculum_areas(base_content)
        
        enhancements = {
            'current_complexity': complexity.value,
            'identified_areas': [area.value for area in curriculum_areas],
            'enhancement_strategy': self._determine_enhancement_strategy(complexity, curriculum_areas)
        }
        
        # Generate specific enhancement suggestions
        if complexity == VocabularyComplexity.VERY_SIMPLE:
            enhancements['vocabulary_enhancement'] = 'Add descriptive words and varied sentence starters'
            enhancements['structure_enhancement'] = 'Introduce compound sentences with "and", "but"'
        elif complexity == VocabularyComplexity.SIMPLE:
            enhancements['vocabulary_enhancement'] = 'Include more specific nouns and action words'
            enhancements['structure_enhancement'] = 'Add questions and varied sentence types'
        elif complexity == VocabularyComplexity.MODERATE:
            enhancements['vocabulary_enhancement'] = 'Introduce abstract concepts and connecting words'
            enhancements['structure_enhancement'] = 'Use complex sentences with because, although'
        else:  # COMPLEX
            enhancements['vocabulary_enhancement'] = 'Include subject-specific terminology'
            enhancements['structure_enhancement'] = 'Encourage varied and sophisticated expression'
        
        # Add curriculum area specific enhancements
        if CurriculumArea.ENGLISH in curriculum_areas:
            enhancements['literacy_focus'] = 'Emphasize reading comprehension and expression'
        if CurriculumArea.MATHEMATICS in curriculum_areas:
            enhancements['numeracy_focus'] = 'Include problem-solving and logical thinking'
        if CurriculumArea.SCIENCE in curriculum_areas:
            enhancements['inquiry_focus'] = 'Encourage observation and hypothesis formation'
        
        # Align with learning objectives
        if learning_objectives:
            objective_enhancements = []
            for objective in learning_objectives:
                if 'read' in objective.lower():
                    objective_enhancements.append('Include reading comprehension activities')
                elif 'write' in objective.lower():
                    objective_enhancements.append('Add writing practice opportunities')
                elif 'problem' in objective.lower():
                    objective_enhancements.append('Include problem-solving challenges')
                elif 'creative' in objective.lower():
                    objective_enhancements.append('Add creative expression elements')
            
            if objective_enhancements:
                enhancements['objective_alignment'] = '; '.join(objective_enhancements)
        
        return enhancements
    
    def analyze_vocabulary_complexity(self, text: str) -> VocabularyComplexity:
        """
        Analyze vocabulary complexity of input text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            VocabularyComplexity level
        """
        if not text or not text.strip():
            return VocabularyComplexity.VERY_SIMPLE
        
        words = text.lower().split()
        if not words:
            return VocabularyComplexity.VERY_SIMPLE
        
        # Count words by complexity level
        complexity_scores = {
            VocabularyComplexity.VERY_SIMPLE: 0,
            VocabularyComplexity.SIMPLE: 0,
            VocabularyComplexity.MODERATE: 0,
            VocabularyComplexity.COMPLEX: 0
        }
        
        for word in words:
            # Remove punctuation for word matching
            clean_word = ''.join(c for c in word if c.isalpha())
            if not clean_word:
                continue
                
            # Check which complexity level this word belongs to
            found = False
            for complexity, vocab_set in self.vocabulary_by_complexity.items():
                if clean_word in vocab_set:
                    complexity_scores[complexity] += 1
                    found = True
                    break
            
            # If word not found in any set, assume it's moderate complexity
            if not found:
                complexity_scores[VocabularyComplexity.MODERATE] += 1
        
        # Improved logic: prioritize higher complexity if present
        total_words = sum(complexity_scores.values())
        if total_words == 0:
            return VocabularyComplexity.VERY_SIMPLE
        
        # Calculate percentages for better decision making
        percentages = {k: (v / total_words) * 100 for k, v in complexity_scores.items()}
        
        # If 30%+ of words are complex, classify as complex
        if percentages[VocabularyComplexity.COMPLEX] >= 30:
            return VocabularyComplexity.COMPLEX
        # If 40%+ of words are moderate or complex, classify as moderate
        elif (percentages[VocabularyComplexity.MODERATE] + percentages[VocabularyComplexity.COMPLEX]) >= 40:
            return VocabularyComplexity.MODERATE
        # If 50%+ of words are simple+, classify as simple
        elif (percentages[VocabularyComplexity.SIMPLE] + percentages[VocabularyComplexity.MODERATE] + percentages[VocabularyComplexity.COMPLEX]) >= 50:
            return VocabularyComplexity.SIMPLE
        else:
            return VocabularyComplexity.VERY_SIMPLE
    
    def assess_developmental_appropriateness(self, text: str, age_group: AgeGroup) -> DevelopmentalAppropriateness:
        """
        Assess if content is developmentally appropriate for given age group.
        
        Args:
            text: Input text to assess
            age_group: Target age group
            
        Returns:
            DevelopmentalAppropriateness assessment
        """
        if not age_group:
            return DevelopmentalAppropriateness.APPROPRIATE
        
        text_complexity = self.analyze_vocabulary_complexity(text)
        target_complexity = self.age_group_complexity.get(age_group, VocabularyComplexity.SIMPLE)
        
        # Define complexity ordering for comparison
        complexity_order = [
            VocabularyComplexity.VERY_SIMPLE,
            VocabularyComplexity.SIMPLE,
            VocabularyComplexity.MODERATE,
            VocabularyComplexity.COMPLEX
        ]
        
        text_level = complexity_order.index(text_complexity)
        target_level = complexity_order.index(target_complexity)
        
        # Assess appropriateness based on level difference
        if text_level < target_level - 1:
            return DevelopmentalAppropriateness.TOO_SIMPLE
        elif text_level == target_level - 1 or text_level == target_level:
            return DevelopmentalAppropriateness.APPROPRIATE
        elif text_level == target_level + 1:
            return DevelopmentalAppropriateness.CHALLENGING
        else:
            return DevelopmentalAppropriateness.TOO_COMPLEX
    
    def map_age_group_to_curriculum_stage(self, age_group: AgeGroup) -> IrishCurriculumStage:
        """Map age group to Irish curriculum stage."""
        return self.age_to_curriculum_stage.get(age_group, IrishCurriculumStage.FIRST_CLASS_STAGE)
    
    def get_developmental_milestone(self, curriculum_stage: IrishCurriculumStage) -> DevelopmentalMilestone:
        """Get appropriate developmental milestone for curriculum stage."""
        return self.stage_to_milestone.get(curriculum_stage, DevelopmentalMilestone.DEVELOPING_READER)
    
    def identify_curriculum_areas(self, text: str) -> List[CurriculumArea]:
        """Identify relevant curriculum areas from text content."""
        text_lower = text.lower()
        identified_areas = []
        
        for area, keywords in self.curriculum_area_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                identified_areas.append(area)
        
        # Default to English if no specific area identified (language learning context)
        if not identified_areas:
            identified_areas.append(CurriculumArea.ENGLISH)
        
        return identified_areas
    
    def assess_curriculum_alignment(self, text: str, curriculum_stage: IrishCurriculumStage) -> Dict[str, Any]:
        """Assess how well content aligns with curriculum stage requirements."""
        learning_objectives = self.stage_learning_objectives.get(curriculum_stage, {})
        curriculum_areas = self.identify_curriculum_areas(text)
        
        # Assess alignment with learning objectives
        alignment_score = 0.0
        aligned_objectives = []
        
        text_lower = text.lower()
        for objective, description in learning_objectives.items():
            objective_keywords = description.lower().split()
            if any(keyword in text_lower for keyword in objective_keywords if len(keyword) > 3):
                alignment_score += 0.25
                aligned_objectives.append(objective)
        
        alignment_score = min(1.0, alignment_score)  # Cap at 1.0
        
        return {
            'alignment_score': alignment_score,
            'aligned_objectives': aligned_objectives,
            'curriculum_areas': [area.value for area in curriculum_areas],
            'stage_appropriate': alignment_score >= 0.25,
            'learning_focus': self._determine_learning_focus(curriculum_areas, curriculum_stage)
        }
    
    def _determine_learning_focus(self, curriculum_areas: List[CurriculumArea], 
                                 curriculum_stage: IrishCurriculumStage) -> str:
        """Determine primary learning focus based on curriculum areas and stage."""
        if CurriculumArea.ENGLISH in curriculum_areas:
            if curriculum_stage in [IrishCurriculumStage.JUNIOR_INFANTS_STAGE, IrishCurriculumStage.SENIOR_INFANTS_STAGE]:
                return "early_literacy_development"
            elif curriculum_stage in [IrishCurriculumStage.FIRST_CLASS_STAGE, IrishCurriculumStage.SECOND_CLASS_STAGE]:
                return "reading_writing_fluency"
            else:
                return "advanced_language_skills"
        
        elif CurriculumArea.MATHEMATICS in curriculum_areas:
            return "numeracy_and_problem_solving"
        elif CurriculumArea.SCIENCE in curriculum_areas:
            return "scientific_inquiry"
        elif CurriculumArea.SPHE in curriculum_areas:
            return "social_emotional_learning"
        else:
            return "integrated_learning"
    
    def _determine_enhancement_strategy(self, complexity: VocabularyComplexity, areas: List[CurriculumArea]) -> str:
        """Determine enhancement strategy based on complexity and curriculum areas."""
        if complexity == VocabularyComplexity.VERY_SIMPLE:
            return "gradual_vocabulary_expansion"
        elif complexity == VocabularyComplexity.SIMPLE:
            return "structured_complexity_increase"
        elif complexity == VocabularyComplexity.MODERATE:
            return "advanced_concept_integration"
        else:
            return "sophisticated_expression_refinement"
    
    def generate_age_appropriate_suggestions(self, text: str, age_group: AgeGroup) -> Dict[str, str]:
        """
        Generate suggestions for age-appropriate response structure.
        
        Args:
            text: Input text
            age_group: Target age group
            
        Returns:
            Dictionary with age-appropriate response suggestions
        """
        if not age_group:
            return {"approach": "general", "complexity": "simple"}
        
        appropriateness = self.assess_developmental_appropriateness(text, age_group)
        target_complexity = self.age_group_complexity.get(age_group, VocabularyComplexity.SIMPLE)
        
        suggestions = {
            "target_vocabulary": target_complexity.value,
            "appropriateness": appropriateness.value,
            "sentence_structure": self._get_sentence_structure_guidance(age_group),
            "encouragement_style": self._get_encouragement_style(age_group)
        }
        
        # Add specific guidance based on appropriateness
        if appropriateness == DevelopmentalAppropriateness.TOO_SIMPLE:
            suggestions["guidance"] = "Gently introduce more varied vocabulary"
        elif appropriateness == DevelopmentalAppropriateness.TOO_COMPLEX:
            suggestions["guidance"] = "Simplify language and break into smaller parts"
        elif appropriateness == DevelopmentalAppropriateness.CHALLENGING:
            suggestions["guidance"] = "Provide support while encouraging growth"
        else:
            suggestions["guidance"] = "Continue with current complexity level"
        
        return suggestions
    
    def _get_sentence_structure_guidance(self, age_group: AgeGroup) -> str:
        """Get sentence structure guidance for age group."""
        structure_map = {
            AgeGroup.JUNIOR_INFANTS: "very_short_simple",      # 2-4 words
            AgeGroup.SENIOR_INFANTS: "short_simple",           # 4-6 words
            AgeGroup.FIRST_CLASS: "simple_sentences",          # 6-8 words
            AgeGroup.SECOND_CLASS: "compound_simple",          # 8-12 words
            AgeGroup.THIRD_CLASS: "varied_sentences",          # 10-15 words
            AgeGroup.FOURTH_CLASS: "complex_sentences"         # 12+ words
        }
        return structure_map.get(age_group, "simple_sentences")
    
    def _get_encouragement_style(self, age_group: AgeGroup) -> str:
        """Get encouragement style for age group."""
        style_map = {
            AgeGroup.JUNIOR_INFANTS: "enthusiastic_simple",
            AgeGroup.SENIOR_INFANTS: "warm_encouraging",
            AgeGroup.FIRST_CLASS: "positive_growth_focused",
            AgeGroup.SECOND_CLASS: "constructive_specific",
            AgeGroup.THIRD_CLASS: "supportive_challenging",
            AgeGroup.FOURTH_CLASS: "respectful_collaborative"
        }
        return style_map.get(age_group, "positive_growth_focused")
    
    def generate_curriculum_aligned_suggestions(self, text: str, curriculum_stage: IrishCurriculumStage,
                                              age_group: AgeGroup) -> Dict[str, str]:
        """Generate curriculum-aligned educational suggestions."""
        alignment_assessment = self.assess_curriculum_alignment(text, curriculum_stage)
        learning_objectives = self.stage_learning_objectives.get(curriculum_stage, {})
        
        suggestions = {
            'curriculum_stage': curriculum_stage.value,
            'developmental_milestone': self.get_developmental_milestone(curriculum_stage).value,
            'alignment_score': f"{alignment_assessment['alignment_score']:.2f}",
            'stage_appropriate': str(alignment_assessment['stage_appropriate']),
            'learning_focus': alignment_assessment['learning_focus'],
            'curriculum_areas': ', '.join(alignment_assessment['curriculum_areas'])
        }
        
        # Stage-specific guidance
        if curriculum_stage == IrishCurriculumStage.JUNIOR_INFANTS_STAGE:
            suggestions.update({
                'approach': 'Play-based learning with lots of encouragement',
                'focus': 'Basic language and social skills development',
                'methods': 'Songs, games, visual aids, hands-on activities'
            })
        elif curriculum_stage == IrishCurriculumStage.SENIOR_INFANTS_STAGE:
            suggestions.update({
                'approach': 'Structured play with learning goals',
                'focus': 'Reading readiness and number concepts',
                'methods': 'Story time, counting games, letter recognition'
            })
        elif curriculum_stage == IrishCurriculumStage.FIRST_CLASS_STAGE:
            suggestions.update({
                'approach': 'Formal learning with support',
                'focus': 'Basic literacy and numeracy skills',
                'methods': 'Guided reading, writing practice, problem solving'
            })
        elif curriculum_stage == IrishCurriculumStage.SECOND_CLASS_STAGE:
            suggestions.update({
                'approach': 'Independent work with guidance',
                'focus': 'Comprehension and expression skills',
                'methods': 'Discussion, creative writing, collaborative projects'
            })
        elif curriculum_stage == IrishCurriculumStage.THIRD_CLASS_STAGE:
            suggestions.update({
                'approach': 'Research and analysis focus',
                'focus': 'Critical thinking and creativity',
                'methods': 'Project work, investigations, presentations'
            })
        else:  # FOURTH_CLASS_STAGE
            suggestions.update({
                'approach': 'Preparation for transition',
                'focus': 'Leadership and advanced skills',
                'methods': 'Independent research, peer teaching, synthesis tasks'
            })
        
        return suggestions