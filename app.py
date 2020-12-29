from flask import Flask

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


app.add_url_rule("/about", "about", about)

if __name__ == "__main__": # Executa app.run() quando chamar python app.py
	app.run(debug=True)