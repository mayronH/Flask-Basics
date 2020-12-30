from flask import *

app = Flask(__name__) #Criando um Objeto da classe Flask

@app.route('/') #decorator
def index():
	return "Hello World!"


@app.route('/home/<name>')
def home(name):
	return "Hello, " + name


@app.route('/age/<int:age>')
def age(age):
	return "Idade: %d"%age


def about():
	return "Sobre: "

# Função para criar urls no lugar dos decorators
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


if __name__ == "__main__": # Executa app.run() quando chamar python app.py
	app.run(debug=True)