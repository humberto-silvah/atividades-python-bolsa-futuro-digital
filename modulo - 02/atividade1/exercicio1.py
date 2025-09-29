class Animal:
    
    def __init__(self, nome):
        self.nome = nome
        
    def emitir_som(self):
        return "Som genérico"

class Cachorro(Animal):
    
    def emitir_som(self):
        return "Latido"
    

charlie = Cachorro("Charlie")
print(f"O cachorro {charlie.nome} faz: {charlie.emitir_som()}") 

animail_generico = Animal("Animal Genérico")
print(f"O animal {animail_generico.nome} faz: {animail_generico.emitir_som()}")