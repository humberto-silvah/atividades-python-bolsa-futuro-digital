from models.biblioteca import Biblioteca


def main():
    biblioteca = Biblioteca()   

    print("=== Sistema de Biblioteca ===")
    while True:
        print("\nMenu:")
        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Cadastrar Usuario")       
        print("4. Listar Usuarios")
        print("5. Emprestar Livro")
        print("6. Devolver Livro")
        print("7. Sair")

        escolha = input("\nEscolha uma opção: ")
        match escolha:
            case "7":
                print("Saindo do sistema. Ate mais!")
                break
            case "1":
                biblioteca.cadastrar_livro()
            case "2":
                biblioteca.listar_livros()
            
                
            

    
    
    


if __name__ == "__main__":
    main()