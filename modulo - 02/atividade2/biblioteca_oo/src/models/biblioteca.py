from models.livro import Livro
from models.usuario import Usuario
from utils.formatadores import Formatadores
cabecalho = Formatadores.cabecalho

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
        cabecalho("Cadastro de Livro") 
        self.titulo = input("\nTitulo do livro: ")
        self.autor = input("Autor do livro: ")
        self.ano = input("Ano de publicação: ")
        novo_livro = Livro(self.titulo, self.autor, self.ano)
        self.livros.append(novo_livro)
        print(f"\nLivro: '{self.titulo}' cadastrado com sucesso!")  
   
    def listar_livros(self):
        cabecalho("Lista de Livros") 
        if not self.livros:
            print("\nNenhum livro cadastrado na biblioteca.")
            return       
        for i, livro in enumerate(self.livros, start=1):
            status = "Disponivel" if livro.disponivel else "Indisponivel"
            print(f"{i}. Titulo:{livro.titulo} - Autor:{livro.autor} Ano:{livro.ano} - {status}")

    def cadastrar_usuario(self):
        cabecalho("Cadastro de Usuário") 
        self.nome = input("\nNome do usuário: ")
        self.id = input("ID do usuário: ")
        novo_usuario = Usuario(self.nome, self.id)
        self.usuarios.append(novo_usuario)
        print(f"\nUsuário: '{self.nome}' cadastrado com sucesso!")

    def listar_usuarios(self):        
        cabecalho("Lista de Usuários") 
        if not self.usuarios:
            print("\nNenhum usuário cadastrado na biblioteca.")
            return
        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"{i}. Nome:{usuario.nome} - ID:{usuario.id} - Livros Emprestados:{len(usuario.livros_emprestados)}")