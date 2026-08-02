#Classe Carro (herda de Veiculo)

from classe_base import Veiculo


class Carro(Veiculo):
    def __init__(self, placa, modelo, marca, ano, valor, quantidade_portas):
        super().__init__(placa, modelo, marca, ano, valor)
        self.quantidade_portas = quantidade_portas

    def calcular_ipva(self):
        return self.valor * 0.04  # 4% do valor do veículo

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Quantidade de portas: {self.quantidade_portas}")
        print("Tipo: Carro")
