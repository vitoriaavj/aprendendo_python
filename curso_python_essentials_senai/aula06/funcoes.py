#Funções auxiliares: entrada de dados e ações do menu

from classe_car import Carro
from classe_moto import Moto


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")


def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def cadastrar_carro(garagem):
    print("\n--- Cadastro de Carro ---")
    placa = input("Placa: ").strip()

    if garagem.buscar_veiculo(placa) is not None:
        print(f"\nErro: já existe um veículo cadastrado com a placa {placa}.")
        return

    modelo = input("Modelo: ").strip()
    marca = input("Marca: ").strip()
    ano = ler_int("Ano: ")
    valor = ler_float("Valor do veículo: R$ ")
    quantidade_portas = ler_int("Quantidade de portas: ")

    carro = Carro(placa, modelo, marca, ano, valor, quantidade_portas)
    garagem.adicionar_veiculo(carro)


def cadastrar_moto(garagem):
    print("\n--- Cadastro de Moto ---")
    placa = input("Placa: ").strip()

    if garagem.buscar_veiculo(placa) is not None:
        print(f"\nErro: já existe um veículo cadastrado com a placa {placa}.")
        return

    modelo = input("Modelo: ").strip()
    marca = input("Marca: ").strip()
    ano = ler_int("Ano: ")
    valor = ler_float("Valor do veículo: R$ ")
    cilindradas = ler_int("Cilindradas: ")

    moto = Moto(placa, modelo, marca, ano, valor, cilindradas)
    garagem.adicionar_veiculo(moto)


def buscar_veiculo_menu(garagem):
    placa = input("\nDigite a placa do veículo: ").strip()
    veiculo = garagem.buscar_veiculo(placa)
    if veiculo is not None:
        veiculo.exibir_dados()
    else:
        print(f"\nVeículo com placa {placa} não encontrado.")


def remover_veiculo_menu(garagem):
    placa = input("\nDigite a placa do veículo a remover: ").strip()
    garagem.remover_veiculo(placa)


def calcular_ipva_menu(garagem):
    placa = input("\nDigite a placa do veículo: ").strip()
    veiculo = garagem.buscar_veiculo(placa)
    if veiculo is not None:
        print(f"\nIPVA do veículo {placa}: R$ {veiculo.calcular_ipva():.2f}")
    else:
        print(f"\nVeículo com placa {placa} não encontrado.")


def submenu_listar(garagem):
    print("\n--- Listar Veículos ---")
    print("1 - Todos")
    print("2 - Apenas carros")
    print("3 - Apenas motos")
    print("4 - A partir de um determinado ano")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        garagem.listar_veiculos()
    elif opcao == "2":
        garagem.listar_carros()
    elif opcao == "3":
        garagem.listar_motos()
    elif opcao == "4":
        ano = ler_int("Digite o ano mínimo: ")
        garagem.listar_por_ano(ano)
    else:
        print("Opção inválida.")
