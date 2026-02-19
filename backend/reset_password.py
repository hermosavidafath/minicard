#!/usr/bin/env python3
"""Script untuk reset password user"""

from app import create_app
from extensions import db
from models import User

app = create_app()

with app.app_context():
    print("=" * 60)
    print("RESET PASSWORD USER")
    print("=" * 60)
    
    # Tampilkan daftar user
    users = User.query.all()
    print("\nDaftar user yang tersedia:")
    for i, user in enumerate(users, 1):
        print(f"{i}. {user.username}")
    
    # Input username
    username = input("\nMasukkan username yang ingin direset: ").strip()
    
    user = User.query.filter_by(username=username).first()
    
    if not user:
        print(f"❌ User '{username}' tidak ditemukan!")
    else:
        # Input password baru
        new_password = input("Masukkan password baru (min 6 karakter): ").strip()
        
        if len(new_password) < 6:
            print("❌ Password harus minimal 6 karakter!")
        else:
            user.set_password(new_password)
            db.session.commit()
            print(f"\n✅ Password untuk user '{username}' berhasil direset!")
            print(f"Username: {username}")
            print(f"Password baru: {new_password}")
            print("\nSekarang bisa login dengan password baru.")
