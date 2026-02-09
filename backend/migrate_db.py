#!/usr/bin/env python3
"""
Script untuk migrasi database
Jalankan dengan: python migrate_db.py
"""

from app import create_app
from extensions import db
from models import User, Profile, Paste
import os

def backup_database():
    """Backup database yang ada"""
    app = create_app()
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    
    if db_uri.startswith('sqlite:///'):
        db_path = db_uri.replace('sqlite:///', '')
        if os.path.exists(db_path):
            backup_path = db_path + '.backup'
            import shutil
            shutil.copy2(db_path, backup_path)
            print(f"Database di-backup ke: {backup_path}")
            return True
    return False

def migrate_database():
    """Migrasi database dengan aman"""
    print("=== MIGRASI DATABASE ===")
    
    # Backup dulu
    if backup_database():
        print("✅ Backup berhasil")
    else:
        print("⚠️  Tidak ada database untuk di-backup")
    
    app = create_app()
    
    with app.app_context():
        try:
            # Coba buat tabel yang belum ada tanpa menghapus yang sudah ada
            db.create_all()
            print("✅ Tabel berhasil dibuat/diperbarui")
            
            # Verifikasi
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"Tabel yang tersedia: {tables}")
            
            # Periksa apakah semua model memiliki tabel
            expected_tables = ['user', 'profile', 'paste']
            missing_tables = [t for t in expected_tables if t not in tables]
            
            if missing_tables:
                print(f"❌ Tabel yang hilang: {missing_tables}")
            else:
                print("✅ Semua tabel sudah ada")
                
        except Exception as e:
            print(f"❌ Error saat migrasi: {e}")
            return False
    
    return True

if __name__ == '__main__':
    migrate_database()