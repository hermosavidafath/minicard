from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, URL

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class ProfileForm(FlaskForm):
    display_name = StringField('Nama Tampilan', validators=[Length(max=100)])
    bio = TextAreaField('Bio/Tentang Kamu', validators=[Length(max=500)])
    age = StringField('Umur', validators=[Length(max=20)])
    location = StringField('Lokasi', validators=[Length(max=100)])
    interests = TextAreaField('Hobi/Minat', validators=[Length(max=300)])
    
    # Social Media Links
    instagram = StringField('Instagram', validators=[Optional(), Length(max=100)])
    twitter = StringField('Twitter/X', validators=[Optional(), Length(max=100)])
    tiktok = StringField('TikTok', validators=[Optional(), Length(max=100)])
    youtube = StringField('YouTube', validators=[Optional(), Length(max=100)])
    discord = StringField('Discord', validators=[Optional(), Length(max=100)])
    
    avatar_url = StringField('Link Foto Profil', validators=[Optional(), URL(), Length(max=500)])
    
    # Customization
    background_color = StringField('Warna Background', validators=[Length(max=7)], default='#1a1a1a')
    text_color = StringField('Warna Teks', validators=[Length(max=7)], default='#ffffff')
    accent_color = StringField('Warna Aksen', validators=[Length(max=7)], default='#ff6b6b')
    
    public = BooleanField('Profil Publik', default=True)

class PasteForm(FlaskForm):
    title = StringField('Title', validators=[Length(max=200)])
    content = TextAreaField('Content', validators=[DataRequired()])
    public = BooleanField('Public')

class EmptyForm(FlaskForm):
    """Simple empty form used to provide CSRF token for small actions (delete)."""
    pass
