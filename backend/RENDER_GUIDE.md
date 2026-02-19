# 🚀 Panduan Deploy ke Render.com

## Mengapa Render?
- ✅ **Gratis** untuk PostgreSQL + Web Service
- ✅ **Auto SSL** certificate
- ✅ **Auto deploy** dari GitHub
- ✅ **Mudah** setup database
- ✅ **Reliable** untuk production

---

## 📋 Step-by-Step Guide

### STEP 1: Persiapan Repository
```bash
# Pastikan semua file sudah di-commit
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### STEP 2: Buat Database PostgreSQL

1. **Login** ke [render.com](https://render.com)
2. **Dashboard** → **New** → **PostgreSQL**
3. **Settings**:
   ```
   Name: rentry-db
   Database: rentry  
   User: rentry
   Region: Oregon (US West)
   PostgreSQL Version: 15
   Plan: Free
   ```
4. **Create Database**
5. **PENTING**: Copy **Internal Database URL**
   ```
   postgresql://rentry:xxxxx@dpg-xxxxx-a.oregon-postgres.render.com/rentry
   ```

### STEP 3: Deploy Web Service

1. **Dashboard** → **New** → **Web Service**
2. **Connect Repository**: Pilih GitHub repo kamu
3. **Settings**:
   ```
   Name: rentry-app
   Root Directory: backend
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn wsgi:application
   Plan: Free
   ```

### STEP 4: Environment Variables

Di **Web Service** → **Environment**:

| Name | Value |
|------|-------|
| `DATABASE_URL` | `postgresql://rentry:xxxxx@dpg-xxxxx-a.oregon-postgres.render.com/rentry` |
| `SECRET_KEY` | `[generate random 64 char string]` |
| `FLASK_ENV` | `production` |

**Generate SECRET_KEY**:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### STEP 5: Deploy!

1. **Create Web Service**
2. **Wait** for build & deploy (5-10 menit)
3. **Check logs** untuk error
4. **Test** aplikasi di URL yang diberikan

---

## ✅ Verification

Setelah deploy berhasil:

1. **Buka URL** aplikasi (https://rentry-app.onrender.com)
2. **Register** user baru
3. **Create paste** 
4. **Create profile**
5. **Refresh page** → data masih ada ✅

---

## 🔧 Troubleshooting

### Build Failed
**Error**: `No module named 'psycopg2'`
**Fix**: Pastikan `psycopg2-binary==2.9.7` ada di requirements.txt

### Database Connection Error
**Error**: `DATABASE_URL environment variable is required`
**Fix**: Set DATABASE_URL di Environment Variables

### App Crashes
**Error**: `relation "user" does not exist`
**Fix**: Database tables belum dibuat
- Check logs untuk error detail
- Tables akan auto-create saat first run

### Slow Cold Start
**Normal**: Free tier sleep setelah 15 menit idle
**Fix**: Upgrade ke paid plan ($7/month) untuk always-on

---

## 📊 Free Tier Limits

**PostgreSQL Free**:
- 1 GB storage
- 1 million rows
- 97 connection limit

**Web Service Free**:
- 750 hours/month
- Sleep after 15 min idle
- 512 MB RAM
- 0.1 CPU

---

## 🚀 Production Tips

### Custom Domain
1. **Web Service** → **Settings** → **Custom Domains**
2. Add your domain
3. Update DNS CNAME record

### Environment Management
- Use separate databases for staging/production
- Never commit secrets to Git
- Use Render's secret management

### Monitoring
- Check **Metrics** tab for performance
- Monitor **Logs** for errors
- Set up **Alerts** for downtime

### Scaling
- Upgrade to **Starter** plan ($7/month) for:
  - Always-on (no sleep)
  - More resources
  - Better performance

---

## 💡 Pro Tips

1. **Database Backup**: Render auto-backups, but export important data
2. **Environment Sync**: Keep staging/production env vars in sync
3. **Health Checks**: Add `/health` endpoint untuk monitoring
4. **Logging**: Use structured logging untuk debugging
5. **Caching**: Add Redis untuk better performance

---

## 🆘 Support

**Render Issues**:
- [Render Docs](https://render.com/docs)
- [Community Forum](https://community.render.com)
- Support ticket via dashboard

**App Issues**:
- Check application logs
- Verify environment variables
- Test database connection

---

## 🎉 Success!

Jika semua berjalan lancar, aplikasi kamu sekarang:
- ✅ **Live** di internet
- ✅ **Secure** dengan HTTPS
- ✅ **Scalable** dengan PostgreSQL
- ✅ **Reliable** dengan Render infrastructure

**Share URL kamu dan biarkan orang lain pakai!** 🚀