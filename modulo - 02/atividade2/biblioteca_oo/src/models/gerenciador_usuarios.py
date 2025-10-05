from models.usuario import Usuario


class GerenciadorUsuarios:
    def __init__(self):
        self._usuarios = []


    def cadastrar_usuario(self, nome, id):
        novo_usuario = Usuario(nome, id)
        self._usuarios.append(novo_usuario)
        print(f"\nUsuario: '{nome}' cadastrado com sucesso!")


    def buscar_por_id(self, id):
        for usuario in self._usuarios:
            if usuario.id == id:
                return usuario
            
        return None


    def listar_usuarios(self):
        if not self._usuarios:
            print("Nenhum usuario cadastrado.")
            return
        
        print("\nUsuarios cadastrados:")
        
        for i, usuario in enumerate(self._usuarios, start=1):
            print(f"\n{i}- Nome: {usuario.nome} - ID: {usuario.id} - Livros Emprestados: {[livro.titulo for livro in usuario.livros_emprestados]}")