from datetime import datetime
from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    pastes = db.relationship('Paste', backref='owner', lazy=True)
    profiles = db.relationship('Profile', backref='owner', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    display_name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    age = db.Column(db.String(20))
    location = db.Column(db.String(100))
    interests = db.Column(db.Text)
    social_links = db.Column(db.Text)  # JSON string untuk menyimpan berbagai social media
    avatar_url = db.Column(db.String(500))
    background_color = db.Column(db.String(7), default='#1a1a1a')
    text_color = db.Column(db.String(7), default='#ffffff')
    accent_color = db.Column(db.String(7), default='#ff6b6b')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    public = db.Column(db.Boolean, default=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    title = db.Column(db.String(200))
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    public = db.Column(db.Boolean, default=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    edit_token = db.Column(db.String(128), nullable=True)  # Token untuk edit tanpa login
