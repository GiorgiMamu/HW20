from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from db import db, init_db
from models import User, Note
from forms import RegisterForm, LoginForm, NoteForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '097d0b65c5d89fa9da3e425a90167fd1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'

init_db(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('notes'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Email already registered', 'warning')
            return redirect(url_for('login'))
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('notes'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('notes'))
        flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful', 'success')
    return redirect(url_for('login'))

@app.route('/')
@app.route('/notes')
@login_required
def notes():
    notes = Note.query.filter_by(user_id=current_user.id).order_by(Note.created_at.desc()).all()
    return render_template('notes.html', notes=notes)

@app.route('/add_note', methods=['GET', 'POST'])
@login_required
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(content=form.content.data, user_id=current_user.id)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('notes'))
    return render_template('add_note.html', form=form)

@app.route('/delete_note/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get(note_id)
    if not note:
        abort(404)
    if note.user_id != current_user.id:
        flash('You are not authorized to delete this note', 'danger')
        return redirect(url_for('notes'))
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted', 'success')
    return redirect(url_for('notes'))


if __name__ == '__main__':
    app.run(debug=True)
