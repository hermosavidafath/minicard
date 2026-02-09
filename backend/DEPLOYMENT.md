# Deployment Guide

## Platform Hosting Options

### 1. Heroku (Recommended untuk pemula)

#### Setup:
```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login ke Heroku
heroku login

# Buat aplikasi baru
heroku create your-app-name

# Set environment variables
heroku config:set SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')
heroku config:set FLASK_ENV=production

# Deploy
git add .
git commit -m "Ready for deployment"
git push heroku main
```

#### One-Click Deploy:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### 2. Railway

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
railway up
```

### 3. Render

1. Connect GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `gunicorn wsgi:application`
4. Set environment variables

### 4. PythonAnywhere

1. Upload files via web interface
2. Create web app with manual configuration
3. Set WSGI file to point to `wsgi.py`
4. Install requirements in console

### 5. DigitalOcean App Platform

1. Connect GitHub repository
2. Auto-detect Python app
3. Set environment variables
4. Deploy

## Environment Variables untuk Production

```bash
SECRET_KEY=your-super-secret-key-here
FLASK_ENV=production
DATABASE_URL=your-database-url
RATELIMIT_DEFAULT=1000 per day;100 per hour
```

## Database untuk Production

### PostgreSQL (Recommended)
```bash
# Heroku
heroku addons:create heroku-postgresql:mini

# Manual setup
pip install psycopg2-binary
# Set DATABASE_URL=postgresql://user:pass@host:port/db
```

### SQLite (Simple)
- Sudah dikonfigurasi secara default
- Cocok untuk traffic rendah-menengah
- File database akan hilang saat redeploy di beberapa platform

## Pre-deployment Checklist

- [ ] Set SECRET_KEY yang kuat
- [ ] Set FLASK_ENV=production
- [ ] Konfigurasi database production
- [ ] Test aplikasi lokal dengan `gunicorn wsgi:application`
- [ ] Commit semua perubahan ke Git
- [ ] Set rate limiting sesuai kebutuhan

## Testing Production Setup

```bash
# Test dengan gunicorn
pip install gunicorn
gunicorn wsgi:application

# Test dengan environment production
export FLASK_ENV=production
export SECRET_KEY=test-secret-key
python wsgi.py
```

## Monitoring & Maintenance

1. **Logs**: Monitor aplikasi logs untuk error
2. **Database**: Backup database secara berkala
3. **Updates**: Update dependencies secara berkala
4. **Security**: Monitor untuk vulnerability

## Custom Domain

Setelah deploy, kamu bisa setup custom domain:
- Heroku: `heroku domains:add yourdomain.com`
- Railway: Setup di dashboard
- Render: Setup di dashboard

## SSL Certificate

Semua platform modern sudah include SSL gratis:
- Let's Encrypt certificate otomatis
- HTTPS redirect sudah dikonfigurasi di `config.py`