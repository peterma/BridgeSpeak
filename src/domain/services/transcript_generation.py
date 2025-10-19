"""
Transcript generation service for creating sample conversation transcripts.

This module provides utilities for generating realistic conversation transcripts
that follow the ConversationTurn structure and include appropriate bilingual
elements, trauma-informed language, and Irish cultural context.
"""

import json
import time
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path

from .conversation_types import ConversationTurn, ConversationPhase


@dataclass
class TranscriptMetadata:
    """Metadata for a conversation transcript"""
    scenario_id: str
    transcript_id: str
    age_group: str
    difficulty_variant: str
    created_at: str
    description: Optional[str] = None
    estimated_duration: Optional[str] = None


@dataclass
class TranscriptData:
    """Complete transcript data structure"""
    metadata: TranscriptMetadata
    transcript: List[ConversationTurn]


class TranscriptGenerator:
    """Utility class for generating conversation transcripts"""
    
    def __init__(self):
        self.base_timestamp = time.time()
        
    def generate_timestamp(self, offset_seconds: float = 0) -> float:
        """Generate a realistic timestamp with offset"""
        return self.base_timestamp + offset_seconds
    
    def create_chinese_comfort_turn(
        self, 
        content: str, 
        timestamp_offset: float = 0,
        encouragement_level: str = "gentle"
    ) -> ConversationTurn:
        """Create a Chinese comfort phase turn"""
        return ConversationTurn(
            phase=ConversationPhase.CHINESE_COMFORT,
            speaker="xiao_mei",
            content=content,
            language="zh-CN",
            timestamp=self.generate_timestamp(timestamp_offset),
            encouragement_level=encouragement_level
        )
    
    def create_english_demonstration_turn(
        self, 
        content: str, 
        timestamp_offset: float = 0,
        encouragement_level: str = "standard"
    ) -> ConversationTurn:
        """Create an English demonstration phase turn"""
        return ConversationTurn(
            phase=ConversationPhase.ENGLISH_DEMONSTRATION,
            speaker="xiao_mei",
            content=content,
            language="en-IE",
            timestamp=self.generate_timestamp(timestamp_offset),
            encouragement_level=encouragement_level
        )
    
    def create_child_practice_turn(
        self, 
        content: str, 
        timestamp_offset: float = 0,
        encouragement_level: str = "standard"
    ) -> ConversationTurn:
        """Create a child practice phase turn"""
        return ConversationTurn(
            phase=ConversationPhase.CHILD_PRACTICE,
            speaker="child",
            content=content,
            language="en-IE",
            timestamp=self.generate_timestamp(timestamp_offset),
            encouragement_level=encouragement_level
        )
    
    def create_encouraging_feedback_turn(
        self, 
        content: str, 
        timestamp_offset: float = 0,
        encouragement_level: str = "enthusiastic"
    ) -> ConversationTurn:
        """Create an encouraging feedback phase turn"""
        return ConversationTurn(
            phase=ConversationPhase.ENCOURAGING_FEEDBACK,
            speaker="xiao_mei",
            content=content,
            language="mixed",
            timestamp=self.generate_timestamp(timestamp_offset),
            encouragement_level=encouragement_level
        )
    
    def create_transcript_metadata(
        self,
        scenario_id: str,
        age_group: str,
        difficulty_variant: str,
        description: Optional[str] = None
    ) -> TranscriptMetadata:
        """Create transcript metadata"""
        transcript_id = f"{scenario_id}_{difficulty_variant}_{age_group}"
        return TranscriptMetadata(
            scenario_id=scenario_id,
            transcript_id=transcript_id,
            age_group=age_group,
            difficulty_variant=difficulty_variant,
            created_at=datetime.now(timezone.utc).isoformat(),
            description=description
        )
    
    def save_transcript_to_json(
        self, 
        transcript_data: TranscriptData, 
        output_path: Path
    ) -> None:
        """Save transcript data to JSON file"""
        # Convert dataclasses to dictionaries for JSON serialization
        transcript_dict = {
            "metadata": asdict(transcript_data.metadata),
            "transcript": [asdict(turn) for turn in transcript_data.transcript]
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(transcript_dict, f, indent=2, ensure_ascii=False)
    
    def load_transcript_from_json(self, input_path: Path) -> TranscriptData:
        """Load transcript data from JSON file"""
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Reconstruct dataclasses from dictionaries
        metadata = TranscriptMetadata(**data["metadata"])
        transcript = [
            ConversationTurn(
                phase=ConversationPhase(turn["phase"]),
                speaker=turn["speaker"],
                content=turn["content"],
                language=turn["language"],
                timestamp=turn["timestamp"],
                encouragement_level=turn.get("encouragement_level", "standard")
            )
            for turn in data["transcript"]
        ]
        
        return TranscriptData(metadata=metadata, transcript=transcript)
    
    def validate_transcript(self, transcript_data: TranscriptData) -> List[str]:
        """Validate transcript data and return any issues"""
        issues = []
        
        # Check metadata
        if not transcript_data.metadata.scenario_id:
            issues.append("Missing scenario_id in metadata")
        
        if not transcript_data.metadata.age_group:
            issues.append("Missing age_group in metadata")
        
        # Check transcript structure
        if not transcript_data.transcript:
            issues.append("Empty transcript")
            return issues
        
        # Check conversation flow
        phases = [turn.phase for turn in transcript_data.transcript]
        if ConversationPhase.CHINESE_COMFORT not in phases:
            issues.append("Missing Chinese comfort phase")
        
        if ConversationPhase.CHILD_PRACTICE not in phases:
            issues.append("Missing child practice phase")
        
        # Check timestamps are in order
        timestamps = [turn.timestamp for turn in transcript_data.transcript]
        if timestamps != sorted(timestamps):
            issues.append("Timestamps are not in chronological order")
        
        # Check for appropriate bilingual content
        chinese_turns = [turn for turn in transcript_data.transcript if turn.language == "zh-CN"]
        english_turns = [turn for turn in transcript_data.transcript if turn.language == "en-IE"]
        
        if not chinese_turns:
            issues.append("No Chinese language content found")
        
        if not english_turns:
            issues.append("No English language content found")
        
        return issues


# Age-appropriate content templates with strict word limits
AGE_GROUP_TEMPLATES = {
    "junior-infants": {
        "vocabulary_complexity": "simple",
        "sentence_length": "short",
        "max_words": 8,
        "encouragement_style": "gentle",
        "cultural_context": "basic",
        "avoid_words": ["introduce", "participate", "emergency", "situation", "complex", "difficult"]
    },
    "senior-infants": {
        "vocabulary_complexity": "simple",
        "sentence_length": "short_to_medium",
        "max_words": 12,
        "encouragement_style": "gentle_to_standard",
        "cultural_context": "basic",
        "avoid_words": ["emergency", "situation", "participation"]
    },
    "first-class": {
        "vocabulary_complexity": "medium",
        "sentence_length": "medium",
        "max_words": 15,
        "encouragement_style": "standard",
        "cultural_context": "intermediate",
        "avoid_words": ["emergency", "situation"]
    },
    "second-class": {
        "vocabulary_complexity": "medium",
        "sentence_length": "medium_to_long",
        "max_words": 18,
        "encouragement_style": "standard",
        "cultural_context": "intermediate",
        "avoid_words": []
    },
    "third-class": {
        "vocabulary_complexity": "medium_to_advanced",
        "sentence_length": "medium_to_long",
        "max_words": 20,
        "encouragement_style": "standard_to_enthusiastic",
        "cultural_context": "advanced",
        "avoid_words": []
    },
    "fourth-class": {
        "vocabulary_complexity": "advanced",
        "sentence_length": "long",
        "max_words": 25,
        "encouragement_style": "enthusiastic",
        "cultural_context": "advanced",
        "avoid_words": []
    }
}


# Irish English vocabulary and cultural context
IRISH_VOCABULARY = {
    "toilet": "toilet",  # Not "bathroom" or "restroom"
    "break": "break",    # Not "recess"
    "rubbish": "rubbish",  # Not "trash" or "garbage"
    "crisps": "crisps",  # Not "chips"
    "biscuit": "biscuit",  # Not "cookie"
    "jumper": "jumper",  # Not "sweater"
    "trousers": "trousers",  # Not "pants"
    "football": "football",  # Not "soccer"
    "maths": "maths",  # Not "math"
    "colour": "colour",  # Not "color"
    "favourite": "favourite",  # Not "favorite"
    "centre": "centre",  # Not "center"
    "realise": "realise",  # Not "realize"
    "organise": "organise",  # Not "organize"
    "recognise": "recognise",  # Not "recognize"
}

# Irish cultural context phrases
IRISH_CULTURAL_PHRASES = {
    "school_context": [
        "in the classroom",
        "at break time",
        "during lunch",
        "in the playground",
        "with your teacher",
        "in Irish school"
    ],
    "polite_requests": [
        "Please, may I",
        "Could I please",
        "Would it be okay if",
        "I'd like to"
    ],
    "gratitude": [
        "Thank you very much",
        "Thanks a million",
        "That's brilliant",
        "That's grand"
    ]
}


# Trauma-informed language patterns
TRAUMA_INFORMED_PHRASES = {
    "chinese_comfort": [
        "没关系，慢慢来",  # "It's okay, take your time"
        "你很勇敢",  # "You are brave"
        "我在这里帮助你",  # "I am here to help you"
        "你做得很好",  # "You are doing well"
        "别担心，我们可以一起练习",  # "Don't worry, we can practice together"
        "你非常聪明",  # "You are very smart"
    ],
    "encouraging_feedback": [
        "好棒! That was wonderful!",
        "太棒了! You did it perfectly!",
        "很好! I'm so proud of you!",
        "真不错! You're learning so well!",
        "太棒了! You can do it!",
        "很好! Well done!",
        "真不错! You're doing great!",
        "好棒! That's brilliant!",
    ],
    "gentle_correction": [
        "Almost there! Try saying it like this...",
        "Good try! Let me help you with that...",
        "You're close! Here's how we say it...",
        "That's a good start! Let's try again...",
        "You're doing well! Just a little more...",
    ],
    "encouraging_phrases": [
        "You can do it!",
        "Try again!",
        "Take your time!",
        "It's okay!",
        "Well done!",
        "Good job!",
        "You're doing great!",
        "That's brilliant!",
        "You're learning so well!",
        "I'm proud of you!",
        "You're so brave!",
        "You're getting better!",
    ],
    "avoid_phrases": [
        "wrong",
        "bad",
        "stupid",
        "can't",
        "impossible",
        "never",
        "always",
        "shouldn't",
        "mustn't",
        "terrible",
        "awful"
    ]
}
