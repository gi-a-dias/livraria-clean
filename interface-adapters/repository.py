import os

class TxtRepository:
    def __init__(self, arquivo_path="dados.txt"):
        self.arquivo_path = arquivo_path
        if not os.path.exists(self.arquivo_path):
            with open(self.arquivo_path, "w") as f:
                f.write("O Hobbit;Fantasia;45.0\n1984;Ficção;30.0\n")

    def obter_todos(self):
        livros = []
        with open(self.arquivo_path, "r", encoding="utf-8") as f:
            for linha in f:
                if linha.strip():
                    partes = linha.strip().split(";")
                    livros.append({"titulo": partes[0], "genero": partes[1], "preco": float(partes[2])})
        return livros

    def salvar(self, livro):
        with open(self.arquivo_path, "a", encoding="utf-8") as f:
            f.write(f"{livro['titulo']};{livro['genero']};{livro['preco']}\n")