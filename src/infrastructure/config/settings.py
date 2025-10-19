"""
Application Settings Management

Centralized configuration management replacing scattered environment variable access.
"""

from pydantic import Field
from pydantic_settings import BaseSettings
from typing import Optional
from pathlib import Path


class DatabaseSettings(BaseSettings):
    """Database configuration settings."""
    
    url: str = Field(default="sqlite:///./dev.db", env="DATABASE_URL")
    echo_sql: bool = Field(default=False, env="DATABASE_ECHO_SQL")
    pool_size: int = Field(default=5, env="DATABASE_POOL_SIZE")
    max_overflow: int = Field(default=10, env="DATABASE_MAX_OVERFLOW")


class ExternalServiceSettings(BaseSettings):
    """External AI service configuration (preserving existing integrations)."""
    
    # Speech-to-text service
    deepgram_api_key: Optional[str] = Field(env="DEEPGRAM_API_KEY")
    deepgram_model: str = Field(default="nova-2", env="DEEPGRAM_MODEL")
    
    # Text-to-speech service  
    cartesia_api_key: Optional[str] = Field(env="CARTESIA_API_KEY")
    cartesia_voice_id: str = Field(default="default", env="CARTESIA_VOICE_ID")
    
    # LLM service
    google_api_key: Optional[str] = Field(env="GOOGLE_API_KEY")
    google_model: str = Field(default="gemini-pro", env="GOOGLE_MODEL")
    
    # Video avatar service
    tavus_api_key: Optional[str] = Field(env="TAVUS_API_KEY")
    tavus_replica_id: Optional[str] = Field(env="TAVUS_REPLICA_ID")
    
    model_config = {"env_file": ".env", "extra": "ignore"}


class EducationalSettings(BaseSettings):
    """Educational and child safety configuration."""
    
    # Trauma-informed design settings
    default_trauma_sensitivity: str = Field(default="moderate", env="DEFAULT_TRAUMA_SENSITIVITY")
    min_positivity_threshold: float = Field(default=0.6, env="MIN_POSITIVITY_THRESHOLD")
    max_negativity_score: float = Field(default=0.3, env="MAX_NEGATIVITY_SCORE")
    
    # Bilingual progression settings
    default_chinese_comfort_level: float = Field(default=0.7, env="DEFAULT_CHINESE_COMFORT_LEVEL")
    english_confidence_threshold: float = Field(default=0.4, env="ENGLISH_CONFIDENCE_THRESHOLD")
    
    # Learning session settings
    max_session_duration_minutes: int = Field(default=30, env="MAX_SESSION_DURATION_MINUTES")
    min_session_gap_minutes: int = Field(default=10, env="MIN_SESSION_GAP_MINUTES")
    
    # Curriculum alignment
    irish_curriculum_version: str = Field(default="2019", env="IRISH_CURRICULUM_VERSION")
    default_age_group: str = Field(default="JUNIOR_INFANTS", env="DEFAULT_AGE_GROUP")
    
    model_config = {"env_file": ".env", "extra": "ignore"}


class PerformanceSettings(BaseSettings):
    """Performance and monitoring configuration."""
    
    # Response time requirements
    max_response_time_ms: int = Field(default=2000, env="MAX_RESPONSE_TIME_MS")
    pipeline_timeout_ms: int = Field(default=5000, env="PIPELINE_TIMEOUT_MS")
    
    # Caching settings
    enable_redis_cache: bool = Field(default=True, env="ENABLE_REDIS_CACHE")
    redis_url: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")
    cache_ttl_seconds: int = Field(default=3600, env="CACHE_TTL_SECONDS")
    
    # Logging and monitoring
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    enable_performance_monitoring: bool = Field(default=True, env="ENABLE_PERFORMANCE_MONITORING")
    
    model_config = {"env_file": ".env", "extra": "ignore"}


class ApplicationSettings(BaseSettings):
    """Main application configuration."""
    
    # Application metadata
    app_name: str = Field(default="AI TIK HKT Demo", env="APP_NAME")
    app_version: str = Field(default="1.0.0", env="APP_VERSION")
    app_env: str = Field(default="development", env="APP_ENV")
    debug: bool = Field(default=True, env="DEBUG")
    
    # API settings
    api_host: str = Field(default="localhost", env="API_HOST")
    api_port: int = Field(default=8000, env="API_PORT")
    api_prefix: str = Field(default="/api/v1", env="API_PREFIX")
    
    # Security settings
    secret_key: str = Field(default="dev-secret-key-change-in-production", env="SECRET_KEY")
    allowed_origins: list = Field(default=["http://localhost:3000"], env="ALLOWED_ORIGINS")
    
    # File paths
    content_dir: Path = Field(default=Path("./content"), env="CONTENT_DIR")
    logs_dir: Path = Field(default=Path("./logs"), env="LOGS_DIR")
    
    model_config = {"env_file": ".env", "extra": "ignore"}


class Settings:
    """Unified settings container."""
    
    def __init__(self):
        self.app = ApplicationSettings()
        self.database = DatabaseSettings()
        self.external_services = ExternalServiceSettings()
        self.educational = EducationalSettings()
        self.performance = PerformanceSettings()
    
    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.app.app_env.lower() in ("development", "dev")
    
    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.app.app_env.lower() in ("production", "prod")
    
    def validate_external_services(self) -> dict:
        """Validate that required external service credentials are available."""
        missing = []
        
        if not self.external_services.deepgram_api_key:
            missing.append("DEEPGRAM_API_KEY")
        if not self.external_services.cartesia_api_key:
            missing.append("CARTESIA_API_KEY")
        if not self.external_services.google_api_key:
            missing.append("GOOGLE_API_KEY")
        if not self.external_services.tavus_api_key:
            missing.append("TAVUS_API_KEY")
        if not self.external_services.tavus_replica_id:
            missing.append("TAVUS_REPLICA_ID")
        
        return {
            "valid": len(missing) == 0,
            "missing_keys": missing
        }


# Global settings instance
settings = Settings()