from dataclasses import dataclass


@dataclass(frozen=True)
class Livro:
    """Entidade de domínio que representa um livro da livraria."""

    titulo: str
    genero: str
    preco: float

    def __post_init__(self):
        if not self.titulo.strip():
            raise ValueError("O título é obrigatório.")
        if not self.genero.strip():
            raise ValueError("O gênero é obrigatório.")
        if self.preco < 0:
            raise ValueError("O preço não pode ser negativo.")
