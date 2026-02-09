#!/usr/bin/env python3
"""
Database Manager - Script untuk mengelola database
Jalankan dengan: python db_manager.py [command]

Commands:
  init     - Inisialisasi database baru (hapus semua data)
  migrate  - Update struktur database tanpa hapus data
  check    - Periksa status database
  backup   - Backup database
  seed     - Isi database dengan data sample
"""

import sys
import os
import json
from datetime import datetime
from app import create_app
from extensions import db
from models import User, Profile, Paste

def init_database():
    """Inisialisasi database baru"""
    print("🔄 Menginisialisasi database...")
    app = create_app()
    
    with app.app_context():
        # Hapus semua tabel
        db.drop_all()
        print("✅ Tabel lama dihapus")
        
        # Buat tabel baru
        db.create_all()
        print("✅ Tabel baru dibuat")
        
        # Verifikasi
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"📋 Tabel: {', '.join(tables)}")
        
        print("✅ Database berhasil diinisialisasi!")

def migrate_database():
    """Update struktur database"""
    print("🔄 Melakukan migrasi database...")
    app = create_app()
    
    with app.app_context():
        # Backup dulu
        backup_database()
        
        # Update struktur
        db.create_all()
        print("✅ Struktur database diperbarui")

def check_database():
    """Periksa status database"""
    app = create_app()
    
    with app.app_context():
        print("📊 STATUS DATABASE")
        print("=" * 50)
        print(f"URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        # Tabel
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"Tabel: {', '.join(tables)}")
        
        # Statistik
        user_count = User.query.count()
        profile_count = Profile.query.count()
        paste_count = Paste.query.count()
        
        print(f"\n📈 STATISTIK:")
        print(f"  Users: {user_count}")
        print(f"  Profiles: {profile_count}")
        print(f"  Pastes: {paste_count}")
        
        # User terbaru
        if user_count > 0:
            latest_user = User.query.order_by(User.created_at.desc()).first()
            print(f"  User terbaru: {latest_user.username} ({latest_user.created_at})")

def backup_database():
    """Backup database"""
    app = create_app()
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    
    if db_uri.startswith('sqlite:///'):
        db_path = db_uri.replace('sqlite:///', '')
        if os.path.exists(db_path):
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = f"{db_path}.backup_{timestamp}"
            import shutil
            shutil.copy2(db_path, backup_path)
            print(f"💾 Database di-backup ke: {backup_path}")
            return backup_path
    
    print("❌ Tidak bisa backup database")
    return None

def seed_database():
    """Isi database dengan data sample"""
    print("🌱 Mengisi database dengan data sample...")
    app = create_app()
    
    with app.app_context():
        # Buat user sample jika belum ada
        if User.query.count() == 0:
            users_data = [
                {'username': 'admin', 'password': 'admin123'},
                {'username': 'demo', 'password': 'demo123'},
                {'username': 'test', 'password': 'test123'}
            ]
            
            for user_data in users_data:
                user = User(username=user_data['username'])
                user.set_password(user_data['password'])
                db.session.add(user)
            
            db.session.commit()
            print("✅ User sample dibuat")
        
        # Buat profile sample
        admin_user = User.query.filter_by(username='admin').first()
        if admin_user and Profile.query.filter_by(owner_id=admin_user.id).count() == 0:
            import secrets
            
            social_links = {
                'instagram': 'admin_ig',
                'twitter': 'admin_tw',
                'discord': 'admin#1234'
            }
            
            profile = Profile(
                slug=secrets.token_urlsafe(8),
                display_name='Administrator',
                bio='Ini adalah profil admin untuk testing',
                age='25',
                location='Jakarta',
                interests='Programming, Gaming, Music',
                social_links=json.dumps(social_links),
                background_color='#2c3e50',
                text_color='#ecf0f1',
                accent_color='#3498db',
                public=True,
                owner=admin_user
            )
            db.session.add(profile)
            db.session.commit()
            print("✅ Profile sample dibuat")
        
        # Buat paste sample
        if Paste.query.count() == 0:
            paste = Paste(
                slug=secrets.token_urlsafe(6),
                title='Welcome to Rentry!',
                content='# Selamat Datang!\n\nIni adalah paste sample untuk testing aplikasi rentry.',
                public=True,
                owner=admin_user
            )
            db.session.add(paste)
            db.session.commit()
            print("✅ Paste sample dibuat")
        
        print("🎉 Data sample berhasil ditambahkan!")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    command = sys.argv[1].lower()
    
    if command == 'init':
        init_database()
    elif command == 'migrate':
        migrate_database()
    elif command == 'check':
        check_database()
    elif command == 'backup':
        backup_database()
    elif command == 'seed':
        seed_database()
    else:
        print(f"❌ Command tidak dikenal: {command}")
        print(__doc__)

if __name__ == '__main__':
    main()