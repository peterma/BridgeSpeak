"""
Character Customization System for Xiao Mei

Provides character customization framework with seasonal outfits, progress-based rewards,
and visual feedback for learning milestones.
"""

import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set
from enum import Enum
import json


class CustomizationCategory(str, Enum):
    """Categories of character customization options"""
    CLOTHING = "clothing"
    ACCESSORIES = "accessories"
    HAIRSTYLE = "hairstyle"
    BACKGROUND = "background"
    SEASONAL = "seasonal"
    SPECIAL_OCCASION = "special_occasion"


class UnlockCondition(str, Enum):
    """Conditions for unlocking customization items"""
    LESSON_COMPLETED = "lesson_completed"
    STREAK_ACHIEVED = "streak_achieved"
    MILESTONE_REACHED = "milestone_reached"
    SEASONAL_EVENT = "seasonal_event"
    PERFECT_SCORE = "perfect_score"
    HELP_OTHER_CHILD = "help_other_child"
    CULTURAL_CELEBRATION = "cultural_celebration"


@dataclass
class CustomizationItem:
    """A single customization item for the character"""
    item_id: str
    name: str
    description: str
    category: CustomizationCategory
    unlock_condition: UnlockCondition
    unlock_requirements: Dict[str, any]
    visual_config: Dict[str, str]
    cultural_significance: Optional[str] = None
    seasonal_availability: Optional[List[str]] = None
    rarity: str = "common"  # common, rare, legendary
    
    def to_dict(self) -> Dict[str, any]:
        """Convert to dictionary for storage and API"""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "description": self.description,
            "category": self.category.value,
            "unlock_condition": self.unlock_condition.value,
            "unlock_requirements": self.unlock_requirements,
            "visual_config": self.visual_config,
            "cultural_significance": self.cultural_significance,
            "seasonal_availability": self.seasonal_availability,
            "rarity": self.rarity
        }


@dataclass
class LearningMilestone:
    """Learning milestone that triggers rewards"""
    milestone_id: str
    name: str
    description: str
    requirements: Dict[str, any]
    reward_items: List[str]  # List of customization item IDs
    celebration_message: str
    cultural_context: Optional[str] = None


@dataclass 
class ChildProgress:
    """Tracks child's learning progress for customization unlocks"""
    child_id: str
    lessons_completed: int = 0
    current_streak: int = 0
    longest_streak: int = 0
    perfect_scores: int = 0
    total_interactions: int = 0
    cultural_events_participated: int = 0
    milestones_achieved: Set[str] = field(default_factory=set)
    unlocked_items: Set[str] = field(default_factory=set)
    equipped_items: Dict[str, str] = field(default_factory=dict)  # category -> item_id
    last_activity_date: float = field(default_factory=time.time)
    
    def to_dict(self) -> Dict[str, any]:
        """Convert to dictionary for storage"""
        return {
            "child_id": self.child_id,
            "lessons_completed": self.lessons_completed,
            "current_streak": self.current_streak,
            "longest_streak": self.longest_streak,
            "perfect_scores": self.perfect_scores,
            "total_interactions": self.total_interactions,
            "cultural_events_participated": self.cultural_events_participated,
            "milestones_achieved": list(self.milestones_achieved),
            "unlocked_items": list(self.unlocked_items),
            "equipped_items": self.equipped_items,
            "last_activity_date": self.last_activity_date
        }


class CharacterCustomizationService:
    """Service for managing character customization and progress-based rewards"""

    def __init__(self):
        self.customization_items = self._initialize_customization_items()
        self.learning_milestones = self._initialize_learning_milestones()
        self.child_progress_store: Dict[str, ChildProgress] = {}

    def _initialize_customization_items(self) -> Dict[str, CustomizationItem]:
        """Initialize the library of customization items"""
        items = {}
        
        # Seasonal Clothing
        items["spring_cardigan"] = CustomizationItem(
            item_id="spring_cardigan",
            name="Spring Shamrock Cardigan",
            description="Light green cardigan with shamrock patterns for Irish spring",
            category=CustomizationCategory.CLOTHING,
            unlock_condition=UnlockCondition.SEASONAL_EVENT,
            unlock_requirements={"season": "spring", "lessons_in_season": 3},
            visual_config={
                "clothing_type": "cardigan",
                "color": "light_green",
                "pattern": "shamrocks",
                "style": "casual"
            },
            cultural_significance="Represents Irish spring traditions and connection to nature",
            seasonal_availability=["spring"],
            rarity="common"
        )
        
        items["summer_gaa_shirt"] = CustomizationItem(
            item_id="summer_gaa_shirt",
            name="Dublin GAA Training Shirt",
            description="Bright blue and white shirt like Dublin GAA team colors",
            category=CustomizationCategory.CLOTHING,
            unlock_condition=UnlockCondition.STREAK_ACHIEVED,
            unlock_requirements={"streak_length": 5, "season": "summer"},
            visual_config={
                "clothing_type": "sports_shirt",
                "color": "dublin_blue",
                "accent_color": "white",
                "pattern": "team_stripes"
            },
            cultural_significance="Celebrates Irish GAA sports culture and teamwork",
            seasonal_availability=["summer"],
            rarity="rare"
        )
        
        items["autumn_wool_sweater"] = CustomizationItem(
            item_id="autumn_wool_sweater",
            name="Cozy Irish Wool Sweater",
            description="Warm orange sweater with traditional Irish cable knit patterns",
            category=CustomizationCategory.CLOTHING,
            unlock_condition=UnlockCondition.MILESTONE_REACHED,
            unlock_requirements={"milestone_id": "autumn_learning_master"},
            visual_config={
                "clothing_type": "sweater",
                "color": "autumn_orange",
                "pattern": "cable_knit",
                "texture": "wool"
            },
            cultural_significance="Traditional Irish craftsmanship and autumn comfort",
            seasonal_availability=["autumn"],
            rarity="rare"
        )
        
        items["winter_christmas_coat"] = CustomizationItem(
            item_id="winter_christmas_coat",
            name="Festive Christmas Coat",
            description="Warm red coat with snowflake patterns for Irish Christmas",
            category=CustomizationCategory.CLOTHING,
            unlock_condition=UnlockCondition.CULTURAL_CELEBRATION,
            unlock_requirements={"celebration": "christmas", "participation": True},
            visual_config={
                "clothing_type": "coat",
                "color": "festive_red",
                "pattern": "snowflakes",
                "style": "winter_formal"
            },
            cultural_significance="Irish Christmas traditions and family warmth",
            seasonal_availability=["winter"],
            rarity="legendary"
        )
        
        # Accessories
        items["chinese_hair_clips"] = CustomizationItem(
            item_id="chinese_hair_clips",
            name="Traditional Chinese Hair Clips",
            description="Beautiful red and gold hair clips with Chinese patterns",
            category=CustomizationCategory.ACCESSORIES,
            unlock_condition=UnlockCondition.LESSON_COMPLETED,
            unlock_requirements={"lessons_count": 1},
            visual_config={
                "accessory_type": "hair_clips",
                "color": "red_gold",
                "pattern": "traditional_chinese",
                "position": "hair_sides"
            },
            cultural_significance="Honors Chinese heritage and traditional beauty",
            rarity="common"
        )
        
        items["trinity_college_pin"] = CustomizationItem(
            item_id="trinity_college_pin",
            name="Trinity College Dublin Pin",
            description="Special pin representing Dublin's famous university",
            category=CustomizationCategory.ACCESSORIES,
            unlock_condition=UnlockCondition.PERFECT_SCORE,
            unlock_requirements={"perfect_scores": 3},
            visual_config={
                "accessory_type": "pin",
                "color": "trinity_blue",
                "design": "college_crest",
                "position": "cardigan_lapel"
            },
            cultural_significance="Represents educational excellence and Dublin pride",
            rarity="rare"
        )
        
        # Hairstyles
        items["chinese_buns"] = CustomizationItem(
            item_id="chinese_buns",
            name="Traditional Chinese Buns",
            description="Elegant hair buns with decorative Chinese hair accessories",
            category=CustomizationCategory.HAIRSTYLE,
            unlock_condition=UnlockCondition.CULTURAL_CELEBRATION,
            unlock_requirements={"celebration": "chinese_new_year", "participation": True},
            visual_config={
                "hairstyle_type": "twin_buns",
                "accessories": "chinese_traditional",
                "color": "natural_black",
                "style": "formal_traditional"
            },
            cultural_significance="Traditional Chinese hairstyle for special occasions",
            rarity="legendary"
        )
        
        # Backgrounds
        items["dublin_zoo_background"] = CustomizationItem(
            item_id="dublin_zoo_background",
            name="Dublin Zoo Adventure",
            description="Colorful background featuring Dublin Zoo with friendly animals",
            category=CustomizationCategory.BACKGROUND,
            unlock_condition=UnlockCondition.STREAK_ACHIEVED,
            unlock_requirements={"streak_length": 7},
            visual_config={
                "background_type": "outdoor_scene",
                "location": "dublin_zoo",
                "elements": ["animals", "trees", "playground"],
                "mood": "cheerful_adventure"
            },
            cultural_significance="Celebrates Dublin landmarks children love",
            rarity="rare"
        )
        
        items["phoenix_park_background"] = CustomizationItem(
            item_id="phoenix_park_background",
            name="Phoenix Park Picnic",
            description="Beautiful park setting with Dublin's Phoenix Park",
            category=CustomizationCategory.BACKGROUND,
            unlock_condition=UnlockCondition.MILESTONE_REACHED,
            unlock_requirements={"milestone_id": "dublin_explorer"},
            visual_config={
                "background_type": "park_scene",
                "location": "phoenix_park",
                "elements": ["grass", "trees", "monument", "picnic_setup"],
                "mood": "peaceful_family"
            },
            cultural_significance="Dublin's largest park, perfect for family activities",
            rarity="rare"
        )
        
        return items

    def _initialize_learning_milestones(self) -> Dict[str, LearningMilestone]:
        """Initialize learning milestones that trigger rewards"""
        return {
            "first_lesson": LearningMilestone(
                milestone_id="first_lesson",
                name="First Steps",
                description="Complete your very first lesson with Xiao Mei",
                requirements={"lessons_completed": 1},
                reward_items=["chinese_hair_clips"],
                celebration_message="你好! Welcome to learning! Here are special Chinese hair clips to celebrate! 很好!"
            ),
            "streak_starter": LearningMilestone(
                milestone_id="streak_starter",
                name="Learning Streak",
                description="Complete 3 lessons in a row",
                requirements={"current_streak": 3},
                reward_items=["spring_cardigan"],
                celebration_message="Brilliant! You're on a learning streak! Here's a beautiful spring cardigan! 太棒了!"
            ),
            "gaa_champion": LearningMilestone(
                milestone_id="gaa_champion",
                name="GAA Team Spirit",
                description="Achieve 5 perfect scores like a GAA champion",
                requirements={"perfect_scores": 5},
                reward_items=["summer_gaa_shirt"],
                celebration_message="Fair play! You're a champion learner! Here's your Dublin GAA shirt! 冠军!"
            ),
            "dublin_explorer": LearningMilestone(
                milestone_id="dublin_explorer",
                name="Dublin Explorer",
                description="Complete 10 lessons about Dublin culture",
                requirements={"lessons_completed": 10, "cultural_focus": "dublin"},
                reward_items=["phoenix_park_background", "trinity_college_pin"],
                celebration_message="Grand! You know Dublin well now! Here are special Dublin rewards! 都柏林专家!"
            ),
            "autumn_learning_master": LearningMilestone(
                milestone_id="autumn_learning_master",
                name="Autumn Learning Master",
                description="Complete 15 lessons during autumn season",
                requirements={"lessons_completed": 15, "season": "autumn"},
                reward_items=["autumn_wool_sweater"],
                celebration_message="Lovely! You're an autumn learning master! Here's a cozy Irish sweater! 秋天大师!"
            )
        }

    def register_child(self, child_id: str) -> ChildProgress:
        """Register a new child for progress tracking"""
        if child_id not in self.child_progress_store:
            progress = ChildProgress(child_id=child_id)
            # Start with basic Chinese accessories
            progress.unlocked_items.add("chinese_hair_clips")
            progress.equipped_items[CustomizationCategory.ACCESSORIES.value] = "chinese_hair_clips"
            self.child_progress_store[child_id] = progress
        return self.child_progress_store[child_id]

    def update_child_progress(self, 
                            child_id: str, 
                            activity_type: str, 
                            **context) -> Dict[str, any]:
        """Update child's progress and check for new unlocks"""
        progress = self.register_child(child_id)
        progress.last_activity_date = time.time()
        progress.total_interactions += 1
        
        # Update progress based on activity type
        newly_unlocked = []
        milestones_achieved = []
        
        if activity_type == "lesson_completed":
            progress.lessons_completed += 1
            progress.current_streak += 1
            progress.longest_streak = max(progress.longest_streak, progress.current_streak)
            
            if context.get("perfect_score", False):
                progress.perfect_scores += 1
                
        elif activity_type == "lesson_failed":
            progress.current_streak = 0
            
        elif activity_type == "cultural_event":
            progress.cultural_events_participated += 1
        
        # Check for milestone achievements
        for milestone_id, milestone in self.learning_milestones.items():
            if milestone_id not in progress.milestones_achieved:
                if self._check_milestone_requirements(progress, milestone, context):
                    progress.milestones_achieved.add(milestone_id)
                    milestones_achieved.append(milestone)
                    
                    # Unlock reward items
                    for item_id in milestone.reward_items:
                        if item_id not in progress.unlocked_items:
                            progress.unlocked_items.add(item_id)
                            newly_unlocked.append(self.customization_items[item_id])
        
        # Check for additional item unlocks
        for item_id, item in self.customization_items.items():
            if item_id not in progress.unlocked_items:
                if self._check_unlock_requirements(progress, item, context):
                    progress.unlocked_items.add(item_id)
                    newly_unlocked.append(item)
        
        return {
            "progress_updated": True,
            "newly_unlocked_items": [item.to_dict() for item in newly_unlocked],
            "milestones_achieved": [
                {
                    "milestone": milestone.name,
                    "celebration_message": milestone.celebration_message,
                    "rewards": milestone.reward_items
                } for milestone in milestones_achieved
            ],
            "current_progress": progress.to_dict()
        }

    def _check_milestone_requirements(self, 
                                   progress: ChildProgress, 
                                   milestone: LearningMilestone,
                                   context: Dict[str, any]) -> bool:
        """Check if milestone requirements are met"""
        requirements = milestone.requirements
        
        if "lessons_completed" in requirements:
            if progress.lessons_completed < requirements["lessons_completed"]:
                return False
                
        if "current_streak" in requirements:
            if progress.current_streak < requirements["current_streak"]:
                return False
                
        if "perfect_scores" in requirements:
            if progress.perfect_scores < requirements["perfect_scores"]:
                return False
                
        if "cultural_focus" in requirements:
            # This would need additional tracking in a real implementation
            if context.get("cultural_focus") != requirements["cultural_focus"]:
                return False
                
        if "season" in requirements:
            current_season = context.get("season", "spring")
            if current_season != requirements["season"]:
                return False
        
        return True

    def _check_unlock_requirements(self, 
                                 progress: ChildProgress, 
                                 item: CustomizationItem,
                                 context: Dict[str, any]) -> bool:
        """Check if item unlock requirements are met"""
        requirements = item.unlock_requirements
        
        if item.unlock_condition == UnlockCondition.LESSON_COMPLETED:
            return progress.lessons_completed >= requirements.get("lessons_count", 1)
            
        elif item.unlock_condition == UnlockCondition.STREAK_ACHIEVED:
            streak_req = requirements.get("streak_length", 3)
            season_req = requirements.get("season")
            if season_req:
                current_season = context.get("season", "spring")
                return (progress.current_streak >= streak_req and 
                       current_season == season_req)
            return progress.current_streak >= streak_req
            
        elif item.unlock_condition == UnlockCondition.PERFECT_SCORE:
            return progress.perfect_scores >= requirements.get("perfect_scores", 1)
            
        elif item.unlock_condition == UnlockCondition.SEASONAL_EVENT:
            current_season = context.get("season", "spring")
            season_req = requirements.get("season")
            lessons_req = requirements.get("lessons_in_season", 1)
            if season_req == current_season:
                # In a real implementation, would track lessons per season
                return progress.lessons_completed >= lessons_req
            return False
            
        elif item.unlock_condition == UnlockCondition.CULTURAL_CELEBRATION:
            celebration = requirements.get("celebration")
            current_celebration = context.get("current_celebration")
            return (celebration == current_celebration and 
                   context.get("participation", False))
        
        return False

    def equip_customization_item(self, 
                               child_id: str, 
                               item_id: str) -> Dict[str, any]:
        """Equip a customization item for the child"""
        progress = self.register_child(child_id)
        
        if item_id not in progress.unlocked_items:
            return {
                "success": False,
                "error": "Item not unlocked",
                "item_id": item_id
            }
        
        if item_id not in self.customization_items:
            return {
                "success": False,
                "error": "Item not found",
                "item_id": item_id
            }
        
        item = self.customization_items[item_id]
        category = item.category.value
        
        # Unequip previous item in same category if any
        old_item_id = progress.equipped_items.get(category)
        
        # Equip new item
        progress.equipped_items[category] = item_id
        
        return {
            "success": True,
            "equipped_item": item.to_dict(),
            "previous_item": old_item_id,
            "category": category,
            "visual_config": item.visual_config
        }

    def get_child_customization_state(self, child_id: str) -> Dict[str, any]:
        """Get complete customization state for a child"""
        progress = self.register_child(child_id)
        
        unlocked_items = {
            item_id: self.customization_items[item_id].to_dict()
            for item_id in progress.unlocked_items
            if item_id in self.customization_items
        }
        
        equipped_items = {
            category: self.customization_items[item_id].to_dict()
            for category, item_id in progress.equipped_items.items()
            if item_id in self.customization_items
        }
        
        return {
            "child_id": child_id,
            "progress": progress.to_dict(),
            "unlocked_items": unlocked_items,
            "equipped_items": equipped_items,
            "available_milestones": {
                milestone_id: {
                    "name": milestone.name,
                    "description": milestone.description,
                    "requirements": milestone.requirements,
                    "achieved": milestone_id in progress.milestones_achieved
                }
                for milestone_id, milestone in self.learning_milestones.items()
            }
        }

    def get_visual_character_config(self, child_id: str) -> Dict[str, any]:
        """Get visual configuration for rendering the customized character"""
        progress = self.register_child(child_id)
        
        visual_config = {
            "base_character": "xiaomei_8_year_old_chinese_girl",
            "customizations": {}
        }
        
        for category, item_id in progress.equipped_items.items():
            if item_id in self.customization_items:
                item = self.customization_items[item_id]
                visual_config["customizations"][category] = item.visual_config
        
        return visual_config

    def get_seasonal_recommendations(self, season: str) -> List[Dict[str, any]]:
        """Get seasonal customization recommendations"""
        seasonal_items = []
        
        for item in self.customization_items.values():
            if (item.seasonal_availability and 
                season in item.seasonal_availability):
                seasonal_items.append({
                    "item": item.to_dict(),
                    "unlock_hint": f"Complete {item.unlock_requirements} to unlock this {season} item!"
                })
        
        return seasonal_items