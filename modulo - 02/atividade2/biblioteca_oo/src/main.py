from models.biblioteca import Biblioteca
from utils.formatadores import Formatadores


def main():
    biblioteca = Biblioteca()   
    Formatadores.cabecalho("Biblioteca BFD Aluno Humberto")

    biblioteca.cadastrar_livro("aaaa", "b", 1949)
    biblioteca.cadastrar_livro("cccc", "d", 1960)
    biblioteca.cadastrar_usuario("Alice", "1")
    biblioteca.cadastrar_usuario("Bob", "2")
    biblioteca.listar_livros_disponiveis()
    biblioteca.listar_usuarios()
    biblioteca.emprestar_livro("1", "aaaa")
    biblioteca.listar_livros_disponiveis()
    biblioteca.listar_usuarios()
   

    """
    while True:
        Formatadores.cabecalho_menu()
        #1- Cadastrar Livro
        #2- Cadastrar Usuario
        #3- Emprestar Livro
        #4- Devolver Livro
        #5- Listar livros disponíveis
        #6- Listar livros emprestados
        #7- Listar usuários e seus livros
        #8- Sair

        escolha = input("\nEscolha uma opção: ")
        match escolha:
            case "7":
                Formatadores.cabecalho("Sistema Encerrado")
                break

            case "1":
                Formatadores.cabecalho("Cadastro de Livro") 
                titulo = input("\nTítulo do livro: ")
                autor = input("Autor do livro: ")
                ano = input("Ano de publicação: ")
                biblioteca.cadastrar_livro(titulo, autor, ano)

            case "2":
                Formatadores.cabecalho("Cadastro de Usuario")
                nome = input("\nNome do usuario: ")
                id = input("ID do usuário: ")
                biblioteca.cadastrar_usuario(nome, id)

            case "3":
                Formatadores.cabecalho("Empréstimo de Livro")
                usuario_id = input("\nID do usuário: ")
                titulo_livro = input("Título do livro: ")
                biblioteca.emprestar_livro(usuario_id, titulo_livro)

            case "4":
                Formatadores.cabecalho("Devolução de Livro")
                print("Funcao desabilitada no momento.")

            case "5":
                Formatadores.cabecalho("Lista de Livros Disponíveis")
                biblioteca.listar_livros_disponiveis()

            case "6":
                Formatadores.cabecalho("Lista de Livros Emprestados")
                print("Funcao desabilitada no momento.")
            
            case _:
                print("Opcao invalida. Tente novamente.")"""
                
            

if __name__ == "__main__":
    main()