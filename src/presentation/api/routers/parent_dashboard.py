"""
Parent Dashboard API Router

Provides REST endpoints for parent-controlled sensitivity settings and dashboard functionality.
Implements trauma-informed parent controls for Story 1.4.
"""

from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
import time

from src.domain.services.parent_dashboard import ParentDashboardService, SensitivitySettings
from src.infrastructure.config.dependencies import get_settings

router = APIRouter(prefix="/api/v1", tags=["parent-dashboard"])


# Pydantic models for API requests/responses
class SensitivitySettingsRequest(BaseModel):
    interaction_pacing: str = "extra_patient"  # extra_patient, standard, responsive
    encouragement_frequency: int = 45  # seconds between gentle prompts
    celebration_intensity: str = "gentle"  # gentle, moderate, enthusiastic
    exit_reminder_frequency: int = 180  # seconds between break reminders
    cultural_comfort_emphasis: bool = True
    anxiety_override: bool = False
    parent_notes: Optional[str] = None


class SensitivitySettingsResponse(BaseModel):
    child_id: str
    interaction_pacing: str
    encouragement_frequency: int
    celebration_intensity: str
    exit_reminder_frequency: int
    cultural_comfort_emphasis: bool
    anxiety_override: bool
    parent_notes: Optional[str]
    last_updated: float


class ChildDashboardData(BaseModel):
    child_id: str
    sensitivity_level: str
    encouragement_frequency: int
    celebration_intensity: str
    anxiety_override: bool
    last_updated: float
    parent_notes: Optional[str]


class ParentDashboardResponse(BaseModel):
    parent_id: str
    children: List[ChildDashboardData]
    last_login: float
    total_children: int


class SensitivityRecommendationsResponse(BaseModel):
    child_id: str
    recommended_settings: Dict[str, Any]
    reasoning: str
    confidence_score: float


# Service instance (in production, this would be injected via DI)
_parent_dashboard_service = ParentDashboardService()


@router.get("/parents/{parent_id}/dashboard", response_model=ParentDashboardResponse)
async def get_parent_dashboard(parent_id: str) -> ParentDashboardResponse:
    """
    Get parent dashboard data including all children and their sensitivity settings.
    
    This endpoint provides the parent with an overview of all their children's
    trauma-informed sensitivity settings and allows them to manage these settings.
    """
    try:
        dashboard_data = _parent_dashboard_service.get_parent_dashboard_data(parent_id)
        
        if "error" in dashboard_data:
            raise HTTPException(status_code=404, detail=dashboard_data["error"])
        
        # Convert to response model
        children_data = []
        for child_data in dashboard_data["children"]:
            children_data.append(ChildDashboardData(**child_data))
        
        return ParentDashboardResponse(
            parent_id=dashboard_data["parent_id"],
            children=children_data,
            last_login=dashboard_data["last_login"],
            total_children=dashboard_data["total_children"]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving parent dashboard: {str(e)}")


@router.get("/children/{child_id}/sensitivity-settings", response_model=SensitivitySettingsResponse)
async def get_child_sensitivity_settings(child_id: str) -> SensitivitySettingsResponse:
    """
    Get sensitivity settings for a specific child.
    
    Returns the current trauma-informed sensitivity settings that control
    how the platform interacts with the child to ensure emotional safety.
    """
    try:
        settings = _parent_dashboard_service.get_sensitivity_settings(child_id)
        
        if not settings:
            raise HTTPException(status_code=404, detail="Child sensitivity settings not found")
        
        return SensitivitySettingsResponse(
            child_id=settings.child_id,
            interaction_pacing=settings.interaction_pacing.value,
            encouragement_frequency=settings.encouragement_frequency,
            celebration_intensity=settings.celebration_intensity.value,
            exit_reminder_frequency=settings.exit_reminder_frequency,
            cultural_comfort_emphasis=settings.cultural_comfort_emphasis,
            anxiety_override=settings.anxiety_override,
            parent_notes=settings.parent_notes,
            last_updated=settings.last_updated
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving sensitivity settings: {str(e)}")


@router.put("/children/{child_id}/sensitivity-settings", response_model=SensitivitySettingsResponse)
async def update_child_sensitivity_settings(
    child_id: str, 
    settings_request: SensitivitySettingsRequest
) -> SensitivitySettingsResponse:
    """
    Update sensitivity settings for a specific child.
    
    Allows parents to adjust trauma-informed interaction parameters to match
    their child's anxiety levels and learning needs.
    """
    try:
        # Update settings using the service
        success = _parent_dashboard_service.update_sensitivity_settings(
            child_id=child_id,
            interaction_pacing=settings_request.interaction_pacing,
            encouragement_frequency=settings_request.encouragement_frequency,
            celebration_intensity=settings_request.celebration_intensity,
            exit_reminder_frequency=settings_request.exit_reminder_frequency,
            cultural_comfort_emphasis=settings_request.cultural_comfort_emphasis,
            anxiety_override=settings_request.anxiety_override,
            parent_notes=settings_request.parent_notes
        )
        
        if not success:
            raise HTTPException(status_code=404, detail="Child not found or settings could not be updated")
        
        # Return updated settings
        updated_settings = _parent_dashboard_service.get_sensitivity_settings(child_id)
        
        return SensitivitySettingsResponse(
            child_id=updated_settings.child_id,
            interaction_pacing=updated_settings.interaction_pacing.value,
            encouragement_frequency=updated_settings.encouragement_frequency,
            celebration_intensity=updated_settings.celebration_intensity.value,
            exit_reminder_frequency=updated_settings.exit_reminder_frequency,
            cultural_comfort_emphasis=updated_settings.cultural_comfort_emphasis,
            anxiety_override=updated_settings.anxiety_override,
            parent_notes=updated_settings.parent_notes,
            last_updated=updated_settings.last_updated
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating sensitivity settings: {str(e)}")


@router.post("/children/{child_id}/sensitivity-settings", response_model=SensitivitySettingsResponse)
async def create_child_sensitivity_settings(
    child_id: str,
    parent_id: str,
    settings_request: SensitivitySettingsRequest
) -> SensitivitySettingsResponse:
    """
    Create initial sensitivity settings for a new child.
    
    Sets up default trauma-informed settings that can be customized by parents
    based on their child's specific needs and anxiety levels.
    """
    try:
        # Create new settings
        settings = _parent_dashboard_service.create_sensitivity_settings(child_id, parent_id)
        
        # Update with requested values
        success = _parent_dashboard_service.update_sensitivity_settings(
            child_id=child_id,
            interaction_pacing=settings_request.interaction_pacing,
            encouragement_frequency=settings_request.encouragement_frequency,
            celebration_intensity=settings_request.celebration_intensity,
            exit_reminder_frequency=settings_request.exit_reminder_frequency,
            cultural_comfort_emphasis=settings_request.cultural_comfort_emphasis,
            anxiety_override=settings_request.anxiety_override,
            parent_notes=settings_request.parent_notes
        )
        
        if not success:
            raise HTTPException(status_code=500, detail="Failed to create sensitivity settings")
        
        # Return created settings
        created_settings = _parent_dashboard_service.get_sensitivity_settings(child_id)
        
        return SensitivitySettingsResponse(
            child_id=created_settings.child_id,
            interaction_pacing=created_settings.interaction_pacing.value,
            encouragement_frequency=created_settings.encouragement_frequency,
            celebration_intensity=created_settings.celebration_intensity.value,
            exit_reminder_frequency=created_settings.exit_reminder_frequency,
            cultural_comfort_emphasis=created_settings.cultural_comfort_emphasis,
            anxiety_override=created_settings.anxiety_override,
            parent_notes=created_settings.parent_notes,
            last_updated=created_settings.last_updated
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating sensitivity settings: {str(e)}")


@router.get("/children/{child_id}/sensitivity-recommendations", response_model=SensitivityRecommendationsResponse)
async def get_sensitivity_recommendations(child_id: str) -> SensitivityRecommendationsResponse:
    """
    Get AI-powered recommendations for sensitivity settings based on child's interaction patterns.
    
    Provides trauma-informed recommendations to help parents optimize their child's
    learning experience based on observed behavior and interaction patterns.
    """
    try:
        recommendations = _parent_dashboard_service.get_sensitivity_recommendations(child_id)
        
        if not recommendations:
            raise HTTPException(status_code=404, detail="No recommendations available for this child")
        
        return SensitivityRecommendationsResponse(
            child_id=child_id,
            recommended_settings=recommendations.get("recommended_settings", {}),
            reasoning=recommendations.get("reasoning", "No specific reasoning available"),
            confidence_score=recommendations.get("confidence_score", 0.0)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving recommendations: {str(e)}")


@router.post("/children/{child_id}/apply-anxiety-override")
async def apply_anxiety_override(child_id: str) -> Dict[str, str]:
    """
    Apply anxiety override settings for a particularly anxious child.
    
    Instantly applies maximum trauma-informed settings to provide extra
    emotional safety and reduce interaction pressure.
    """
    try:
        success = _parent_dashboard_service.apply_anxiety_override(child_id)
        
        if not success:
            raise HTTPException(status_code=404, detail="Child not found or override could not be applied")
        
        return {"message": "Anxiety override applied successfully", "child_id": child_id}
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error applying anxiety override: {str(e)}")


@router.post("/children/{child_id}/apply-confidence-settings")
async def apply_confidence_settings(child_id: str) -> Dict[str, str]:
    """
    Apply confidence settings for a more confident child.
    
    Adjusts settings to allow for more interactive and engaging experiences
    while still maintaining trauma-informed principles.
    """
    try:
        success = _parent_dashboard_service.apply_confidence_settings(child_id)
        
        if not success:
            raise HTTPException(status_code=404, detail="Child not found or confidence settings could not be applied")
        
        return {"message": "Confidence settings applied successfully", "child_id": child_id}
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error applying confidence settings: {str(e)}")
