from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.user import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash('E-mail já cadastrado no sistema.', 'danger')
            return redirect(url_for('auth.cadastro'))

        novo_usuario = User(nome=nome, email=email, senha=senha, tipo_usuario='comum')
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Conta criada com sucesso! Faça seu login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('cadastro.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        user = User.query.filter_by(email=email, senha=senha).first()
        if user:
            session['user_id'] = user.id
            session['user_nome'] = user.nome
            session['user_tipo'] = user.tipo_usuario
            flash(f'Bem-vindo(a), {user.nome}!', 'success')
            return redirect(url_for('user.index'))
        else:
            flash('Credenciais inválidas. Verifique seu e-mail e senha.', 'danger')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Sessão encerrada com sucesso.', 'info')
    return redirect(url_for('auth.login'))