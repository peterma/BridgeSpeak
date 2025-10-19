"""
Service Factory for Educational Services

Creates instances of domain services following dependency injection patterns.
This factory encapsulates service creation logic and manages dependencies.
"""

from typing import Dict, Any, Optional
from src.domain.services.language_detection import LanguageDetectionService
from src.domain.services.trauma_validation import TraumaValidationService
from src.domain.services.bilingual_context import BilingualContextService
from src.domain.services.curriculum_integration import CurriculumIntegrationService

from src.application.interfaces.services import (
    ILanguageDetectionService,
    ITraumaValidationService, 
    IBilingualContextService,
    ICurriculumIntegrationService
)


class EducationalServiceFactory:
    """
    Factory for creating educational domain services.
    
    Manages service instantiation and dependency resolution for the educational domain.
    Provides a centralized location for service creation logic.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the service factory.
        
        Args:
            config: Optional configuration dictionary for service customization
        """
        self.config = config or {}
        self._service_cache: Dict[str, Any] = {}
        self._use_singletons = self.config.get('use_singletons', True)
    
    def create_language_detection_service(self) -> ILanguageDetectionService:
        """
        Create a language detection service instance.
        
        Returns:
            ILanguageDetectionService implementation
        """
        if self._use_singletons and 'language_detection' in self._service_cache:
            return self._service_cache['language_detection']
        
        service = LanguageDetectionService()
        
        if self._use_singletons:
            self._service_cache['language_detection'] = service
        
        return service
    
    def create_trauma_validation_service(self) -> ITraumaValidationService:
        """
        Create a trauma validation service instance.
        
        Returns:
            ITraumaValidationService implementation
        """
        if self._use_singletons and 'trauma_validation' in self._service_cache:
            return self._service_cache['trauma_validation']
        
        service = TraumaValidationService()
        
        if self._use_singletons:
            self._service_cache['trauma_validation'] = service
        
        return service
    
    def create_bilingual_context_service(self) -> IBilingualContextService:
        """
        Create a bilingual context service instance.
        
        Returns:
            IBilingualContextService implementation
        """
        if self._use_singletons and 'bilingual_context' in self._service_cache:
            return self._service_cache['bilingual_context']
        
        service = BilingualContextService()
        
        if self._use_singletons:
            self._service_cache['bilingual_context'] = service
        
        return service
    
    def create_curriculum_integration_service(self) -> ICurriculumIntegrationService:
        """
        Create a curriculum integration service instance.
        
        Returns:
            ICurriculumIntegrationService implementation
        """
        if self._use_singletons and 'curriculum_integration' in self._service_cache:
            return self._service_cache['curriculum_integration']
        
        service = CurriculumIntegrationService()
        
        if self._use_singletons:
            self._service_cache['curriculum_integration'] = service
        
        return service
    
    def create_all_services(self) -> Dict[str, Any]:
        """
        Create all educational services.
        
        Returns:
            Dictionary containing all service instances
        """
        return {
            'language_detection': self.create_language_detection_service(),
            'trauma_validation': self.create_trauma_validation_service(),
            'bilingual_context': self.create_bilingual_context_service(),
            'curriculum_integration': self.create_curriculum_integration_service()
        }
    
    def clear_cache(self):
        """Clear the service cache to force new instances."""
        self._service_cache.clear()
    
    def get_service_info(self) -> Dict[str, Any]:
        """
        Get information about the factory and cached services.
        
        Returns:
            Dictionary with factory information
        """
        return {
            'use_singletons': self._use_singletons,
            'cached_services': list(self._service_cache.keys()),
            'config': self.config
        }


# Global factory instance for easy access
educational_service_factory = EducationalServiceFactory()


def get_language_detection_service() -> ILanguageDetectionService:
    """Get language detection service instance."""
    return educational_service_factory.create_language_detection_service()


def get_trauma_validation_service() -> ITraumaValidationService:
    """Get trauma validation service instance."""
    return educational_service_factory.create_trauma_validation_service()


def get_bilingual_context_service() -> IBilingualContextService:
    """Get bilingual context service instance."""
    return educational_service_factory.create_bilingual_context_service()


def get_curriculum_integration_service() -> ICurriculumIntegrationService:
    """Get curriculum integration service instance."""
    return educational_service_factory.create_curriculum_integration_service()


def get_all_educational_services() -> Dict[str, Any]:
    """Get all educational services."""
    return educational_service_factory.create_all_services()


def configure_service_factory(config: Dict[str, Any]):
    """
    Configure the global service factory.
    
    Args:
        config: Configuration dictionary
    """
    global educational_service_factory
    educational_service_factory = EducationalServiceFactory(config)