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
        print("2- Listar Livros")
        print("3- Cadastrar Usuario")       
        print("4- Listar Usuarios")
        print("5- Emprestar Livro")
        print("6- Devolver Livro")
        print("7- Sair")
        print(f":{Formatadores.divisao_menu}:") # Cabeçalho
        return