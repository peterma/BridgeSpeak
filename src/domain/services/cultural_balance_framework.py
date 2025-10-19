"""
Cultural Balance Framework Service

Provides balanced cultural integration that maintains Chinese heritage pride
while encouraging Irish cultural integration. Ensures authentic representation
of both cultures without pressure or cultural hierarchy.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from enum import Enum
from .cultural_representation import CulturalRepresentationService


class CulturalBridgeType(str, Enum):
    """Types of cultural bridges for bicultural integration"""
    FAMILY_VALUES = "family_values"
    EDUCATION_LEARNING = "education_learning"
    CELEBRATION_TRADITIONS = "celebration_traditions"
    FOOD_SHARING = "food_sharing"
    MUSIC_DANCE = "music_dance"
    STORYTELLING = "storytelling"
    COMMUNITY_SPIRIT = "community_spirit"
    RESPECT_ELDERS = "respect_elders"


@dataclass
class ChineseHeritageElements:
    """Chinese heritage elements for cultural pride maintenance"""
    family_values: List[str] = field(default_factory=lambda: [
        "Family is the foundation of Chinese culture - 家庭是中华文化的根基",
        "Respect for parents and elders - 尊敬父母和长辈",
        "Filial piety and family duty - 孝道和家庭责任",
        "Multi-generational family living - 多代同堂的家庭生活",
        "Family support and unity - 家庭支持和团结"
    ])
    
    education_values: List[str] = field(default_factory=lambda: [
        "Education is highly valued in Chinese culture - 教育在中华文化中备受重视",
        "Hard work and perseverance in learning - 学习中的努力和坚持",
        "Respect for teachers and knowledge - 尊敬老师和知识",
        "Academic achievement and excellence - 学术成就和卓越",
        "Lifelong learning tradition - 终身学习的传统"
    ])
    
    celebration_traditions: List[str] = field(default_factory=lambda: [
        "Chinese New Year - the most important family celebration - 春节是最重要的家庭庆祝",
        "Mid-Autumn Festival - family reunion and mooncakes - 中秋节家庭团圆和月饼",
        "Dragon Boat Festival - cultural heritage and family time - 端午节文化遗产和家庭时光",
        "Lantern Festival - community celebration and family fun - 元宵节社区庆祝和家庭乐趣",
        "Qingming Festival - honoring ancestors and family history - 清明节纪念祖先和家族历史"
    ])
    
    food_culture: List[str] = field(default_factory=lambda: [
        "Chinese food brings families together - 中餐让家庭团聚",
        "Sharing meals shows love and care - 分享餐食表达爱和关怀",
        "Traditional Chinese cooking methods - 传统中式烹饪方法",
        "Food as medicine and wellness - 食物即药物和健康",
        "Regional Chinese cuisine diversity - 中国地方菜系的多样性"
    ])
    
    cultural_identity: List[str] = field(default_factory=lambda: [
        "Chinese language and characters - 中文和汉字",
        "Traditional Chinese arts and crafts - 传统中国艺术和手工艺",
        "Chinese philosophy and wisdom - 中国哲学和智慧",
        "Chinese history and heritage - 中国历史和文化遗产",
        "Chinese values and ethics - 中国价值观和道德"
    ])


@dataclass
class IrishIntegrationElements:
    """Irish integration elements for cultural bridge building"""
    irish_hospitality: List[str] = field(default_factory=lambda: [
        "Céad míle fáilte - a hundred thousand welcomes",
        "Irish people are known for their friendliness and warmth",
        "Irish hospitality makes everyone feel welcome",
        "Irish community spirit and neighborly care",
        "Irish storytelling tradition brings people together"
    ])
    
    irish_family_values: List[str] = field(default_factory=lambda: [
        "Irish families are close-knit and supportive",
        "Irish grandparents play important roles in family life",
        "Irish family gatherings and celebrations",
        "Irish respect for family traditions and heritage",
        "Irish community support for families"
    ])
    
    irish_education: List[str] = field(default_factory=lambda: [
        "Irish education system values creativity and critical thinking",
        "Irish schools encourage individual expression and learning",
        "Irish teachers are supportive and encouraging",
        "Irish education includes cultural and artistic development",
        "Irish learning environment is inclusive and welcoming"
    ])
    
    irish_celebrations: List[str] = field(default_factory=lambda: [
        "St. Patrick's Day celebrates Irish culture and identity",
        "Irish Christmas traditions focus on family and community",
        "Irish Halloween originated in Celtic traditions",
        "Irish music and dance bring communities together",
        "Irish festivals celebrate creativity and community spirit"
    ])


@dataclass
class BalancedCulturalScenario:
    """Result of balanced cultural integration"""
    dublin_context: str
    chinese_heritage_pride: List[str]
    cultural_bridge_opportunities: List[str]
    authentic_representation: bool
    integration_encouragement: str
    heritage_celebration: str


class CulturalBalanceFramework:
    """Framework for balanced Chinese-Irish cultural integration"""

    def __init__(self, cultural_service: Optional[CulturalRepresentationService] = None):
        self.cultural_service = cultural_service or CulturalRepresentationService()
        self.chinese_heritage = ChineseHeritageElements()
        self.irish_integration = IrishIntegrationElements()
        self.cultural_bridges = self._initialize_cultural_bridges()

    def _initialize_cultural_bridges(self) -> Dict[CulturalBridgeType, Dict[str, Any]]:
        """Initialize cultural bridge templates for bicultural integration"""
        return {
            CulturalBridgeType.FAMILY_VALUES: {
                "chinese_element": "Chinese families value multi-generational living and filial piety",
                "irish_element": "Irish families are close-knit with strong community support",
                "bridge_statement": "Both Chinese and Irish cultures value strong family bonds and support",
                "integration_opportunity": "Chinese children can experience Irish family warmth while maintaining Chinese family values",
                "heritage_pride": "Your Chinese family values are wonderful and can be shared with Irish friends"
            },
            CulturalBridgeType.EDUCATION_LEARNING: {
                "chinese_element": "Chinese culture highly values education and academic achievement",
                "irish_element": "Irish education encourages creativity, critical thinking, and individual expression",
                "bridge_statement": "Both cultures value learning, but in different ways - Chinese focus on discipline, Irish on creativity",
                "integration_opportunity": "Chinese children can combine Chinese study discipline with Irish creative learning",
                "heritage_pride": "Your Chinese approach to learning is valuable and can enhance Irish education"
            },
            CulturalBridgeType.CELEBRATION_TRADITIONS: {
                "chinese_element": "Chinese festivals like New Year and Mid-Autumn Festival bring families together",
                "irish_element": "Irish celebrations like St. Patrick's Day and Christmas focus on community and family",
                "bridge_statement": "Both cultures celebrate with family and community, showing shared values of togetherness",
                "integration_opportunity": "Chinese children can participate in Irish celebrations while sharing Chinese traditions",
                "heritage_pride": "Your Chinese festivals are beautiful and can be shared with Irish friends"
            },
            CulturalBridgeType.FOOD_SHARING: {
                "chinese_element": "Chinese food culture emphasizes sharing meals and family togetherness",
                "irish_element": "Irish food traditions focus on comfort, hospitality, and community meals",
                "bridge_statement": "Both cultures use food to show love, care, and bring people together",
                "integration_opportunity": "Chinese children can enjoy Irish comfort food while sharing Chinese culinary traditions",
                "heritage_pride": "Chinese food culture is rich and can be appreciated by Irish friends"
            },
            CulturalBridgeType.MUSIC_DANCE: {
                "chinese_element": "Chinese traditional music and dance tell stories of Chinese culture and history",
                "irish_element": "Irish music and dance celebrate Irish identity and bring communities together",
                "bridge_statement": "Both cultures use music and dance to express cultural identity and tell stories",
                "integration_opportunity": "Chinese children can enjoy Irish music while sharing Chinese artistic traditions",
                "heritage_pride": "Chinese music and dance are beautiful expressions of Chinese culture"
            },
            CulturalBridgeType.STORYTELLING: {
                "chinese_element": "Chinese storytelling tradition includes ancient legends, folktales, and family stories",
                "irish_element": "Irish storytelling tradition is central to Irish culture and community bonding",
                "bridge_statement": "Both cultures have rich storytelling traditions that teach values and connect generations",
                "integration_opportunity": "Chinese children can share Chinese stories while learning Irish tales",
                "heritage_pride": "Chinese stories and legends are valuable cultural treasures to share"
            },
            CulturalBridgeType.COMMUNITY_SPIRIT: {
                "chinese_element": "Chinese communities support each other and value collective harmony",
                "irish_element": "Irish communities are known for neighborly care and community support",
                "bridge_statement": "Both cultures value community support and helping others",
                "integration_opportunity": "Chinese children can experience Irish community warmth while contributing Chinese values",
                "heritage_pride": "Chinese community values of harmony and support are appreciated in Ireland"
            },
            CulturalBridgeType.RESPECT_ELDERS: {
                "chinese_element": "Chinese culture emphasizes deep respect for elders and their wisdom",
                "irish_element": "Irish culture values elders and their role in family and community life",
                "bridge_statement": "Both cultures show respect for elders, though in different ways",
                "integration_opportunity": "Chinese children can show Chinese respect while learning Irish elder interactions",
                "heritage_pride": "Chinese respect for elders is a beautiful tradition to maintain"
            }
        }

    def balance_cultural_content(self, dublin_scenario: str, child_profile: Dict[str, Any]) -> BalancedCulturalScenario:
        """Create balanced cultural integration for Dublin scenario"""
        
        # Get relevant Chinese heritage elements
        heritage_elements = self._get_relevant_heritage_elements(dublin_scenario)
        
        # Create cultural bridge opportunities
        bridge_opportunities = self._create_bridge_opportunities(dublin_scenario)
        
        # Generate integration encouragement
        integration_encouragement = self._generate_integration_encouragement(dublin_scenario)
        
        # Generate heritage celebration
        heritage_celebration = self._generate_heritage_celebration(heritage_elements)
        
        return BalancedCulturalScenario(
            dublin_context=dublin_scenario,
            chinese_heritage_pride=heritage_elements,
            cultural_bridge_opportunities=bridge_opportunities,
            authentic_representation=True,
            integration_encouragement=integration_encouragement,
            heritage_celebration=heritage_celebration
        )

    def _get_relevant_heritage_elements(self, dublin_scenario: str) -> List[str]:
        """Get relevant Chinese heritage elements for the scenario"""
        scenario_lower = dublin_scenario.lower()
        relevant_elements = []
        
        # Family-related scenarios
        if any(word in scenario_lower for word in ["family", "home", "parents", "grandparents"]):
            relevant_elements.extend(self.chinese_heritage.family_values[:2])
        
        # Education-related scenarios
        if any(word in scenario_lower for word in ["school", "learning", "teacher", "study"]):
            relevant_elements.extend(self.chinese_heritage.education_values[:2])
        
        # Celebration-related scenarios
        if any(word in scenario_lower for word in ["celebration", "festival", "holiday", "party"]):
            relevant_elements.extend(self.chinese_heritage.celebration_traditions[:2])
        
        # Food-related scenarios
        if any(word in scenario_lower for word in ["food", "meal", "eating", "cooking"]):
            relevant_elements.extend(self.chinese_heritage.food_culture[:2])
        
        # Default to general cultural identity if no specific match
        if not relevant_elements:
            relevant_elements.extend(self.chinese_heritage.cultural_identity[:2])
        
        return relevant_elements

    def _create_bridge_opportunities(self, dublin_scenario: str) -> List[str]:
        """Create cultural bridge opportunities for the scenario"""
        scenario_lower = dublin_scenario.lower()
        bridges = []
        
        # Identify relevant bridge types based on scenario content
        if any(word in scenario_lower for word in ["family", "home", "parents"]):
            bridge = self.cultural_bridges[CulturalBridgeType.FAMILY_VALUES]
            bridges.append(bridge["bridge_statement"])
            bridges.append(bridge["integration_opportunity"])
        
        if any(word in scenario_lower for word in ["school", "learning", "education"]):
            bridge = self.cultural_bridges[CulturalBridgeType.EDUCATION_LEARNING]
            bridges.append(bridge["bridge_statement"])
            bridges.append(bridge["integration_opportunity"])
        
        if any(word in scenario_lower for word in ["celebration", "festival", "holiday"]):
            bridge = self.cultural_bridges[CulturalBridgeType.CELEBRATION_TRADITIONS]
            bridges.append(bridge["bridge_statement"])
            bridges.append(bridge["integration_opportunity"])
        
        if any(word in scenario_lower for word in ["food", "meal", "eating"]):
            bridge = self.cultural_bridges[CulturalBridgeType.FOOD_SHARING]
            bridges.append(bridge["bridge_statement"])
            bridges.append(bridge["integration_opportunity"])
        
        # Always include community spirit bridge
        community_bridge = self.cultural_bridges[CulturalBridgeType.COMMUNITY_SPIRIT]
        bridges.append(community_bridge["bridge_statement"])
        
        return bridges

    def _generate_integration_encouragement(self, dublin_scenario: str) -> str:
        """Generate encouragement for Irish cultural integration"""
        return (
            "You can enjoy Irish culture while keeping your Chinese heritage close to your heart. "
            "Irish people are welcoming and will appreciate learning about Chinese traditions from you. "
            "Being bicultural means you have the best of both worlds - Chinese wisdom and Irish warmth!"
        )

    def _generate_heritage_celebration(self, heritage_elements: List[str]) -> str:
        """Generate celebration of Chinese heritage"""
        if heritage_elements:
            return (
                f"Remember, your Chinese heritage is something to be proud of! "
                f"{heritage_elements[0]} This is part of who you are and makes you special. "
                "You can share these beautiful Chinese values with your Irish friends."
            )
        else:
            return (
                "Your Chinese heritage is a beautiful part of who you are. "
                "Chinese culture has so much to offer - wisdom, traditions, and values that are valuable anywhere in the world. "
                "Be proud of your Chinese identity while also enjoying Irish culture!"
            )

    def create_cultural_sharing_opportunity(self, chinese_concept: str, irish_context: str) -> str:
        """Create opportunity for cultural sharing between Chinese and Irish elements"""
        return (
            f"You can share about {chinese_concept} with your Irish friends, "
            f"and they can teach you about {irish_context}. "
            "This is how we learn from each other and build understanding between cultures!"
        )

    def validate_cultural_balance(self, scenario: BalancedCulturalScenario) -> Dict[str, Any]:
        """Validate that cultural balance is maintained"""
        validation = {
            "balanced": True,
            "heritage_preserved": True,
            "integration_encouraged": True,
            "issues": [],
            "strengths": []
        }
        
        # Check heritage preservation
        if not scenario.chinese_heritage_pride:
            validation["heritage_preserved"] = False
            validation["issues"].append("Missing Chinese heritage pride elements")
        else:
            validation["strengths"].append("Chinese heritage pride is maintained")
        
        # Check integration encouragement
        if not scenario.cultural_bridge_opportunities:
            validation["integration_encouraged"] = False
            validation["issues"].append("Missing cultural bridge opportunities")
        else:
            validation["strengths"].append("Cultural integration is encouraged")
        
        # Check for authentic representation
        if not scenario.authentic_representation:
            validation["balanced"] = False
            validation["issues"].append("Cultural representation may not be authentic")
        else:
            validation["strengths"].append("Authentic cultural representation maintained")
        
        # Check for pressure or hierarchy
        content = f"{scenario.integration_encouragement} {scenario.heritage_celebration}"
        if any(word in content.lower() for word in ["must", "should", "better", "superior"]):
            validation["balanced"] = False
            validation["issues"].append("Content may create cultural pressure or hierarchy")
        
        return validation

    def get_cultural_bridge_statement(self, bridge_type: CulturalBridgeType) -> str:
        """Get cultural bridge statement for specific bridge type"""
        bridge = self.cultural_bridges.get(bridge_type)
        if bridge:
            return bridge["bridge_statement"]
        return "Both Chinese and Irish cultures have valuable traditions and values."

    def get_integration_opportunity(self, bridge_type: CulturalBridgeType) -> str:
        """Get integration opportunity for specific bridge type"""
        bridge = self.cultural_bridges.get(bridge_type)
        if bridge:
            return bridge["integration_opportunity"]
        return "You can enjoy both Chinese and Irish cultural elements."

    def get_heritage_pride_statement(self, bridge_type: CulturalBridgeType) -> str:
        """Get heritage pride statement for specific bridge type"""
        bridge = self.cultural_bridges.get(bridge_type)
        if bridge:
            return bridge["heritage_pride"]
        return "Your Chinese heritage is valuable and something to be proud of."
