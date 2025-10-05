from models.livro import Livro


class Catalogo:
    def __init__(self, livros):
        self._livros = livros


    def buscar_por_titulo(self, titulo):
        resultados = [livro for livro in self._livros if titulo.lower() in livro.titulo.lower()]

        if resultados:
            print("\nResultados encontrados:")
            for livro in resultados:
                print(f"- {livro.titulo} ({livro.autor}, {livro.ano})")
        
        else:
            print("\nNenhum livro encontrado com esse título.")


    def buscar_por_autor(self, autor):
        resultados = [livro for livro in self._livros if autor.lower() in livro.autor.lower()]

        if resultados:
            print("\nLivros desse autor:")
            for livro in resultados:
                print(f"- {livro.titulo} ({livro.ano})")
        
        else:
            print("\nNenhum livro encontrado desse autor.")


    def listar_disponiveis(self):
        disponiveis = [livro for livro in self._livros if livro.disponivel]
        if not disponiveis:
            print("\nNenhum livro disponível no momento.")
            return
        
        print("\nLivros disponíveis:")

        for i, livro in enumerate(self._livros_disponiveis, start=1):
            print(f"\n{i}- Titulo: {livro.titulo} - Autor: {livro.autor} - Ano: {livro.ano}")
