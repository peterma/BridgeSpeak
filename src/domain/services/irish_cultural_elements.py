"""
Irish Cultural Elements Integration Service

Provides comprehensive Irish cultural elements integration for conversation scenarios,
including GAA sports, Irish holidays, traditional foods, and seasonal content.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from enum import Enum
import datetime
from .cultural_representation import CulturalRepresentationService


class IrishHolidayType(str, Enum):
    """Irish holiday types for seasonal content"""
    ST_PATRICKS_DAY = "st_patricks_day"
    CHRISTMAS = "christmas"
    HALLOWEEN = "halloween"
    EASTER = "easter"
    NEW_YEAR = "new_year"


class GAASportType(str, Enum):
    """GAA sport types for sports integration"""
    HURLING = "hurling"
    GAELIC_FOOTBALL = "gaelic_football"
    CAMOGIE = "camogie"
    HANDBALL = "handball"
    ROUNDERS = "rounders"


@dataclass
class SeasonalContent:
    """Seasonal cultural content with activities and vocabulary"""
    traditions: List[str]
    family_activities: List[str]
    school_celebrations: List[str]
    dublin_specific: List[str] = field(default_factory=list)
    multicultural_celebration: List[str] = field(default_factory=list)


@dataclass
class IrishCulturalElements:
    """Comprehensive Irish cultural elements database"""
    gaa_sports: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    irish_holidays: Dict[str, SeasonalContent] = field(default_factory=dict)
    traditional_foods: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    irish_music_dance: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    social_patterns: Dict[str, List[str]] = field(default_factory=dict)


@dataclass
class CulturalIntegrationResult:
    """Result of cultural integration process"""
    integrated_content: str
    cultural_elements_used: List[str]
    bicultural_bridges: List[str]
    age_appropriateness: str
    seasonal_relevance: Optional[str] = None


class IrishCulturalElementsService:
    """Service for integrating Irish cultural elements into conversation scenarios"""

    def __init__(self, cultural_service: Optional[CulturalRepresentationService] = None):
        self.cultural_service = cultural_service or CulturalRepresentationService()
        self.irish_elements = self._initialize_irish_cultural_elements()
        self.seasonal_calendar = self._initialize_seasonal_calendar()

    def _initialize_irish_cultural_elements(self) -> IrishCulturalElements:
        """Initialize comprehensive Irish cultural elements database"""
        return IrishCulturalElements(
            gaa_sports={
                "hurling": {
                    "description": "Traditional Irish sport with wooden stick (hurley) and small ball (sliotar)",
                    "cultural_significance": "Ancient Irish sport dating back 3000 years, teaches teamwork and skill",
                    "child_friendly_aspects": [
                        "Teamwork and cooperation",
                        "Practice makes perfect",
                        "Supporting teammates",
                        "Celebrating goals together"
                    ],
                    "vocabulary": ["hurling", "hurley", "sliotar", "goals", "team", "practice", "match"],
                    "positive_associations": [
                        "Fast and exciting like hurling!",
                        "Teamwork like GAA players!",
                        "Practice like hurling champions!",
                        "Supporting each other like teammates!"
                    ],
                    "age_appropriate_content": {
                        "Junior Infants": "Hurling is a fast Irish sport with sticks and balls",
                        "Senior Infants": "Hurling players use hurleys to hit the sliotar into goals",
                        "1st Class": "Hurling is Ireland's national sport, played with hurleys and sliotars",
                        "2nd Class": "Hurling combines speed, skill, and teamwork in Ireland's ancient sport",
                        "3rd Class": "Hurling is Ireland's fastest field sport, requiring skill with hurley and sliotar",
                        "4th Class": "Hurling is Ireland's national sport, combining ancient tradition with modern skill"
                    }
                },
                "gaelic_football": {
                    "description": "Irish football combining soccer and rugby elements",
                    "cultural_significance": "Popular Irish sport showing Irish athleticism and community spirit",
                    "child_friendly_aspects": [
                        "Running and kicking",
                        "Teamwork and strategy",
                        "Supporting your team",
                        "Celebrating together"
                    ],
                    "vocabulary": ["Gaelic football", "goals", "points", "team", "match", "practice", "kick"],
                    "positive_associations": [
                        "Strong like Gaelic football players!",
                        "Teamwork like GAA teams!",
                        "Running fast like footballers!",
                        "Supporting each other like teammates!"
                    ],
                    "age_appropriate_content": {
                        "Junior Infants": "Gaelic football is an Irish sport with kicking and running",
                        "Senior Infants": "Gaelic football players kick the ball to score goals and points",
                        "1st Class": "Gaelic football combines soccer and rugby in Ireland's popular sport",
                        "2nd Class": "Gaelic football requires skill in kicking, catching, and teamwork",
                        "3rd Class": "Gaelic football is Ireland's most popular sport, combining skill and strategy",
                        "4th Class": "Gaelic football showcases Irish athleticism and community spirit in sport"
                    }
                },
                "camogie": {
                    "description": "Women's version of hurling, played by girls and women",
                    "cultural_significance": "Shows Irish women's strength, skill, and equality in sports",
                    "child_friendly_aspects": [
                        "Girls can play sports too",
                        "Strength and skill development",
                        "Teamwork and friendship",
                        "Breaking gender barriers"
                    ],
                    "vocabulary": ["camogie", "women's hurling", "team", "skill", "strength", "equality"],
                    "positive_associations": [
                        "Strong like camogie players!",
                        "Girls can be athletes too!",
                        "Skill and strength like camogie champions!",
                        "Teamwork like camogie teams!"
                    ],
                    "age_appropriate_content": {
                        "Junior Infants": "Camogie is hurling for girls, showing girls can play sports too",
                        "Senior Infants": "Camogie players are strong and skilled, just like boys in hurling",
                        "1st Class": "Camogie is the women's version of hurling, showing equality in Irish sports",
                        "2nd Class": "Camogie demonstrates that girls can excel in traditional Irish sports",
                        "3rd Class": "Camogie showcases Irish women's athleticism and skill in traditional sports",
                        "4th Class": "Camogie represents Irish women's strength and equality in national sports"
                    }
                }
            },
            irish_holidays={
                "st_patricks_day": SeasonalContent(
                    traditions=[
                        "Wearing green clothing",
                        "Watching St. Patrick's Day parades",
                        "Listening to traditional Irish music",
                        "Learning about St. Patrick and Irish history"
                    ],
                    family_activities=[
                        "Attending Dublin St. Patrick's Day parade",
                        "Learning traditional Irish dancing",
                        "Making green crafts and decorations",
                        "Sharing Irish stories and legends"
                    ],
                    school_celebrations=[
                        "Cultural dress-up day with green clothing",
                        "Irish language activities and songs",
                        "Learning about Irish history and culture",
                        "Shamrock art and craft activities"
                    ],
                    dublin_specific=[
                        "Dublin St. Patrick's Day parade on O'Connell Street",
                        "Temple Bar cultural celebrations",
                        "Grafton Street green decorations",
                        "Dublin Castle cultural events"
                    ],
                    multicultural_celebration=[
                        "Celebrating Irish pride like Chinese New Year pride",
                        "Sharing Chinese traditions with Irish friends",
                        "Learning about both cultures together",
                        "Celebrating diversity and inclusion"
                    ]
                ),
                "christmas": SeasonalContent(
                    traditions=[
                        "Christmas markets and festive lights",
                        "Nativity plays and Christmas carols",
                        "Family gatherings and gift giving",
                        "Traditional Irish Christmas foods"
                    ],
                    family_activities=[
                        "Visiting Christmas markets in Dublin",
                        "Seeing Grafton Street Christmas lights",
                        "Attending Christmas concerts and shows",
                        "Making traditional Irish Christmas treats"
                    ],
                    school_celebrations=[
                        "Christmas concerts and nativity plays",
                        "Christmas craft activities",
                        "Learning Christmas carols in Irish and English",
                        "Christmas party celebrations"
                    ],
                    dublin_specific=[
                        "Grafton Street Christmas lights and decorations",
                        "Brown Thomas Christmas window displays",
                        "Dublin Christmas markets",
                        "Christmas events at Dublin Castle"
                    ],
                    multicultural_celebration=[
                        "Celebrating Christmas with Chinese and Irish traditions",
                        "Sharing Chinese New Year preparations",
                        "Learning about different winter celebrations",
                        "Family traditions from both cultures"
                    ]
                ),
                "halloween": SeasonalContent(
                    traditions=[
                        "Trick or treating in neighborhoods",
                        "Carving pumpkins and making decorations",
                        "Telling Irish ghost stories and legends",
                        "Dressing up in costumes"
                    ],
                    family_activities=[
                        "Trick or treating with family and friends",
                        "Making Halloween decorations together",
                        "Telling Irish Halloween stories",
                        "Attending community Halloween events"
                    ],
                    school_celebrations=[
                        "Halloween costume parades",
                        "Pumpkin carving competitions",
                        "Irish Halloween story telling",
                        "Halloween party celebrations"
                    ],
                    dublin_specific=[
                        "Dublin Halloween festivals and events",
                        "Haunted Dublin tours for families",
                        "Community Halloween celebrations",
                        "Dublin Zoo Halloween events"
                    ],
                    multicultural_celebration=[
                        "Sharing Chinese ghost stories and Irish legends",
                        "Learning about different Halloween traditions",
                        "Celebrating autumn festivals from both cultures",
                        "Family traditions and storytelling"
                    ]
                )
            },
            traditional_foods={
                "irish_stew": {
                    "description": "Traditional Irish meat and vegetable stew, comfort food for families",
                    "cultural_significance": "Represents Irish hospitality and family togetherness",
                    "child_friendly_aspects": [
                        "Warm and comforting",
                        "Made with love by family",
                        "Traditional family recipe",
                        "Brings family together"
                    ],
                    "vocabulary": ["Irish stew", "meat", "vegetables", "family meal", "traditional", "comfort food"],
                    "cultural_bridge": "Like Chinese hot pot, Irish stew brings families together around the table",
                    "age_appropriate_content": {
                        "Junior Infants": "Irish stew is warm food that families eat together",
                        "Senior Infants": "Irish stew is made with meat and vegetables, like Chinese soup",
                        "1st Class": "Irish stew is traditional comfort food that brings Irish families together",
                        "2nd Class": "Irish stew represents Irish hospitality and family values in cooking",
                        "3rd Class": "Irish stew is a traditional Irish dish showing family togetherness",
                        "4th Class": "Irish stew embodies Irish culinary tradition and family hospitality"
                    }
                },
                "soda_bread": {
                    "description": "Traditional Irish bread made with baking soda, simple and wholesome",
                    "cultural_significance": "Shows Irish resourcefulness and simple, good food",
                    "child_friendly_aspects": [
                        "Easy to make with family",
                        "Simple and wholesome",
                        "Traditional Irish recipe",
                        "Good for sharing"
                    ],
                    "vocabulary": ["soda bread", "bread", "traditional", "baking", "family cooking", "wholesome"],
                    "cultural_bridge": "Like Chinese steamed buns, soda bread is simple, traditional food made with family",
                    "age_appropriate_content": {
                        "Junior Infants": "Soda bread is Irish bread that families make together",
                        "Senior Infants": "Soda bread is simple bread made with baking soda",
                        "1st Class": "Soda bread is traditional Irish bread, simple and wholesome",
                        "2nd Class": "Soda bread shows Irish resourcefulness in simple, good cooking",
                        "3rd Class": "Soda bread represents traditional Irish baking and family cooking",
                        "4th Class": "Soda bread embodies Irish culinary simplicity and family traditions"
                    }
                },
                "potatoes": {
                    "description": "Staple Irish food, historically important in Irish diet and culture",
                    "cultural_significance": "Historical importance in Irish diet, shows Irish resilience",
                    "child_friendly_aspects": [
                        "Versatile and easy to cook",
                        "Good for growing in gardens",
                        "Family staple food",
                        "Can be prepared many ways"
                    ],
                    "vocabulary": ["potatoes", "Irish food", "staple", "versatile", "family food", "garden"],
                    "cultural_bridge": "Like rice in Chinese culture, potatoes are important in Irish food traditions",
                    "age_appropriate_content": {
                        "Junior Infants": "Potatoes are important Irish food that families eat",
                        "Senior Infants": "Potatoes are versatile food that can be cooked many ways",
                        "1st Class": "Potatoes are a staple of Irish diet and family cooking",
                        "2nd Class": "Potatoes have historical importance in Irish food culture",
                        "3rd Class": "Potatoes represent Irish culinary tradition and family food culture",
                        "4th Class": "Potatoes embody Irish food heritage and family cooking traditions"
                    }
                }
            },
            irish_music_dance={
                "traditional_music": {
                    "description": "Irish traditional music with fiddles, tin whistles, and bodhrán drums",
                    "cultural_significance": "Heart of Irish culture, brings communities together",
                    "child_friendly_aspects": [
                        "Fun to listen and dance to",
                        "Tells stories of Ireland",
                        "Brings people together",
                        "Easy to clap along with"
                    ],
                    "vocabulary": ["Irish music", "fiddle", "tin whistle", "bodhrán", "traditional", "dance"],
                    "cultural_bridge": "Like Chinese traditional music, Irish music tells stories of our people",
                    "age_appropriate_content": {
                        "Junior Infants": "Irish music is fun music that tells stories",
                        "Senior Infants": "Irish music uses fiddles and drums to make happy sounds",
                        "1st Class": "Irish traditional music brings communities together with stories",
                        "2nd Class": "Irish music represents Irish storytelling tradition and community spirit",
                        "3rd Class": "Irish traditional music embodies Irish cultural heritage and community",
                        "4th Class": "Irish music showcases Irish cultural identity and community togetherness"
                    }
                },
                "irish_dancing": {
                    "description": "Traditional Irish dancing with precise footwork and lively movements",
                    "cultural_significance": "Shows Irish discipline, skill, and cultural pride",
                    "child_friendly_aspects": [
                        "Fun to learn and practice",
                        "Good exercise and coordination",
                        "Can be done with friends",
                        "Shows Irish cultural pride"
                    ],
                    "vocabulary": ["Irish dancing", "footwork", "traditional", "dance", "practice", "coordination"],
                    "cultural_bridge": "Like Chinese traditional dance, Irish dancing shows cultural pride and skill",
                    "age_appropriate_content": {
                        "Junior Infants": "Irish dancing is fun dancing with special steps",
                        "Senior Infants": "Irish dancing uses precise footwork and lively movements",
                        "1st Class": "Irish dancing shows Irish cultural pride and discipline",
                        "2nd Class": "Irish dancing represents Irish cultural tradition and skill development",
                        "3rd Class": "Irish dancing embodies Irish cultural identity and artistic expression",
                        "4th Class": "Irish dancing showcases Irish cultural heritage and artistic discipline"
                    }
                }
            },
            social_patterns={
                "politeness": [
                    "Always say 'please' and 'thank you' - very important in Ireland",
                    "Use 'excuse me' to get attention politely",
                    "Hold doors open for others - shows Irish courtesy",
                    "Say 'sorry' even for small things - Irish politeness",
                    "Use 'grand' to mean 'good' or 'fine' - Irish expression"
                ],
                "queuing": [
                    "Wait patiently in queues - Irish people respect order",
                    "Don't push or rush ahead - be patient and polite",
                    "Respect the order of people waiting",
                    "Be patient at bus stops and shops",
                    "Queue quietly and politely - Irish queue culture"
                ],
                "greetings": [
                    "Say 'good morning' to teachers and adults",
                    "Use 'how are you?' as a greeting - Irish friendliness",
                    "Respond with 'grand, thanks' to 'how are you?'",
                    "Say 'see you later' instead of just 'bye'",
                    "Use 'lovely to meet you' for new people"
                ],
                "conversation": [
                    "Talk about the weather as conversation starter - Irish tradition",
                    "Be friendly and casual but respectful",
                    "Listen carefully to others - Irish storytelling tradition",
                    "Ask questions to show interest",
                    "Use Irish expressions like 'brilliant!' and 'fair play!'"
                ],
                "courtesy": [
                    "Respect elders and teachers - Irish family values",
                    "Help others when you can - Irish community spirit",
                    "Share and take turns - Irish cooperation",
                    "Be kind to younger children - Irish care for others",
                    "Show appreciation for help received - Irish gratitude"
                ]
            }
        )

    def _initialize_seasonal_calendar(self) -> Dict[str, Dict[str, Any]]:
        """Initialize seasonal cultural calendar"""
        return {
            "spring": {
                "months": ["March", "April", "May"],
                "cultural_events": ["St. Patrick's Day", "Easter", "Spring flowers blooming"],
                "activities": ["Phoenix Park visits", "GAA season starts", "School Easter break"],
                "vocabulary": ["spring", "flowers", "Easter", "St. Patrick's Day", "new growth", "rebirth"],
                "dublin_specific": ["Dublin St. Patrick's Day parade", "Phoenix Park spring flowers", "GAA season opening"]
            },
            "summer": {
                "months": ["June", "July", "August"],
                "cultural_events": ["GAA matches", "Summer festivals", "School holidays"],
                "activities": ["Phoenix Park picnics", "Dublin Zoo visits", "Beach trips", "GAA matches"],
                "vocabulary": ["summer", "holidays", "GAA matches", "picnics", "beach", "festivals"],
                "dublin_specific": ["Croke Park GAA matches", "Dublin summer festivals", "Phoenix Park summer activities"]
            },
            "autumn": {
                "months": ["September", "October", "November"],
                "cultural_events": ["Back to school", "Harvest festivals", "Halloween"],
                "activities": ["School activities", "Halloween preparations", "Indoor activities", "Harvest celebrations"],
                "vocabulary": ["autumn", "school", "Halloween", "harvest", "cozy", "back to school"],
                "dublin_specific": ["Dublin Halloween festivals", "School term activities", "Autumn in Phoenix Park"]
            },
            "winter": {
                "months": ["December", "January", "February"],
                "cultural_events": ["Christmas", "New Year", "Winter solstice"],
                "activities": ["Christmas shopping", "Family gatherings", "Indoor activities", "Christmas markets"],
                "vocabulary": ["winter", "Christmas", "family", "cozy", "celebration", "New Year"],
                "dublin_specific": ["Grafton Street Christmas lights", "Dublin Christmas markets", "Winter family activities"]
            }
        }

    async def integrate_cultural_elements(self, 
                                        base_content: str, 
                                        child_profile: Dict[str, Any],
                                        location_context: Optional[str] = None) -> CulturalIntegrationResult:
        """Integrate Irish cultural elements into conversation content"""
        
        age_group = self._get_age_group(child_profile.get("age", 8))
        current_season = self._get_current_season()
        
        # Start with base content
        integrated_content = base_content
        cultural_elements_used = []
        bicultural_bridges = []
        
        # Add GAA sports elements if appropriate
        if self._should_include_gaa_elements(location_context, current_season):
            gaa_integration = self._integrate_gaa_elements(age_group)
            integrated_content += f" {gaa_integration['content']}"
            cultural_elements_used.extend(gaa_integration['elements'])
            bicultural_bridges.extend(gaa_integration['bridges'])
        
        # Add Irish holiday elements if seasonally appropriate
        if self._should_include_holiday_elements(current_season):
            holiday_integration = self._integrate_holiday_elements(current_season, age_group)
            integrated_content += f" {holiday_integration['content']}"
            cultural_elements_used.extend(holiday_integration['elements'])
            bicultural_bridges.extend(holiday_integration['bridges'])
        
        # Add traditional food elements if appropriate
        if self._should_include_food_elements(location_context):
            food_integration = self._integrate_food_elements(age_group)
            integrated_content += f" {food_integration['content']}"
            cultural_elements_used.extend(food_integration['elements'])
            bicultural_bridges.extend(food_integration['bridges'])
        
        # Add Irish social patterns
        social_integration = self._integrate_social_patterns(age_group)
        integrated_content += f" {social_integration['content']}"
        cultural_elements_used.extend(social_integration['elements'])
        
        return CulturalIntegrationResult(
            integrated_content=integrated_content,
            cultural_elements_used=cultural_elements_used,
            bicultural_bridges=bicultural_bridges,
            age_appropriateness=age_group,
            seasonal_relevance=current_season
        )

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

    def _get_current_season(self) -> str:
        """Get current season based on date"""
        month = datetime.datetime.now().month
        if month in [12, 1, 2]:
            return "winter"
        elif month in [3, 4, 5]:
            return "spring"
        elif month in [6, 7, 8]:
            return "summer"
        else:
            return "autumn"

    def _should_include_gaa_elements(self, location_context: Optional[str], season: str) -> bool:
        """Determine if GAA elements should be included"""
        if location_context and "park" in location_context.lower():
            return True
        if season in ["spring", "summer"]:  # GAA season
            return True
        return False

    def _should_include_holiday_elements(self, season: str) -> bool:
        """Determine if holiday elements should be included"""
        return True  # Always include seasonal holiday elements

    def _should_include_food_elements(self, location_context: Optional[str]) -> bool:
        """Determine if food elements should be included"""
        if location_context and ("market" in location_context.lower() or "home" in location_context.lower()):
            return True
        return False

    def _integrate_gaa_elements(self, age_group: str) -> Dict[str, Any]:
        """Integrate GAA sports elements"""
        gaa_sport = "hurling"  # Default to hurling
        sport_info = self.irish_elements.gaa_sports[gaa_sport]
        
        content = sport_info["age_appropriate_content"][age_group]
        elements = [f"GAA {gaa_sport}"]
        bridges = [sport_info.get("cultural_bridge", "Both cultures value teamwork and practice")]
        
        return {
            "content": content,
            "elements": elements,
            "bridges": bridges
        }

    def _integrate_holiday_elements(self, season: str, age_group: str) -> Dict[str, Any]:
        """Integrate Irish holiday elements"""
        if season == "spring":
            holiday = "st_patricks_day"
        elif season == "winter":
            holiday = "christmas"
        elif season == "autumn":
            holiday = "halloween"
        else:
            holiday = "st_patricks_day"  # Default
        
        holiday_info = self.irish_elements.irish_holidays[holiday]
        
        # Create age-appropriate content
        if age_group in ["Junior Infants", "Senior Infants"]:
            content = f"In {season}, we celebrate {holiday.replace('_', ' ')} with family and friends."
        else:
            content = f"During {season}, Irish families celebrate {holiday.replace('_', ' ')} with {', '.join(holiday_info.traditions[:2])}."
        
        elements = [f"Irish {holiday}"]
        bridges = holiday_info.multicultural_celebration[:1]
        
        return {
            "content": content,
            "elements": elements,
            "bridges": bridges
        }

    def _integrate_food_elements(self, age_group: str) -> Dict[str, Any]:
        """Integrate traditional Irish food elements"""
        food = "irish_stew"  # Default to Irish stew
        food_info = self.irish_elements.traditional_foods[food]
        
        content = food_info["age_appropriate_content"][age_group]
        elements = [f"Irish {food}"]
        bridges = [food_info.get("cultural_bridge", "Both cultures value family meals")]
        
        return {
            "content": content,
            "elements": elements,
            "bridges": bridges
        }

    def _integrate_social_patterns(self, age_group: str) -> Dict[str, Any]:
        """Integrate Irish social interaction patterns"""
        if age_group in ["Junior Infants", "Senior Infants"]:
            patterns = self.irish_elements.social_patterns["politeness"][:2]
        else:
            patterns = self.irish_elements.social_patterns["politeness"][:3]
        
        content = f"Remember Irish politeness: {', '.join(patterns)}."
        elements = ["Irish social patterns"]
        
        return {
            "content": content,
            "elements": elements,
            "bridges": []
        }

    def get_seasonal_cultural_content(self, season: str) -> Dict[str, Any]:
        """Get seasonal cultural content for specific season"""
        return self.seasonal_calendar.get(season, {})

    def get_gaa_sport_info(self, sport_type: GAASportType) -> Dict[str, Any]:
        """Get information about specific GAA sport"""
        return self.irish_elements.gaa_sports.get(sport_type.value, {})

    def get_irish_holiday_info(self, holiday_type: IrishHolidayType) -> SeasonalContent:
        """Get information about specific Irish holiday"""
        return self.irish_elements.irish_holidays.get(holiday_type.value, SeasonalContent([], [], []))

    def validate_cultural_authenticity(self, content: str) -> Dict[str, Any]:
        """Validate cultural authenticity of integrated content"""
        validation = {
            "authentic": True,
            "issues": [],
            "strengths": []
        }
        
        # Check for positive Irish cultural references
        positive_elements = [
            "gaa", "dublin", "irish", "traditional", "family", "community",
            "hurling", "gaelic football", "st. patrick", "christmas", "halloween"
        ]
        
        content_lower = content.lower()
        has_positive_elements = any(element in content_lower for element in positive_elements)
        
        if has_positive_elements:
            validation["strengths"].append("Contains positive Irish cultural references")
        else:
            validation["issues"].append("Could include more positive Irish cultural elements")
        
        # Check for problematic stereotypes
        problematic_terms = [
            "leprechaun", "pot of gold", "fighting irish", "drunk", "ira", "troubles"
        ]
        
        for term in problematic_terms:
            if term in content_lower:
                validation["authentic"] = False
                validation["issues"].append(f"Contains potentially problematic reference: {term}")
        
        return validation
