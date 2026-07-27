# Importa a biblioteca os para executar comandos do sistema operacional
# Neste caso, será usada para limpar a tela
import os

# Importa a classe Pessoa do arquivo pessoa.py
from pessoa import Pessoa
# Importa a classe Conta do arquivo conta.py
from conta import Conta
# Cria uma variável para armazenar a pessoa cadastrada
# Inicialmente ela não aponta para nenhum objeto
pessoa = None
# Cria uma variável para armazenar a conta cadastrada
# Inicialmente ela também não possui objeto
conta = None

# Cria um laço de repetição infinito
# O programa ficará executando até encontrar o comando break
while True:
    # Exibe o menu principal do sistema
    print("""
        ************* MOVIMENTAÇÃO BANCÁRIA ********

        1 - CADASTRO PESSOA
        2 - VISUALIZAR DADOS PESSOA
        3 - SALDO
        4 - DEPÓSITO
        5 - SAQUE
        0 - SAIR
    """)

    # Recebe a opção escolhida pelo usuário
    # int() transforma o texto digitado em número inteiro
    op = int(input("ESCOLHA UMA OPÇÃO \n"))
    # Estrutura de decisão semelhante ao switch/case de outras linguagens
    # Analisa o valor da variável op
    match op:
        # Caso o usuário escolha a opção 1
        case 1:
            # Solicita o nome da pessoa
            nome = input("DIGITE O NOME \n")
            # Solicita a idade e converte para inteiro
            idade = int(input("DIGITE A IDADE \n"))
            # Solicita o CPF
            # O ideal é usar string, pois CPF pode começar com zero
            cpf = input("DIGITE O CPF \n")
            # Cria um objeto Pessoa usando os dados informados
            pessoa = Pessoa(nome, idade, cpf)
            # Cria uma conta vinculada à pessoa cadastrada
            conta = Conta(pessoa)
            # Limpa a tela no Windows
            os.system("cls")
        # Caso escolha a opção 2

        case 2:
            # Limpa a tela antes de mostrar os dados
            os.system("cls")
            # Verifica se existe uma pessoa cadastrada
            if pessoa is None:
                # Caso não exista, informa ao usuário
                print("Cadastre uma pessoa primeiro.")
            else:
                # Exibe os dados da pessoa cadastrada
                pessoa.exibeDados()

        # Caso escolha a opção 3
        case 3:
            # Limpa a tela
            os.system("cls")

            # Verifica se existe uma conta criada
            if conta is None:
                print("Cadastre uma pessoa primeiro.")
            else:
                # Exibe o saldo usando a propriedade saldo
                # :.2f mostra duas casas decimais
                print(f"O SALDO DA CONTA É R$ {conta.saldo:.2f}")

        # Caso escolha a opção 4
        case 4:
            # Limpa a tela
            os.system("cls")
            # Verifica se existe uma conta
            if conta is None:
                print("Cadastre uma pessoa primeiro.")
            else:
                # Solicita o valor do depósito
                # float permite números com casas decimais
                valor = float(input("DIGITE O VALOR DE DEPÓSITO \n"))
                # Chama o método depositar da classe Conta
                conta.depositar(valor)

        # Caso escolha a opção 5
        case 5:
            # Limpa a tela
            os.system("cls")

            # Verifica se existe uma conta
            if conta is None:
                print("Cadastre uma pessoa primeiro.")
            else:
                # Solicita o valor do saque
                valor = float(input("DIGITE O VALOR DO SAQUE \n"))
                # Chama o método sacar da classe Conta
                conta.sacar(valor)

        # Caso escolha a opção 0
        case 0:
            # Limpa a tela
            os.system("cls")
            # Mensagem de encerramento
            print("SAIU DO SISTEMA!!!")
            # Encerra o while True
            break

        # Caso nenhuma opção anterior seja escolhida
        case _:
            # Limpa a tela
            os.system("cls")

            # Informa que a opção não existe
            print("Opção inválida!")