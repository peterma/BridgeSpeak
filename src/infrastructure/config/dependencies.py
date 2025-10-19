"""
Dependency Injection Container

This module sets up the dependency injection container for the application.
It will eventually replace manual service instantiation throughout the codebase.
"""

from functools import lru_cache
from typing import Dict, Any
import os
from pathlib import Path

# Application interfaces
from src.application.interfaces.repositories import (
    IChildProfileRepository,
    ILearningSessionRepository, 
    IConversationTurnRepository,
    IVocabularyProgressRepository
)
from src.application.interfaces.services import (
    ILanguageDetectionService,
    IBilingualContextService,
    ITraumaValidationService,
    ICurriculumIntegrationService,
    ILearningAnalyticsService
)


class DependencyContainer:
    """
    Dependency injection container for the application.
    
    This will eventually replace the manual service instantiation scattered
    throughout the current codebase.
    """
    
    def __init__(self):
        self._repositories: Dict[str, Any] = {}
        self._services: Dict[str, Any] = {}
        self._singletons: Dict[str, Any] = {}
    
    def register_repository(self, interface_type: type, implementation: Any) -> None:
        """Register a repository implementation."""
        self._repositories[interface_type.__name__] = implementation
    
    def register_service(self, interface_type: type, implementation: Any) -> None:
        """Register a service implementation.""" 
        self._services[interface_type.__name__] = implementation
    
    def register_singleton(self, interface_type: type, implementation: Any) -> None:
        """Register a singleton service."""
        self._singletons[interface_type.__name__] = implementation
    
    def get_repository(self, interface_type: type) -> Any:
        """Get repository implementation."""
        return self._repositories.get(interface_type.__name__)
    
    def get_service(self, interface_type: type) -> Any:
        """Get service implementation."""
        return self._services.get(interface_type.__name__)
    
    def get_singleton(self, interface_type: type) -> Any:
        """Get singleton service."""
        return self._singletons.get(interface_type.__name__)


# Global container instance
_container = DependencyContainer()


def get_container() -> DependencyContainer:
    """Get the global dependency injection container."""
    return _container


# FastAPI Dependency Functions
# These will be used with FastAPI's Depends() to inject services into endpoints

def get_child_profile_repository() -> IChildProfileRepository:
    """FastAPI dependency for child profile repository."""
    repo = _container.get_repository(IChildProfileRepository)
    if repo is None:
        raise RuntimeError("Child profile repository not registered")
    return repo


def get_learning_session_repository() -> ILearningSessionRepository:
    """FastAPI dependency for learning session repository."""
    repo = _container.get_repository(ILearningSessionRepository)
    if repo is None:
        raise RuntimeError("Learning session repository not registered")
    return repo


def get_conversation_turn_repository() -> IConversationTurnRepository:
    """FastAPI dependency for conversation turn repository."""
    repo = _container.get_repository(IConversationTurnRepository)
    if repo is None:
        raise RuntimeError("Conversation turn repository not registered")
    return repo


def get_vocabulary_progress_repository() -> IVocabularyProgressRepository:
    """FastAPI dependency for vocabulary progress repository."""
    repo = _container.get_repository(IVocabularyProgressRepository)
    if repo is None:
        raise RuntimeError("Vocabulary progress repository not registered")
    return repo


def get_language_detection_service() -> ILanguageDetectionService:
    """FastAPI dependency for language detection service."""
    service = _container.get_service(ILanguageDetectionService)
    if service is None:
        # Fallback to service factory if not registered in container
        from src.infrastructure.factories.service_factory import get_language_detection_service as factory_get
        return factory_get()
    return service


def get_bilingual_context_service() -> IBilingualContextService:
    """FastAPI dependency for bilingual context service."""
    service = _container.get_service(IBilingualContextService)
    if service is None:
        # Fallback to service factory if not registered in container
        from src.infrastructure.factories.service_factory import get_bilingual_context_service as factory_get
        return factory_get()
    return service


def get_trauma_validation_service() -> ITraumaValidationService:
    """FastAPI dependency for trauma validation service."""
    service = _container.get_service(ITraumaValidationService)
    if service is None:
        # Fallback to service factory if not registered in container
        from src.infrastructure.factories.service_factory import get_trauma_validation_service as factory_get
        return factory_get()
    return service


def get_curriculum_integration_service() -> ICurriculumIntegrationService:
    """FastAPI dependency for curriculum integration service."""
    service = _container.get_service(ICurriculumIntegrationService)
    if service is None:
        # Fallback to service factory if not registered in container
        from src.infrastructure.factories.service_factory import get_curriculum_integration_service as factory_get
        return factory_get()
    return service


def get_learning_analytics_service() -> ILearningAnalyticsService:
    """FastAPI dependency for learning analytics service."""
    service = _container.get_service(ILearningAnalyticsService)
    if service is None:
        raise RuntimeError("Learning analytics service not registered")
    return service


# Configuration Management
@lru_cache()
def get_settings() -> Dict[str, Any]:
    """
    Get application settings with caching.
    
    This will eventually replace scattered environment variable access
    throughout the current codebase.
    """
    return {
        # Database settings
        "database_url": os.getenv("DATABASE_URL", "sqlite:///./dev.db"),
        
        # External service settings (existing integrations)
        "deepgram_api_key": os.getenv("DEEPGRAM_API_KEY"),
        "cartesia_api_key": os.getenv("CARTESIA_API_KEY"), 
        "google_api_key": os.getenv("GOOGLE_API_KEY"),
        "tavus_api_key": os.getenv("TAVUS_API_KEY"),
        "tavus_replica_id": os.getenv("TAVUS_REPLICA_ID"),
        
        # Application settings
        "app_env": os.getenv("APP_ENV", "development"),
        "debug": os.getenv("DEBUG", "true").lower() == "true",
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        
        # Educational settings
        "default_trauma_sensitivity": os.getenv("DEFAULT_TRAUMA_SENSITIVITY", "moderate"),
        "min_positivity_threshold": float(os.getenv("MIN_POSITIVITY_THRESHOLD", "0.6")),
        
        # Performance settings 
        "max_response_time_ms": int(os.getenv("MAX_RESPONSE_TIME_MS", "2000")),
        "max_session_duration_minutes": int(os.getenv("MAX_SESSION_DURATION_MINUTES", "30")),
    }


def initialize_services():
    """
    Initialize domain services in the dependency injection container.
    
    This registers the extracted domain services with the DI container.
    Call this during application startup.
    """
    from src.infrastructure.factories.service_factory import educational_service_factory
    
    # Register services in the container
    _container.register_service(
        ILanguageDetectionService, 
        educational_service_factory.create_language_detection_service()
    )
    _container.register_service(
        ITraumaValidationService,
        educational_service_factory.create_trauma_validation_service()
    )
    _container.register_service(
        IBilingualContextService,
        educational_service_factory.create_bilingual_context_service()
    )
    _container.register_service(
        ICurriculumIntegrationService,
        educational_service_factory.create_curriculum_integration_service()
    )


def get_all_services_info() -> Dict[str, Any]:
    """
    Get information about all registered services.
    
    Returns:
        Dictionary with service registration information
    """
    from src.infrastructure.factories.service_factory import educational_service_factory
    
    return {
        'container_services': {
            'repositories': list(_container._repositories.keys()),
            'services': list(_container._services.keys()),
            'singletons': list(_container._singletons.keys())
        },
        'factory_info': educational_service_factory.get_service_info()
    }