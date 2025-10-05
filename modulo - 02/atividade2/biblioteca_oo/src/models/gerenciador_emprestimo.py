class GerenciadorEmprestimos:
    

    def __init__(self, livros_disponiveis, livros_emprestados):
        self._livros_disponiveis = livros_disponiveis
        self._livros_emprestados = livros_emprestados


    def emprestar_livro(self, usuario, titulo_livro):
        for livro in self._livros_disponiveis:
            if livro.titulo.lower() == titulo_livro.lower() and livro.disponivel:
                livro.disponivel = False
                usuario.adicionar_livro(livro)
                self._livros_disponiveis.remove(livro)
                self._livros_emprestados.append(livro)
                print(f"Livro: {livro.titulo} emprestado para {usuario.nome}.")
                return
            
        print(f"Livro: {titulo_livro} não está disponível para empréstimo.")


    def devolver_livro(self, usuario, titulo_livro):
        for livro in self._livros_emprestados:
            if livro.titulo.lower() == titulo_livro.lower() and not livro.disponivel:
                livro.disponivel = True
                usuario.remover_livro(livro)
                self._livros_emprestados.remove(livro)
                self._livros_disponiveis.append(livro)
                print(f"Livro: {livro.titulo} devolvido à biblioteca.")
                return
            
        print(f"Nenhum livro chamado {titulo_livro} encontrado para devolução.")
