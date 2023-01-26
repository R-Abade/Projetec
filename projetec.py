from flask import render_template
from flask import Flask, request, redirect, session, flash, url_for
import usuarios

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', titulo="Home")


@app.route('/atv-metas')
def atv_metas():
    return render_template('atv_metas.html', titulo='Atividades')


@app.route('/qs')
def quem_somos():
    return render_template('qs.html', titulo='Quem Somos')


@app.route('/login')
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = usuarios.buscar(email, senha)
        if usuario is None:
            flash('Usuário/ Senha Inválidos.')
        else:
            session['usuario_email'] = usuario.email
            session['usuario_nome'] = usuario.nome
            return redirect(url_for('index'))
    return render_template('login.html', titulo='login')


@app.route('/logout')
def logout():
    session.pop('usuario_email', None)
    session.pop('usuario_nome', None)
    return redirect(url_for('index'))


app.run(debug=True)



 # em manutenção!!