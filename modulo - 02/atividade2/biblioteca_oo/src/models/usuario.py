class Usuario:
    
    def __init__(self, nome, id):
        self._nome = nome
        self._id = id
        self._livros_emprestados = []

    @property
    def nome(self):
        return self._nome
    @property
    def id(self):
        return self._id
   
    @property
    def livros_emprestados(self):
        return self._livros_emprestados
    
    
    