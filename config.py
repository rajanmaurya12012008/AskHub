import os

class Config:
    """
    Configuration settings for AskHub application.
    These values default to local development settings,
    but can be overridden using environment variables.
    """
    # Flask configuration
    # SECRET_KEY is used for session signing. Keep it secure in production.
    SECRET_KEY = os.environ.get('SECRET_KEY', 'askhub-development-secret-key-987654321')
    
    # MySQL Database configuration
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'rajanmysql') # Default MySQL password is often blank on local setups
    DB_NAME = os.environ.get('DB_NAME', 'askhub')
    DB_PORT = int(os.environ.get('DB_PORT', 3306))
