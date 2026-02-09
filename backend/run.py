#!/usr/bin/env python3
"""
Script untuk menjalankan aplikasi Rentry
"""

import os
from app import create_app

if __name__ == '__main__':
    # Buat aplikasi
    app = create_app()
    
    # Pastikan database sudah diinisialisasi
    with app.app_context():
        from extensions import db
        db.create_all()
        print(f"✅ Database ready: {app.config['SQLALCHEMY_DATABASE_URI']}")
    
    # Jalankan aplikasi
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'True').lower() == 'true'
    
    print(f"🚀 Starting Rentry server...")
    print(f"   Host: {host}")
    print(f"   Port: {port}")
    print(f"   Debug: {debug}")
    print(f"   URL: http://localhost:{port}")
    
    app.run(host=host, port=port, debug=debug)