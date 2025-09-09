import logging
import os
from datetime import datetime
from pathlib import Path

class Logger:
    _instance = None
    _logger = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._setup_logger()
        return cls._instance
    
    def _setup_logger(self):
        """Setup logger configuration"""
        # Create logs directory if it doesn't exist
        log_dir = Path("/app/storage/logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # Create logger
        self._logger = logging.getLogger('api_logger')
        self._logger.setLevel(logging.INFO)
        
        # Prevent duplicate handlers
        if self._logger.handlers:
            return
        
        # Create formatters
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
        )
        console_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        
        # File handler
        file_handler = logging.FileHandler('/app/storage/logs/api.log')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(file_formatter)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(console_formatter)
        
        # Add handlers to logger
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)
    
    def info(self, message: str):
        """Log info message"""
        self._logger.info(message)
    
    def error(self, message: str):
        """Log error message"""
        self._logger.error(message)
    
    def warning(self, message: str):
        """Log warning message"""
        self._logger.warning(message)
    
    def debug(self, message: str):
        """Log debug message"""
        self._logger.debug(message)
    
    def critical(self, message: str):
        """Log critical message"""
        self._logger.critical(message)
    
    @classmethod
    def get_logger(cls):
        """Get logger instance"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

# Convenience function to get logger
def get_logger():
    """Get logger instance"""
    return Logger.get_logger()
