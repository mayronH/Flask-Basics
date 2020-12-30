import os

from flask import Flask
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
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
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
	return "Hello, " + name

# Especifíca o paramêtro para integer
@app.route('/age/<int:age>')
def age(age):
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
    if name == 'admin':
        # Função para redirecionar para a função com o nome admin
        return redirect(url_for('admin'))
    if name == 'librarion':
        return redirect(url_for('librarion'))
    if name == 'student':
        return redirect(url_for('student'))


@app.route('/hello/<user>')
def message(user):
    # Passar um objeto para o template
    return render_template('message.html', name=user)


@app.route('/table/<int:num>')
def table(num):
    return render_template('tableOf.html', n=num)


@app.route('/signup')
def signUpForm():
    return render_template('singup.html')


# Cria 2 rotas success, uma para POST e outra para GET
@app.route('/success', methods=['POST', 'GET'])
def printData():
    if request.method == 'POST':
        # O .form é um dicionário que contem um par de chave-valor vindo dos parametros do form
        result = request.form
        
        return render_template("showData.html", result=result)


@app.route('/cookie')
def cookie():
    # Função make_response converte o valor de uma view para uma instância response
    res = make_response("<h1>Cookie is set</h1>")
    # set_cookie é uma função da classe response, serve para armazenar a informação em um cookie(nome, conteudo, tempo de vida)
    res.set_cookie('foo', 'bar')

    return res

@app.route('/session')
def testSession():
    res = make_response("<p>Variável da sessão criada, <a href='/get'>get variable</a></p>")
    session['response'] = 'session#1'
    
    return res


@app.route('/get')
def getVariable():
    if 'response' in session:
        s = session['response']
        
        return render_template('getSession.html', name=s)


@app.route('/upload')
def upload():
    return render_template("uploadForm.html")


@app.route('/uploadPost', methods=['POST'])
def filePost():
    if request.method == 'POST':
        # Pega as informações do arquivo enviado pelo formulário
        f = request.files['file']

        # Valida quaisquer problemas que possa ter com o nome do arquivo enviado
        filename = secure_filename(f.filename)

        # Salva o arquivo na pasta configurada em UPLOAD_FOLDER
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return render_template('uploadedFile.html', name = filename)


if __name__ == "__main__": # Executa app.run() quando chamar python app.py
	app.run(debug=True)