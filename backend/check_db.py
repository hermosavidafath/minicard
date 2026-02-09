#!/usr/bin/env python3
"""
Script untuk memeriksa isi database
Jalankan dengan: python check_db.py
"""

from app import create_app
from extensions import db
from models import User, Profile, Paste

def check_database():
    """Periksa struktur dan isi database"""
    app = create_app()
    
    with app.app_context():
        print("=== INFORMASI DATABASE ===")
        print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        # Periksa tabel yang ada
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"Tabel yang ada: {tables}")
        
        if not tables:
            print("❌ Tidak ada tabel! Jalankan init_db.py terlebih dahulu.")
            return
        
        print("\n=== STRUKTUR TABEL ===")
        for table_name in tables:
            columns = inspector.get_columns(table_name)
            print(f"\nTabel: {table_name}")
            for col in columns:
                print(f"  - {col['name']}: {col['type']}")
        
        print("\n=== ISI DATABASE ===")
        
        # Hitung jumlah record di setiap tabel
        user_count = User.query.count()
        profile_count = Profile.query.count()
        paste_count = Paste.query.count()
        
        print(f"Users: {user_count}")
        print(f"Profiles: {profile_count}")
        print(f"Pastes: {paste_count}")
        
        # Tampilkan beberapa data sample
        if user_count > 0:
            print("\n--- Sample Users ---")
            users = User.query.limit(5).all()
            for user in users:
                print(f"ID: {user.id}, Username: {user.username}, Created: {user.created_at}")
        
        if profile_count > 0:
            print("\n--- Sample Profiles ---")
            profiles = Profile.query.limit(5).all()
            for profile in profiles:
                print(f"ID: {profile.id}, Slug: {profile.slug}, Name: {profile.display_name}")
        
        if paste_count > 0:
            print("\n--- Sample Pastes ---")
            pastes = Paste.query.limit(5).all()
            for paste in pastes:
                print(f"ID: {paste.id}, Slug: {paste.slug}, Title: {paste.title}")

if __name__ == '__main__':
    check_database()