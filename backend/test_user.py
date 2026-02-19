#!/usr/bin/env python3
"""Test script untuk membuat user manual"""

from app import create_app
from extensions import db
from models import User

app = create_app()

with app.app_context():
    # Cek user yang ada
    users = User.query.all()
    print(f"Total users: {len(users)}")
    for u in users:
        print(f"  - {u.username}")
    
    # Coba buat user baru
    test_user = User.query.filter_by(username='testuser').first()
    if not test_user:
        test_user = User(username='testuser')
        test_user.set_password('password123')
        db.session.add(test_user)
        db.session.commit()
        print("\nUser 'testuser' berhasil dibuat!")
        print("Username: testuser")
        print("Password: password123")
    else:
        print("\nUser 'testuser' sudah ada")
