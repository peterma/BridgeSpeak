"""
Parent Dashboard Service for Trauma-Informed Sensitivity Controls

Provides parent-controlled sensitivity settings for adjusting platform behavior
based on child's anxiety levels and learning needs.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
import time


class SensitivityLevel(str, Enum):
    """Sensitivity levels for child interaction"""
    EXTRA_PATIENT = "extra_patient"  # For highly anxious children
    STANDARD = "standard"            # Default trauma-informed approach
    RESPONSIVE = "responsive"        # For confident children


class EncouragementIntensity(str, Enum):
    """Intensity levels for encouragement"""
    GENTLE = "gentle"        # Subtle, calming encouragement
    MODERATE = "moderate"    # Balanced encouragement
    ENTHUSIASTIC = "enthusiastic"  # More expressive encouragement


@dataclass
class SensitivitySettings:
    """Parent-controlled sensitivity settings for their child"""
    child_id: str
    interaction_pacing: SensitivityLevel = SensitivityLevel.STANDARD
    encouragement_frequency: int = 45  # seconds between gentle prompts
    celebration_intensity: EncouragementIntensity = EncouragementIntensity.MODERATE
    exit_reminder_frequency: int = 180  # seconds between break reminders
    cultural_comfort_emphasis: bool = True  # prioritize Chinese comfort phase
    anxiety_override: bool = False  # special settings for highly anxious children
    parent_notes: Optional[str] = None
    last_updated: float = 0.0
    
    def __post_init__(self):
        if self.last_updated == 0.0:
            self.last_updated = time.time()
    
    def apply_for_anxious_child(self):
        """Apply settings optimized for highly anxious children"""
        self.interaction_pacing = SensitivityLevel.EXTRA_PATIENT
        self.encouragement_frequency = 60  # Longer intervals
        self.celebration_intensity = EncouragementIntensity.GENTLE
        self.exit_reminder_frequency = 120  # More frequent break reminders
        self.anxiety_override = True
        self.last_updated = time.time()
    
    def apply_for_confident_child(self):
        """Apply settings for more confident children"""
        self.interaction_pacing = SensitivityLevel.RESPONSIVE
        self.encouragement_frequency = 30  # More frequent encouragement
        self.celebration_intensity = EncouragementIntensity.ENTHUSIASTIC
        self.exit_reminder_frequency = 300  # Less frequent break reminders
        self.anxiety_override = False
        self.last_updated = time.time()


class ParentDashboardService:
    """Service for managing parent-controlled sensitivity settings"""
    
    def __init__(self):
        self.child_settings: Dict[str, SensitivitySettings] = {}
        self.parent_sessions: Dict[str, Dict[str, Any]] = {}  # parent_id -> session data
    
    def create_sensitivity_settings(self, child_id: str, parent_id: str) -> SensitivitySettings:
        """Create default sensitivity settings for a child"""
        settings = SensitivitySettings(child_id=child_id)
        self.child_settings[child_id] = settings
        
        # Initialize parent session if needed
        if parent_id not in self.parent_sessions:
            self.parent_sessions[parent_id] = {
                "children": [],
                "last_login": time.time(),
                "preferences": {}
            }
        
        if child_id not in self.parent_sessions[parent_id]["children"]:
            self.parent_sessions[parent_id]["children"].append(child_id)
        
        return settings
    
    def get_sensitivity_settings(self, child_id: str) -> Optional[SensitivitySettings]:
        """Get sensitivity settings for a child"""
        return self.child_settings.get(child_id)
    
    def update_sensitivity_settings(self, child_id: str, **updates) -> bool:
        """Update sensitivity settings for a child"""
        if child_id not in self.child_settings:
            return False
        
        settings = self.child_settings[child_id]
        
        # Update allowed fields
        allowed_fields = {
            'interaction_pacing', 'encouragement_frequency', 'celebration_intensity',
            'exit_reminder_frequency', 'cultural_comfort_emphasis', 'anxiety_override',
            'parent_notes'
        }
        
        for field, value in updates.items():
            if field in allowed_fields and hasattr(settings, field):
                setattr(settings, field, value)
        
        settings.last_updated = time.time()
        return True
    
    def apply_anxiety_override(self, child_id: str) -> bool:
        """Apply anxiety-specific settings for a child"""
        if child_id not in self.child_settings:
            return False
        
        self.child_settings[child_id].apply_for_anxious_child()
        return True
    
    def apply_confidence_settings(self, child_id: str) -> bool:
        """Apply confidence-optimized settings for a child"""
        if child_id not in self.child_settings:
            return False
        
        self.child_settings[child_id].apply_for_confident_child()
        return True
    
    def get_parent_dashboard_data(self, parent_id: str) -> Dict[str, Any]:
        """Get dashboard data for a parent"""
        if parent_id not in self.parent_sessions:
            return {"error": "Parent not found"}
        
        parent_data = self.parent_sessions[parent_id]
        children_data = []
        
        for child_id in parent_data["children"]:
            settings = self.child_settings.get(child_id)
            if settings:
                children_data.append({
                    "child_id": child_id,
                    "sensitivity_level": settings.interaction_pacing.value,
                    "encouragement_frequency": settings.encouragement_frequency,
                    "celebration_intensity": settings.celebration_intensity.value,
                    "anxiety_override": settings.anxiety_override,
                    "last_updated": settings.last_updated,
                    "parent_notes": settings.parent_notes
                })
        
        return {
            "parent_id": parent_id,
            "children": children_data,
            "last_login": parent_data["last_login"],
            "total_children": len(children_data)
        }
    
    def get_sensitivity_recommendations(self, child_id: str) -> Dict[str, Any]:
        """Get sensitivity recommendations based on child's interaction patterns"""
        settings = self.child_settings.get(child_id)
        if not settings:
            return {"error": "Child not found"}
        
        recommendations = {
            "current_level": settings.interaction_pacing.value,
            "recommendations": []
        }
        
        # Generate recommendations based on current settings
        if settings.anxiety_override:
            recommendations["recommendations"].append({
                "type": "anxiety_support",
                "message": "Anxiety-specific settings are active. Consider gradual reduction as child gains confidence.",
                "suggested_action": "Monitor child's comfort level and adjust pacing gradually"
            })
        
        if settings.encouragement_frequency > 60:
            recommendations["recommendations"].append({
                "type": "encouragement_timing",
                "message": "Long encouragement intervals may help reduce pressure for anxious children.",
                "suggested_action": "Maintain current timing or increase if child shows signs of pressure"
            })
        
        if settings.celebration_intensity == EncouragementIntensity.GENTLE:
            recommendations["recommendations"].append({
                "type": "celebration_level",
                "message": "Gentle celebration helps avoid overwhelming sensitive children.",
                "suggested_action": "Consider increasing intensity as child becomes more comfortable"
            })
        
        return recommendations
    
    def validate_settings(self, child_id: str) -> Dict[str, Any]:
        """Validate that settings are appropriate for trauma-informed design"""
        settings = self.child_settings.get(child_id)
        if not settings:
            return {"valid": False, "error": "Child not found"}
        
        validation_results = {
            "valid": True,
            "warnings": [],
            "trauma_informed_compliant": True
        }
        
        # Check trauma-informed compliance
        if settings.encouragement_frequency < 30:
            validation_results["warnings"].append("Very frequent encouragement may create pressure")
            validation_results["trauma_informed_compliant"] = False
        
        if settings.exit_reminder_frequency < 60:
            validation_results["warnings"].append("Frequent exit reminders may create anxiety")
            validation_results["trauma_informed_compliant"] = False
        
        if not settings.cultural_comfort_emphasis:
            validation_results["warnings"].append("Cultural comfort emphasis is recommended for trauma-informed design")
        
        return validation_results
    
    def get_usage_statistics(self, parent_id: str) -> Dict[str, Any]:
        """Get usage statistics for parent dashboard"""
        if parent_id not in self.parent_sessions:
            return {"error": "Parent not found"}
        
        parent_data = self.parent_sessions[parent_id]
        total_children = len(parent_data["children"])
        
        # Count settings by type
        sensitivity_counts = {"extra_patient": 0, "standard": 0, "responsive": 0}
        anxiety_overrides = 0
        
        for child_id in parent_data["children"]:
            settings = self.child_settings.get(child_id)
            if settings:
                sensitivity_counts[settings.interaction_pacing.value] += 1
                if settings.anxiety_override:
                    anxiety_overrides += 1
        
        return {
            "parent_id": parent_id,
            "total_children": total_children,
            "sensitivity_distribution": sensitivity_counts,
            "anxiety_overrides": anxiety_overrides,
            "last_login": parent_data["last_login"],
            "dashboard_usage": "active" if time.time() - parent_data["last_login"] < 86400 else "inactive"
        }
