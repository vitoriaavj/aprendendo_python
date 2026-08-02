#Classe Garagem

from classe_car import Carro
from classe_moto import Moto


class Garagem:
    def __init__(self):
        self.lista_veiculos = []

    def adicionar_veiculo(self, veiculo):
        if self.buscar_veiculo(veiculo.placa) is not None:
            print(f"\nErro: já existe um veículo cadastrado com a placa {veiculo.placa}.")
            return False
        self.lista_veiculos.append(veiculo)
        print(f"\nVeículo com placa {veiculo.placa} cadastrado com sucesso!")
        return True

    def listar_veiculos(self, veiculos=None):
        veiculos = self.lista_veiculos if veiculos is None else veiculos

        if not veiculos:
            print("\nNenhum veículo cadastrado.")
            return

        print("\n===== LISTA DE VEÍCULOS =====")
        for veiculo in veiculos:
            veiculo.exibir_dados()
        print("-" * 40)
        print(f"Total de veículos: {len(veiculos)}")

    def listar_carros(self):
        carros = [v for v in self.lista_veiculos if isinstance(v, Carro)]
        self.listar_veiculos(carros)

    def listar_motos(self):
        motos = [v for v in self.lista_veiculos if isinstance(v, Moto)]
        self.listar_veiculos(motos)

    def listar_por_ano(self, ano_minimo):
        filtrados = [v for v in self.lista_veiculos if v.ano >= ano_minimo]
        self.listar_veiculos(filtrados)

    def buscar_veiculo(self, placa):
        for veiculo in self.lista_veiculos:
            if veiculo.placa.upper() == placa.upper():
                return veiculo
        return None

    def remover_veiculo(self, placa):
        veiculo = self.buscar_veiculo(placa)
        if veiculo is not None:
            self.lista_veiculos.remove(veiculo)
            print(f"\nVeículo com placa {placa} removido com sucesso!")
            return True
        print(f"\nVeículo com placa {placa} não encontrado.")
        return False

    def calcular_total_ipva(self):
        total = sum(veiculo.calcular_ipva() for veiculo in self.lista_veiculos)
        return total
