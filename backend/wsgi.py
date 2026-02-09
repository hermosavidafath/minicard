#!/usr/bin/env python3
"""
WSGI entry point for production deployment
"""

import os
from app import create_app

# Create application instance
application = create_app()

# Initialize database on startup (only if needed)
if __name__ == "__main__":
    with application.app_context():
        from extensions import db
        db.create_all()
    application.run()