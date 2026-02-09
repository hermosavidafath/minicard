# Setup Guide - Rentry Backend

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Database
```bash
# Periksa status database
python db_manager.py check

# Jika database belum ada, inisialisasi:
python db_manager.py init

# Isi dengan data sample (opsional):
python db_manager.py seed
```

### 3. Setup Environment
```bash
# Copy file environment
copy .env.example .env

# Edit .env sesuai kebutuhan
```

### 4. Run Application
```bash
python app.py
```

Aplikasi akan berjalan di http://localhost:5000

## Database Management

### Perintah Dasar
```bash
# Cek status database
python db_manager.py check

# Backup database
python db_manager.py backup

# Update struktur database
python db_manager.py migrate
```

### User Default (setelah seed)
- Username: `admin`, Password: `admin123`
- Username: `demo`, Password: `demo123`
- Username: `test`, Password: `test123`

## File Struktur

```
backend/
├── app.py              # Main application
├── config.py           # Configuration
├── models.py           # Database models
├── forms.py            # WTForms
├── extensions.py       # Flask extensions
├── db_manager.py       # Database management script
├── requirements.txt    # Python dependencies
├── instance/           # Database files
│   └── rentry.sqlite   # SQLite database
├── templates/          # HTML templates
└── static/            # CSS/JS files
```

## Development Tips

1. **Database Changes**: Selalu backup sebelum mengubah struktur
2. **Testing**: Gunakan data sample dengan `python db_manager.py seed`
3. **Debug**: Set `debug=True` di app.py untuk development
4. **Environment**: Gunakan `.env` untuk konfigurasi sensitif

## Production Deployment

1. Set environment variables:
   ```bash
   export SECRET_KEY="your-secret-key"
   export DATABASE_URL="your-database-url"
   ```

2. Use production WSGI server:
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

3. Setup reverse proxy (nginx/apache)
4. Enable HTTPS
5. Setup regular database backups