from models.biblioteca import Biblioteca
from utils.formatadores import Formatadores
cabecalho = Formatadores.cabecalho
divisao = "-" * 25

def main():
    biblioteca = Biblioteca()   
    cabecalho("Biblioteca BFD Aluno Humberto")

    while True:
        Formatadores.cabechalho_menu()
        #1. Cadastrar Livro
        #2. Listar Livros
        #3. Cadastrar Usuario
        #4. Listar Usuarios
        #5. Emprestar Livro
        #6. Devolver Livro
        #7. Sair

        escolha = input("\nEscolha uma opção: ")
        match escolha:
            case "7":
                cabecalho("Sistema Encerrado")
                break
            case "1":
                biblioteca.cadastrar_livro()
            case "2":
                biblioteca.listar_livros()
            case "3":
                biblioteca.cadastrar_usuario()
            case "4":
                biblioteca.listar_usuarios()
            case "5":
                print("Funcao desabilitada no momento.")
            case "6":
                print("Funcao desabilitada no momento.")
            case _:
                print("Opcao invalida. Tente novamente.")
                
            

    
    
    


if __name__ == "__main__":
    main()