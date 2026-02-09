import os
from dotenv import load_dotenv

load_dotenv()

# base directory for this module (backend/)
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'please-change-me-in-production'
    
    # Database configuration
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        # Use provided DATABASE_URL (for production)
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        # Use local SQLite (for development)
        default_sqlite_path = os.path.join(basedir, 'instance', 'rentry.sqlite').replace('\\', '/')
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{default_sqlite_path}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RATELIMIT_DEFAULT = os.environ.get('RATELIMIT_DEFAULT', '200 per day;50 per hour')
    
    # Production settings
    PREFERRED_URL_SCHEME = 'https' if os.environ.get('FLASK_ENV') == 'production' else 'http'
    SESSION_COOKIE_SECURE = os.environ.get('FLASK_ENV') == 'production'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
