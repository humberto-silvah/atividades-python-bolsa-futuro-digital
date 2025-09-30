from models.biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()
    biblioteca.cadastrar_livro()
    biblioteca.cadastrar_livro()
    biblioteca.listar_livros()
    
    


if __name__ == "__main__":
    main()