from models.livro import Livro
from models.usuario import Usuario


class Biblioteca:
    
    def __init__(self):
        self._todos_livros = []
        self._usuarios = []
        self._livros_disponiveis = []
        self._livros_emprestaros = []     

    @property
    def todos_livros(self):
        return self._todos_livros    
    
    @property
    def usuarios(self):
        return self._usuarios
    
    @property
    def livros_disponiveis(self):
        return self._livros_disponiveis
    
    @property
    def livro_emprestados(self):
        return self._livros_emprestaros
    
    @livros_disponiveis.setter
    def livros_disponiveis(self, valor):
        self._livros_disponiveis = valor

    @livro_emprestados.setter
    def livro_emprestados(self, valor):
        self._livros_emprestaros = valor

    @todos_livros.setter
    def todos_livros(self, valor):
        self._todos_livros = valor

    @usuarios.setter
    def usuarios(self, valor):
        self._usuarios = valor

    def cadastrar_livro(self, titulo, autor, ano):
        novo_livro = Livro(titulo, autor, ano)
        self._todos_livros.append(novo_livro)
        self._livros_disponiveis.append(novo_livro)
        print(f"\nLivro: '{titulo}' cadastrado com sucesso!")


    def cadastrar_usuario(self, nome, id):     
        novo_usuario = Usuario(nome, id)
        self._usuarios.append(novo_usuario)
        print(f"\nUsuário: '{nome}' cadastrado com sucesso!")


    def listar_usuarios(self):
        if not self._usuarios:
            print("\nNenhum usuário cadastrado na biblioteca.")
            return
        for i, usuario in enumerate(self._usuarios, start=1):
            print(f"\n{i}- Nome: {usuario.nome} - ID: {usuario.id} - Livros Emprestados: {[livro.titulo for livro in usuario.livros_emprestados]}")

  
    def listar_livros_disponiveis(self):
        if not self._todos_livros:
            print("\nLivro nao existe ou nao cadastrado.")
            return
        if not self._livros_disponiveis:
            print("\nlivro ja foi emprestado.")
            return
        for i, livro in enumerate(self._livros_disponiveis, start=1):
            print(f"\n{i}- Titulo: {livro.titulo} - Autor: {livro.autor} - Ano: {livro.ano}")


    def emprestar_livro(self, usuario_id, titulo_livro):
        usuario = self.buscar_usuario_por_id(usuario_id)
        if not usuario:
            print(f"\nUsuário com ID '{usuario_id}' não encontrado.")
            return     
        for livro in self._livros_disponiveis:
            if livro.titulo.lower() == titulo_livro.lower() and livro.disponivel:
                livro.disponivel = False
                usuario.adicionar_livro(livro)
                self._livros_disponiveis.remove(livro)
                self._livros_emprestaros.append(livro)
                print(f"\nLivro '{livro.titulo}' emprestado para o usuário '{usuario.nome}'.")
                return               
        print(f"\nLivro '{titulo_livro}' não está disponível para empréstimo.")


    def devolver_livro(self, usuario_id, titulo_livro):
        usuario = self.buscar_usuario_por_id(usuario_id)
        if not usuario:
            print(f"\nUsuário com ID '{usuario_id}' não encontrado.")
            return      
        for livro in self._livros_emprestaros:
            if livro.titulo.lower() == titulo_livro.lower() and livro.disponivel:
                livro.disponivel = True
                usuario.remover_livro(livro)
                self._livros_emprestaros.remove(livro)
                self._livros_disponiveis.append(livro)
                print(f"\nLivro '{livro.titulo}' devolvido a biblioteca.")
                return                
        print(f"\nLivro '{titulo_livro}' está disponível para empréstimo.")

        
    def buscar_usuario_por_id(self, id):
            for usuario in self._usuarios:
                if usuario.id == id:
                    return usuario
            return None
  
    
    def listar_todos_livros(self):
        if not self._todos_livros:
            print("\nNenhum livro cadastrado na biblioteca.")
            return
        for i, livro in enumerate(self._todos_livros, start=1):
            print(f"\n{i}- Titulo: {livro.titulo} - Autor: {livro.autor} - Ano: {livro.ano} - {'Disponível' if livro.disponivel else 'Indisponível'}")


