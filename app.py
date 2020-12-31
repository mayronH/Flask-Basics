"""Arquivo principal da aplicacao em flask, as configuracoes e a inicializacao acontece aqui"""
import os

from flask import abort
from flask import Flask
from flask import flash
from flask import make_response
from flask import render_template
from flask import redirect 
from flask import request
from flask import session
from flask import url_for
from werkzeug.utils import secure_filename

app = Flask(__name__) #Criando um Objeto da classe Flask

# Variáveis globais
UPLOAD_FOLDER = 'files'

# Configurações para a aplicação Flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024 # 3mb
# Configura a SECRET_KEY, necessária para as sessions
app.secret_key = b'\xa2\xec\xb0\xb6\xf6(\x8e@\xbe\r&\xa6\xc0\xe22h'

# Cria uma rota /
@app.route('/') #decorator
# Nessa rota chama a função index
def index():
    # Que retorna "Hello World!"
	return "Hello World!"


# Cria uma rota dinámica em que o nome é uma string que pode váriar
@app.route('/home/<name>')
# Passa o paramêtro da url para a função
def home(name):
    """Pega um parametro da url e apresenta na tela"""
    return "Hello, " + name


# Especifíca o paramêtro para integer
@app.route('/age/<int:age>')
def age(age):
    """Função que pega o parametro inteiro da url e apresenta na tela"""
    # Formata String
    return "Idade: %d"%age


# No lugar de criar uma rota com o decorator cria somente a função
def about():
	return "Sobre: "

# Cria a rota /about e chama a função about()
app.add_url_rule("/about", "about", about)

@app.route('/admin')
def admin():
    return 'admin'


@app.route('/librarion')
def librarion():
    return 'librarion'


@app.route('/student')
def student():
    return 'student'


@app.route('/user/<name>')
def user(name):
    """Função para redirecionar para outras funções de acordo com o parametro da url"""
    if name == 'admin':
        # Função para redirecionar para a função com o nome admin
        return redirect(url_for('admin'))
    if name == 'librarion':
        return redirect(url_for('librarion'))
    if name == 'student':
        return redirect(url_for('student'))


@app.route('/hello/<user>')
def message(user):
    """Pega um parametro e envia para um template"""
    # Passar um objeto para o template
    return render_template('message.html', name=user)


@app.route('/table/<int:num>')
def table(num):
    return render_template('tableOf.html', n=num)


@app.route('/signup')
def signUpForm():
    """Registrar"""
    return render_template('singup.html')


# Cria 2 rotas success, uma para POST e outra para GET
@app.route('/success', methods=['POST', 'GET'])
def printData():
    """Processa a informações do registro"""
    if request.method == 'POST':
        # O .form é um dicionário que contem um par de chave-valor vindo dos parametros do form
        result = request.form
        
        return render_template("showData.html", result=result)
    # Retorna para uma página de erro com status code 401
    abort(401)
    # É possível mudar a mensagem de erro
    # abort(401, description="Não permitido")


@app.route('/cookie')
def cookie():
    """Cria um cookie"""
    # Função make_response converte o valor de uma view para uma instância response
    res = make_response("<h1>Cookie is set</h1>")
    # set_cookie é uma função da classe response, serve para armazenar a informação em um cookie(nome, conteudo, tempo de vida)
    res.set_cookie('foo', 'bar')

    return res

@app.route('/session')
def testSession():
    """Cria uma session"""
    res = make_response("<p>Variável da sessão criada, <a href='/get'>get variable</a></p>")
    session['response'] = 'session#1'
    
    return res


@app.route('/get')
def getVariable():
    """Pega uma session armazenada na aplicação"""
    if 'response' in session:
        s = session['response']
        
        return render_template('getSession.html', name=s)


@app.route('/upload')
def upload():
    """Formulario de upload"""
    return render_template("uploadForm.html")


@app.route('/uploadPost', methods=['POST'])
def filePost():
    """Processa as informações do upload e armazena o arquivo"""
    if request.method == 'POST':
        # Pega as informações do arquivo enviado pelo formulário
        f = request.files['file']

        # Valida quaisquer problemas que possa ter com o nome do arquivo enviado
        filename = secure_filename(f.filename)

        # Salva o arquivo na pasta configurada em UPLOAD_FOLDER
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return render_template('uploadedFile.html', name = filename)


@app.route('/homelogin')  
def homeLogin():
    """Tela de login""" 
    return render_template("homeLogin.html")
 
@app.route('/login', methods = ['GET', 'POST'])  
def login():
    """Processa o login e retorna uma mensagem de boas vindas"""  
    error = None;  
    if request.method == "POST":  
        if request.form['pwd'] == '123456':
            # Flash é uma forma de enviar uma mensagem para a view, o tempo de vida do flash é de um request pro outro.
            flash("Bem vindo")  
            return redirect(url_for('homeLogin'))  

        error = "Usuário ou senha inválido"   
            
    return render_template('login.html', error=error)  

if __name__ == "__main__": # Executa app.run() quando chamar python app.py
    """Executa a aplicacao Flask"""
    app.run(debug=True)