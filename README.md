# Rentry Clone - Pastebin dengan Profile

Aplikasi web seperti rentry.co yang memungkinkan users membuat paste dan profile personal.

## ⚠️ PENTING: PostgreSQL Required!

**SQLite TIDAK COCOK untuk production web app!**
- File database hilang saat restart di cloud hosting
- Tidak support multiple concurrent users
- Render/Heroku tidak menyimpan file permanen

**✅ Aplikasi ini WAJIB pakai PostgreSQL untuk production!**

---

## 🚀 Quick Deploy ke Render (Gratis!)

### 1️⃣ Fork Repository
Fork repository ini ke GitHub kamu

### 2️⃣ Deploy Database
1. Login ke [render.com](https://render.com)
2. New → PostgreSQL → Create (Free plan)
3. Copy **Internal Database URL**

### 3️⃣ Deploy Web App
1. New → Web Service → Connect GitHub
2. Root Directory: `backend`
3. Build: `pip install -r requirements.txt`
4. Start: `gunicorn wsgi:application`
5. Environment Variables:
   - `DATABASE_URL` = [paste URL dari step 2]
   - `SECRET_KEY` = [generate random string]
   - `FLASK_ENV` = `production`

### 4️⃣ Done! 🎉
Aplikasi live dalam 5-10 menit!

**📖 Panduan lengkap**: [RENDER_GUIDE.md](backend/RENDER_GUIDE.md)

---

## ✨ Features

- 📝 **Paste Management**: Buat, edit, hapus paste dengan markdown support
- 👤 **User Profiles**: Profile personal dengan customization warna dan social links
- 🔐 **Authentication**: Register, login, dan session management
- 🎨 **Customization**: Custom colors untuk profile
- 📱 **Responsive**: Mobile-friendly design
- 🔒 **Privacy**: Public/private paste dan profile
- ⚡ **Rate Limiting**: Protection dari spam
- 🗄️ **PostgreSQL**: Production-ready database

---

## 🛠️ Local Development

### Prerequisites
- Python 3.11+
- PostgreSQL database
- Git

### Setup
```bash
# Clone repository
git clone <your-repo-url>
cd rentry-project/backend

# Install dependencies
pip install -r requirements.txt

# Set environment variable
export DATABASE_URL="postgresql://user:password@localhost:5432/rentry_dev"

# Run application
python app.py
```

**⚠️ Catatan**: Tidak ada mode SQLite untuk development. Harus pakai PostgreSQL!

---

## 🗄️ Database

**PostgreSQL Only** - SQLAlchemy ORM

### Models:
- **User**: Authentication dan user data
- **Profile**: User profiles dengan customization  
- **Paste**: Text pastes dengan markdown support

### Local PostgreSQL Setup:
```bash
# Install PostgreSQL
# Ubuntu: sudo apt install postgresql
# macOS: brew install postgresql
# Windows: Download dari postgresql.org

# Create database
createdb rentry_dev

# Set environment
export DATABASE_URL="postgresql://username:password@localhost:5432/rentry_dev"
```

---

## 🌐 Deployment Options

### Render (Recommended - Free)
- PostgreSQL: Free (1GB)
- Web Service: Free (750 hours/month)
- **Guide**: [RENDER_GUIDE.md](backend/RENDER_GUIDE.md)

### Heroku
- PostgreSQL: Paid ($9/month minimum)
- Dyno: $7/month
- **Guide**: [DEPLOYMENT.md](backend/DEPLOYMENT.md)

### Railway
- Usage-based pricing (~$5/month)
- **Guide**: [DEPLOYMENT.md](backend/DEPLOYMENT.md)

---

## ⚙️ Environment Variables

**Required**:
```bash
DATABASE_URL=postgresql://user:password@host:port/database
SECRET_KEY=your-super-secret-key
FLASK_ENV=production
```

**Optional**:
```bash
RATELIMIT_DEFAULT=1000 per day;100 per hour
```

---

## 🎨 Features Detail

### Paste Features
- Markdown rendering dengan syntax highlighting
- Public/private visibility
- Edit/delete untuk owner
- Anonymous paste support (dengan owner_id NULL)
- Rate limiting protection

### Profile Features  
- Custom display name dan bio
- Social media links (Instagram, Twitter, TikTok, YouTube, Discord)
- Color customization (background, text, accent)
- Avatar URL support
- Public/private profiles
- Profile discovery page

### Security Features
- CSRF protection (Flask-WTF)
- Rate limiting (Flask-Limiter) 
- Secure session cookies
- Password hashing (Werkzeug)
- Input validation (WTForms)
- SQL injection protection (SQLAlchemy ORM)

---

## 📁 Project Structure

```
backend/
├── app.py              # Main Flask application
├── wsgi.py             # WSGI entry point
├── config.py           # PostgreSQL configuration
├── models.py           # Database models
├── forms.py            # WTForms
├── extensions.py       # Flask extensions
├── requirements.txt    # Dependencies (includes psycopg2-binary)
├── Procfile           # Process file
├── render.yaml        # Render configuration
├── templates/         # HTML templates
└── static/           # CSS/JS files
```

---

## 🔧 Development Commands

```bash
# Check database connection
python -c "from config import Config; print(Config.SQLALCHEMY_DATABASE_URI)"

# Test app
python app.py

# Production test
gunicorn wsgi:application
```

---

## 🆘 Troubleshooting

### Database Connection Error
```bash
# Check DATABASE_URL
echo $DATABASE_URL

# Test connection
python -c "import psycopg2; psycopg2.connect('$DATABASE_URL')"
```

### Missing psycopg2
```bash
pip install psycopg2-binary
```

### Tables Not Created
Tables auto-create on first run. Check logs for errors.

---

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Test dengan PostgreSQL
4. Commit changes
5. Create Pull Request

---

## 📄 License

MIT License

---

## 🔗 Demo

**Live Demo**: [Your Render URL]

**Test Account**: Register sendiri (no default users untuk security)

---

## 📚 Documentation

- [Render Deployment Guide](backend/RENDER_GUIDE.md)
- [General Deployment Guide](backend/DEPLOYMENT.md)
- [Database Documentation](backend/DATABASE.md)

---

**⚡ Ready for Production dengan PostgreSQL!** 🚀