import unittest

from core.entities import Livro
from core.use_cases import LivrariaUseCase


class RepositorioEmMemoria:
    def __init__(self):
        self.livros = [Livro("O Hobbit", "Fantasia", 45.0)]

    def obter_todos(self):
        return list(self.livros)

    def salvar(self, livro):
        self.livros.append(livro)

    def atualizar(self, indice, livro):
        if indice < 0 or indice >= len(self.livros):
            raise IndexError("Livro não encontrado.")
        self.livros[indice] = livro


class TestLivrariaUseCase(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioEmMemoria()
        self.caso_de_uso = LivrariaUseCase(self.repositorio)

    def test_lista_livros(self):
        self.assertEqual(self.caso_de_uso.listar_livros()[0].titulo, "O Hobbit")

    def test_adiciona_livro(self):
        self.caso_de_uso.adicionar_livro("Duna", "Ficção", 39.9)
        self.assertEqual(len(self.repositorio.livros), 2)
        self.assertEqual(self.repositorio.livros[1].titulo, "Duna")

    def test_edita_livro(self):
        self.caso_de_uso.editar_livro(0, "O Hobbit - Edição nova", "Fantasia", 50)
        livro = self.repositorio.livros[0]
        self.assertEqual(livro.titulo, "O Hobbit - Edição nova")
        self.assertEqual(livro.preco, 50.0)

    def test_edicao_de_indice_inexistente_falha(self):
        with self.assertRaises(IndexError):
            self.caso_de_uso.editar_livro(10, "Livro", "Gênero", 10)

    def test_nao_permite_preco_negativo(self):
        with self.assertRaises(ValueError):
            self.caso_de_uso.adicionar_livro("Livro", "Gênero", -1)


if __name__ == "__main__":
    unittest.main()
