"""
Repository Interface Definitions

These interfaces define the contracts for data access without coupling to specific implementations.
This enables testing with mock repositories and future database migrations.
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from uuid import UUID
from datetime import datetime, date

# Domain model imports (these will be created in Phase 2)
# from src.domain.models.child_profile import ChildProfile
# from src.domain.models.learning_session import LearningSession
# from src.domain.models.conversation_turn import ConversationTurn
# from src.domain.models.vocabulary_progress import VocabularyProgress

# Temporary type aliases until we create proper domain models
ChildProfile = Dict[str, Any]
LearningSession = Dict[str, Any] 
ConversationTurn = Dict[str, Any]
VocabularyProgress = Dict[str, Any]


class IChildProfileRepository(ABC):
    """Repository interface for child profile data access."""
    
    @abstractmethod
    async def create(self, child_profile: ChildProfile) -> ChildProfile:
        """Create a new child profile."""
        pass
    
    @abstractmethod
    async def get_by_id(self, child_id: UUID) -> Optional[ChildProfile]:
        """Retrieve child profile by ID."""
        pass
    
    @abstractmethod
    async def get_by_parent_id(self, parent_id: UUID) -> List[ChildProfile]:
        """Get all children for a parent."""
        pass
    
    @abstractmethod
    async def update(self, child_id: UUID, updates: Dict[str, Any]) -> Optional[ChildProfile]:
        """Update child profile data."""
        pass
    
    @abstractmethod
    async def delete(self, child_id: UUID) -> bool:
        """Delete a child profile."""
        pass


class ILearningSessionRepository(ABC):
    """Repository interface for learning session data access."""
    
    @abstractmethod
    async def create(self, session: LearningSession) -> LearningSession:
        """Create a new learning session."""
        pass
    
    @abstractmethod
    async def get_by_id(self, session_id: UUID) -> Optional[LearningSession]:
        """Retrieve session by ID."""
        pass
    
    @abstractmethod
    async def get_by_child_id(
        self, 
        child_id: UUID, 
        limit: int = 50,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None
    ) -> List[LearningSession]:
        """Get sessions for a child with optional date filtering."""
        pass
    
    @abstractmethod
    async def update_session_end(self, session_id: UUID, end_time: datetime) -> bool:
        """Mark a session as completed."""
        pass
    
    @abstractmethod
    async def get_active_session(self, child_id: UUID) -> Optional[LearningSession]:
        """Get currently active session for a child."""
        pass


class IConversationTurnRepository(ABC):
    """Repository interface for conversation turn data access."""
    
    @abstractmethod
    async def create(self, turn: ConversationTurn) -> ConversationTurn:
        """Record a new conversation turn."""
        pass
    
    @abstractmethod
    async def get_by_session_id(self, session_id: UUID) -> List[ConversationTurn]:
        """Get all turns for a learning session."""
        pass
    
    @abstractmethod
    async def get_recent_turns(
        self, 
        child_id: UUID, 
        limit: int = 10
    ) -> List[ConversationTurn]:
        """Get recent conversation turns for analysis."""
        pass


class IVocabularyProgressRepository(ABC):
    """Repository interface for vocabulary progress tracking."""
    
    @abstractmethod
    async def create_or_update(self, progress: VocabularyProgress) -> VocabularyProgress:
        """Create or update vocabulary progress record."""
        pass
    
    @abstractmethod
    async def get_by_child_id(self, child_id: UUID) -> List[VocabularyProgress]:
        """Get all vocabulary progress for a child."""
        pass
    
    @abstractmethod
    async def get_by_word(self, child_id: UUID, word: str) -> Optional[VocabularyProgress]:
        """Get progress for a specific word."""
        pass
    
    @abstractmethod
    async def get_words_needing_practice(
        self, 
        child_id: UUID, 
        limit: int = 10
    ) -> List[VocabularyProgress]:
        """Get words that need additional practice."""
        pass
    
    @abstractmethod
    async def update_practice_count(self, child_id: UUID, word: str) -> bool:
        """Increment practice count for a word."""
        pass