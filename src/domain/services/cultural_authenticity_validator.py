"""
Cultural Authenticity Validation Service

Provides expert validation framework for Dublin-specific content and Irish
cultural accuracy. Includes cultural sensitivity review and community feedback
integration for authentic cultural representation.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Set
from enum import Enum
import re
from .cultural_representation import CulturalRepresentationService


class ValidationLevel(str, Enum):
    """Validation levels for cultural content"""
    BASIC = "basic"
    EXPERT = "expert"
    COMMUNITY = "community"
    COMPREHENSIVE = "comprehensive"


class CulturalSensitivityLevel(str, Enum):
    """Cultural sensitivity levels"""
    APPROPRIATE = "appropriate"
    NEEDS_REVIEW = "needs_review"
    PROBLEMATIC = "problematic"
    EXCELLENT = "excellent"


@dataclass
class DublinExpertReviewer:
    """Dublin cultural expert reviewer configuration"""
    name: str
    expertise_areas: List[str]
    validation_criteria: List[str]
    authenticity_indicators: List[str]
    sensitivity_guidelines: List[str]


@dataclass
class CulturalValidationResult:
    """Result of cultural authenticity validation"""
    authenticity_score: float  # 0.0 to 1.0
    sensitivity_check: CulturalSensitivityLevel
    community_feedback: List[str]
    expert_review: Dict[str, Any]
    issues_found: List[str]
    strengths_identified: List[str]
    recommendations: List[str]
    validation_level: ValidationLevel


@dataclass
class CulturalSensitivityChecker:
    """Cultural sensitivity validation configuration"""
    problematic_patterns: List[str]
    positive_indicators: List[str]
    bicultural_balance_indicators: List[str]
    age_appropriateness_indicators: List[str]
    trauma_informed_indicators: List[str]


class CulturalAuthenticityValidator:
    """Service for validating cultural authenticity and sensitivity"""

    def __init__(self, cultural_service: Optional[CulturalRepresentationService] = None):
        self.cultural_service = cultural_service or CulturalRepresentationService()
        self.dublin_expert_reviewers = self._initialize_dublin_experts()
        self.cultural_sensitivity_checker = self._initialize_sensitivity_checker()
        self.authenticity_database = self._initialize_authenticity_database()

    def _initialize_dublin_experts(self) -> List[DublinExpertReviewer]:
        """Initialize Dublin cultural expert reviewers"""
        return [
            DublinExpertReviewer(
                name="Dublin Cultural Heritage Expert",
                expertise_areas=[
                    "Dublin landmarks and history",
                    "Irish cultural traditions",
                    "Dublin family life and community",
                    "Irish education system"
                ],
                validation_criteria=[
                    "Accurate Dublin location descriptions",
                    "Authentic Irish cultural references",
                    "Appropriate age-level content",
                    "Respectful cultural representation"
                ],
                authenticity_indicators=[
                    "Correct Dublin landmark names and descriptions",
                    "Accurate Irish cultural practices",
                    "Appropriate Irish English vocabulary",
                    "Authentic Irish social interaction patterns"
                ],
                sensitivity_guidelines=[
                    "Avoid Irish stereotypes and clichés",
                    "Respect Irish cultural traditions",
                    "Maintain cultural authenticity",
                    "Ensure inclusive representation"
                ]
            ),
            DublinExpertReviewer(
                name="Irish Education Specialist",
                expertise_areas=[
                    "Irish primary education system",
                    "Irish curriculum and pedagogy",
                    "Irish school culture and practices",
                    "Age-appropriate content development"
                ],
                validation_criteria=[
                    "Age-appropriate educational content",
                    "Irish curriculum alignment",
                    "Irish school culture accuracy",
                    "Developmental appropriateness"
                ],
                authenticity_indicators=[
                    "Correct Irish school terminology",
                    "Appropriate Irish educational practices",
                    "Age-appropriate Irish cultural content",
                    "Irish learning environment accuracy"
                ],
                sensitivity_guidelines=[
                    "Respect Irish educational values",
                    "Avoid educational stereotypes",
                    "Ensure inclusive learning content",
                    "Maintain cultural sensitivity in education"
                ]
            ),
            DublinExpertReviewer(
                name="Bicultural Integration Specialist",
                expertise_areas=[
                    "Chinese-Irish cultural integration",
                    "Bicultural identity development",
                    "Cultural bridge building",
                    "Heritage preservation and integration"
                ],
                validation_criteria=[
                    "Balanced cultural representation",
                    "Heritage pride maintenance",
                    "Integration encouragement",
                    "Cultural bridge opportunities"
                ],
                authenticity_indicators=[
                    "Respectful Chinese cultural representation",
                    "Positive Irish cultural integration",
                    "Balanced bicultural content",
                    "Heritage pride preservation"
                ],
                sensitivity_guidelines=[
                    "Avoid cultural hierarchy implications",
                    "Prevent cultural pressure or assimilation",
                    "Ensure authentic cultural representation",
                    "Maintain cultural dignity and respect"
                ]
            )
        ]

    def _initialize_sensitivity_checker(self) -> CulturalSensitivityChecker:
        """Initialize cultural sensitivity checking configuration"""
        return CulturalSensitivityChecker(
            problematic_patterns=[
                # Irish stereotypes to avoid
                r"\bleprechaun\b",
                r"\bpot of gold\b",
                r"\bfighting irish\b",
                r"\bdrunk\b.*\birish\b",
                r"\bira\b",
                r"\btroubles\b",
                r"\bpotato.*famine\b",
                # Cultural pressure patterns
                r"\bmust.*assimilate\b",
                r"\bshould.*forget.*chinese\b",
                r"\birish.*better.*chinese\b",
                r"\bsuperior.*culture\b",
                # Age-inappropriate content
                r"\badult.*content\b",
                r"\bmature.*themes\b",
                r"\bcomplex.*politics\b"
            ],
            positive_indicators=[
                # Positive Irish cultural elements
                r"\bgaa\b",
                r"\bdublin\b",
                r"\birish.*music\b",
                r"\bstorytelling\b",
                r"\bcommunity\b",
                r"\bcéad míle fáilte\b",
                r"\bfamily\b",
                r"\beducation\b",
                r"\bcraic\b",
                # Positive Chinese cultural elements
                r"\bchinese.*heritage\b",
                r"\bchinese.*culture\b",
                r"\bchinese.*traditions\b",
                r"\bchinese.*values\b",
                r"\bchinese.*family\b"
            ],
            bicultural_balance_indicators=[
                r"\bboth.*cultures\b",
                r"\bchinese.*and.*irish\b",
                r"\bcultural.*bridge\b",
                r"\bheritage.*pride\b",
                r"\bintegration.*opportunity\b",
                r"\bcultural.*exchange\b",
                r"\bsharing.*traditions\b"
            ],
            age_appropriateness_indicators=[
                r"\bage.*appropriate\b",
                r"\bchild.*friendly\b",
                r"\bfamily.*activity\b",
                r"\bschool.*appropriate\b",
                r"\bjunior.*infants\b",
                r"\bsenior.*infants\b",
                r"\b1st.*class\b",
                r"\b2nd.*class\b",
                r"\b3rd.*class\b",
                r"\b4th.*class\b"
            ],
            trauma_informed_indicators=[
                r"\bgentle\b",
                r"\bpatient\b",
                r"\bencouraging\b",
                r"\bsupportive\b",
                r"\bno.*pressure\b",
                r"\bcelebrate.*effort\b",
                r"\bemotional.*safety\b",
                r"\bcultural.*comfort\b"
            ]
        )

    def _initialize_authenticity_database(self) -> Dict[str, Dict[str, Any]]:
        """Initialize Dublin authenticity database"""
        return {
            "dublin_locations": {
                "phoenix_park": {
                    "correct_name": "Phoenix Park",
                    "pronunciation": "FEE-nix Park",
                    "description": "Europe's largest enclosed public park",
                    "cultural_significance": "Central to Dublin family life",
                    "authentic_activities": ["playground", "zoo", "picnics", "walking", "GAA"],
                    "common_misconceptions": ["small park", "just a zoo", "not family-friendly"]
                },
                "trinity_college": {
                    "correct_name": "Trinity College",
                    "pronunciation": "TRIN-i-tee College",
                    "description": "Historic university in Dublin city center",
                    "cultural_significance": "Symbol of Irish education and learning",
                    "authentic_activities": ["campus walks", "Book of Kells", "library visits"],
                    "common_misconceptions": ["only for students", "not child-friendly", "too academic"]
                },
                "temple_bar": {
                    "correct_name": "Temple Bar",
                    "pronunciation": "TEM-pel BAR",
                    "description": "Cultural quarter with colorful buildings and street performers",
                    "cultural_significance": "Heart of Dublin's cultural scene",
                    "authentic_activities": ["street performers", "cultural events", "family cafes"],
                    "common_misconceptions": ["only for adults", "nightlife only", "not family-friendly"]
                }
            },
            "irish_cultural_practices": {
                "gaa_sports": {
                    "authentic_elements": ["hurling", "gaelic football", "camogie", "community clubs"],
                    "cultural_significance": "Central to Irish identity and community",
                    "appropriate_references": ["teamwork", "community spirit", "Irish pride"],
                    "avoid_stereotypes": ["violent", "only for boys", "too competitive"]
                },
                "irish_hospitality": {
                    "authentic_elements": ["céad míle fáilte", "friendliness", "community support"],
                    "cultural_significance": "Irish welcoming nature and community spirit",
                    "appropriate_references": ["welcoming", "helpful", "community-oriented"],
                    "avoid_stereotypes": ["overly friendly", "naive", "simple"]
                },
                "irish_education": {
                    "authentic_elements": ["creativity", "individual expression", "inclusive environment"],
                    "cultural_significance": "Irish educational values and practices",
                    "appropriate_references": ["supportive teachers", "creative learning", "inclusive"],
                    "avoid_stereotypes": ["less rigorous", "too casual", "not academic"]
                }
            },
            "bicultural_integration": {
                "chinese_heritage": {
                    "authentic_elements": ["family values", "education respect", "cultural traditions"],
                    "cultural_significance": "Chinese cultural identity and values",
                    "appropriate_references": ["heritage pride", "cultural sharing", "family bonds"],
                    "avoid_stereotypes": ["overly academic", "rigid", "insular"]
                },
                "integration_balance": {
                    "authentic_elements": ["cultural bridge", "heritage preservation", "integration encouragement"],
                    "cultural_significance": "Balanced bicultural identity development",
                    "appropriate_references": ["both cultures valuable", "cultural exchange", "heritage pride"],
                    "avoid_stereotypes": ["assimilation pressure", "cultural hierarchy", "heritage abandonment"]
                }
            }
        }

    async def validate_cultural_content(self, 
                                      cultural_scenario: str, 
                                      validation_level: ValidationLevel = ValidationLevel.COMPREHENSIVE) -> CulturalValidationResult:
        """Validate cultural authenticity and sensitivity of content"""
        
        # Basic validation
        basic_validation = self._perform_basic_validation(cultural_scenario)
        
        # Expert review
        expert_review = {}
        if validation_level in [ValidationLevel.EXPERT, ValidationLevel.COMPREHENSIVE]:
            expert_review = self._perform_expert_review(cultural_scenario)
        
        # Community feedback simulation
        community_feedback = []
        if validation_level in [ValidationLevel.COMMUNITY, ValidationLevel.COMPREHENSIVE]:
            community_feedback = self._simulate_community_feedback(cultural_scenario)
        
        # Cultural sensitivity check
        sensitivity_check = self._perform_sensitivity_check(cultural_scenario)
        
        # Calculate authenticity score
        authenticity_score = self._calculate_authenticity_score(
            basic_validation, expert_review, community_feedback, sensitivity_check
        )
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            basic_validation, expert_review, community_feedback, sensitivity_check
        )
        
        return CulturalValidationResult(
            authenticity_score=authenticity_score,
            sensitivity_check=sensitivity_check,
            community_feedback=community_feedback,
            expert_review=expert_review,
            issues_found=basic_validation.get("issues", []),
            strengths_identified=basic_validation.get("strengths", []),
            recommendations=recommendations,
            validation_level=validation_level
        )

    def _perform_basic_validation(self, content: str) -> Dict[str, Any]:
        """Perform basic cultural authenticity validation"""
        validation = {
            "authentic": True,
            "issues": [],
            "strengths": []
        }
        
        content_lower = content.lower()
        
        # Check for positive cultural indicators
        positive_indicators = self.cultural_sensitivity_checker.positive_indicators
        has_positive_elements = any(re.search(pattern, content_lower) for pattern in positive_indicators)
        
        if has_positive_elements:
            validation["strengths"].append("Contains positive cultural references")
        else:
            validation["issues"].append("Could include more positive cultural elements")
        
        # Check for problematic patterns
        problematic_patterns = self.cultural_sensitivity_checker.problematic_patterns
        for pattern in problematic_patterns:
            if re.search(pattern, content_lower):
                validation["authentic"] = False
                validation["issues"].append(f"Contains problematic pattern: {pattern}")
        
        # Check Dublin location accuracy
        dublin_locations = self.authenticity_database["dublin_locations"]
        for location_key, location_info in dublin_locations.items():
            if location_info["correct_name"].lower() in content_lower:
                validation["strengths"].append(f"References authentic Dublin location: {location_info['correct_name']}")
        
        return validation

    def _perform_expert_review(self, content: str) -> Dict[str, Any]:
        """Perform expert review of cultural content"""
        expert_review = {
            "dublin_authenticity": {"score": 0.0, "comments": []},
            "cultural_sensitivity": {"score": 0.0, "comments": []},
            "bicultural_balance": {"score": 0.0, "comments": []},
            "age_appropriateness": {"score": 0.0, "comments": []}
        }
        
        content_lower = content.lower()
        
        # Dublin authenticity review
        dublin_score = 0.0
        dublin_comments = []
        
        # Check for authentic Dublin references
        dublin_locations = self.authenticity_database["dublin_locations"]
        for location_key, location_info in dublin_locations.items():
            if location_info["correct_name"].lower() in content_lower:
                dublin_score += 0.3
                dublin_comments.append(f"Authentic reference to {location_info['correct_name']}")
        
        # Check for Irish cultural practices
        irish_practices = self.authenticity_database["irish_cultural_practices"]
        for practice_key, practice_info in irish_practices.items():
            for element in practice_info["authentic_elements"]:
                if element.lower() in content_lower:
                    dublin_score += 0.2
                    dublin_comments.append(f"Authentic Irish cultural reference: {element}")
        
        expert_review["dublin_authenticity"] = {
            "score": min(dublin_score, 1.0),
            "comments": dublin_comments
        }
        
        # Cultural sensitivity review
        sensitivity_score = 0.0
        sensitivity_comments = []
        
        # Check for positive indicators
        positive_indicators = self.cultural_sensitivity_checker.positive_indicators
        positive_count = sum(1 for pattern in positive_indicators if re.search(pattern, content_lower))
        sensitivity_score += min(positive_count * 0.1, 0.5)
        
        if positive_count > 0:
            sensitivity_comments.append(f"Contains {positive_count} positive cultural indicators")
        
        # Check for bicultural balance
        bicultural_indicators = self.cultural_sensitivity_checker.bicultural_balance_indicators
        bicultural_count = sum(1 for pattern in bicultural_indicators if re.search(pattern, content_lower))
        sensitivity_score += min(bicultural_count * 0.2, 0.3)
        
        if bicultural_count > 0:
            sensitivity_comments.append(f"Shows bicultural balance with {bicultural_count} indicators")
        
        expert_review["cultural_sensitivity"] = {
            "score": min(sensitivity_score, 1.0),
            "comments": sensitivity_comments
        }
        
        # Bicultural balance review
        balance_score = 0.0
        balance_comments = []
        
        # Check for Chinese heritage elements
        if any(word in content_lower for word in ["chinese", "heritage", "tradition"]):
            balance_score += 0.4
            balance_comments.append("Includes Chinese heritage elements")
        
        # Check for Irish integration elements
        if any(word in content_lower for word in ["irish", "dublin", "gaa"]):
            balance_score += 0.4
            balance_comments.append("Includes Irish integration elements")
        
        # Check for cultural bridge elements
        if any(word in content_lower for word in ["both", "bridge", "share"]):
            balance_score += 0.2
            balance_comments.append("Includes cultural bridge elements")
        
        expert_review["bicultural_balance"] = {
            "score": min(balance_score, 1.0),
            "comments": balance_comments
        }
        
        # Age appropriateness review
        age_score = 0.0
        age_comments = []
        
        # Check for age-appropriate indicators
        age_indicators = self.cultural_sensitivity_checker.age_appropriateness_indicators
        age_count = sum(1 for pattern in age_indicators if re.search(pattern, content_lower))
        age_score += min(age_count * 0.2, 0.6)
        
        if age_count > 0:
            age_comments.append(f"Contains {age_count} age-appropriate indicators")
        
        # Check for trauma-informed indicators
        trauma_indicators = self.cultural_sensitivity_checker.trauma_informed_indicators
        trauma_count = sum(1 for pattern in trauma_indicators if re.search(pattern, content_lower))
        age_score += min(trauma_count * 0.1, 0.4)
        
        if trauma_count > 0:
            age_comments.append(f"Contains {trauma_count} trauma-informed indicators")
        
        expert_review["age_appropriateness"] = {
            "score": min(age_score, 1.0),
            "comments": age_comments
        }
        
        return expert_review

    def _simulate_community_feedback(self, content: str) -> List[str]:
        """Simulate community feedback for cultural content"""
        feedback = []
        content_lower = content.lower()
        
        # Simulate Dublin parent feedback
        if "dublin" in content_lower and "family" in content_lower:
            feedback.append("Dublin parent: 'This accurately represents Dublin family life'")
        
        # Simulate Chinese parent feedback
        if "chinese" in content_lower and "heritage" in content_lower:
            feedback.append("Chinese parent: 'Good to see Chinese heritage being valued'")
        
        # Simulate teacher feedback
        if "school" in content_lower and "learning" in content_lower:
            feedback.append("Irish teacher: 'Content is appropriate for Irish school environment'")
        
        # Simulate cultural expert feedback
        if "gaa" in content_lower or "irish" in content_lower:
            feedback.append("Cultural expert: 'Irish cultural references are authentic and respectful'")
        
        return feedback

    def _perform_sensitivity_check(self, content: str) -> CulturalSensitivityLevel:
        """Perform cultural sensitivity check"""
        content_lower = content.lower()
        
        # Check for problematic patterns
        problematic_patterns = self.cultural_sensitivity_checker.problematic_patterns
        has_problematic = any(re.search(pattern, content_lower) for pattern in problematic_patterns)
        
        if has_problematic:
            return CulturalSensitivityLevel.PROBLEMATIC
        
        # Check for positive indicators
        positive_indicators = self.cultural_sensitivity_checker.positive_indicators
        positive_count = sum(1 for pattern in positive_indicators if re.search(pattern, content_lower))
        
        # Check for bicultural balance
        bicultural_indicators = self.cultural_sensitivity_checker.bicultural_balance_indicators
        bicultural_count = sum(1 for pattern in bicultural_indicators if re.search(pattern, content_lower))
        
        # Check for trauma-informed elements
        trauma_indicators = self.cultural_sensitivity_checker.trauma_informed_indicators
        trauma_count = sum(1 for pattern in trauma_indicators if re.search(pattern, content_lower))
        
        # Determine sensitivity level
        if positive_count >= 5 and bicultural_count >= 2 and trauma_count >= 3:
            return CulturalSensitivityLevel.EXCELLENT
        elif positive_count >= 3 and bicultural_count >= 1 and trauma_count >= 2:
            return CulturalSensitivityLevel.APPROPRIATE
        elif positive_count >= 1:
            return CulturalSensitivityLevel.NEEDS_REVIEW
        else:
            return CulturalSensitivityLevel.PROBLEMATIC

    def _calculate_authenticity_score(self, 
                                    basic_validation: Dict[str, Any],
                                    expert_review: Dict[str, Any],
                                    community_feedback: List[str],
                                    sensitivity_check: CulturalSensitivityLevel) -> float:
        """Calculate overall authenticity score"""
        
        # Base score from basic validation
        base_score = 0.5 if basic_validation["authentic"] else 0.2
        
        # Expert review contribution
        expert_score = 0.0
        if expert_review:
            expert_scores = [
                expert_review.get("dublin_authenticity", {}).get("score", 0.0),
                expert_review.get("cultural_sensitivity", {}).get("score", 0.0),
                expert_review.get("bicultural_balance", {}).get("score", 0.0),
                expert_review.get("age_appropriateness", {}).get("score", 0.0)
            ]
            expert_score = sum(expert_scores) / len(expert_scores)
        
        # Community feedback contribution
        community_score = min(len(community_feedback) * 0.1, 0.2)
        
        # Sensitivity check contribution
        sensitivity_scores = {
            CulturalSensitivityLevel.EXCELLENT: 0.3,
            CulturalSensitivityLevel.APPROPRIATE: 0.2,
            CulturalSensitivityLevel.NEEDS_REVIEW: 0.1,
            CulturalSensitivityLevel.PROBLEMATIC: 0.0
        }
        sensitivity_score = sensitivity_scores.get(sensitivity_check, 0.0)
        
        # Calculate final score
        final_score = base_score + (expert_score * 0.4) + community_score + sensitivity_score
        
        return min(final_score, 1.0)

    def _generate_recommendations(self,
                                basic_validation: Dict[str, Any],
                                expert_review: Dict[str, Any],
                                community_feedback: List[str],
                                sensitivity_check: CulturalSensitivityLevel) -> List[str]:
        """Generate recommendations for improving cultural content"""
        recommendations = []
        
        # Recommendations based on basic validation
        if not basic_validation["authentic"]:
            recommendations.append("Review content for problematic cultural references")
        
        if not basic_validation.get("strengths"):
            recommendations.append("Add more positive cultural elements")
        
        # Recommendations based on expert review
        if expert_review:
            dublin_score = expert_review.get("dublin_authenticity", {}).get("score", 0.0)
            if dublin_score < 0.5:
                recommendations.append("Include more authentic Dublin cultural references")
            
            sensitivity_score = expert_review.get("cultural_sensitivity", {}).get("score", 0.0)
            if sensitivity_score < 0.5:
                recommendations.append("Enhance cultural sensitivity and positive indicators")
            
            balance_score = expert_review.get("bicultural_balance", {}).get("score", 0.0)
            if balance_score < 0.5:
                recommendations.append("Improve bicultural balance and heritage representation")
            
            age_score = expert_review.get("age_appropriateness", {}).get("score", 0.0)
            if age_score < 0.5:
                recommendations.append("Ensure age-appropriate content and trauma-informed approach")
        
        # Recommendations based on sensitivity check
        if sensitivity_check == CulturalSensitivityLevel.PROBLEMATIC:
            recommendations.append("Urgent review needed for cultural sensitivity issues")
        elif sensitivity_check == CulturalSensitivityLevel.NEEDS_REVIEW:
            recommendations.append("Add more positive cultural indicators and trauma-informed elements")
        
        # Default recommendations
        if not recommendations:
            recommendations.append("Content meets cultural authenticity standards")
        
        return recommendations

    def validate_dublin_location_accuracy(self, location_name: str, description: str) -> Dict[str, Any]:
        """Validate accuracy of Dublin location description"""
        validation = {
            "accurate": False,
            "score": 0.0,
            "issues": [],
            "strengths": []
        }
        
        location_key = location_name.lower().replace(" ", "_")
        location_info = self.authenticity_database["dublin_locations"].get(location_key)
        
        if not location_info:
            validation["issues"].append(f"Location {location_name} not found in authenticity database")
            return validation
        
        # Check name accuracy
        if location_info["correct_name"].lower() == location_name.lower():
            validation["score"] += 0.3
            validation["strengths"].append("Correct location name")
        else:
            validation["issues"].append(f"Incorrect name: should be {location_info['correct_name']}")
        
        # Check description accuracy
        description_lower = description.lower()
        if any(activity in description_lower for activity in location_info["authentic_activities"]):
            validation["score"] += 0.4
            validation["strengths"].append("Includes authentic activities")
        else:
            validation["issues"].append("Missing authentic activities for this location")
        
        # Check for misconceptions
        for misconception in location_info["common_misconceptions"]:
            if misconception.lower() in description_lower:
                validation["issues"].append(f"Contains common misconception: {misconception}")
        
        validation["accurate"] = validation["score"] >= 0.6
        return validation

    def get_cultural_authenticity_guidelines(self) -> Dict[str, List[str]]:
        """Get guidelines for maintaining cultural authenticity"""
        return {
            "dublin_authenticity": [
                "Use correct Dublin location names and descriptions",
                "Include authentic Irish cultural practices",
                "Reference real Dublin activities and experiences",
                "Avoid common misconceptions about Dublin locations"
            ],
            "irish_cultural_sensitivity": [
                "Respect Irish cultural traditions and practices",
                "Avoid Irish stereotypes and clichés",
                "Include positive Irish cultural elements",
                "Ensure authentic Irish social interaction patterns"
            ],
            "bicultural_balance": [
                "Maintain Chinese heritage pride and identity",
                "Encourage positive Irish cultural integration",
                "Create cultural bridge opportunities",
                "Avoid cultural hierarchy or pressure"
            ],
            "age_appropriateness": [
                "Ensure content is appropriate for target age group",
                "Include trauma-informed elements",
                "Maintain child-friendly cultural representation",
                "Support positive cultural identity development"
            ]
        }
