import sqlite3
from flask import render_template
from flask import Flask, request, redirect, session, flash, url_for


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


lista_usuarios = [
    Usuario('Abade', 'raphaelabade10@gmail.com', '123'),
    Usuario('ZGamezin', 'zgames@gmail.com', 'abc')
]

dict_usuarios = {usuario.email: usuario for usuario in lista_usuarios}


def bd_connect():
    conn = sqlite3.connect('database.db', isolation_level=None)
    conn.row_factory = sqlite3.Row
    return conn


def bd_cursor(conn, execute):
    cur = conn.cursor()
    cur.execute(execute)
    cur.close()


def add(request):
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    conn = bd_connect()
    bd_cursor(conn, f"""INSERT INTO users (nome, email, senha) VALUES
    ('{nome}', '{email}', '{senha}')""")
    conn.commit()
    conn.close()
    return flash('Cadastramento efetuado!')


def buscar(email, senha):
    usuario = dict_usuarios.get(email)
    if usuario != None and usuario.senha == senha:
        return usuario
    else:
        return None


def buscar_por_email(email):
    return dict_usuarios.get(email, None)

 # em manutenção!!
