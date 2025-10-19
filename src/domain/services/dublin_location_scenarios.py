"""
Dublin Location Scenario Service for Cultural Context Integration

Provides authentic Dublin-specific conversation scenarios for Chinese children
learning English in Ireland. Implements 15+ Dublin locations with cultural
context and age-appropriate content.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from enum import Enum
import time
from .conversation_types import ScenarioType, ConversationPhase, ScenarioContent, ConversationTurn, ScenarioSession
from .cultural_representation import CulturalRepresentationService


class DublinLocationType(str, Enum):
    """Dublin location types for scenario categorization"""
    TRANSPORTATION = "transportation"
    LANDMARKS = "landmarks"
    CULTURAL_AREAS = "cultural_areas"
    EDUCATIONAL = "educational"
    RECREATION = "recreation"


@dataclass
class DublinLocation:
    """Dublin location with cultural context and scenario information"""
    name: str
    location_type: DublinLocationType
    description: str
    cultural_significance: str
    child_friendly_activities: List[str]
    irish_vocabulary: List[str]
    pronunciation_guide: Dict[str, str]
    age_appropriateness: List[str]  # Age groups this location is suitable for
    seasonal_relevance: List[str]  # Seasons when this location is most relevant


@dataclass
class DublinCulturalScenario:
    """Enhanced scenario with Dublin cultural context"""
    location: DublinLocation
    cultural_elements: Dict[str, Any]
    age_appropriate_content: str
    bicultural_integration: str
    irish_social_patterns: List[str]
    seasonal_content: Optional[str] = None


class DublinLocationScenarioService:
    """Service for generating Dublin-specific cultural scenarios"""

    def __init__(self, cultural_service: Optional[CulturalRepresentationService] = None):
        self.cultural_service = cultural_service or CulturalRepresentationService()
        self.dublin_locations = self._initialize_dublin_locations()
        self.irish_cultural_elements = self._initialize_irish_cultural_elements()
        self.social_interaction_patterns = self._initialize_social_patterns()
        self.seasonal_content = self._initialize_seasonal_content()

    def _initialize_dublin_locations(self) -> Dict[str, DublinLocation]:
        """Initialize comprehensive Dublin location database"""
        return {
            "dart_train": DublinLocation(
                name="DART Train",
                location_type=DublinLocationType.TRANSPORTATION,
                description="Dublin Area Rapid Transit - the train system connecting Dublin suburbs to city center",
                cultural_significance="Essential Dublin transport, used by families for city visits and school commutes",
                child_friendly_activities=[
                    "Buying tickets with parents",
                    "Looking out windows at Dublin Bay",
                    "Learning station names",
                    "Meeting other children on the train"
                ],
                irish_vocabulary=[
                    "DART", "ticket", "platform", "station", "journey", "return ticket", "single ticket"
                ],
                pronunciation_guide={
                    "DART": "DART (like 'art' with D)",
                    "platform": "PLAT-form",
                    "journey": "JUR-nee"
                },
                age_appropriateness=["Junior Infants", "Senior Infants", "1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["all_seasons"]
            ),
            "phoenix_park": DublinLocation(
                name="Phoenix Park",
                location_type=DublinLocationType.RECREATION,
                description="Europe's largest enclosed public park, home to Dublin Zoo and playgrounds",
                cultural_significance="Central to Dublin family life, where children play and families gather",
                child_friendly_activities=[
                    "Playing in playgrounds",
                    "Visiting Dublin Zoo",
                    "Walking with family",
                    "Feeding ducks at ponds",
                    "Playing football/GAA"
                ],
                irish_vocabulary=[
                    "Phoenix Park", "playground", "zoo", "ducks", "pond", "football", "GAA", "picnic"
                ],
                pronunciation_guide={
                    "Phoenix": "FEE-nix",
                    "playground": "PLAY-ground",
                    "picnic": "PIC-nic"
                },
                age_appropriateness=["Junior Infants", "Senior Infants", "1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["spring", "summer", "autumn"]
            ),
            "trinity_college": DublinLocation(
                name="Trinity College",
                location_type=DublinLocationType.EDUCATIONAL,
                description="Historic university in Dublin city center, famous for the Book of Kells",
                cultural_significance="Symbol of Irish education and learning, inspiring for children",
                child_friendly_activities=[
                    "Walking through the campus",
                    "Seeing the Book of Kells (with parents)",
                    "Playing in the college green",
                    "Learning about Irish history"
                ],
                irish_vocabulary=[
                    "Trinity College", "university", "library", "Book of Kells", "campus", "students"
                ],
                pronunciation_guide={
                    "Trinity": "TRIN-i-tee",
                    "Kells": "KELZ",
                    "campus": "CAM-pus"
                },
                age_appropriateness=["1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["all_seasons"]
            ),
            "temple_bar": DublinLocation(
                name="Temple Bar",
                location_type=DublinLocationType.CULTURAL_AREAS,
                description="Cultural quarter with colorful buildings, street performers, and family-friendly activities",
                cultural_significance="Heart of Dublin's cultural scene, shows Irish creativity and community spirit",
                child_friendly_activities=[
                    "Watching street performers",
                    "Looking at colorful buildings",
                    "Visiting family-friendly cafes",
                    "Learning about Irish music"
                ],
                irish_vocabulary=[
                    "Temple Bar", "street performers", "music", "colorful", "cafes", "culture"
                ],
                pronunciation_guide={
                    "Temple Bar": "TEM-pel BAR",
                    "performers": "per-FORM-ers",
                    "colorful": "KUL-er-ful"
                },
                age_appropriateness=["Senior Infants", "1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["spring", "summer", "autumn"]
            ),
            "gpo": DublinLocation(
                name="GPO (General Post Office)",
                location_type=DublinLocationType.LANDMARKS,
                description="Historic post office on O'Connell Street, important in Irish history",
                cultural_significance="Symbol of Irish independence and communication, teaches about Irish history",
                child_friendly_activities=[
                    "Sending postcards with parents",
                    "Learning about Irish history",
                    "Seeing the historic building",
                    "Understanding communication"
                ],
                irish_vocabulary=[
                    "GPO", "post office", "postcard", "stamp", "letter", "history", "O'Connell Street"
                ],
                pronunciation_guide={
                    "GPO": "G-P-O",
                    "O'Connell": "oh-KON-el",
                    "postcard": "POST-card"
                },
                age_appropriateness=["2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["all_seasons"]
            ),
            "dublin_castle": DublinLocation(
                name="Dublin Castle",
                location_type=DublinLocationType.LANDMARKS,
                description="Historic castle in Dublin city center, now used for state occasions",
                cultural_significance="Important part of Irish history, shows how Ireland has changed over time",
                child_friendly_activities=[
                    "Walking around the castle grounds",
                    "Learning about Irish history",
                    "Seeing the beautiful buildings",
                    "Understanding Irish heritage"
                ],
                irish_vocabulary=[
                    "Dublin Castle", "castle", "history", "heritage", "grounds", "buildings"
                ],
                pronunciation_guide={
                    "castle": "KAS-el",
                    "heritage": "HER-i-tij",
                    "grounds": "GROUNDZ"
                },
                age_appropriateness=["2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["all_seasons"]
            ),
            "dublin_zoo": DublinLocation(
                name="Dublin Zoo",
                location_type=DublinLocationType.RECREATION,
                description="Zoo located in Phoenix Park, home to many animals from around the world",
                cultural_significance="Beloved Dublin attraction, teaches children about animals and conservation",
                child_friendly_activities=[
                    "Seeing animals from around the world",
                    "Learning about conservation",
                    "Playing in the zoo playground",
                    "Having family picnics"
                ],
                irish_vocabulary=[
                    "Dublin Zoo", "animals", "zoo", "conservation", "playground", "picnic"
                ],
                pronunciation_guide={
                    "zoo": "ZOO",
                    "animals": "AN-i-mals",
                    "conservation": "kon-ser-VAY-shun"
                },
                age_appropriateness=["Junior Infants", "Senior Infants", "1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["spring", "summer", "autumn"]
            ),
            "grafton_street": DublinLocation(
                name="Grafton Street",
                location_type=DublinLocationType.CULTURAL_AREAS,
                description="Famous shopping street in Dublin with street performers and shops",
                cultural_significance="Heart of Dublin shopping and street culture, shows Irish creativity",
                child_friendly_activities=[
                    "Watching street performers",
                    "Shopping with family",
                    "Seeing Christmas lights in winter",
                    "Learning about Irish street culture"
                ],
                irish_vocabulary=[
                    "Grafton Street", "shopping", "performers", "Christmas lights", "street culture"
                ],
                pronunciation_guide={
                    "Grafton": "GRAF-ton",
                    "shopping": "SHOP-ing",
                    "Christmas": "KRIS-mas"
                },
                age_appropriateness=["Senior Infants", "1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["all_seasons"]
            ),
            "ha_penny_bridge": DublinLocation(
                name="Ha'penny Bridge",
                location_type=DublinLocationType.LANDMARKS,
                description="Historic bridge over the River Liffey, famous Dublin landmark",
                cultural_significance="Iconic Dublin bridge, shows how Dublin has grown over time",
                child_friendly_activities=[
                    "Walking across the bridge",
                    "Looking at the River Liffey",
                    "Learning about Dublin's history",
                    "Taking family photos"
                ],
                irish_vocabulary=[
                    "Ha'penny Bridge", "bridge", "River Liffey", "landmark", "history"
                ],
                pronunciation_guide={
                    "Ha'penny": "HAY-pen-ee",
                    "Liffey": "LIF-ee",
                    "landmark": "LAND-mark"
                },
                age_appropriateness=["1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["all_seasons"]
            ),
            "dublin_bus": DublinLocation(
                name="Dublin Bus",
                location_type=DublinLocationType.TRANSPORTATION,
                description="Dublin's bus system, used by families throughout the city",
                cultural_significance="Essential Dublin transport, teaches children about city navigation",
                child_friendly_activities=[
                    "Riding the bus with family",
                    "Learning bus numbers and routes",
                    "Meeting other passengers",
                    "Understanding city transport"
                ],
                irish_vocabulary=[
                    "Dublin Bus", "bus", "route", "passengers", "transport", "bus stop"
                ],
                pronunciation_guide={
                    "bus": "BUS",
                    "route": "ROOT",
                    "passengers": "PAS-en-jers"
                },
                age_appropriateness=["Junior Infants", "Senior Infants", "1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["all_seasons"]
            ),
            "st_stephens_green": DublinLocation(
                name="St. Stephen's Green",
                location_type=DublinLocationType.RECREATION,
                description="Beautiful park in Dublin city center with playground and duck pond",
                cultural_significance="Peaceful green space in the heart of Dublin, shows Irish love of nature",
                child_friendly_activities=[
                    "Playing in the playground",
                    "Feeding ducks at the pond",
                    "Walking with family",
                    "Having picnics"
                ],
                irish_vocabulary=[
                    "St. Stephen's Green", "park", "playground", "ducks", "pond", "picnic"
                ],
                pronunciation_guide={
                    "Stephen's": "STEE-vens",
                    "playground": "PLAY-ground",
                    "picnic": "PIC-nic"
                },
                age_appropriateness=["Junior Infants", "Senior Infants", "1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["spring", "summer", "autumn"]
            ),
            "dublin_airport": DublinLocation(
                name="Dublin Airport",
                location_type=DublinLocationType.TRANSPORTATION,
                description="Ireland's main airport, where families travel to visit relatives",
                cultural_significance="Gateway to Ireland, connects Irish families with relatives worldwide",
                child_friendly_activities=[
                    "Meeting relatives arriving",
                    "Learning about different countries",
                    "Understanding travel and airports",
                    "Seeing planes take off and land"
                ],
                irish_vocabulary=[
                    "Dublin Airport", "airport", "planes", "travel", "relatives", "countries"
                ],
                pronunciation_guide={
                    "airport": "AIR-port",
                    "planes": "PLANES",
                    "relatives": "REL-a-tivs"
                },
                age_appropriateness=["Senior Infants", "1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["all_seasons"]
            ),
            "croke_park": DublinLocation(
                name="Croke Park",
                location_type=DublinLocationType.CULTURAL_AREAS,
                description="Home of GAA sports, where hurling and Gaelic football are played",
                cultural_significance="Heart of Irish sports culture, teaches about GAA and Irish identity",
                child_friendly_activities=[
                    "Watching GAA matches with family",
                    "Learning about hurling and Gaelic football",
                    "Understanding Irish sports culture",
                    "Supporting local teams"
                ],
                irish_vocabulary=[
                    "Croke Park", "GAA", "hurling", "Gaelic football", "matches", "teams"
                ],
                pronunciation_guide={
                    "Croke": "CROKE",
                    "hurling": "HUR-ling",
                    "Gaelic": "GAY-lik"
                },
                age_appropriateness=["1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["spring", "summer", "autumn"]
            ),
            "dublin_libraries": DublinLocation(
                name="Dublin Libraries",
                location_type=DublinLocationType.EDUCATIONAL,
                description="Public libraries throughout Dublin, centers of learning and community",
                cultural_significance="Irish love of learning and storytelling, free access to books for all",
                child_friendly_activities=[
                    "Borrowing books with family",
                    "Attending story time sessions",
                    "Learning about Irish stories",
                    "Meeting other children"
                ],
                irish_vocabulary=[
                    "library", "books", "story time", "borrowing", "learning", "stories"
                ],
                pronunciation_guide={
                    "library": "LYE-bra-ree",
                    "borrowing": "BOR-oh-ing",
                    "learning": "LERN-ing"
                },
                age_appropriateness=["Junior Infants", "Senior Infants", "1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["all_seasons"]
            ),
            "dublin_markets": DublinLocation(
                name="Dublin Markets",
                location_type=DublinLocationType.CULTURAL_AREAS,
                description="Traditional markets like Moore Street and Temple Bar Food Market",
                cultural_significance="Irish market culture, shows community spirit and local food traditions",
                child_friendly_activities=[
                    "Shopping for fresh food with family",
                    "Learning about Irish food traditions",
                    "Meeting local vendors",
                    "Understanding market culture"
                ],
                irish_vocabulary=[
                    "markets", "fresh food", "vendors", "traditions", "community", "local"
                ],
                pronunciation_guide={
                    "markets": "MAR-kets",
                    "vendors": "VEN-dors",
                    "traditions": "tra-DI-shuns"
                },
                age_appropriateness=["Senior Infants", "1st Class", "2nd Class", "3rd Class", "4th Class"],
                seasonal_relevance=["all_seasons"]
            )
        }

    def _initialize_irish_cultural_elements(self) -> Dict[str, Any]:
        """Initialize Irish cultural elements for scenario integration"""
        return {
            "gaa_sports": {
                "hurling": {
                    "description": "Traditional Irish sport with wooden stick and small ball",
                    "cultural_significance": "Ancient Irish sport, teaches teamwork and skill",
                    "child_friendly_aspects": ["Teamwork", "Practice", "Supporting teammates", "Celebrating goals"],
                    "vocabulary": ["hurling", "hurley", "sliotar", "goals", "team", "practice"]
                },
                "gaelic_football": {
                    "description": "Irish football combining soccer and rugby elements",
                    "cultural_significance": "Popular Irish sport, shows Irish athleticism and community spirit",
                    "child_friendly_aspects": ["Teamwork", "Running", "Kicking", "Supporting team"],
                    "vocabulary": ["Gaelic football", "goals", "points", "team", "match", "practice"]
                },
                "camogie": {
                    "description": "Women's version of hurling",
                    "cultural_significance": "Shows Irish women's strength and skill in sports",
                    "child_friendly_aspects": ["Girls can play sports", "Strength and skill", "Teamwork"],
                    "vocabulary": ["camogie", "women's hurling", "team", "skill", "strength"]
                }
            },
            "irish_holidays": {
                "st_patricks_day": {
                    "description": "Irish national holiday celebrating Irish culture and heritage",
                    "cultural_significance": "Day of Irish pride and celebration, shows Irish identity",
                    "child_friendly_aspects": ["Green clothing", "Parade watching", "Irish music", "Family celebration"],
                    "vocabulary": ["St. Patrick's Day", "green", "parade", "shamrock", "Irish music", "celebration"]
                },
                "christmas": {
                    "description": "Christmas traditions in Ireland with family focus",
                    "cultural_significance": "Family-centered celebration, shows Irish family values",
                    "child_friendly_aspects": ["Family gatherings", "Christmas lights", "Gift giving", "Traditional food"],
                    "vocabulary": ["Christmas", "family", "lights", "gifts", "traditional food", "celebration"]
                },
                "halloween": {
                    "description": "Halloween traditions in Ireland, where the holiday originated",
                    "cultural_significance": "Irish cultural export, shows Irish storytelling tradition",
                    "child_friendly_aspects": ["Trick or treating", "Costumes", "Irish stories", "Family fun"],
                    "vocabulary": ["Halloween", "trick or treat", "costumes", "Irish stories", "family fun"]
                }
            },
            "traditional_foods": {
                "irish_stew": {
                    "description": "Traditional Irish meat and vegetable stew",
                    "cultural_significance": "Comfort food that brings families together",
                    "child_friendly_aspects": ["Warm and comforting", "Family meal", "Traditional recipe"],
                    "vocabulary": ["Irish stew", "meat", "vegetables", "family meal", "traditional"]
                },
                "soda_bread": {
                    "description": "Traditional Irish bread made with baking soda",
                    "cultural_significance": "Simple, traditional Irish food, shows Irish resourcefulness",
                    "child_friendly_aspects": ["Easy to make", "Traditional recipe", "Family cooking"],
                    "vocabulary": ["soda bread", "bread", "traditional", "baking", "family cooking"]
                },
                "potatoes": {
                    "description": "Staple Irish food, important in Irish history and culture",
                    "cultural_significance": "Historical importance in Irish diet and culture",
                    "child_friendly_aspects": ["Versatile food", "Easy to cook", "Family staple"],
                    "vocabulary": ["potatoes", "Irish food", "staple", "versatile", "family food"]
                }
            }
        }

    def _initialize_social_patterns(self) -> Dict[str, List[str]]:
        """Initialize Irish social interaction patterns"""
        return {
            "politeness": [
                "Always say 'please' and 'thank you'",
                "Use 'excuse me' to get attention politely",
                "Hold doors open for others",
                "Say 'sorry' even for small things",
                "Use 'grand' to mean 'good' or 'fine'"
            ],
            "queuing": [
                "Wait patiently in queues",
                "Don't push or rush ahead",
                "Respect the order of people waiting",
                "Be patient at bus stops and shops",
                "Queue quietly and politely"
            ],
            "greetings": [
                "Say 'good morning' to teachers and adults",
                "Use 'how are you?' as a greeting",
                "Respond with 'grand, thanks' to 'how are you?'",
                "Say 'see you later' instead of just 'bye'",
                "Use 'lovely to meet you' for new people"
            ],
            "conversation": [
                "Talk about the weather as conversation starter",
                "Be friendly and casual but respectful",
                "Listen carefully to others",
                "Ask questions to show interest",
                "Use Irish expressions like 'brilliant!' and 'fair play!'"
            ],
            "courtesy": [
                "Respect elders and teachers",
                "Help others when you can",
                "Share and take turns",
                "Be kind to younger children",
                "Show appreciation for help received"
            ]
        }

    def _initialize_seasonal_content(self) -> Dict[str, Dict[str, Any]]:
        """Initialize seasonal cultural content"""
        return {
            "spring": {
                "cultural_events": ["St. Patrick's Day", "Easter", "Spring flowers blooming"],
                "activities": ["Phoenix Park visits", "GAA season starts", "School Easter break"],
                "vocabulary": ["spring", "flowers", "Easter", "St. Patrick's Day", "new growth"]
            },
            "summer": {
                "cultural_events": ["GAA matches", "Summer festivals", "School holidays"],
                "activities": ["Phoenix Park picnics", "Dublin Zoo visits", "Beach trips"],
                "vocabulary": ["summer", "holidays", "GAA matches", "picnics", "beach"]
            },
            "autumn": {
                "cultural_events": ["Back to school", "Harvest festivals", "Halloween"],
                "activities": ["School activities", "Halloween preparations", "Indoor activities"],
                "vocabulary": ["autumn", "school", "Halloween", "harvest", "cozy"]
            },
            "winter": {
                "cultural_events": ["Christmas", "New Year", "Winter solstice"],
                "activities": ["Christmas shopping", "Family gatherings", "Indoor activities"],
                "vocabulary": ["winter", "Christmas", "family", "cozy", "celebration"]
            }
        }

    async def generate_location_scenario(self, location_name: str, child_profile: Dict[str, Any]) -> Optional[DublinCulturalScenario]:
        """Generate age-appropriate Dublin location scenario with cultural context"""
        location = self.dublin_locations.get(location_name)
        if not location:
            return None

        # Validate age appropriateness
        child_age = child_profile.get("age", 8)
        age_group = self._get_age_group(child_age)
        if age_group not in location.age_appropriateness:
            return None

        # Generate cultural elements for this location
        cultural_elements = self._get_cultural_elements_for_location(location)
        
        # Create age-appropriate content
        age_appropriate_content = self._create_age_appropriate_content(location, age_group)
        
        # Create bicultural integration
        bicultural_integration = self._create_bicultural_integration(location, cultural_elements)
        
        # Get Irish social patterns relevant to this location
        irish_social_patterns = self._get_relevant_social_patterns(location)
        
        # Get seasonal content if applicable
        seasonal_content = self._get_seasonal_content(location)

        return DublinCulturalScenario(
            location=location,
            cultural_elements=cultural_elements,
            age_appropriate_content=age_appropriate_content,
            bicultural_integration=bicultural_integration,
            irish_social_patterns=irish_social_patterns,
            seasonal_content=seasonal_content
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

    def _get_cultural_elements_for_location(self, location: DublinLocation) -> Dict[str, Any]:
        """Get relevant cultural elements for a specific location"""
        elements = {}
        
        # Add GAA sports elements for recreation locations
        if location.location_type == DublinLocationType.RECREATION:
            elements["gaa_sports"] = self.irish_cultural_elements["gaa_sports"]
        
        # Add traditional foods for market locations
        if "market" in location.name.lower():
            elements["traditional_foods"] = self.irish_cultural_elements["traditional_foods"]
        
        # Add holiday elements for cultural areas
        if location.location_type == DublinLocationType.CULTURAL_AREAS:
            elements["irish_holidays"] = self.irish_cultural_elements["irish_holidays"]
        
        return elements

    def _create_age_appropriate_content(self, location: DublinLocation, age_group: str) -> str:
        """Create age-appropriate content for the location"""
        if age_group in ["Junior Infants", "Senior Infants"]:
            return f"Let's visit {location.name}! It's a {location.description.lower()}. We can {', '.join(location.child_friendly_activities[:2])}."
        elif age_group in ["1st Class", "2nd Class"]:
            return f"Today we're going to {location.name}. {location.description}. This is important because {location.cultural_significance.lower()}. We can {', '.join(location.child_friendly_activities[:3])}."
        else:  # 3rd Class, 4th Class
            return f"We're visiting {location.name} today. {location.description}. This location is culturally significant because {location.cultural_significance}. Some activities we can do include {', '.join(location.child_friendly_activities)}."

    def _create_bicultural_integration(self, location: DublinLocation, cultural_elements: Dict[str, Any]) -> str:
        """Create bicultural integration content connecting Chinese and Irish cultures"""
        base_integration = f"Just like we have special places in China, {location.name} is special in Ireland. "
        
        # Add specific cultural bridges based on location type
        if location.location_type == DublinLocationType.EDUCATIONAL:
            base_integration += "Both Chinese and Irish cultures value education and learning. "
        elif location.location_type == DublinLocationType.RECREATION:
            base_integration += "Both cultures love spending time with family in beautiful places. "
        elif location.location_type == DublinLocationType.CULTURAL_AREAS:
            base_integration += "Both Chinese and Irish cultures celebrate their traditions and creativity. "
        
        return base_integration + "We can appreciate both our Chinese heritage and Irish culture!"

    def _get_relevant_social_patterns(self, location: DublinLocation) -> List[str]:
        """Get Irish social patterns relevant to the location"""
        patterns = []
        
        # All locations need basic politeness
        patterns.extend(self.social_interaction_patterns["politeness"][:2])
        
        # Transportation locations need queuing patterns
        if location.location_type == DublinLocationType.TRANSPORTATION:
            patterns.extend(self.social_interaction_patterns["queuing"][:2])
        
        # All locations need greeting patterns
        patterns.extend(self.social_interaction_patterns["greetings"][:2])
        
        return patterns

    def _get_seasonal_content(self, location: DublinLocation) -> Optional[str]:
        """Get seasonal content relevant to the location"""
        # This would be enhanced with actual season detection
        # For now, return content for current season
        current_season = "spring"  # This would be determined by actual date
        
        if current_season in location.seasonal_relevance or "all_seasons" in location.seasonal_relevance:
            seasonal_info = self.seasonal_content.get(current_season, {})
            activities = seasonal_info.get("activities", [])
            if activities:
                return f"In {current_season}, we can {', '.join(activities[:2])} at {location.name}."
        
        return None

    def get_available_locations(self) -> List[str]:
        """Get list of available Dublin locations"""
        return list(self.dublin_locations.keys())

    def get_locations_by_type(self, location_type: DublinLocationType) -> List[DublinLocation]:
        """Get locations filtered by type"""
        return [location for location in self.dublin_locations.values() 
                if location.location_type == location_type]

    def get_locations_for_age_group(self, age_group: str) -> List[DublinLocation]:
        """Get locations appropriate for specific age group"""
        return [location for location in self.dublin_locations.values() 
                if age_group in location.age_appropriateness]

    def validate_cultural_authenticity(self, scenario: DublinCulturalScenario) -> Dict[str, Any]:
        """Validate cultural authenticity of generated scenario"""
        validation = {
            "authentic": True,
            "issues": [],
            "strengths": []
        }
        
        # Check location authenticity
        if scenario.location.name in self.dublin_locations:
            validation["strengths"].append("Location is authentic Dublin landmark")
        else:
            validation["authentic"] = False
            validation["issues"].append("Location not recognized as authentic Dublin location")
        
        # Check cultural elements
        if scenario.cultural_elements:
            validation["strengths"].append("Includes authentic Irish cultural elements")
        else:
            validation["issues"].append("Missing Irish cultural context")
        
        # Check bicultural integration
        if "Chinese" in scenario.bicultural_integration and "Irish" in scenario.bicultural_integration:
            validation["strengths"].append("Balanced bicultural integration")
        else:
            validation["issues"].append("Insufficient bicultural balance")
        
        return validation
