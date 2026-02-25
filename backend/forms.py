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
    display_name = StringField('display name', validators=[DataRequired(), Length(max=100)])
    bio = TextAreaField('about you', validators=[Optional()])
    age = StringField('age', validators=[Optional(), Length(max=20)])
    location = StringField('location', validators=[Optional(), Length(max=100)])
    interests = TextAreaField('hobbies & interests', validators=[Optional()])
    
    # Social Media Links
    instagram = StringField('instagram', validators=[Optional(), Length(max=100)])
    twitter = StringField('twitter/x', validators=[Optional(), Length(max=100)])
    tiktok = StringField('tiktok', validators=[Optional(), Length(max=100)])
    youtube = StringField('youtube', validators=[Optional(), Length(max=100)])
    discord = StringField('discord', validators=[Optional(), Length(max=100)])
    
    avatar_url = StringField('profile picture link', validators=[Optional(), URL(), Length(max=500)])
    
    # Customization
    background_color = StringField('background color', validators=[Length(max=7)], default='#1a1a1a')
    text_color = StringField('text color', validators=[Length(max=7)], default='#ffffff')
    accent_color = StringField('accent color', validators=[Length(max=7)], default='#ff6b6b')
    
    public = BooleanField('public profile', default=True)

class PasteForm(FlaskForm):
    title = StringField('Title', validators=[Length(max=200)])
    content = TextAreaField('Content', validators=[DataRequired()])
    public = BooleanField('Public')

class EmptyForm(FlaskForm):
    """Simple empty form used to provide CSRF token for small actions (delete)."""
    pass
