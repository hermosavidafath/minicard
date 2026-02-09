# Rentry Clone - Pastebin dengan Profile

Aplikasi web seperti rentry.co yang memungkinkan users membuat paste dan profile personal.

## ✨ Features

- 📝 **Paste Management**: Buat, edit, hapus paste dengan markdown support
- 👤 **User Profiles**: Profile personal dengan customization warna dan social links
- 🔐 **Authentication**: Register, login, dan session management
- 🎨 **Customization**: Custom colors untuk profile
- 📱 **Responsive**: Mobile-friendly design
- 🔒 **Privacy**: Public/private paste dan profile
- ⚡ **Rate Limiting**: Protection dari spam

## 🚀 Quick Deploy

### Heroku (1-Click Deploy)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Railway
```bash
railway up
```

### Render
1. Fork repository ini
2. Connect ke Render
3. Deploy otomatis

## 🛠️ Local Development

### Prerequisites
- Python 3.11+
- Git

### Setup
```bash
# Clone repository
git clone <your-repo-url>
cd rentry-project/backend

# Install dependencies
pip install -r requirements.txt

# Setup database
python db_manager.py init
python db_manager.py seed  # Optional: sample data

# Run application
python run.py
```

Aplikasi akan berjalan di http://localhost:5000

## 📁 Project Structure

```
backend/
├── app.py              # Main Flask application
├── wsgi.py             # WSGI entry point for production
├── config.py           # Configuration
├── models.py           # Database models
├── forms.py            # WTForms
├── extensions.py       # Flask extensions
├── db_manager.py       # Database management
├── requirements.txt    # Dependencies
├── Procfile           # Heroku process file
├── Dockerfile         # Docker configuration
├── instance/          # Database files
├── templates/         # HTML templates
└── static/           # CSS/JS files
```

## 🗄️ Database

Menggunakan SQLAlchemy dengan SQLite (default) atau PostgreSQL (production).

### Models:
- **User**: Authentication dan user data
- **Profile**: User profiles dengan customization
- **Paste**: Text pastes dengan markdown support

### Management:
```bash
python db_manager.py check    # Status database
python db_manager.py backup   # Backup database
python db_manager.py migrate  # Update struktur
```

## 🌐 Deployment

Aplikasi siap deploy ke berbagai platform:

- **Heroku**: One-click deploy dengan button di atas
- **Railway**: `railway up`
- **Render**: Connect GitHub repository
- **DigitalOcean**: App Platform
- **Docker**: `docker-compose up`

Lihat [DEPLOYMENT.md](backend/DEPLOYMENT.md) untuk panduan lengkap.

## ⚙️ Configuration

### Environment Variables
```bash
SECRET_KEY=your-secret-key
FLASK_ENV=production
DATABASE_URL=your-database-url
RATELIMIT_DEFAULT=1000 per day;100 per hour
```

### Production Setup
```bash
cd backend
python deploy.py  # Check readiness
gunicorn wsgi:application  # Test production server
```

## 🎨 Features Detail

### Paste Features
- Markdown rendering
- Public/private visibility
- Edit/delete untuk owner
- Anonymous paste support
- Rate limiting

### Profile Features
- Custom display name dan bio
- Social media links (Instagram, Twitter, TikTok, YouTube, Discord)
- Color customization (background, text, accent)
- Avatar support
- Public/private profiles

### Security
- CSRF protection
- Rate limiting
- Secure session cookies
- Password hashing
- Input validation

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push ke branch
5. Create Pull Request

## 📄 License

MIT License - lihat [LICENSE](LICENSE) file.

## 🆘 Support

- 📖 Dokumentasi: Lihat file `.md` di folder backend
- 🐛 Issues: Create GitHub issue
- 💬 Diskusi: GitHub Discussions

## 🔗 Demo

Live demo: [Your deployed URL here]

Default users (setelah seed):
- Username: `admin`, Password: `admin123`
- Username: `demo`, Password: `demo123`