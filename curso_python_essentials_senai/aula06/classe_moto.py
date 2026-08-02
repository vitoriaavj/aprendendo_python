#Classe Moto (herda de Veiculo)

from classe_base import Veiculo


class Moto(Veiculo):
    def __init__(self, placa, modelo, marca, ano, valor, cilindradas):
        super().__init__(placa, modelo, marca, ano, valor)
        self.cilindradas = cilindradas

    def calcular_ipva(self):
        return self.valor * 0.02  # 2% do valor do veículo

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Cilindradas: {self.cilindradas}")
        print("Tipo: Moto")
