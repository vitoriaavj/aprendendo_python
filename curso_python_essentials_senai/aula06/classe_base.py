#Classe Veiculo (classe base)

class Veiculo:
    def __init__(self, placa, modelo, marca, ano, valor):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.valor = valor

    def exibir_dados(self):
        print("-" * 40)
        print(f"Placa: {self.placa}")
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"IPVA: R$ {self.calcular_ipva():.2f}")

    def calcular_ipva(self):
        # Método genérico, sobrescrito nas subclasses (polimorfismo)
        return 0.0
