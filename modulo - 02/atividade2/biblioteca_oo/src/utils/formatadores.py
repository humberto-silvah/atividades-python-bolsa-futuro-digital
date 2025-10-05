class Menu:

    
    divisao = "=" * 60
    divisao_menu = "-" * 40


    def cabecalho(string):
        print(f"\n{Menu.divisao}")
        print(f"|{string.upper():^58}|")
        print(f"{Menu.divisao}\n")
        return


    def cabecalho_menu():
        print(f"\n:{'Menu:':-^40}:") # Cabeçalho
        print("1- Cadastrar Livro")
        print("2- Cadastrar Usuario")
        print("3- Lista Tados os livros")
        print("4- Emprestar Livro")       
        print("5- Devolver Livro")
        print("6- Listar livros disponíveis")
        print("7- Listar livros emprestados")
        print("8- Listar usuários e seus livros")
        print("9- Sair")
        print(f":{Menu.divisao_menu}:") # Cabeçalho
        return