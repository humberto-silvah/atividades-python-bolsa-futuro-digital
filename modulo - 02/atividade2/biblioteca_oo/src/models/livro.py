class Livro:

    def __init__(self, titulo, autor, ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._disponivel = True

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
        return self._disponivel
    
    @disponivel.setter
    def disponivel(self, valor):
        self._disponivel = valor

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"{self.titulo} - {self.autor} ({self.ano}) - {status}"
    

   
