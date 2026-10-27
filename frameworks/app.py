from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for

from core.use_cases import LivrariaUseCase
from interface_adapters.txt_repository import TxtRepository


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def create_app(arquivo_dados: str | Path | None = None) -> Flask:
    app = Flask(__name__, template_folder=str(PROJECT_ROOT / "templates"))
    app.secret_key = "livraria-clean-chave-local"

    caminho_dados = Path(arquivo_dados) if arquivo_dados else PROJECT_ROOT / "dados.txt"
    use_case = LivrariaUseCase(TxtRepository(caminho_dados))

    @app.get("/")
    def index():
        try:
            livros = use_case.listar_livros()
        except (OSError, ValueError) as erro:
            flash(f"Não foi possível ler os livros: {erro}", "erro")
            livros = []
        return render_template("index.html", livros=livros)

    @app.post("/adicionar")
    def adicionar():
        try:
            use_case.adicionar_livro(
                request.form.get("titulo", ""),
                request.form.get("genero", ""),
                request.form.get("preco", ""),
            )
            flash("Livro cadastrado com sucesso.", "sucesso")
        except (ValueError, TypeError) as erro:
            flash(f"Não foi possível cadastrar o livro: {erro}", "erro")
        except OSError as erro:
            flash(f"Erro ao gravar os dados: {erro}", "erro")
        return redirect(url_for("index"))

    @app.post("/editar/<int:indice>")
    def editar(indice: int):
        try:
            use_case.editar_livro(
                indice,
                request.form.get("titulo", ""),
                request.form.get("genero", ""),
                request.form.get("preco", ""),
            )
            flash("Livro atualizado com sucesso.", "sucesso")
        except (ValueError, TypeError, IndexError) as erro:
            flash(f"Não foi possível editar o livro: {erro}", "erro")
        except OSError as erro:
            flash(f"Erro ao gravar os dados: {erro}", "erro")
        return redirect(url_for("index"))

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
