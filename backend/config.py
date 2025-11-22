import os
from dotenv import load_dotenv

load_dotenv()

# base directory for this module (backend/)
basedir = os.path.abspath(os.path.dirname(__file__))
# build an absolute sqlite URI that points to backend/instance/rentry.sqlite
default_sqlite_path = os.path.join(basedir, 'instance', 'rentry.sqlite').replace('\\', '/')
default_sqlite_uri = f"sqlite:///{default_sqlite_path}"

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'please-change-me'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or default_sqlite_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RATELIMIT_DEFAULT = os.environ.get('RATELIMIT_DEFAULT', '200 per day;50 per hour')
