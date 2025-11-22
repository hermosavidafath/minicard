# backend/app.py
import os, secrets
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from config import Config
from extensions import db, login_manager, csrf, limiter
from models import User, Paste
from forms import RegisterForm, LoginForm, PasteForm
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime

# optional markdown rendering
try:
    import markdown2
    HAVE_MARKDOWN = True
except Exception:
    HAVE_MARKDOWN = False

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)

    # init extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)

    login_manager.login_view = 'login'

    # register user loader for flask-login
    @login_manager.user_loader
    def load_user(user_id):
        try:
            return User.query.get(int(user_id))
        except Exception:
            return None

    # create instance folder (for sqlite file if using relative path)
    os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

    # register routes
    @app.route('/')
    def index():
        pastes = Paste.query.filter_by(public=True).order_by(Paste.created_at.desc()).limit(50).all()
        return render_template('index.html', pastes=pastes)

    @app.route('/register', methods=['GET','POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            if User.query.filter_by(username=form.username.data).first():
                flash('Username sudah dipakai')
                return redirect(url_for('register'))
            u = User(username=form.username.data)
            u.set_password(form.password.data)
            db.session.add(u)
            db.session.commit()
            flash('Akun dibuat, silakan login')
            return redirect(url_for('login'))
        return render_template('register.html', form=form)

    @app.route('/login', methods=['GET','POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            u = User.query.filter_by(username=form.username.data).first()
            if u and u.check_password(form.password.data):
                login_user(u)
                flash('Logged in')
                return redirect(url_for('index'))
            flash('Invalid credentials')
            return redirect(url_for('login'))
        return render_template('login.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Logged out')
        return redirect(url_for('index'))

    @app.route('/new', methods=['GET','POST'])
    @limiter.limit("10 per minute")
    def new_paste():
        form = PasteForm()
        if form.validate_on_submit():
            slug = secrets.token_urlsafe(6)
            edit_token = secrets.token_urlsafe(16)
            p = Paste(slug=slug, title=form.title.data, content=form.content.data,
                      public=bool(form.public.data), edit_token=edit_token)
            if current_user.is_authenticated:
                p.owner = current_user
            db.session.add(p)
            db.session.commit()
            flash(f'Paste dibuat. Link: {request.url_root.rstrip("/")}/{slug} — Edit token: {edit_token}')
            return redirect(url_for('view_paste', slug=slug))
        return render_template('new.html', form=form)

    @app.route('/<slug>')
    def view_paste(slug):
        p = Paste.query.filter_by(slug=slug).first_or_404()
        if not p.public:
            if not current_user.is_authenticated or (p.owner_id != current_user.id):
                abort(403)
        rendered_html = None
        if HAVE_MARKDOWN:
            try:
                rendered_html = markdown2.markdown(p.content)
            except Exception:
                rendered_html = None
        can_edit = current_user.is_authenticated and p.owner_id == current_user.id
        return render_template('view.html', paste=p, rendered_html=rendered_html, can_edit=can_edit)

    @app.route('/<slug>/edit', methods=['GET','POST'])
    @login_required
    def edit_paste(slug):
        p = Paste.query.filter_by(slug=slug).first_or_404()
        if p.owner_id != current_user.id:
            flash('Kamu bukan pemilik paste ini')
            return redirect(url_for('view_paste', slug=slug))
        form = PasteForm(obj=p)
        if form.validate_on_submit():
            p.title = form.title.data
            p.content = form.content.data
            p.public = bool(form.public.data)
            db.session.commit()
            flash('Berhasil disimpan')
            return redirect(url_for('view_paste', slug=slug))
        return render_template('edit.html', form=form, paste=p)

    @app.route('/<slug>/delete', methods=['POST'])
    @login_required
    def delete_paste(slug):
        p = Paste.query.filter_by(slug=slug).first_or_404()
        if p.owner_id != current_user.id:
            abort(403)
        db.session.delete(p)
        db.session.commit()
        flash('Paste dihapus')
        return redirect(url_for('index'))

    @app.route('/mypastes')
    @login_required
    def mypastes():
        pastes = Paste.query.filter_by(owner_id=current_user.id).order_by(Paste.created_at.desc()).all()
        return render_template('mypastes.html', pastes=pastes)

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('base.html', body='<div class="card">Forbidden — private paste.</div>'), 403

    return app


# When running directly, create app and ensure DB exists inside app context
if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        # create tables if not present
        db.create_all()
        db_path = app.config.get('SQLALCHEMY_DATABASE_URI', '')
        print('Using DB:', db_path)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
