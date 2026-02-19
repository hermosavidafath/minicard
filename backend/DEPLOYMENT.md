# Deployment Guide - PostgreSQL ONLY

## ⚠️ PENTING: SQLite TIDAK COCOK untuk Production!

**Mengapa SQLite tidak bisa:**
- File database hilang saat restart di cloud
- Tidak support multiple users concurrent
- Render/Heroku tidak menyimpan file permanen

**Solusi: WAJIB pakai PostgreSQL!**

---

## 🚀 RENDER DEPLOYMENT (Recommended)

### Step 1: Persiapan Code
```bash
# Pastikan .gitignore sudah benar
git add .
git commit -m "Ready for PostgreSQL deployment"
git push origin main
```

### Step 2: Buat Database di Render
1. Login ke [Render.com](https://render.com)
2. Dashboard → **New** → **PostgreSQL**
3. Settings:
   - **Name**: `rentry-db`
   - **Database**: `rentry`
   - **User**: `rentry`
   - **Region**: Oregon (US West)
   - **Plan**: Free
4. **Create Database**
5. **Copy Internal Database URL** (postgresql://...)

### Step 3: Deploy Web Service
1. Dashboard → **New** → **Web Service**
2. Connect GitHub repository
3. Settings:
   - **Name**: `rentry-app`
   - **Root Directory**: `backend`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn wsgi:application`

### Step 4: Environment Variables
Di Web Service → Environment:
```
DATABASE_URL = [paste Internal Database URL dari Step 2]
SECRET_KEY = [generate random string]
FLASK_ENV = production
```

### Step 5: Deploy!
Klik **Create Web Service** → Deploy otomatis!

---

## 🔧 HEROKU DEPLOYMENT

### Prerequisites
```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli
heroku login
```

### Deploy Steps
```bash
cd backend

# Create app
heroku create your-app-name

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:mini

# Set environment variables
heroku config:set SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')
heroku config:set FLASK_ENV=production

# Deploy
git push heroku main
```

---

## 🚂 RAILWAY DEPLOYMENT

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway up

# Add PostgreSQL
railway add postgresql

# Set environment variables di dashboard
```

---

## 🐳 DOCKER + PostgreSQL

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/rentry
      - SECRET_KEY=your-secret-key
      - FLASK_ENV=production
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: rentry
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

```bash
docker-compose up -d
```

---

## ✅ Verification Checklist

Setelah deploy, cek:
- [ ] App bisa diakses via URL
- [ ] Database connection OK
- [ ] Bisa register user baru
- [ ] Bisa create paste
- [ ] Bisa create profile
- [ ] Data tersimpan setelah refresh

---

## 🆘 Troubleshooting

### Error: "DATABASE_URL environment variable is required"
**Solusi**: Set DATABASE_URL di environment variables

### Error: "relation does not exist"
**Solusi**: Database tables belum dibuat
```bash
# Di Render console atau Heroku:
python -c "from wsgi import application; application.app_context().push(); from extensions import db; db.create_all()"
```

### Error: "psycopg2 not found"
**Solusi**: Pastikan `psycopg2-binary` ada di requirements.txt

---

## 🔒 Security Notes

- SECRET_KEY harus unique per deployment
- DATABASE_URL jangan di-commit ke Git
- Gunakan environment variables untuk semua config
- Enable HTTPS (otomatis di Render/Heroku)

---

## 💰 Cost Estimate

**Render (Recommended):**
- PostgreSQL: Free (1GB storage)
- Web Service: Free (750 hours/month)

**Heroku:**
- PostgreSQL: Free tier discontinued
- Dyno: $7/month minimum

**Railway:**
- $5/month untuk usage-based pricing