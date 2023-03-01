import sqlite3
from flask import render_template
from flask import Flask, request, redirect, session, flash, url_for, abort, g
import usuarios


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * from posts WHERE id =?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)
app.secret_key = 'opa'


@app.route('/')
def home():
    return render_template('home.html', titulo="Home")


@app.route('/atv-metas')
def atv_metas():
    return render_template('atv_metas.html', titulo='Atividades')


@app.route('/qs')
def quem_somos():
    return render_template('qs.html', titulo='Quem Somos')


@app.route('/cadastrarUser', methods=('GET', 'POST'))
# def cadUser():
#   if request.method == 'POST':
#      nome = request.form['nome']
#     email = request.form['email']
#    senha = request.form['senha']
#   conn = get_db_connection()
#  usuario = usuarios.buscar(nome, email, senha)
# if usuario != None:
#    flash('Usuário existente!')
#   return redirect(url_for('home'))
# else:
# conn = usuarios.bd_connect()
#   usuarios.bd_cursor(conn, f"""INSERT INTO users (nome, email, senha) VALUES
# ('{nome}', '{email}', '{senha}')""")
# conn.close()
# return redirect(url_for('home'))
# return render_template('cadastrarUser.html')
@app.route('/cadastrarUser', methods=(['POST', 'GET']))
def cadUser():
    if request.method == 'POST':
        add = usuarios.add(request)
        if add[0]:
            flash(add[0])
            return redirect(url_for('home'))
        session["usuario_email"] = add[1]
        return redirect(url_for('home'))

    for user in g:
        return redirect(url_for('home'))
    return render_template("cadastrarUser.html")


@app.route('/login', methods=['GET', 'POST'])
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
            return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario_email', None)
    session.pop('usuario_nome', None)
    return redirect(url_for('home'))


def usuario_logado():
    return 'usuario_email' in session


@app.errorhandler(403)
def acesso_negado(erro):
    return render_template('acesso_negado.html', titulo='Ops!'), 403


app.run(debug=True)


# em manutenção!!
