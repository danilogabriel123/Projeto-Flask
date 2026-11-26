from flask import Blueprint, render_template, session, redirect, url_for, flash
from app.models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def index():
    return render_template('index.html')

@user_bp.route('/perfil')
def perfil():
    if 'user_id' not in session:
        flash('Acesso restrito. Efetue o login para continuar.', 'warning')
        return redirect(url_for('auth.login'))

    usuario = User.query.get(session['user_id'])
    return render_template('perfil.html', usuario=usuario)