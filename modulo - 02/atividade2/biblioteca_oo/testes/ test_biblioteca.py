from src.models.biblioteca import Biblioteca
from src.utils.formatadores import Menu


class Tbiblioteca:


    def main():
        biblioteca = Biblioteca() 

        Menu.cabecalho("Biblioteca BFD Aluno Humberto")

        Menu.cabecalho("cadastro livros")
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
        biblioteca.listar_usuarios()


    if __name__ == "__main__":
        main()


