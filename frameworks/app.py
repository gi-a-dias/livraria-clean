from flask import Flask, render_template, request, redirect, url_for
from interface_adapters.repository import TxtRepository
from core.use_cases import LivrariaUseCase

app = Flask(__name__, template_folder='../templates')

# Injeção de Dependência na prática
repositorio = TxtRepository()
use_case = LivrariaUseCase(repositorio)


@app.route('/')
def index():
    livros = use_case.listar_livros()
    return render_template('index.html', livros=livros)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    titulo = request.form.get('titulo')
    genero = request.form.get('genero')
    preco = float(request.form.get('preco'))

    use_case.adicionar_livro(titulo, genero, preco)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)