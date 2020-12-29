from flask import *

app = Flask(__name__) #Criando um Objeto da classe Flask

@app.route('/') #decorator
def home():
	return "Hello World!"


@app.route('/home/<name>')
def home(name):
	return "Hello, " + name


@app.route('/home/<int:age>')
def home(age):
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
        return redirect(url_for('admin'))
    if name == 'librarion':
        return redirect(url_for('librarion'))
    if name == 'student':
        return redirect(url_for('student'))

if __name__ == "__main__": # Executa app.run() quando chamar python app.py
	app.run(debug=True)