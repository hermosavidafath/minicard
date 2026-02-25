# MyCard

MyCard adalah platform sederhana untuk membuat personal bio page yang bisa dibagikan dengan link unik.

Users dapat membuat card, mengatur tampilan warna, dan menambahkan informasi personal dengan tampilan yang clean dan minimal.

## ✨ Features

- 🎨 Customizable bio card (color & style)
- 📝 Create and manage multiple cards
- 🔐 User authentication (register & login)
- 🔗 Unique shareable link
- 📱 Responsive design
- 🗄️ PostgreSQL database

## 🛠️ Tech Stack

- Python (Flask)
- PostgreSQL
- SQLAlchemy
- WTForms
- HTML, CSS
- Gunicorn (production)

## 🚀 Run Locally

```bash
git clone <repo-url>
cd backend
pip install -r requirements.txt

export DATABASE_URL="postgresql://user:password@localhost:5432/mycard_dev"
export SECRET_KEY="your-secret-key"

python app.py
DATABASE_URL=postgresql://user:password@host:port/database
SECRET_KEY=your-secret-key
FLASK_ENV=production
backend/
├── app.py
├── models.py
├── forms.py
├── config.py
├── templates/
└── static/
