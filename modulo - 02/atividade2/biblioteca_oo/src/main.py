from models.biblioteca import Biblioteca
from utils.formatadores import Menu

biblioteca = Biblioteca()

#tratamento de erro de cada funcao ------------------
#1
def cadastro_usuario_main(biblioteca):  
    try:
        nome = input("Nome do usuario: ").strip()
        if not nome:
            raise ValueError("O nome não pode estar vazio.")
        
        id = input("ID do usuario: ").strip()
        if not id:
            raise ValueError("O ID não pode estar vazio.")

        usuario_existente = biblioteca.buscar_usuario_por_id(id)
        if usuario_existente:
            raise ValueError(f"Já existe um usuario com o ID {id}.")
        
        biblioteca.cadastrar_usuario(nome, id)
        
    except ValueError as e:
        print(f"Erro: {e}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

#-------------------------------------------------------------------------------
#2
def cadastro_livro_main(biblioteca):
    try:
        titulo = input("Titulo do livro: ").strip()
        if not titulo:
            raise ValueError("O título do livro não pode estar vazio.")
        
        autor = input("Autor do livro: ").strip()
        if not autor:
            raise ValueError("O autor não pode estar vazio.")
        
        ano = input("Ano de publicação (4 dígitos): ").strip()
        if not (ano.isdigit() and len(ano) == 4):
            raise ValueError("Digite um ano valido com exatamente 4 numeros (ex: 2024).")   
          
        ano = int(ano)   

        for livro in biblioteca.todos_livros:
            if livro.titulo.lower() == titulo.lower() and livro.autor.lower() == autor.lower():
                raise ValueError(f"O livro {titulo} de {autor} já está cadastrado.")  
              
        biblioteca.cadastrar_livro(titulo, autor, ano)

        print(f" Livro {titulo} cadastrado com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

#------------------------------------------------------------------------------------------
#3
def emprestar_livro_main(biblioteca):
    try:
        usuario_id = input("ID do usuario: ").strip()
        if not usuario_id:
            raise ValueError("O ID do usuario não pode estar vazio.")
        
        titulo_livro = input("Titulo do livro: ").strip()
        if not titulo_livro:
            raise ValueError("O titulo do livro não pode estar vazio.")
        
        biblioteca.emprestar_livro(usuario_id, titulo_livro)

    except ValueError as e:
        print(f"Erro: {e}")
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

#----------------------------------------------------------------------------------------------------
#4
def devolver_livro_main(biblioteca):
    try:
        usuario_id = input("ID do usuario: ").strip()
        if not usuario_id:
            raise ValueError("O ID do usuario não pode estar vazio.")
        
        titulo_livro = input("Titulo do livro: ").strip()
        if not titulo_livro:
            raise ValueError("O titulo do livro não pode estar vazio.")
        
        biblioteca.devolver_livro(usuario_id, titulo_livro)

    except ValueError as e:
        print(f"Erro: {e}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

#----------------------------------------------------------------------------------------------------


def main():    
    Menu.cabecalho("Biblioteca BFD Aluno Humberto")

#mode de execuçao direta----------------------------------

    """ Menu.cabecalho("cadastro livros")
    biblioteca.cadastrar_livro("aaaa", "b", 1949)
    biblioteca.cadastrar_livro("cccc", "d", 1960)
    Menu.cabecalho("cad usuarios")
    biblioteca.cadastrar_usuario("Alice", "1")
    biblioteca.cadastrar_usuario("Bob", "2")
    Menu.cabecalho("lisvros dispo")
    biblioteca.listar_livros_disponiveis()
    Menu.cabecalho("lista usuarios")
    biblioteca.listar_usuarios()
    Menu.cabecalho("empestimo")
    biblioteca.emprestar_livro("2", "aaaa")
    Menu.cabecalho("todos livros")
    biblioteca.listar_todos_livros()
    Menu.cabecalho("livros dispo")
    biblioteca.listar_livros_disponiveis()
    Menu.cabecalho("lista usuarios")
    biblioteca.listar_usuarios()"""
   
#modo de execuçao interativa--------------------------------------

    while True:       
        Menu.cabecalho_menu()
        #1- Cadastrar Livro
        #2- Cadastrar Usuario
        #3- Lista todos os livros
        #4- Emprestar Livro
        #5- Devolver Livro
        #6- Listar livros disponíveis
        #7- Listar livros emprestados
        #8- Listar usuários e seus livros
        #9- Sair

        escolha = input("\nEscolha uma opção: ")
        match escolha:
            
            case "1":
                Menu.cabecalho("Cadastro de Livro") 
                cadastro_livro_main(biblioteca)

            case "2":
                Menu.cabecalho("Cadastro de Usuario")
                cadastro_usuario_main(biblioteca)

            case "3":
                Menu.cabecalho("catalogo")
                biblioteca.listar_todos_livros()
               
            case "4":
                Menu.cabecalho("Empréstimo de Livro")
                emprestar_livro_main(biblioteca)
                
            case "5":
                Menu.cabecalho("Devolução de Livro")
                devolver_livro_main(biblioteca)
                
            case "6":
                Menu.cabecalho("Lista de Livros Disponíveis")
                biblioteca.listar_livros_disponiveis()

            case "7":
                Menu.cabecalho("Lista de Livros Emprestados")
                biblioteca.listar_livros_emprestados()
                
            case "8":
                Menu.cabecalho("Listar usuários e seus livros")
                biblioteca.listar_usuarios()
                                
            case "9":
                Menu.cabecalho("Sistema Encerrado")
                break  

            case _:
                print("Opcao invalida. Tente novamente.")
                           

if __name__ == "__main__":
    main()