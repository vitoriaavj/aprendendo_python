#Menu principal do sistema

from classe_garagem import Garagem
from funcoes import (
    cadastrar_carro,
    cadastrar_moto,
    submenu_listar,
    buscar_veiculo_menu,
    remover_veiculo_menu,
    calcular_ipva_menu,
)


def exibir_menu():
    print("\n===== SISTEMA DE CADASTRO DE VEÍCULOS =====")
    print("1 - Cadastrar Carro")
    print("2 - Cadastrar Moto")
    print("3 - Listar Veículos")
    print("4 - Buscar Veículo")
    print("5 - Remover Veículo")
    print("6 - Calcular IPVA de um Veículo")
    print("7 - Calcular Total de IPVA")
    print("0 - Sair")


def main():
    garagem = Garagem()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_carro(garagem)
        elif opcao == "2":
            cadastrar_moto(garagem)
        elif opcao == "3":
            submenu_listar(garagem)
        elif opcao == "4":
            buscar_veiculo_menu(garagem)
        elif opcao == "5":
            remover_veiculo_menu(garagem)
        elif opcao == "6":
            calcular_ipva_menu(garagem)
        elif opcao == "7":
            total = garagem.calcular_total_ipva()
            print(f"\nTotal de IPVA de todos os veículos: R$ {total:.2f}")
        elif opcao == "0":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
