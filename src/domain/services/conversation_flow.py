"""
Conversation Flow Service for Scenario-Based Learning

Manages the bilingual conversation flow with Chinese comfort → English practice pattern.
Integrates with Xiao Mei character service and scenario generation for natural conversations.
"""

import asyncio
import time
from dataclasses import dataclass
from typing import Dict, List, Optional, Any, AsyncGenerator
from enum import Enum

from .conversation_types import ScenarioType, ConversationPhase, ConversationTurn, ScenarioSession
from .scenario_generation import ScenarioGenerationService
from .encouragement_system import BilingualPraiseEngine, PersonalJourneyNarrative
from .trauma_validation import NonCompetitiveLanguageFilter


class FlowState(str, Enum):
    """States in the conversation flow"""
    INITIALIZING = "initializing"
    CHINESE_COMFORT = "chinese_comfort"
    TRANSITION_PAUSE = "transition_pause"
    ENGLISH_DEMONSTRATION = "english_demonstration"
    WAITING_FOR_CHILD = "waiting_for_child"
    ENCOURAGING_FEEDBACK = "encouraging_feedback"
    COMPLETED = "completed"


class ChildResponseType(str, Enum):
    """Types of child responses"""
    ATTEMPT = "attempt"
    SILENCE = "silence"
    UNEXPECTED = "unexpected"
    SUCCESS = "success"


@dataclass
class FlowConfiguration:
    """Configuration for conversation flow timing and behavior"""
    transition_pause_ms: int = 1000  # 1 second pause
    child_wait_timeout_ms: int = 10000  # 10 seconds to wait for child
    encouragement_pause_ms: int = 500  # 0.5 second before encouragement
    patient_waiting: bool = True  # No time pressure on child
    max_attempts_per_scenario: int = 3  # Allow repetition
    gentle_wait_prompt_interval_ms: int = 30000  # Gentle prompt every 30s if still waiting


@dataclass
class FlowResult:
    """Result of a conversation flow execution"""
    success: bool
    scenario_type: ScenarioType
    child_id: str
    session_id: str
    turns_completed: int
    total_duration_ms: int
    child_response_type: ChildResponseType
    encouragement_given: str
    completed_successfully: bool


class ConversationFlowService:
    """Service for managing bilingual conversation flows"""

    def __init__(self, scenario_service: ScenarioGenerationService):
        self.scenario_service = scenario_service
        self.config = FlowConfiguration()
        self.active_flows: Dict[str, FlowState] = {}
        self.praise_engine = BilingualPraiseEngine()
        self.journey_narrative = PersonalJourneyNarrative()
        self.non_competitive_filter = NonCompetitiveLanguageFilter()

    async def execute_scenario_flow(self, 
                                  scenario_type: ScenarioType, 
                                  child_id: str) -> AsyncGenerator[ConversationTurn, None]:
        """Execute complete bilingual flow for a scenario"""
        
        # Create scenario session
        session = self.scenario_service.create_scenario_session(scenario_type, child_id)
        if not session:
            raise ValueError(f"Could not create session for scenario {scenario_type}")
        
        session_id = session.session_id
        self.active_flows[session_id] = FlowState.INITIALIZING
        
        try:
            # Phase 1: Chinese Comfort
            self.active_flows[session_id] = FlowState.CHINESE_COMFORT
            chinese_turn = self.scenario_service.get_chinese_comfort_phase(scenario_type)
            if chinese_turn:
                self.scenario_service.add_turn_to_session(session_id, chinese_turn)
                yield chinese_turn
            
            # Phase 2: Transition Pause
            self.active_flows[session_id] = FlowState.TRANSITION_PAUSE
            await asyncio.sleep(self.config.transition_pause_ms / 1000.0)
            
            # Phase 3: English Demonstration
            self.active_flows[session_id] = FlowState.ENGLISH_DEMONSTRATION
            english_turn = self.scenario_service.get_english_demonstration_phase(scenario_type)
            if english_turn:
                self.scenario_service.add_turn_to_session(session_id, english_turn)
                yield english_turn
            
            # Phase 4: Patient Waiting for Child Response
            self.active_flows[session_id] = FlowState.WAITING_FOR_CHILD
            child_turn = await self._wait_for_child_response(session_id)
            if child_turn:
                self.scenario_service.add_turn_to_session(session_id, child_turn)
                yield child_turn
            
            # Phase 5: Encouraging Feedback
            self.active_flows[session_id] = FlowState.ENCOURAGING_FEEDBACK
            feedback_turn = await self._generate_encouraging_feedback(session_id, child_turn)
            if feedback_turn:
                self.scenario_service.add_turn_to_session(session_id, feedback_turn)
                yield feedback_turn
            
            # Mark as completed
            self.active_flows[session_id] = FlowState.COMPLETED
            self.scenario_service.complete_session(session_id)
            
        finally:
            # Clean up active flow tracking
            if session_id in self.active_flows:
                del self.active_flows[session_id]

    async def _wait_for_child_response(self, session_id: str) -> Optional[ConversationTurn]:
        """Wait patiently for child response without time pressure"""
        
        # In real implementation, this would wait for actual speech input
        # For now, simulate patient waiting behavior
        
        if self.config.patient_waiting:
            # Simulate patient waiting - no timeout pressure
            start_wait = time.time()
            last_prompt_time = start_wait
            
            # Simulated loop: in real system, we'd await actual input events
            await asyncio.sleep(2.0)  # initial think time
            
            # Check if we should give a gentle prompt
            now = time.time()
            if (now - last_prompt_time) * 1000 >= self.config.gentle_wait_prompt_interval_ms:
                last_prompt_time = now
                gentle_prompt = ConversationTurn(
                    phase=ConversationPhase.ENCOURAGING_FEEDBACK,
                    speaker="xiao_mei",
                    content="慢慢来 (Màn màn lái) - take your time, I'm here with you",
                    language="mixed",
                    timestamp=time.time(),
                    encouragement_level="gentle"
                )
                # In a real pipeline we would emit this prompt; here we just proceed
                _ = gentle_prompt
            
            # Simulate child attempting the phrase subsequently
            simulated_response = "Hello, my name is..."
            return ConversationTurn(
                phase=ConversationPhase.CHILD_PRACTICE,
                speaker="child",
                content=simulated_response,
                language="en-IE",
                timestamp=time.time(),
                encouragement_level="standard"
            )
        
        return None

    async def _generate_encouraging_feedback(self, 
                                           session_id: str, 
                                           child_turn: Optional[ConversationTurn]) -> Optional[ConversationTurn]:
        """Generate encouraging feedback regardless of child's response quality"""
        
        # Brief pause before encouragement
        await asyncio.sleep(self.config.encouragement_pause_ms / 1000.0)
        
        # Always provide positive encouragement - trauma-informed approach
        if child_turn:
            # Child attempted - celebrate the effort
            encouragement = self.praise_engine.generate_bilingual_praise()
            encouragement = self.journey_narrative.add_to(encouragement)
        else:
            # Child was silent - gentle encouragement
            encouragement = "没关系 (Méi guānxi) - that's okay! Let's try together. You're learning!"
            encouragement = self.journey_narrative.add_to(encouragement)
        encouragement = self.non_competitive_filter.clean(encouragement)
        
        return ConversationTurn(
            phase=ConversationPhase.ENCOURAGING_FEEDBACK,
            speaker="xiao_mei",
            content=encouragement,
            language="mixed",  # Chinese + English encouragement
            timestamp=time.time(),
            encouragement_level="enthusiastic"
        )

    def create_simple_success_celebration(self, scenario_type: ScenarioType) -> ConversationTurn:
        """Create a simple success celebration response"""
        celebrations = {
            ScenarioType.INTRODUCING_YOURSELF: "太好了! (Tài hǎo le!) You introduced yourself brilliantly!",
            ScenarioType.ASKING_FOR_TOILET: "很好! (Hěn hǎo!) Perfect way to ask for the toilet!",
            ScenarioType.ASKING_FOR_HELP: "真棒! (Zhēn bàng!) You asked for help so politely!",
            ScenarioType.EXPRESSING_HUNGER: "好极了! (Hǎo jí le!) Great way to say you're hungry!",
            ScenarioType.SAYING_GOODBYE: "完美! (Wánměi!) Perfect goodbye! So polite!"
        }
        
        celebration_text = celebrations.get(
            scenario_type, 
            self.praise_engine.generate_bilingual_praise()
        )
        celebration_text = self.journey_narrative.add_to(celebration_text)
        celebration_text = self.non_competitive_filter.clean(celebration_text)
        
        return ConversationTurn(
            phase=ConversationPhase.ENCOURAGING_FEEDBACK,
            speaker="xiao_mei",
            content=celebration_text,
            language="mixed",
            timestamp=time.time(),
            encouragement_level="enthusiastic"
        )

    def get_flow_state(self, session_id: str) -> Optional[FlowState]:
        """Get current flow state for a session"""
        return self.active_flows.get(session_id)

    def is_flow_active(self, session_id: str) -> bool:
        """Check if a flow is currently active"""
        return session_id in self.active_flows

    def get_active_flows_count(self) -> int:
        """Get count of currently active flows"""
        return len(self.active_flows)

    def configure_timing(self, 
                        transition_pause_ms: Optional[int] = None,
                        child_wait_timeout_ms: Optional[int] = None,
                        encouragement_pause_ms: Optional[int] = None) -> None:
        """Configure timing parameters for conversation flow"""
        if transition_pause_ms is not None:
            self.config.transition_pause_ms = transition_pause_ms
        if child_wait_timeout_ms is not None:
            self.config.child_wait_timeout_ms = child_wait_timeout_ms
        if encouragement_pause_ms is not None:
            self.config.encouragement_pause_ms = encouragement_pause_ms

    def enable_patient_mode(self, enabled: bool = True) -> None:
        """Enable or disable patient waiting mode (no time pressure)"""
        self.config.patient_waiting = enabled

    async def execute_simple_flow(self, scenario_type: ScenarioType, child_id: str) -> FlowResult:
        """Execute a simple conversation flow and return results"""
        start_time = time.time()
        turns_completed = 0
        
        try:
            turns = []
            async for turn in self.execute_scenario_flow(scenario_type, child_id):
                turns.append(turn)
                turns_completed += 1
            
            duration_ms = int((time.time() - start_time) * 1000)
            
            # Determine response type based on turns
            child_response_type = ChildResponseType.SUCCESS
            if turns_completed < 4:  # Expected: Chinese, English, Child, Feedback
                child_response_type = ChildResponseType.SILENCE
            
            # Get final encouragement
            encouragement = turns[-1].content if turns else "Good effort!"
            
            return FlowResult(
                success=True,
                scenario_type=scenario_type,
                child_id=child_id,
                session_id=f"{child_id}_{scenario_type.value}",
                turns_completed=turns_completed,
                total_duration_ms=duration_ms,
                child_response_type=child_response_type,
                encouragement_given=encouragement,
                completed_successfully=turns_completed >= 4
            )
            
        except Exception as e:
            duration_ms = int((time.time() - start_time) * 1000)
            return FlowResult(
                success=False,
                scenario_type=scenario_type,
                child_id=child_id,
                session_id="",
                turns_completed=turns_completed,
                total_duration_ms=duration_ms,
                child_response_type=ChildResponseType.UNEXPECTED,
                encouragement_given="That's okay, let's try together!",
                completed_successfully=False
            )

    def validate_bilingual_pattern(self, turns: List[ConversationTurn]) -> Dict[str, Any]:
        """Validate that conversation follows proper bilingual pattern"""
        if len(turns) < 2:
            return {
                "valid": False, 
                "reason": "Insufficient turns",
                "has_chinese_comfort": False,
                "has_english_demonstration": False,
                "has_encouragement": False,
                "follows_pattern": False
            }
        
        # Check for Chinese comfort first
        has_chinese_first = (
            len(turns) > 0 and 
            turns[0].language == "zh-CN" and 
            turns[0].phase == ConversationPhase.CHINESE_COMFORT
        )
        
        # Check for English demonstration second
        has_english_demo = (
            len(turns) > 1 and 
            turns[1].language == "en-IE" and 
            turns[1].phase == ConversationPhase.ENGLISH_DEMONSTRATION
        )
        
        # Check for encouraging feedback
        has_encouragement = any(
            turn.phase == ConversationPhase.ENCOURAGING_FEEDBACK 
            for turn in turns
        )
        
        return {
            "valid": has_chinese_first and has_english_demo,
            "has_chinese_comfort": has_chinese_first,
            "has_english_demonstration": has_english_demo,
            "has_encouragement": has_encouragement,
            "follows_pattern": has_chinese_first and has_english_demo and has_encouragement
        }