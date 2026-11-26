from flask import Blueprint, render_template, session, redirect, url_for, flash
from app.models.user import User

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/usuarios')
def lista_usuarios():
    if 'user_id' not in session:
        flash('Efetue o login primeiro.', 'warning')
        return redirect(url_for('auth.login'))

    if session.get('user_tipo') != 'admin':
        flash('Acesso negado! Recurso exclusivo para administradores.', 'danger')
        return redirect(url_for('user.index'))

    usuarios = User.query.all()
    return render_template('admin_lista.html', usuarios=usuarios)