#!/usr/bin/env python3
"""Script untuk melihat semua data di database"""

from app import create_app
from extensions import db
from models import User, Profile, Paste

app = create_app()

with app.app_context():
    print("\n" + "=" * 70)
    print("DATABASE OVERVIEW")
    print("=" * 70)
    
    # Users
    users = User.query.all()
    print(f"\n📊 USERS ({len(users)} total)")
    print("-" * 70)
    for user in users:
        print(f"  • {user.username} (ID: {user.id}) - Terdaftar: {user.created_at.strftime('%d/%m/%Y')}")
    
    # Profiles
    profiles = Profile.query.all()
    print(f"\n👤 PROFILES ({len(profiles)} total)")
    print("-" * 70)
    for profile in profiles:
        owner = User.query.get(profile.owner_id)
        status = "🌍 Public" if profile.public else "🔒 Private"
        print(f"  • {profile.display_name or owner.username} ({status})")
        print(f"    Slug: {profile.slug}")
        print(f"    Owner: {owner.username}")
        print(f"    URL: /p/{profile.slug}")
        print()
    
    # Pastes
    pastes = Paste.query.all()
    print(f"📝 PASTES ({len(pastes)} total)")
    print("-" * 70)
    for paste in pastes:
        owner = User.query.get(paste.owner_id) if paste.owner_id else None
        status = "🌍 Public" if paste.public else "🔒 Private"
        print(f"  • {paste.title or 'Untitled'} ({status})")
        print(f"    Slug: {paste.slug}")
        print(f"    Owner: {owner.username if owner else 'Anonymous'}")
        print(f"    URL: /{paste.slug}")
        print()
    
    print("=" * 70)
