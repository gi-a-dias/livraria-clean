from core.entities import Livro
from core.repositories import LivroRepository


class LivrariaUseCase:
    """Regras de aplicação. Não conhece Flask nem o formato do arquivo."""

    def __init__(self, repositorio: LivroRepository):
        self.repositorio = repositorio

    def listar_livros(self) -> list[Livro]:
        return self.repositorio.obter_todos()

    def adicionar_livro(self, titulo: str, genero: str, preco: float) -> None:
        livro = Livro(titulo=titulo.strip(), genero=genero.strip(), preco=float(preco))
        self.repositorio.salvar(livro)

    def editar_livro(self, indice: int, titulo: str, genero: str, preco: float) -> None:
        livros = self.repositorio.obter_todos()
        if not isinstance(indice, int) or indice < 0 or indice >= len(livros):
            raise IndexError("Livro não encontrado.")
        livro_atualizado = Livro(
            titulo=titulo.strip(), genero=genero.strip(), preco=float(preco)
        )
        self.repositorio.atualizar(indice, livro_atualizado)
