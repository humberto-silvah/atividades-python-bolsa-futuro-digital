from models.biblioteca import Biblioteca
divisao = "=" * 45
divisao2 = "-" * 25

def main():
    biblioteca = Biblioteca()   
    print(divisao)
    print("|       Biblioteca BDF Aluno Humberto       |")
    print(divisao)

    while True:
        print("\n:---------- Menu ---------:") # Cabeçalho

        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Cadastrar Usuario")       
        print("4. Listar Usuarios")
        print("5. Emprestar Livro")
        print("6. Devolver Livro")
        print("7. Sair")
        
        print(f":{divisao2}:") # Cabeçalho

        escolha = input("\nEscolha uma opção: ")
        match escolha:
            case "7":
                print(divisao)
                print("|            Sistema Encerrado              |")
                print(divisao)
                break
            case "1":
                biblioteca.cadastrar_livro()
            case "2":
                biblioteca.listar_livros()
            case "3":
                print("Funcao desabilitada no momento.")
            case "4":
                print("Funcao desabilitada no momento.")
            case "5":
                print("Funcao desabilitada no momento.")
            case "6":
                print("Funcao desabilitada no momento.")
            case _:
                print("Opcao invalida. Tente novamente.")
                
            

    
    
    


if __name__ == "__main__":
    main()