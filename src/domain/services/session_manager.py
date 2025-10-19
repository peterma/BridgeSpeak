"""
Session Management Service

Provides conversation state persistence and session management for 20-minute learning sessions.
Maintains context across interactions and tracks progress within sessions.
"""

import time
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from enum import Enum

from .conversation_types import ScenarioType, ConversationTurn


class SessionStatus(str, Enum):
    """Status of learning sessions"""
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    EXPIRED = "expired"


@dataclass
class SessionMilestone:
    """Milestone achieved during a session"""
    milestone_id: str
    achieved_at: float  # timestamp
    scenario_type: ScenarioType
    description: str
    complexity_level: str


@dataclass
class ConversationSession:
    """A complete conversation session with state persistence"""
    session_id: str
    child_id: str
    session_start: float  # timestamp
    current_scenario: Optional[ScenarioType]
    conversation_history: List[ConversationTurn]
    progress_milestones: List[SessionMilestone]
    session_duration_target: int = 20  # minutes
    status: SessionStatus = SessionStatus.ACTIVE
    last_interaction: float = 0.0
    context_notes: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.context_notes is None:
            self.context_notes = {}
        if self.last_interaction == 0.0:
            self.last_interaction = time.time()


class SessionManager:
    """Service for managing conversation sessions and state persistence"""
    
    def __init__(self):
        self.active_sessions: Dict[str, ConversationSession] = {}
        self.session_timeout_minutes = 30  # Session expires after 30 min of inactivity
        self.max_session_duration_minutes = 25  # Hard limit on session length
        
    def create_session(self, child_id: str, initial_scenario: Optional[ScenarioType] = None) -> str:
        """Create a new conversation session"""
        session_id = f"session_{child_id}_{int(time.time())}"
        
        session = ConversationSession(
            session_id=session_id,
            child_id=child_id,
            session_start=time.time(),
            current_scenario=initial_scenario,
            conversation_history=[],
            progress_milestones=[],
            context_notes={
                "session_goal": "Practice English conversation scenarios",
                "emotional_state": "ready_to_learn",
                "preferred_complexity": "beginner"
            }
        )
        
        self.active_sessions[session_id] = session
        return session_id
    
    def get_session(self, session_id: str) -> Optional[ConversationSession]:
        """Get an active session by ID"""
        session = self.active_sessions.get(session_id)
        
        if session:
            # Check if session has expired
            if self._is_session_expired(session) and session.status == SessionStatus.ACTIVE:
                session.status = SessionStatus.EXPIRED
                return session
            
            # Check if session has reached target duration
            if self._has_session_reached_target(session) and session.status == SessionStatus.ACTIVE:
                session.status = SessionStatus.COMPLETED
                return session
                
        return session
    
    def update_session_interaction(self, session_id: str, conversation_turn: ConversationTurn) -> bool:
        """Update session with new conversation turn"""
        session = self.get_session(session_id)
        if not session or session.status not in [SessionStatus.ACTIVE, SessionStatus.PAUSED]:
            return False
        
        # Add to conversation history
        session.conversation_history.append(conversation_turn)
        session.last_interaction = time.time()
        
        # Limit conversation history to prevent memory bloat
        if len(session.conversation_history) > 50:
            session.conversation_history = session.conversation_history[-50:]
        
        # Update session status if it was paused
        if session.status == SessionStatus.PAUSED:
            session.status = SessionStatus.ACTIVE
            
        return True
    
    def add_milestone(self, session_id: str, milestone: SessionMilestone) -> bool:
        """Add a milestone achievement to the session"""
        session = self.get_session(session_id)
        if not session:
            return False
            
        session.progress_milestones.append(milestone)
        
        # Update context based on milestone
        if "milestones_achieved" not in session.context_notes:
            session.context_notes["milestones_achieved"] = 0
        session.context_notes["milestones_achieved"] += 1
        
        return True
    
    def update_session_context(self, session_id: str, context_updates: Dict[str, Any]) -> bool:
        """Update session context information"""
        session = self.get_session(session_id)
        if not session:
            return False
            
        session.context_notes.update(context_updates)
        session.last_interaction = time.time()
        return True
    
    def pause_session(self, session_id: str, reason: str = "user_request") -> bool:
        """Pause an active session"""
        session = self.get_session(session_id)
        if not session or session.status != SessionStatus.ACTIVE:
            return False
            
        session.status = SessionStatus.PAUSED
        session.context_notes["pause_reason"] = reason
        session.context_notes["paused_at"] = time.time()
        return True
    
    def resume_session(self, session_id: str) -> bool:
        """Resume a paused session"""
        session = self.get_session(session_id)
        if not session or session.status != SessionStatus.PAUSED:
            return False
            
        # Check if too much time has passed
        if self._is_session_expired(session):
            session.status = SessionStatus.EXPIRED
            return False
            
        session.status = SessionStatus.ACTIVE
        session.last_interaction = time.time()
        
        if "pause_reason" in session.context_notes:
            del session.context_notes["pause_reason"]
        if "paused_at" in session.context_notes:
            del session.context_notes["paused_at"]
            
        return True
    
    def complete_session(self, session_id: str, completion_reason: str = "target_reached") -> bool:
        """Mark session as completed"""
        session = self.get_session(session_id)
        if not session:
            return False
            
        session.status = SessionStatus.COMPLETED
        session.context_notes["completion_reason"] = completion_reason
        session.context_notes["completed_at"] = time.time()
        return True
    
    def get_session_progress(self, session_id: str) -> Dict[str, Any]:
        """Get progress summary for a session"""
        session = self.get_session(session_id)
        if not session:
            return {"error": "Session not found"}
        
        duration_minutes = (time.time() - session.session_start) / 60
        remaining_minutes = max(0, session.session_duration_target - duration_minutes)
        
        return {
            "session_id": session_id,
            "status": session.status.value,
            "duration_minutes": round(duration_minutes, 1),
            "remaining_minutes": round(remaining_minutes, 1),
            "target_duration": session.session_duration_target,
            "conversation_turns": len(session.conversation_history),
            "milestones_achieved": len(session.progress_milestones),
            "current_scenario": session.current_scenario.value if session.current_scenario else None,
            "context_summary": {
                "emotional_state": session.context_notes.get("emotional_state", "unknown"),
                "preferred_complexity": session.context_notes.get("preferred_complexity", "beginner"),
                "milestones_count": session.context_notes.get("milestones_achieved", 0)
            }
        }
    
    def get_conversation_context(self, session_id: str, turns_limit: int = 10) -> List[ConversationTurn]:
        """Get recent conversation context for maintaining continuity"""
        session = self.get_session(session_id)
        if not session:
            return []
            
        # Return recent conversation turns for context
        recent_turns = session.conversation_history[-turns_limit:] if session.conversation_history else []
        return recent_turns
    
    def cleanup_expired_sessions(self) -> int:
        """Clean up expired and completed sessions"""
        current_time = time.time()
        expired_sessions = []
        
        for session_id, session in self.active_sessions.items():
            if (session.status in [SessionStatus.COMPLETED, SessionStatus.EXPIRED] or
                self._is_session_expired(session)):
                expired_sessions.append(session_id)
        
        # Remove expired sessions
        for session_id in expired_sessions:
            del self.active_sessions[session_id]
            
        return len(expired_sessions)
    
    def _is_session_expired(self, session: ConversationSession) -> bool:
        """Check if session has expired due to inactivity"""
        time_since_interaction = (time.time() - session.last_interaction) / 60  # minutes
        return time_since_interaction > self.session_timeout_minutes
    
    def _has_session_reached_target(self, session: ConversationSession) -> bool:
        """Check if session has reached its target duration"""
        duration_minutes = (time.time() - session.session_start) / 60
        return duration_minutes >= session.session_duration_target
    
    def persist_session_state(self, session_id: str) -> Dict[str, Any]:
        """Serialize session state for persistence (e.g., to file or database)"""
        session = self.get_session(session_id)
        if not session:
            return {}
        
        # Convert to serializable format
        serializable_session = {
            "session_id": session.session_id,
            "child_id": session.child_id,
            "session_start": session.session_start,
            "current_scenario": session.current_scenario.value if session.current_scenario else None,
            "status": session.status.value,
            "last_interaction": session.last_interaction,
            "session_duration_target": session.session_duration_target,
            "context_notes": session.context_notes,
            "conversation_history": [
                {
                    "phase": turn.phase.value,
                    "speaker": turn.speaker,
                    "content": turn.content,
                    "language": turn.language,
                    "timestamp": turn.timestamp
                }
                for turn in session.conversation_history
            ],
            "progress_milestones": [
                {
                    "milestone_id": milestone.milestone_id,
                    "achieved_at": milestone.achieved_at,
                    "scenario_type": milestone.scenario_type.value,
                    "description": milestone.description,
                    "complexity_level": milestone.complexity_level
                }
                for milestone in session.progress_milestones
            ]
        }
        
        return serializable_session
    
    def restore_session_state(self, session_data: Dict[str, Any]) -> str:
        """Restore session from persisted state"""
        try:
            # Reconstruct conversation turns
            conversation_history = []
            for turn_data in session_data.get("conversation_history", []):
                from .conversation_types import ConversationPhase
                turn = ConversationTurn(
                    phase=ConversationPhase(turn_data["phase"]),
                    speaker=turn_data["speaker"],
                    content=turn_data["content"],
                    language=turn_data["language"],
                    timestamp=turn_data["timestamp"]
                )
                conversation_history.append(turn)
            
            # Reconstruct milestones
            progress_milestones = []
            for milestone_data in session_data.get("progress_milestones", []):
                milestone = SessionMilestone(
                    milestone_id=milestone_data["milestone_id"],
                    achieved_at=milestone_data["achieved_at"],
                    scenario_type=ScenarioType(milestone_data["scenario_type"]),
                    description=milestone_data["description"],
                    complexity_level=milestone_data["complexity_level"]
                )
                progress_milestones.append(milestone)
            
            # Reconstruct session
            session = ConversationSession(
                session_id=session_data["session_id"],
                child_id=session_data["child_id"],
                session_start=session_data["session_start"],
                current_scenario=ScenarioType(session_data["current_scenario"]) if session_data.get("current_scenario") else None,
                conversation_history=conversation_history,
                progress_milestones=progress_milestones,
                session_duration_target=session_data.get("session_duration_target", 20),
                status=SessionStatus(session_data.get("status", "active")),
                last_interaction=session_data.get("last_interaction", time.time()),
                context_notes=session_data.get("context_notes", {})
            )
            
            self.active_sessions[session.session_id] = session
            return session.session_id
            
        except Exception as e:
            # Return empty string on restoration failure
            return ""
    
    def get_active_session_for_child(self, child_id: str) -> Optional[ConversationSession]:
        """Get the active session for a specific child"""
        for session in self.active_sessions.values():
            if (session.child_id == child_id and 
                session.status in [SessionStatus.ACTIVE, SessionStatus.PAUSED] and
                not self._is_session_expired(session)):
                return session
        return None
    
    def get_session_statistics(self) -> Dict[str, Any]:
        """Get statistics about all sessions"""
        total_sessions = len(self.active_sessions)
        active_count = sum(1 for s in self.active_sessions.values() if s.status == SessionStatus.ACTIVE)
        paused_count = sum(1 for s in self.active_sessions.values() if s.status == SessionStatus.PAUSED)
        completed_count = sum(1 for s in self.active_sessions.values() if s.status == SessionStatus.COMPLETED)
        
        return {
            "total_sessions": total_sessions,
            "active_sessions": active_count,
            "paused_sessions": paused_count,
            "completed_sessions": completed_count,
            "average_duration_minutes": self._calculate_average_session_duration()
        }
    
    def _calculate_average_session_duration(self) -> float:
        """Calculate average session duration"""
        if not self.active_sessions:
            return 0.0
            
        total_duration = 0.0
        session_count = 0
        
        for session in self.active_sessions.values():
            if session.status in [SessionStatus.COMPLETED, SessionStatus.EXPIRED]:
                duration = (session.last_interaction - session.session_start) / 60  # minutes
                total_duration += duration
                session_count += 1
        
        return round(total_duration / session_count, 1) if session_count > 0 else 0.0
    
    def build_conversation_memory(self, session_id: str) -> Dict[str, Any]:
        """Build conversation memory from session history for learning continuity"""
        session = self.get_session(session_id)
        if not session:
            return {}
        
        memory = {
            "practiced_scenarios": set(),
            "successful_interactions": [],
            "challenging_areas": [],
            "emotional_progression": [],
            "learning_patterns": {},
            "milestone_achievements": []
        }
        
        # Analyze conversation history
        for turn in session.conversation_history:
            if turn.phase == ConversationPhase.CHINESE_COMFORT:
                # Extract practiced scenario from content
                if "介绍" in turn.content or "introduce" in turn.content.lower():
                    memory["practiced_scenarios"].add("introducing_yourself")
                elif "厕所" in turn.content or "toilet" in turn.content.lower():
                    memory["practiced_scenarios"].add("asking_for_toilet")
                elif "帮助" in turn.content or "help" in turn.content.lower():
                    memory["practiced_scenarios"].add("asking_for_help")
                elif "饿" in turn.content or "hungry" in turn.content.lower():
                    memory["practiced_scenarios"].add("expressing_hunger")
                elif "再见" in turn.content or "goodbye" in turn.content.lower():
                    memory["practiced_scenarios"].add("saying_goodbye")
            
            elif turn.phase == ConversationPhase.CHILD_PRACTICE:
                if len(turn.content.strip()) > 0:
                    memory["successful_interactions"].append({
                        "timestamp": turn.timestamp,
                        "content": turn.content,
                        "language": turn.language
                    })
                else:
                    memory["challenging_areas"].append({
                        "timestamp": turn.timestamp,
                        "issue": "silence_or_difficulty"
                    })
            
            elif turn.phase == ConversationPhase.ENCOURAGING_FEEDBACK:
                # Track emotional progression through encouragement level
                if hasattr(turn, 'encouragement_level'):
                    memory["emotional_progression"].append({
                        "timestamp": turn.timestamp,
                        "level": turn.encouragement_level
                    })
        
        # Analyze milestones
        for milestone in session.progress_milestones:
            memory["milestone_achievements"].append({
                "milestone_id": milestone.milestone_id,
                "scenario": milestone.scenario_type.value,
                "achieved_at": milestone.achieved_at,
                "complexity": milestone.complexity_level
            })
        
        # Identify learning patterns
        memory["learning_patterns"] = {
            "total_practice_attempts": len(memory["successful_interactions"]),
            "silence_frequency": len(memory["challenging_areas"]),
            "scenario_variety": len(memory["practiced_scenarios"]),
            "engagement_level": self._calculate_engagement_level(memory),
            "progress_velocity": self._calculate_progress_velocity(memory)
        }
        
        # Convert sets to lists for JSON serialization
        memory["practiced_scenarios"] = list(memory["practiced_scenarios"])
        
        return memory
    
    def _calculate_engagement_level(self, memory: Dict[str, Any]) -> str:
        """Calculate child's engagement level from memory patterns"""
        successful_count = len(memory["successful_interactions"])
        challenging_count = len(memory["challenging_areas"])
        
        if successful_count == 0 and challenging_count == 0:
            return "unknown"
        
        engagement_ratio = successful_count / (successful_count + challenging_count)
        
        if engagement_ratio >= 0.8:
            return "high"
        elif engagement_ratio >= 0.5:
            return "moderate"
        else:
            return "low"
    
    def _calculate_progress_velocity(self, memory: Dict[str, Any]) -> str:
        """Calculate how quickly child is progressing"""
        milestones = memory["milestone_achievements"]
        
        if len(milestones) == 0:
            return "starting"
        
        # Calculate time between milestones
        if len(milestones) >= 2:
            time_diffs = []
            for i in range(1, len(milestones)):
                time_diff = milestones[i]["achieved_at"] - milestones[i-1]["achieved_at"]
                time_diffs.append(time_diff / 60)  # Convert to minutes
            
            avg_time_between_milestones = sum(time_diffs) / len(time_diffs)
            
            if avg_time_between_milestones <= 5:
                return "fast"
            elif avg_time_between_milestones <= 10:
                return "steady"
            else:
                return "gradual"
        
        return "early"
    
    def detect_and_create_milestones(self, session_id: str) -> List[SessionMilestone]:
        """Automatically detect achievements and create milestone records"""
        session = self.get_session(session_id)
        if not session:
            return []
        
        new_milestones = []
        existing_milestone_ids = set(m.milestone_id for m in session.progress_milestones)
        
        # Analyze conversation for milestone opportunities
        conversation_memory = self.build_conversation_memory(session_id)
        
        # Milestone: First successful attempt in any scenario
        if (len(conversation_memory["successful_interactions"]) >= 1 and 
            "first_attempt" not in existing_milestone_ids):
            milestone = SessionMilestone(
                milestone_id="first_attempt",
                achieved_at=conversation_memory["successful_interactions"][0]["timestamp"],
                scenario_type=session.current_scenario or ScenarioType.INTRODUCING_YOURSELF,
                description="Made first successful speaking attempt",
                complexity_level="beginner"
            )
            new_milestones.append(milestone)
        
        # Milestone: Consistent engagement (5+ interactions)
        if (len(conversation_memory["successful_interactions"]) >= 5 and 
            "consistent_engagement" not in existing_milestone_ids):
            milestone = SessionMilestone(
                milestone_id="consistent_engagement",
                achieved_at=conversation_memory["successful_interactions"][4]["timestamp"],
                scenario_type=session.current_scenario or ScenarioType.INTRODUCING_YOURSELF,
                description="Demonstrated consistent engagement with 5+ attempts",
                complexity_level="beginner"
            )
            new_milestones.append(milestone)
        
        # Milestone: Multi-scenario practice
        if (len(conversation_memory["practiced_scenarios"]) >= 3 and 
            "scenario_variety" not in existing_milestone_ids):
            milestone = SessionMilestone(
                milestone_id="scenario_variety",
                achieved_at=time.time(),
                scenario_type=session.current_scenario or ScenarioType.INTRODUCING_YOURSELF,
                description="Practiced multiple different scenarios",
                complexity_level="intermediate"
            )
            new_milestones.append(milestone)
        
        # Milestone: Session completion
        if (session.status == SessionStatus.COMPLETED and 
            "session_completed" not in existing_milestone_ids):
            milestone = SessionMilestone(
                milestone_id="session_completed",
                achieved_at=time.time(),
                scenario_type=session.current_scenario or ScenarioType.INTRODUCING_YOURSELF,
                description="Successfully completed full learning session",
                complexity_level="intermediate"
            )
            new_milestones.append(milestone)
        
        # Add new milestones to session
        for milestone in new_milestones:
            self.add_milestone(session_id, milestone)
        
        return new_milestones
    
    def get_resumption_context(self, session_id: str) -> Dict[str, Any]:
        """Get context information for resuming interrupted sessions"""
        session = self.get_session(session_id)
        if not session:
            return {}
        
        memory = self.build_conversation_memory(session_id)
        
        resumption_context = {
            "session_status": session.status.value,
            "time_since_last_interaction": (time.time() - session.last_interaction) / 60,  # minutes
            "progress_summary": {
                "scenarios_practiced": memory["practiced_scenarios"],
                "successful_attempts": len(memory["successful_interactions"]),
                "milestones_achieved": len(memory["milestone_achievements"]),
                "current_scenario": session.current_scenario.value if session.current_scenario else None
            },
            "recommended_resumption_approach": self._get_resumption_recommendation(session, memory),
            "conversation_continuity_cues": self._get_continuity_cues(session, memory)
        }
        
        return resumption_context
    
    def _get_resumption_recommendation(self, session: ConversationSession, memory: Dict[str, Any]) -> str:
        """Recommend how to resume based on session state and memory"""
        time_away = (time.time() - session.last_interaction) / 60  # minutes
        
        if time_away <= 5:
            return "quick_welcome_back"
        elif time_away <= 30:
            return "gentle_reorientation"
        else:
            return "full_context_refresh"
    
    def _get_continuity_cues(self, session: ConversationSession, memory: Dict[str, Any]) -> Dict[str, Any]:
        """Get cues for maintaining conversation continuity"""
        return {
            "last_successful_phrase": memory["successful_interactions"][-1]["content"] if memory["successful_interactions"] else None,
            "next_logical_scenario": self._suggest_next_scenario(memory),
            "emotional_state_context": session.context_notes.get("emotional_state", "ready_to_learn"),
            "recent_achievements": memory["milestone_achievements"][-3:] if len(memory["milestone_achievements"]) >= 3 else memory["milestone_achievements"]
        }
    
    def _suggest_next_scenario(self, memory: Dict[str, Any]) -> str:
        """Suggest next scenario based on learning history"""
        practiced = set(memory["practiced_scenarios"])
        all_scenarios = {"introducing_yourself", "asking_for_toilet", "asking_for_help", "expressing_hunger", "saying_goodbye"}
        
        # Suggest unpracticed scenarios first
        unpracticed = all_scenarios - practiced
        if unpracticed:
            return list(unpracticed)[0]
        
        # If all practiced, suggest based on engagement level
        engagement = memory["learning_patterns"]["engagement_level"]
        if engagement == "high":
            return "asking_for_help"  # More complex scenario
        else:
            return "introducing_yourself"  # Easier scenario