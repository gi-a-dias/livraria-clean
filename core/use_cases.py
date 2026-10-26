class LivrariaUseCase:
    def __init__(self, repositorio):
        # O Use Case recebe uma interface/repositório genérico (DIP aplicado!)
        self.repositorio = repositorio

    def listar_livros(self):
        return self.repositorio.obter_todos()

    def adicionar_livro(self, titulo, genero, preco):
        novo_livro = {"titulo": titulo, "genero": genero, "preco": preco}
        self.repositorio.salvar(novo_livro)