#!/usr/bin/env python3
"""
WSGI entry point for production deployment
WAJIB untuk Render, Heroku, dll
"""

import os
from app import create_app

# Create application instance
application = create_app()

# Initialize database tables on first run
with application.app_context():
    from extensions import db
    try:
        db.create_all()
        print("✅ Database tables initialized")
    except Exception as e:
        print(f"⚠️  Database initialization: {e}")

if __name__ == "__main__":
    application.run()