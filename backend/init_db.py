#!/usr/bin/env python3
"""
Script untuk inisialisasi database
Jalankan dengan: python init_db.py
"""

from app import create_app
from extensions import db
from models import User, Profile, Paste

def init_database():
    """Inisialisasi database dan buat semua tabel"""
    app = create_app()
    
    with app.app_context():
        # Drop semua tabel yang ada (hati-hati, ini akan menghapus data!)
        print("Menghapus tabel yang ada...")
        db.drop_all()
        
        # Buat semua tabel baru
        print("Membuat tabel baru...")
        db.create_all()
        
        # Verifikasi tabel yang dibuat
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"Tabel yang berhasil dibuat: {tables}")
        
        # Buat user admin default (opsional)
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            admin_user = User(username='admin')
            admin_user.set_password('admin123')  # Ganti password ini!
            db.session.add(admin_user)
            db.session.commit()
            print("User admin default dibuat (username: admin, password: admin123)")
        
        print("Database berhasil diinisialisasi!")
        print(f"Database path: {app.config['SQLALCHEMY_DATABASE_URI']}")

if __name__ == '__main__':
    init_database()