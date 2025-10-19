"""
Cultural Representation Service for Xiao Mei Character

Provides design specifications and cultural authenticity guidelines for the
Xiao Mei character to ensure appropriate and respectful representation.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum


class CulturalElement(str, Enum):
    """Cultural elements for authentic representation"""
    CHINESE_HERITAGE = "chinese_heritage"
    IRISH_INTEGRATION = "irish_integration"
    AGE_APPROPRIATE = "age_appropriate"


@dataclass
class CharacterAppearance:
    """Visual design specifications for Xiao Mei character"""
    age_appearance: str = "8 years old"
    clothing_style: str = "casual, child-friendly clothing"
    hair_style: str = "shoulder-length black hair with optional colorful hair clips"
    facial_features: str = "friendly smile, bright eyes, approachable expression"
    cultural_markers: List[str] = None
    seasonal_options: List[str] = None

    def __post_init__(self):
        if self.cultural_markers is None:
            self.cultural_markers = [
                "Traditional Chinese elements in accessories (optional)",
                "Modern Irish school uniform elements when appropriate",
                "Bright, child-friendly colors"
            ]
        if self.seasonal_options is None:
            self.seasonal_options = [
                "Spring: Light cardigan, flower hair clips",
                "Summer: Bright t-shirt, sun hat",
                "Autumn: Cozy sweater, leaf-colored accessories",
                "Winter: Warm coat, festive accessories"
            ]


@dataclass
class VoicePattern:
    """Voice and speech pattern specifications"""
    accent: str = "Clear Irish English with subtle Chinese influence"
    pace: str = "Gentle, patient speaking pace suitable for children"
    tone: str = "Warm, encouraging, never harsh or critical"
    bilingual_markers: List[str] = None
    chinese_phrases: Dict[str, str] = None

    def __post_init__(self):
        if self.bilingual_markers is None:
            self.bilingual_markers = [
                "Always Chinese comfort first, then English demonstration",
                "1-second pause between language transitions",
                "Gentle pronunciation emphasis for learning"
            ]
        if self.chinese_phrases is None:
            self.chinese_phrases = {
                "greeting": "你好! (Nǐ hǎo!) - Hello!",
                "encouragement": "好棒! (Hǎo bàng!) - Great job!",
                "comfort": "很好! (Hěn hǎo!) - Very good!",
                "patience": "没关系 (Méi guānxì) - It's okay",
                "celebration": "太棒了! (Tài bàng le!) - Fantastic!"
            }


class CulturalRepresentationService:
    """Service for managing cultural representation guidelines and specifications"""

    def __init__(self):
        self.appearance = CharacterAppearance()
        self.voice = VoicePattern()

    def get_character_appearance_specs(self) -> CharacterAppearance:
        """Return detailed character appearance specifications"""
        return self.appearance

    def get_voice_pattern_specs(self) -> VoicePattern:
        """Return voice and speech pattern specifications"""
        return self.voice

    def get_cultural_authenticity_guidelines(self) -> Dict[str, List[str]]:
        """Return guidelines for maintaining cultural authenticity"""
        return {
            "chinese_heritage_respect": [
                "Use simplified Chinese characters for young learners",
                "Include family values and respect for elders in interactions",
                "Reference Chinese cultural celebrations appropriately",
                "Maintain authentic pronunciation guidance for Chinese phrases"
            ],
            "irish_cultural_integration": [
                "Reference Dublin landmarks children would know (Phoenix Park, Dublin Zoo)",
                "Include Irish holidays and seasonal celebrations",
                "Use Irish English vocabulary and phrases naturally",
                "Show appreciation for Irish culture while maintaining Chinese identity"
            ],
            "age_appropriate_design": [
                "Avoid mature or sophisticated elements",
                "Use bright, cheerful colors and designs",
                "Ensure clothing and accessories are practical for active children",
                "Maintain peer-like appearance rather than authority figure"
            ],
            "trauma_informed_approach": [
                "Never show negative emotions (anger, frustration, disappointment)",
                "Always maintain patient, understanding expressions",
                "Use calming colors and gentle visual elements",
                "Ensure all visual elements feel safe and welcoming"
            ]
        }

    def get_seasonal_customization_options(self) -> Dict[str, Dict[str, str]]:
        """Return seasonal customization options for character progression"""
        return {
            "spring": {
                "clothing": "Light green cardigan with flower patterns",
                "accessories": "Cherry blossom hair clips",
                "background_elements": "Spring flowers, light colors"
            },
            "summer": {
                "clothing": "Bright yellow t-shirt with sun motifs",
                "accessories": "Sun hat with GAA team colors",
                "background_elements": "Sunny day, outdoor activity themes"
            },
            "autumn": {
                "clothing": "Cozy orange sweater with leaf patterns",
                "accessories": "Maple leaf hair clips in autumn colors",
                "background_elements": "Falling leaves, warm colors"
            },
            "winter": {
                "clothing": "Warm red coat with snowflake patterns",
                "accessories": "Winter hat with pom-pom",
                "background_elements": "Gentle snowfall, cozy indoor scenes"
            }
        }

    def validate_cultural_representation(self, character_description: str) -> Dict[str, bool]:
        """Validate a character description against cultural authenticity guidelines"""
        guidelines = self.get_cultural_authenticity_guidelines()
        
        # Simple validation checks
        validation_results = {
            "age_appropriate": any(
                term in character_description.lower() 
                for term in ["child", "young", "8", "friendly", "bright"]
            ),
            "culturally_respectful": any(
                term in character_description.lower()
                for term in ["chinese", "heritage", "authentic", "respectful"]
            ),
            "trauma_informed": not any(
                term in character_description.lower()
                for term in ["angry", "frustrated", "stern", "harsh", "intimidating"]
            ),
            "irish_integrated": any(
                term in character_description.lower()
                for term in ["irish", "dublin", "english", "ireland"]
            )
        }
        
        return validation_results

    def get_character_voice_configuration(self) -> Dict[str, str]:
        """Return technical voice configuration for TTS integration"""
        return {
            "language_primary": "en-IE",  # Irish English
            "language_secondary": "zh-CN",  # Simplified Chinese
            "pace": "0.9",  # Slightly slower for clarity
            "emphasis": "gentle",
            "volume": "normal",
            "emotional_tone": "warm_encouraging"
        }

    def get_irish_cultural_integration(self) -> Dict[str, Dict[str, any]]:
        """Get Irish cultural integration elements for balanced cultural bridge"""
        return {
            "dublin_landmarks": {
                "child_friendly_locations": [
                    "Dublin Zoo - 'We could visit the animals like in Dublin Zoo!'",
                    "Phoenix Park - 'As big as Phoenix Park where we play!'",
                    "Temple Bar - 'Like the colorful Temple Bar area!'",
                    "Trinity College - 'Like the beautiful Trinity College!'",
                    "Dublin Castle - 'Old like Dublin Castle!'"
                ],
                "usage_context": "Use to make comparisons and create familiarity",
                "pronunciation_guide": {
                    "Dublin": "DUB-lin",
                    "Phoenix": "FEE-nix",
                    "Temple Bar": "TEM-pel BAR"
                }
            },
            "gaa_sports_integration": {
                "sports_references": [
                    "Hurling - 'Fast like hurling!'",
                    "Gaelic football - 'Team work like GAA!'",
                    "Camogie - 'Strong like camogie players!'",
                    "County colors - 'Blue and white like Dublin colors!'"
                ],
                "positive_associations": [
                    "Teamwork and cooperation",
                    "Practice makes perfect",
                    "Supporting each other",
                    "Celebrating achievements"
                ],
                "usage_examples": [
                    "When child succeeds: 'Maith thú! Good job, like scoring in GAA!'",
                    "When encouraging: 'Practice like GAA players do!'",
                    "When celebrating: 'Team celebration like after winning!'"
                ]
            },
            "irish_holidays_celebrations": {
                "st_patricks_day": {
                    "phrases": ["Happy St. Patrick's Day! 圣帕特里克节快乐!", "Green like shamrocks!"],
                    "cultural_bridge": "Irish pride like Chinese New Year pride",
                    "learning_opportunities": ["Green colors", "Irish music", "Celebration traditions"]
                },
                "christmas": {
                    "phrases": ["Nollaig Shona! 圣诞快乐!", "Christmas lights like festival lights!"],
                    "cultural_bridge": "Family gathering like Chinese traditions",
                    "learning_opportunities": ["Winter traditions", "Family time", "Gift giving"]
                },
                "easter": {
                    "phrases": ["Happy Easter! 复活节快乐!", "Spring flowers blooming!"],
                    "cultural_bridge": "New beginnings like Spring Festival",
                    "learning_opportunities": ["Spring themes", "New growth", "Fresh starts"]
                }
            },
            "irish_english_vocabulary": {
                "common_irish_expressions": [
                    "Brilliant! (instead of great) - 太棒了!",
                    "Fair play! (well done) - 做得好!",
                    "Sound! (good/okay) - 好的!",
                    "Grand! (fine/good) - 很好!",
                    "Lovely! (nice) - 很棒!"
                ],
                "pronunciation_emphasis": [
                    "Soft 'th' sounds",
                    "Rolled 'r' in some words",
                    "Rising intonation for questions"
                ],
                "cultural_context": "Use naturally in conversation to model Irish English"
            },
            "irish_cultural_values": {
                "storytelling_tradition": [
                    "Stories teach us lessons",
                    "Every person has stories to share",
                    "Listening to others' stories shows respect"
                ],
                "hospitality_cead_mile_failte": [
                    "Céad míle fáilte - hundred thousand welcomes",
                    "Everyone is welcome here",
                    "Sharing and caring for others"
                ],
                "community_connection": [
                    "Neighbors helping neighbors",
                    "Strong community bonds",
                    "Working together for common goals"
                ]
            }
        }

    def create_balanced_cultural_bridge(self, chinese_concept: str, irish_context: str) -> str:
        """Create balanced cultural bridge statements connecting Chinese and Irish elements"""
        bridge_templates = {
            "family_values": "Family is important in both Chinese and Irish culture - 家庭很重要",
            "respect_for_elders": "We respect our elders, just like Irish grannies and Chinese 奶奶",
            "celebration_traditions": "Chinese festivals and Irish celebrations both bring families together",
            "food_sharing": "Sharing food shows love - dim sum and Irish stew both made with care",
            "music_and_dance": "Chinese music and Irish music both tell stories of our people",
            "education_values": "Both cultures value learning and growing together",
            "storytelling": "Chinese stories and Irish stories both teach us important lessons"
        }
        
        if chinese_concept in bridge_templates:
            return bridge_templates[chinese_concept]
        
        # Generic bridge format
        return f"In China we have {chinese_concept}, and in Ireland you have {irish_context} - both are wonderful!"

    def get_seasonal_irish_cultural_elements(self) -> Dict[str, Dict[str, str]]:
        """Get seasonal Irish cultural elements for character customization"""
        return {
            "spring": {
                "cultural_references": "Daffodils blooming like in Irish countryside",
                "irish_phrases": "Tír gan teanga, tír gan anam (Land without language, land without soul)",
                "seasonal_activities": "Walking in Irish spring rain (soft day)",
                "clothing_elements": "Light green cardigan like spring shamrocks"
            },
            "summer": {
                "cultural_references": "Long Irish summer days until 10pm",
                "irish_phrases": "Ar scáth a chéile a mhaireann na daoine (We live in each other's shelter)",
                "seasonal_activities": "GAA matches on summer afternoons",
                "clothing_elements": "Bright colors like Irish summer festivals"
            },
            "autumn": {
                "cultural_references": "Golden leaves like Irish autumn forests",
                "irish_phrases": "Mol an óige agus tiocfaidh sí (Praise the young and they will flourish)",
                "seasonal_activities": "Back to school like Irish children",
                "clothing_elements": "Cozy sweater like Irish wool"
            },
            "winter": {
                "cultural_references": "Cozy by the fire like Irish winters",
                "irish_phrases": "Nollaig Shona duit (Happy Christmas to you)",
                "seasonal_activities": "Christmas preparations and storytelling",
                "clothing_elements": "Warm coat against Irish winter wind"
            }
        }

    def validate_irish_cultural_sensitivity(self, content: str) -> Dict[str, bool]:
        """Validate content for Irish cultural sensitivity and appropriateness"""
        validation = {
            "culturally_appropriate": True,
            "avoids_stereotypes": True,
            "respectful_references": True,
            "educational_value": True,
            "issues": []
        }
        
        content_lower = content.lower()
        
        # Check for common stereotypes to avoid
        problematic_terms = [
            "leprechaun", "pot of gold", "fighting irish", 
            "drunk", "potato", "ira", "troubles"
        ]
        
        for term in problematic_terms:
            if term in content_lower:
                validation["avoids_stereotypes"] = False
                validation["issues"].append(f"Contains potentially stereotypical reference: {term}")
        
        # Check for positive cultural elements
        positive_elements = [
            "gaa", "dublin", "irish music", "storytelling", "community",
            "céad míle fáilte", "family", "education", "craic"
        ]
        
        has_positive_elements = any(element in content_lower for element in positive_elements)
        if not has_positive_elements and len(content) > 50:  # Only for longer content
            validation["educational_value"] = False
            validation["issues"].append("Could include more positive Irish cultural references")
        
        # Update overall appropriateness
        validation["culturally_appropriate"] = (
            validation["avoids_stereotypes"] and 
            validation["respectful_references"]
        )
        
        return validation