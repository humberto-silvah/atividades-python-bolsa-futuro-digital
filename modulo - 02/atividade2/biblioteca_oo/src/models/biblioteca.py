from models.livro import Livro
from models.usuario import Usuario
from abc import abstractmethod

class Biblioteca:

    def __init__(self):
        self._livros = []
        self._usuarios = []

    @property
    def livros(self):
        return self._livros    
    @property
    def usuarios(self):
        return self._usuarios

    def cadastrar_livro(self):
        print("=== Cadastro de Livros ===")
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        ano = input("Ano de publicação: ")
        novo_livro = Livro(titulo, autor, ano)
        self.livros.append(novo_livro)
        print(f"Livro: '{titulo}' cadastrado com sucesso!")  
   
    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado na biblioteca.")
            return
        print("=== Lista de Livros ===")
        for idx, livro in enumerate(self.livros, start=1):
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f"{idx}. {livro.titulo} - {livro.autor} ({livro.ano}) - {status}")