import tempfile
import unittest
from pathlib import Path

from core.entities import Livro
from interface_adapters.txt_repository import TxtRepository


class TestTxtRepository(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.caminho = Path(self.temp_dir.name) / "dados.txt"
        self.caminho.write_text("O Hobbit;Fantasia;45.0\n1984;Ficção;30.0\n", encoding="utf-8")
        self.repositorio = TxtRepository(self.caminho)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_le_dados_existentes(self):
        livros = self.repositorio.obter_todos()
        self.assertEqual(len(livros), 2)
        self.assertEqual(livros[0], Livro("O Hobbit", "Fantasia", 45.0))

    def test_salva_livro_e_persiste(self):
        self.repositorio.salvar(Livro("Duna", "Ficção", 39.9))
        livros = self.repositorio.obter_todos()
        self.assertEqual(livros[-1].titulo, "Duna")

    def test_atualiza_livro_no_arquivo(self):
        self.repositorio.atualizar(1, Livro("1984", "Distopia", 35.0))
        livros = self.repositorio.obter_todos()
        self.assertEqual(livros[1], Livro("1984", "Distopia", 35.0))

    def test_atualizacao_com_indice_invalido_falha(self):
        with self.assertRaises(IndexError):
            self.repositorio.atualizar(9, Livro("X", "Y", 1))


if __name__ == "__main__":
    unittest.main()
