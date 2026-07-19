#declaração de uma classe
class pessoa:
    def __init__(self, nome, idade, renda):
        self.nome = nome 
        self.idade = idade
        self.renda = renda 
        
    def exibe_dados(self):
        return f"{self.nome} - {self.idade} - R$ {self.renda}"
    
    def exibe_dados2(self):
        return f"{self.nome} - {self.idade}"

#Instancia da classe
p1 = pessoa("Maria Flor", 22, 1500)

#printando objeto da classe
"""print(p1.nome)
print(p1.idade)
print(p1.renda)"""
print(p1.exibe_dados())

p2 = pessoa("Marcos", 31, 3300)
"""print(f"{p2.nome} - {p2.idade} - R$ {p2.renda}")"""
print(p2.exibe_dados())

class funcionario(pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, 0)
        self.salario = salario
        
    def exibe_salario(self):
        print(f"{super().exibe_dados()} Salário R$ {self.salario}")
        
f1 = funcionario("Claudia", 45, 4500)
print(f"{f1.exibe_salario()}")