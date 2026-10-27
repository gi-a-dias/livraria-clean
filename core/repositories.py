from abc import ABC, abstractmethod

from core.entities import Livro


class LivroRepository(ABC):
    """Contrato de persistência conhecido pelo núcleo da aplicação."""

    @abstractmethod
    def obter_todos(self) -> list[Livro]:
        raise NotImplementedError

    @abstractmethod
    def salvar(self, livro: Livro) -> None:
        raise NotImplementedError

    @abstractmethod
    def atualizar(self, indice: int, livro: Livro) -> None:
        """Substitui o livro da posição informada, ou lança IndexError."""
        raise NotImplementedError
