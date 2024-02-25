from flask import Flask, render_template, request, redirect, url_for
import plotly.graph_objs as go
import sqlite3

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    # Conexão com o banco de dados
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    # Cosulta para pagamentos realizados
    cursor.execute("""
        SELECT f.nome, e.nome_fantasia, p.valor, p.data_pagamento
        FROM pagamentos p
        INNER JOIN funcionarios f ON p.nome_func = f.nome
        INNER JOIN empresas_terc e ON f.id_empresa = e.id
        """)
    pagamentos = cursor.fetchall()

    # Feche a conexão com o banco de dados
    cursor.close()
    conn.close()

    return render_template('index.html', pagamentos=pagamentos)

if __name__ == '__main__':
    app.run()


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/enviar_login', methods=['POST'])
def enviar_login():
    nome = request.form['nome']
    email = request.form['email']

    # Conexão com o banco de dados
    conn = sqlite3.connect('project.db')
    c = conn.cursor()

    # Aqui é feita a consulta no banco de dados
    c.execute("SELECT * FROM cadastro WHERE nome = ? AND email = ?", (nome, email))
    user = c.fetchone()

    # Aqui Verificamos se o usuário existe
    if user:
        return redirect(url_for('index'))
    else:
        return 'Usuário não cadastrado'


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/enviar_cadastro', methods=['POST'])
def enviar_cadastro():
    nome = request.form['nome']
    email = request.form['email']


    # Conexão com o banco de dados
    conn = sqlite3.connect('project.db')
    c = conn.cursor()

    # Insira os dados do login
    c.execute("INSERT INTO cadastro (nome, email) VALUES (?, ?)",
              (nome, email))

    # Salve as alterações no banco de dados e encerre a conexão
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


@app.route('/funcionarios')
def funcionarios():

    # Conexão com o banco de dados
    conn = sqlite3.connect('project.db')
    c = conn.cursor()

    # Captura as empresas da tabela
    c.execute("SELECT id, nome_fantasia FROM empresas_terc")
    empresas = c.fetchall()

    # Feche a conexão com o banco de dados
    conn.close

    return render_template('funcionarios.html', empresas=empresas)

def cpf_valido(cpf):
    # Lógica para validar o CPF
    return True  # ou False


@app.route('/enviar_funcionarios', methods=['POST'])
def enviar_funcionarios():
    nome = request.form['nome']
    cpf = request.form['cpf']
    contato = request.form['contato']
    id_empresa = request.form['empresa']

    if not cpf_valido(cpf):
        flash('CPF inválido')
        return redirect(url_for('funcionarios'))

    # Conexão com o banco de dados
    conn = sqlite3.connect('project.db')
    c = conn.cursor()

    # Insira os dados do funcionário para cadastro
    c.execute("INSERT INTO funcionarios (nome, cpf, contato, id_empresa) VALUES (?, ?, ?, ?)", (nome, cpf, contato, id_empresa))

    # Salve as alterações no banco de dados e encerre a conexão
    conn.commit()
    conn.close()

    return redirect(url_for('funcionarios'))

@app.route('/pagamentos')
def pagamentos():
    # Conexão com o banco de dados
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    # Obtenha a lista de nomes de funcionários da tabela "funcionários"
    cursor.execute("""SELECT id, nome FROM funcionarios""")

    funcionarios = cursor.fetchall()


    pagamentos = cursor.fetchall()

    # Feche a conexão com o banco de dados
    cursor.close()
    conn.close()

    return render_template('pagamentos.html', pagamentos=pagamentos, funcionarios=funcionarios)


@app.route('/edit_pagamento/<string:id>', methods=['POST'])
def processar_edicao_pagamento(id):
    nome_func = request.form['nome_func']
    tipo = request.form['tipo']
    valor = request.form['valor']
    data_pagamento = request.form['data']

    #Verifique se o valor de tipo é valido
    if tipo not in ('especie', 'cartao'):
        return 'Tipo inválido'

    # Conexão com o banco de dados
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    # Insira os dados do pagamento para cadastro
    cursor.execute("INSERT INTO pagamentos (nome_func, tipo, valor, data_pagamento) VALUES (?, ?, ?, ?)", (nome_func, tipo, valor, data_pagamento))

    # Salve as alterações no banco de dados e encerre a conexão
    conn.commit()
    conn.close()

    return redirect(url_for('pagamentos'))

if __name__ == '__main__':
    app.run()

@app.route('/empresas_terc')
def empresas_terc():
    return render_template('empresas_terc.html')


@app.route('/enviar_empresas_terc', methods=['POST'])
def enviar_empresas_terc():
    razao_social = request.form['razao_social']
    nome_fantasia = request.form['nome_fantasia']
    cnpj = request.form['cnpj']
    endereco = request.form['endereco']
    bairro = request.form['bairro']
    cidade = request.form['cidade']
    estado = request.form['estado']
    pais = request.form['pais']

   # Conexão com o banco de dados
    conn = sqlite3.connect('project.db')
    c = conn.cursor()

    # Insira os dados do login
    c.execute("INSERT INTO empresas_terc (razao_social, nome_fantasia, cnpj, endereco, bairro, cidade, estado, pais) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (razao_social, nome_fantasia, cnpj, endereco, bairro, cidade, estado, pais))

    # Salve as alterações no banco de dados e encerre a conexão
    conn.commit()
    conn.close()

    return redirect(url_for('empresas_terc'))


@app.route('/dashboard')
def dashboard():
    # Conexão com o banco de dados
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    # Consulta para obter a soma dos valores por empresa terceirizada
    cursor.execute("""
        SELECT e.nome_fantasia, SUM(p.valor)
        FROM pagamentos p
        INNER JOIN funcionarios f ON p.nome_func = f.nome
        INNER JOIN empresas_terc e ON f.id_empresa = e.id
        GROUP BY e.nome_fantasia
    """)
    resultados = cursor.fetchall()

    # Feche a conexão com o banco de dados
    cursor.close()
    conn.close()

    # Extrai os dados da consulta para criar o gráfico
    empresas = [resultado[0] for resultado in resultados]
    valores = [resultado[1] for resultado in resultados]

    # Cria o objeto de gráfico de barras
    data = [go.Bar(x=empresas, y=valores)]

    # Define o layout do gráfico
    layout = go.Layout(title='Soma dos Valores por Empresa Terceirizada')

    # Cria a figura do gráfico
    fig = go.Figure(data=data, layout=layout)

    return render_template('dashboard.html', fig=fig)


# Editar pagamentos
@app.route('/editar/<string:id>', methods=['GET', 'POST'])
def form_pagamento(id):

    if request.method == 'GET':

        # Conexão com o banco de dados
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()
        print(id)
        # Consulta para obter as informações do pagamento com o ID fornecido
        cursor.execute("""
            SELECT p.id, f.nome, e.nome_fantasia, p.valor, p.data_pagamento
            FROM pagamentos p
            INNER JOIN funcionarios f ON p.nome_func = f.nome
            INNER JOIN empresas_terc e ON f.id_empresa = e.id
            WHERE p.id = ?;
            """, (id,))
        pagamento = cursor.fetchone()


        # Feche a conexão com o banco de dados
        cursor.close()
        conn.close()

        if pagamento:
            return render_template('editar.html', id=id, pagamento=pagamento)
        else:
            return "Pagamento não encontrado."

    elif request.method == 'POST':
        # Obtém os novos valores dos campos do formulário
        nome_func = request.form.get('nome_func')
        novo_valor = request.form.get('valor')
        nova_data_pagamento = request.form.get('data')

        # Conexão com o banco de dados
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()

        # Executa a consulta de atualização
        cursor.execute("""
            UPDATE pagamentos
            SET nome_func = ?, valor = ?, data_pagamento = ?
            WHERE id = ?
            """, (nome_func, novo_valor, nova_data_pagamento, id))

        # Confirma as alterações
        conn.commit()

        # Feche a conexão com o banco de dados
        cursor.close()
        conn.close()

        return redirect('/index')  # Redirecionar para a página inicial após a edição


@app.route('/excluir/<id>', methods=['GET', 'POST'])
def excluir_pagamento(id):
    if request.method == 'GET':

        # Conexão com o banco de dados
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()

        # Consulta para obter as informações do pagamento com o ID fornecido
        cursor.execute("""
            DELETE FROM pagamentos
            WHERE id = ?
            """, (id,))
        pagamento = cursor.fetchone()

        # Feche a conexão com o banco de dados
        cursor.close()
        conn.close()

        if pagamento:
            return render_template('excluir.html', id=id, pagamento=pagamento)
        else:
            return "Pagamento não encontrado."

    elif request.method == 'POST':
        # Processar a atualização do pagamento
        # Código para atualizar os dados do pagamento no banco de dados

        return redirect('/index')  # Redirecionar para a página inicial após a edição



    if __name__ == '__main__':
        app.run(port=8080)
