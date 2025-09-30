from models.livro import Livro
from models.usuario import Usuario
from abc import abstractmethod
divisao = "=" * 45 # Cabeçalho

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

        # Cabeçalho
        print() 
        print(divisao)
        print("|            Cadastro de Livro              |")
        print(divisao) 
        # Cabeçalho

        titulo = input("\nTitulo do livro: ")
        autor = input("Autor do livro: ")
        ano = input("Ano de publicação: ")
        novo_livro = Livro(titulo, autor, ano)
        self.livros.append(novo_livro)
        print(f"Livro: '{titulo}' cadastrado com sucesso!")  
   
    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado na biblioteca.")
            return
        # Cabeçalho
        print()
        print(divisao)
        print("|             Lista de Livros               |")
        print(divisao)
        print()
        # Cabeçalho 

        for idx, livro in enumerate(self.livros, start=1):
            status = "Disponivel" if livro.disponivel else "Indisponivel"
            print(f"{idx}. Titulo:{livro.titulo} - Auutor:{livro.autor} Ano:{livro.ano} - {status}")