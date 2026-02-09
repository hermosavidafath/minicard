# Database Documentation

## Overview
Aplikasi ini menggunakan SQLite sebagai database dengan SQLAlchemy sebagai ORM.

## Struktur Database

### Tabel User
- `id`: Primary key
- `username`: Username unik
- `password_hash`: Password yang di-hash
- `created_at`: Waktu pembuatan akun

### Tabel Profile
- `id`: Primary key
- `slug`: URL slug unik untuk profil
- `display_name`: Nama tampilan
- `bio`: Biografi
- `age`: Umur
- `location`: Lokasi
- `interests`: Minat/hobi
- `social_links`: JSON string berisi link media sosial
- `avatar_url`: URL avatar
- `background_color`: Warna background
- `text_color`: Warna teks
- `accent_color`: Warna aksen
- `created_at`: Waktu pembuatan
- `updated_at`: Waktu update terakhir
- `public`: Apakah profil publik
- `owner_id`: Foreign key ke User

### Tabel Paste
- `id`: Primary key
- `slug`: URL slug unik untuk paste
- `title`: Judul paste
- `content`: Isi paste
- `created_at`: Waktu pembuatan
- `updated_at`: Waktu update terakhir
- `public`: Apakah paste publik
- `owner_id`: Foreign key ke User (nullable untuk anonymous paste)
- `edit_token`: Token untuk edit tanpa login

## Konfigurasi Database

Database dikonfigurasi di `config.py`:
```python
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or default_sqlite_uri
```

Default menggunakan SQLite di `backend/instance/rentry.sqlite`

## Script Management

### db_manager.py
Script utama untuk mengelola database:

```bash
# Periksa status database
python db_manager.py check

# Backup database
python db_manager.py backup

# Migrasi database (update struktur tanpa hapus data)
python db_manager.py migrate

# Inisialisasi database baru (hapus semua data)
python db_manager.py init

# Isi dengan data sample
python db_manager.py seed
```

### Script Lainnya
- `init_db.py`: Inisialisasi database dengan user admin default
- `check_db.py`: Periksa struktur dan isi database
- `migrate_db.py`: Migrasi database dengan backup otomatis

## Environment Variables

Untuk production, set environment variable:
```bash
DATABASE_URL=sqlite:///path/to/production.db
# atau untuk PostgreSQL:
DATABASE_URL=postgresql://user:pass@localhost/dbname
```

## Backup & Recovery

Database SQLite otomatis di-backup saat migrasi dengan format:
`rentry.sqlite.backup_YYYYMMDD_HHMMSS`

## Tips

1. **Development**: Gunakan SQLite (default)
2. **Production**: Pertimbangkan PostgreSQL atau MySQL
3. **Backup**: Jalankan backup berkala dengan `db_manager.py backup`
4. **Migrasi**: Selalu backup sebelum migrasi struktur database

## Troubleshooting

### Database tidak ada
```bash
python db_manager.py init
```

### Struktur tidak sesuai
```bash
python db_manager.py migrate
```

### Perlu data testing
```bash
python db_manager.py seed
```