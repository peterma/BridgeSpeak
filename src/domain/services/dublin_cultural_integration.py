"""
Dublin Cultural Integration Service

Main integration service that coordinates all Dublin cultural context components
for Story 2.2. Integrates Dublin locations, Irish cultural elements, cultural
balance framework, seasonal content, and authenticity validation.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
import datetime
from .dublin_location_scenarios import DublinLocationScenarioService, DublinCulturalScenario
from .irish_cultural_elements import IrishCulturalElementsService, CulturalIntegrationResult
from .cultural_balance_framework import CulturalBalanceFramework, BalancedCulturalScenario
from .seasonal_cultural_content import SeasonalCulturalContentService, SeasonalCulturalScenarios
from .cultural_authenticity_validator import CulturalAuthenticityValidator, CulturalValidationResult
from .cultural_representation import CulturalRepresentationService
from .scenario_generation import ScenarioGenerationService
from .conversation_types import ScenarioType, ConversationTurn, ConversationPhase


@dataclass
class DublinCulturalIntegrationResult:
    """Complete result of Dublin cultural integration"""
    dublin_scenario: DublinCulturalScenario
    cultural_integration: CulturalIntegrationResult
    cultural_balance: BalancedCulturalScenario
    seasonal_content: Optional[SeasonalCulturalScenarios]
    authenticity_validation: CulturalValidationResult
    integrated_conversation_turns: List[ConversationTurn]
    cultural_summary: Dict[str, Any]


class DublinCulturalIntegrationService:
    """Main service for Dublin cultural context integration"""

    def __init__(self, 
                 cultural_service: Optional[CulturalRepresentationService] = None,
                 scenario_service: Optional[ScenarioGenerationService] = None):
        
        # Initialize core cultural service
        self.cultural_service = cultural_service or CulturalRepresentationService()
        
        # Initialize Dublin cultural components
        self.dublin_locations = DublinLocationScenarioService(self.cultural_service)
        self.irish_elements = IrishCulturalElementsService(self.cultural_service)
        self.cultural_balance = CulturalBalanceFramework(self.cultural_service)
        self.seasonal_content = SeasonalCulturalContentService(self.cultural_service)
        self.authenticity_validator = CulturalAuthenticityValidator(self.cultural_service)
        
        # Initialize scenario service for integration
        self.scenario_service = scenario_service or ScenarioGenerationService()

    async def generate_dublin_cultural_scenario(self,
                                              location_name: str,
                                              child_profile: Dict[str, Any],
                                              base_scenario_type: Optional[ScenarioType] = None) -> DublinCulturalIntegrationResult:
        """Generate complete Dublin cultural scenario with all integrations"""
        
        # Step 1: Generate Dublin location scenario
        dublin_scenario = await self.dublin_locations.generate_location_scenario(location_name, child_profile)
        if not dublin_scenario:
            raise ValueError(f"Could not generate scenario for location: {location_name}")
        
        # Step 2: Integrate Irish cultural elements
        base_content = dublin_scenario.age_appropriate_content
        cultural_integration = await self.irish_elements.integrate_cultural_elements(
            base_content, child_profile, location_name
        )
        
        # Step 3: Apply cultural balance framework
        cultural_balance = self.cultural_balance.balance_cultural_content(
            cultural_integration.integrated_content, child_profile
        )
        
        # Step 4: Get seasonal content
        current_date = datetime.datetime.now()
        seasonal_content = await self.seasonal_content.get_seasonal_content(current_date, child_profile)
        
        # Step 5: Validate cultural authenticity
        full_content = f"{cultural_balance.dublin_context} {cultural_balance.integration_encouragement}"
        authenticity_validation = await self.authenticity_validator.validate_cultural_content(full_content)
        
        # Step 6: Generate conversation turns
        conversation_turns = self._generate_conversation_turns(
            dublin_scenario, cultural_integration, cultural_balance, child_profile
        )
        
        # Step 7: Create cultural summary
        cultural_summary = self._create_cultural_summary(
            dublin_scenario, cultural_integration, cultural_balance, 
            seasonal_content, authenticity_validation
        )
        
        return DublinCulturalIntegrationResult(
            dublin_scenario=dublin_scenario,
            cultural_integration=cultural_integration,
            cultural_balance=cultural_balance,
            seasonal_content=seasonal_content,
            authenticity_validation=authenticity_validation,
            integrated_conversation_turns=conversation_turns,
            cultural_summary=cultural_summary
        )

    def _generate_conversation_turns(self,
                                   dublin_scenario: DublinCulturalScenario,
                                   cultural_integration: CulturalIntegrationResult,
                                   cultural_balance: BalancedCulturalScenario,
                                   child_profile: Dict[str, Any]) -> List[ConversationTurn]:
        """Generate conversation turns for Dublin cultural scenario"""
        turns = []
        
        # Chinese comfort phase
        chinese_comfort = self._create_chinese_comfort_turn(
            dublin_scenario, cultural_balance, child_profile
        )
        if chinese_comfort:
            turns.append(chinese_comfort)
        
        # English demonstration phase
        english_demo = self._create_english_demonstration_turn(
            dublin_scenario, cultural_integration, child_profile
        )
        if english_demo:
            turns.append(english_demo)
        
        # Cultural bridge phase (using encouraging feedback phase)
        cultural_bridge = self._create_cultural_bridge_turn(
            cultural_balance, child_profile
        )
        if cultural_bridge:
            turns.append(cultural_bridge)
        
        return turns

    def _create_chinese_comfort_turn(self,
                                   dublin_scenario: DublinCulturalScenario,
                                   cultural_balance: BalancedCulturalScenario,
                                   child_profile: Dict[str, Any]) -> Optional[ConversationTurn]:
        """Create Chinese comfort conversation turn"""
        
        # Base comfort message
        comfort_message = f"今天我们学习关于{dublin_scenario.location.name}的知识。"
        
        # Add heritage pride
        if cultural_balance.chinese_heritage_pride:
            heritage_message = cultural_balance.chinese_heritage_pride[0]
            comfort_message += f" {heritage_message}"
        
        # Add cultural bridge
        if cultural_balance.cultural_bridge_opportunities:
            bridge_message = cultural_balance.cultural_bridge_opportunities[0]
            comfort_message += f" {bridge_message}"
        
        return ConversationTurn(
            phase=ConversationPhase.CHINESE_COMFORT,
            speaker="xiao_mei",
            content=comfort_message,
            language="zh-CN",
            timestamp=datetime.datetime.now().timestamp()
        )

    def _create_english_demonstration_turn(self,
                                         dublin_scenario: DublinCulturalScenario,
                                         cultural_integration: CulturalIntegrationResult,
                                         child_profile: Dict[str, Any]) -> Optional[ConversationTurn]:
        """Create English demonstration conversation turn"""
        
        # Start with Dublin location description
        demo_message = f"Let's learn about {dublin_scenario.location.name}. "
        demo_message += dublin_scenario.age_appropriate_content
        
        # Add Irish cultural elements
        if cultural_integration.cultural_elements_used:
            demo_message += f" We can learn about {', '.join(cultural_integration.cultural_elements_used)}."
        
        # Add Irish social patterns
        if dublin_scenario.irish_social_patterns:
            demo_message += f" Remember Irish politeness: {dublin_scenario.irish_social_patterns[0]}."
        
        return ConversationTurn(
            phase=ConversationPhase.ENGLISH_DEMONSTRATION,
            speaker="xiao_mei",
            content=demo_message,
            language="en-IE",
            timestamp=datetime.datetime.now().timestamp()
        )

    def _create_cultural_bridge_turn(self,
                                   cultural_balance: BalancedCulturalScenario,
                                   child_profile: Dict[str, Any]) -> Optional[ConversationTurn]:
        """Create cultural bridge conversation turn"""
        
        bridge_message = cultural_balance.integration_encouragement
        bridge_message += f" {cultural_balance.heritage_celebration}"
        
        return ConversationTurn(
            phase=ConversationPhase.ENCOURAGING_FEEDBACK,
            speaker="xiao_mei",
            content=bridge_message,
            language="en-IE",
            timestamp=datetime.datetime.now().timestamp()
        )

    def _create_cultural_summary(self,
                               dublin_scenario: DublinCulturalScenario,
                               cultural_integration: CulturalIntegrationResult,
                               cultural_balance: BalancedCulturalScenario,
                               seasonal_content: Optional[SeasonalCulturalScenarios],
                               authenticity_validation: CulturalValidationResult) -> Dict[str, Any]:
        """Create comprehensive cultural summary"""
        
        return {
            "dublin_location": {
                "name": dublin_scenario.location.name,
                "type": dublin_scenario.location.location_type.value,
                "cultural_significance": dublin_scenario.location.cultural_significance,
                "age_appropriate": dublin_scenario.location.age_appropriateness
            },
            "irish_cultural_elements": {
                "elements_used": cultural_integration.cultural_elements_used,
                "bicultural_bridges": cultural_integration.bicultural_bridges,
                "seasonal_relevance": cultural_integration.seasonal_relevance
            },
            "cultural_balance": {
                "heritage_pride_elements": len(cultural_balance.chinese_heritage_pride),
                "bridge_opportunities": len(cultural_balance.cultural_bridge_opportunities),
                "authentic_representation": cultural_balance.authentic_representation
            },
            "seasonal_content": {
                "holiday_scenarios": len(seasonal_content.holiday_scenarios) if seasonal_content else 0,
                "seasonal_activities": len(seasonal_content.seasonal_activities) if seasonal_content else 0,
                "integration_opportunities": len(seasonal_content.cultural_integration_opportunities) if seasonal_content else 0
            },
            "authenticity_validation": {
                "authenticity_score": authenticity_validation.authenticity_score,
                "sensitivity_level": authenticity_validation.sensitivity_check.value,
                "issues_found": len(authenticity_validation.issues_found),
                "strengths_identified": len(authenticity_validation.strengths_identified)
            },
            "integration_quality": {
                "overall_score": self._calculate_overall_integration_score(
                    cultural_integration, cultural_balance, authenticity_validation
                ),
                "recommendations": authenticity_validation.recommendations
            }
        }

    def _calculate_overall_integration_score(self,
                                           cultural_integration: CulturalIntegrationResult,
                                           cultural_balance: BalancedCulturalScenario,
                                           authenticity_validation: CulturalValidationResult) -> float:
        """Calculate overall integration quality score"""
        
        # Cultural integration score (30%)
        integration_score = 0.3 if cultural_integration.cultural_elements_used else 0.0
        integration_score += 0.2 if cultural_integration.bicultural_bridges else 0.0
        
        # Cultural balance score (30%)
        balance_score = 0.2 if cultural_balance.chinese_heritage_pride else 0.0
        balance_score += 0.2 if cultural_balance.cultural_bridge_opportunities else 0.0
        balance_score += 0.1 if cultural_balance.authentic_representation else 0.0
        
        # Authenticity validation score (40%)
        authenticity_score = authenticity_validation.authenticity_score * 0.4
        
        return min(integration_score + balance_score + authenticity_score, 1.0)

    async def get_available_dublin_scenarios(self, child_profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Get available Dublin scenarios for child profile"""
        
        age_group = self._get_age_group(child_profile.get("age", 8))
        available_locations = self.dublin_locations.get_locations_for_age_group(age_group)
        
        scenarios = []
        for location in available_locations:
            scenario_info = {
                "location_name": location.name,
                "location_type": location.location_type.value,
                "description": location.description,
                "cultural_significance": location.cultural_significance,
                "child_friendly_activities": location.child_friendly_activities,
                "irish_vocabulary": location.irish_vocabulary,
                "age_appropriateness": location.age_appropriateness,
                "seasonal_relevance": location.seasonal_relevance
            }
            scenarios.append(scenario_info)
        
        return scenarios

    def _get_age_group(self, age: int) -> str:
        """Convert age to Irish curriculum age group"""
        if age <= 5:
            return "Junior Infants"
        elif age <= 6:
            return "Senior Infants"
        elif age <= 7:
            return "1st Class"
        elif age <= 8:
            return "2nd Class"
        elif age <= 9:
            return "3rd Class"
        else:
            return "4th Class"

    async def validate_dublin_cultural_content(self, content: str) -> Dict[str, Any]:
        """Validate Dublin cultural content for authenticity and sensitivity"""
        
        validation_result = await self.authenticity_validator.validate_cultural_content(content)
        
        return {
            "authenticity_score": validation_result.authenticity_score,
            "sensitivity_level": validation_result.sensitivity_check.value,
            "issues_found": validation_result.issues_found,
            "strengths_identified": validation_result.strengths_identified,
            "recommendations": validation_result.recommendations,
            "validation_level": validation_result.validation_level.value
        }

    async def get_seasonal_dublin_content(self, 
                                        child_profile: Dict[str, Any],
                                        target_date: Optional[datetime.datetime] = None) -> Dict[str, Any]:
        """Get seasonal Dublin content for specific date"""
        
        if not target_date:
            target_date = datetime.datetime.now()
        
        seasonal_content = await self.seasonal_content.get_seasonal_content(target_date, child_profile)
        
        return {
            "season": self._get_season_from_date(target_date),
            "holiday_scenarios": [
                {
                    "holiday_name": holiday.holiday_name,
                    "traditions": holiday.traditions,
                    "dublin_activities": holiday.dublin_activities,
                    "family_activities": holiday.family_activities,
                    "cultural_bridges": holiday.cultural_bridges
                }
                for holiday in seasonal_content.holiday_scenarios
            ],
            "seasonal_activities": [
                {
                    "name": activity.name,
                    "description": activity.description,
                    "dublin_locations": activity.dublin_locations,
                    "cultural_significance": activity.cultural_significance,
                    "bicultural_opportunities": activity.bicultural_opportunities
                }
                for activity in seasonal_content.seasonal_activities
            ],
            "dublin_location_enhancements": seasonal_content.dublin_location_enhancements,
            "cultural_integration_opportunities": seasonal_content.cultural_integration_opportunities
        }

    def _get_season_from_date(self, date: datetime.datetime) -> str:
        """Get season from date"""
        month = date.month
        if month in [12, 1, 2]:
            return "winter"
        elif month in [3, 4, 5]:
            return "spring"
        elif month in [6, 7, 8]:
            return "summer"
        else:
            return "autumn"

    async def get_cultural_integration_summary(self) -> Dict[str, Any]:
        """Get summary of Dublin cultural integration capabilities"""
        
        return {
            "dublin_locations": {
                "total_locations": len(self.dublin_locations.get_available_locations()),
                "location_types": [
                    "transportation", "landmarks", "cultural_areas", 
                    "educational", "recreation"
                ]
            },
            "irish_cultural_elements": {
                "gaa_sports": ["hurling", "gaelic_football", "camogie"],
                "irish_holidays": ["st_patricks_day", "christmas", "halloween"],
                "traditional_foods": ["irish_stew", "soda_bread", "potatoes"],
                "social_patterns": ["politeness", "queuing", "greetings", "conversation", "courtesy"]
            },
            "cultural_balance_framework": {
                "chinese_heritage_elements": [
                    "family_values", "education_values", "celebration_traditions",
                    "food_culture", "cultural_identity"
                ],
                "irish_integration_elements": [
                    "irish_hospitality", "irish_family_values", "irish_education",
                    "irish_celebrations"
                ],
                "cultural_bridge_types": [
                    "family_values", "education_learning", "celebration_traditions",
                    "food_sharing", "music_dance", "storytelling", "community_spirit", "respect_elders"
                ]
            },
            "seasonal_content": {
                "seasons": ["spring", "summer", "autumn", "winter"],
                "irish_holidays": ["st_patricks_day", "christmas", "halloween"],
                "dublin_seasonal_activities": "Available for all seasons"
            },
            "authenticity_validation": {
                "validation_levels": ["basic", "expert", "community", "comprehensive"],
                "sensitivity_levels": ["appropriate", "needs_review", "problematic", "excellent"],
                "expert_reviewers": [
                    "Dublin Cultural Heritage Expert",
                    "Irish Education Specialist", 
                    "Bicultural Integration Specialist"
                ]
            }
        }
