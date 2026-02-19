#!/usr/bin/env python3
"""Script untuk melihat semua user yang terdaftar"""

from app import create_app
from extensions import db
from models import User, Profile, Paste

app = create_app()

with app.app_context():
    print("=" * 60)
    print("DAFTAR USER TERDAFTAR")
    print("=" * 60)
    
    users = User.query.all()
    
    if not users:
        print("Belum ada user yang terdaftar.")
    else:
        for i, user in enumerate(users, 1):
            print(f"\n{i}. Username: {user.username}")
            print(f"   User ID: {user.id}")
            print(f"   Terdaftar: {user.created_at.strftime('%d %B %Y, %H:%M')}")
            
            # Hitung jumlah profil
            profile_count = Profile.query.filter_by(owner_id=user.id).count()
            print(f"   Jumlah Profil: {profile_count}")
            
            # Hitung jumlah paste
            paste_count = Paste.query.filter_by(owner_id=user.id).count()
            print(f"   Jumlah Paste: {paste_count}")
            
            # Catatan: Password tidak bisa dilihat karena sudah di-hash
            print(f"   Password: [ENCRYPTED - tidak bisa dilihat]")
    
    print("\n" + "=" * 60)
    print(f"Total User: {len(users)}")
    print("=" * 60)
    
    print("\n💡 CATATAN:")
    print("- Password tidak bisa dilihat karena sudah di-enkripsi (hashed)")
    print("- Jika lupa password, harus reset manual atau buat user baru")
    print("- Untuk reset password user tertentu, gunakan script reset_password.py")
