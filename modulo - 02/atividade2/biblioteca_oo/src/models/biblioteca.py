from models.livro import Livro
from models.usuario import Usuario
from models.catalogo import Catalogo
from models.gerenciador_usuarios import GerenciadorUsuarios
from models.gerenciador_emprestimo import GerenciadorEmprestimos


class Biblioteca:
    def __init__(self):
      
        self._todos_livros = []
        self._livros_disponiveis = []
        self._livros_emprestados = []
        self._usuarios = []

#instancias-------------------------------------------------------
    
        self.catalogo = Catalogo(self._todos_livros)
        self.ger_usuarios = GerenciadorUsuarios()
        self.ger_emprestimos = GerenciadorEmprestimos(
            self._livros_disponiveis, self._livros_emprestados)

#Gets-------------------------------------------------------------

    @property
    def todos_livros(self):
        return self._todos_livros

    @property
    def livros_disponiveis(self):
        return self._livros_disponiveis

    @property
    def livros_emprestados(self):
        return self._livros_emprestados

    @property
    def usuarios(self):
        return self._usuarios

#Cadastros-------------------------------------------------   

    def cadastrar_livro(self, titulo, autor, ano):
        novo_livro = Livro(titulo, autor, ano)
        self._todos_livros.append(novo_livro)
        self._livros_disponiveis.append(novo_livro)
        print(f"\nLivro {titulo} cadastrado com sucesso!")

    def cadastrar_usuario(self, nome, id):
        novo_usuario = Usuario(nome, id)
        self._usuarios.append(novo_usuario)
        print(f"\nUsuário {nome} cadastrado com sucesso!")


#Listagem--------------------------------------------------

    def listar_todos_livros(self):
        if not self._todos_livros:
            print("\nNenhum livro cadastrado na biblioteca.")
            return
        
        for i, livro in enumerate(self._todos_livros, start=1):
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f"{i}- Titulo: {livro.titulo} - Autor: {livro.autor} - Ano: {livro.ano} - {status}")


    def listar_livros_emprestados(self):
        if not self._livros_emprestados:
            print("\nNenhum livro disponível no momento.")
            return
        
        for i, livro in enumerate(self._livros_disponiveis, start=1):
            print(f"{i}- Titulo: {livro.titulo} - Autor: {livro.autor} - Ano: {livro.ano})")
        

    def listar_livros_disponiveis(self):
        if not self._livros_disponiveis:
            print("\nNenhum livro disponível no momento.")
            return
        
        for i, livro in enumerate(self._livros_disponiveis, start=1):
            print(f"{i}- Titulo: {livro.titulo} - Autor: {livro.autor} - Ano: {livro.ano})")


    def listar_usuarios(self):
        if not self._usuarios:
            print("\nNenhum usuário cadastrado.")
            return
        
        for i, usuario in enumerate(self._usuarios, start=1):
            livros = [livro.titulo for livro in usuario.livros_emprestados]
            print(f"{i}- Usuario: {usuario.nome} - ID: {usuario.id} - Livros: {livros}")

#operaçoes-------------------------------------------------------------------

    def emprestar_livro(self, usuario_id, titulo_livro):
        usuario = self.buscar_usuario_por_id(usuario_id)
        if not usuario:
            print(f"Usuário com ID {usuario_id} não encontrado.")
            return
        
        self.ger_emprestimos.emprestar_livro(usuario, titulo_livro)


    def devolver_livro(self, usuario_id, titulo_livro):
        usuario = self.buscar_usuario_por_id(usuario_id)
        if not usuario:
            print(f"Usuário com ID {usuario_id} não encontrado.")
            return
        
        self.ger_emprestimos.devolver_livro(usuario, titulo_livro)

#busca----------------------------------------------------------

    def buscar_usuario_por_id(self, id):
        for usuario in self._usuarios:
            if usuario.id == id:
                return usuario
            
        return None
