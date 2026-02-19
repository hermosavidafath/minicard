#!/usr/bin/env python3
"""
Deployment helper script
"""

import os
import secrets
import subprocess
import sys

def generate_secret_key():
    """Generate a secure secret key"""
    return secrets.token_hex(32)

def check_requirements():
    """Check if all requirements are met"""
    print("🔍 Checking deployment requirements...")
    
    # Check if psycopg2 is installed
    try:
        import psycopg2
        print("✅ psycopg2-binary installed")
    except ImportError:
        print("❌ psycopg2-binary not installed. Run: pip install psycopg2-binary")
        return False
    
    # Check if gunicorn is installed
    try:
        import gunicorn
        print("✅ Gunicorn installed")
    except ImportError:
        print("❌ Gunicorn not installed. Run: pip install gunicorn")
        return False
    
    # Check DATABASE_URL
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        print("❌ DATABASE_URL environment variable not set!")
        print("   Set it to your PostgreSQL URL")
        return False
    elif 'postgresql' not in database_url:
        print("⚠️  DATABASE_URL should be PostgreSQL, not SQLite!")
        print("   Current:", database_url[:50] + "...")
        return False
    else:
        print("✅ DATABASE_URL configured (PostgreSQL)")
    
    # Check if all required files exist
    required_files = [
        'wsgi.py', 'Procfile', 'requirements.txt', 
        'app.py', 'config.py', 'models.py'
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            return False
    
    return True

def test_production():
    """Test production setup locally"""
    print("🧪 Testing production setup...")
    
    # Set production environment
    os.environ['FLASK_ENV'] = 'production'
    os.environ['SECRET_KEY'] = generate_secret_key()
    
    try:
        from wsgi import application
        print("✅ WSGI application loads successfully")
        
        # Test database (create instance directory first)
        os.makedirs('instance', exist_ok=True)
        
        with application.app_context():
            from extensions import db
            db.create_all()
            print("✅ Database initialization successful")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def create_env_file():
    """Create production .env file"""
    env_content = f"""# Production Environment Variables
SECRET_KEY={generate_secret_key()}
FLASK_ENV=production
DATABASE_URL=sqlite:///instance/rentry.sqlite
RATELIMIT_DEFAULT=1000 per day;100 per hour
HOST=0.0.0.0
PORT=5000
DEBUG=False
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ .env file created with secure settings")

def main():
    print("🚀 Rentry Deployment Helper")
    print("=" * 40)
    
    if not check_requirements():
        print("\n❌ Requirements check failed!")
        sys.exit(1)
    
    if not test_production():
        print("\n❌ Production test failed!")
        sys.exit(1)
    
    # Create .env file if it doesn't exist
    if not os.path.exists('.env'):
        create_env_file()
    
    print("\n🎉 Ready for deployment!")
    print("\nNext steps:")
    print("1. Choose a hosting platform (see DEPLOYMENT.md)")
    print("2. Set up your repository on the platform")
    print("3. Configure environment variables")
    print("4. Deploy!")
    
    print("\nQuick test with gunicorn:")
    print("gunicorn wsgi:application")

if __name__ == '__main__':
    main()