class Formatadores:
    divisao = "=" * 45
    divisao_menu = "-" * 25


    def cabecalho(string):
        print(f"\n{Formatadores.divisao}")
        print(f"|{string:^43}|")
        print(f"{Formatadores.divisao}")
        return

    def cabecalho_menu():
        print(f"\n:{'Menu:':-^25}:") # Cabeçalho
        print("1- Cadastrar Livro")
        print("2- Cadastrar Usuario")
        print("3- Emprestar Livro")       
        print("4- Devolver Livro")
        print("5- Listar livros disponíveis")
        print("6- Listar livros emprestados")
        print("7- Listar usuários e seus livros")
        print("8- Sair")
        print(f":{Formatadores.divisao_menu}:") # Cabeçalho
        return