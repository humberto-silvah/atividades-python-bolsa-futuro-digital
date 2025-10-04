class Livro:
    
    def __init__(self, titulo, autor, ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._livro_disponivel = True

    @property
    def titulo(self):
        return self._titulo 
    @property
    def autor(self):
        return self._autor
    @property
    def ano(self):
        return self._ano
    @property
    def disponivel(self):
        return self._livro_disponivel

    @disponivel.setter
    def disponivel(self, valor):
        self._livro_disponivel = valor

    

    

   
