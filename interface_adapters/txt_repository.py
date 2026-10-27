import csv
from pathlib import Path

from core.entities import Livro
from core.repositories import LivroRepository


class TxtRepository(LivroRepository):
    """Implementação do repositório que persiste os livros em dados.txt."""

    def __init__(self, arquivo_path: str | Path = "dados.txt"):
        self.arquivo_path = Path(arquivo_path)
        self.arquivo_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.arquivo_path.exists():
            # Mantém os exemplos iniciais da implementação original, apenas
            # quando o arquivo ainda não existe. Um arquivo existente não é apagado.
            with self.arquivo_path.open("w", encoding="utf-8", newline="") as arquivo:
                escritor = csv.writer(arquivo, delimiter=";")
                escritor.writerow(["O Hobbit", "Fantasia", "45.0"])
                escritor.writerow(["1984", "Ficção", "30.0"])

    def obter_todos(self) -> list[Livro]:
        livros = []
        with self.arquivo_path.open("r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.reader(arquivo, delimiter=";")
            for numero_linha, partes in enumerate(leitor, start=1):
                if not partes or not any(parte.strip() for parte in partes):
                    continue
                if len(partes) != 3:
                    raise ValueError(f"Formato inválido na linha {numero_linha} de dados.txt.")
                try:
                    livros.append(Livro(partes[0], partes[1], float(partes[2])))
                except (ValueError, TypeError) as erro:
                    raise ValueError(f"Dados inválidos na linha {numero_linha} de dados.txt.") from erro
        return livros

    def salvar(self, livro: Livro) -> None:
        with self.arquivo_path.open("a", encoding="utf-8", newline="") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow([livro.titulo, livro.genero, livro.preco])

    def atualizar(self, indice: int, livro: Livro) -> None:
        livros = self.obter_todos()
        if indice < 0 or indice >= len(livros):
            raise IndexError("Livro não encontrado.")
        livros[indice] = livro
        with self.arquivo_path.open("w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            for item in livros:
                escritor.writerow([item.titulo, item.genero, item.preco])
