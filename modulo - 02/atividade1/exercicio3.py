class Funcionario():

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


class Gerente(Funcionario):

    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

regente = Gerente("Ana", 5000, "Vendas")
print(f"Nome: {regente.nome}, Salário: {regente.salario:,.2f}, Departamento: {regente.departamento}")