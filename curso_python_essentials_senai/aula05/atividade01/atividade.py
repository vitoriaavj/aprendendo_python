class Cliente:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

class ContaBancaria:
    def __init__(self, cliente, saldo_inicial=0.0):
        self.cliente = cliente
        self.saldo = saldo_inicial

    def exibir_saldo(self):
        print(f"\nSALDO ATUAL: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        self.saldo += valor
        print("DEPÓSITO REALIZADO COM SUCESSO")

    def sacar(self, valor):
        if valor > self.saldo:
            print("SALDO INSUFICIENTE PARA SAQUE")
        else:
            self.saldo -= valor
            print("SAQUE REALIZADO COM SUCESSO")

class SistemaBancario:
    TENTATIVAS_MAXIMAS = 3

    def __init__(self, conta):
        self.conta = conta

    def autenticar(self):
        tentativas = 0
        while tentativas < self.TENTATIVAS_MAXIMAS:
            senha_digitada = input("Digite sua senha: ")
            if senha_digitada == self.conta.cliente.senha:
                return True
            print("SENHA INVÁLIDA")
            tentativas += 1

        print("O SISTEMA ENCERROU POR EXCESSO DE 3(TRÊS) TENTATIVAS DE ACESSO INVÁLIDOS")
        return False

    def exibir_menu(self):
        print("\n===== MOVIMENTAÇÃO BANCÁRIA =====")
        print("1 - Saldo")
        print("2 - Depósito")
        print("3 - Saque")
        print("0 - Sair")

    def ler_valor(self, mensagem):
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("CÓDIGO INVÁLIDO")

    def executar(self):
        if not self.autenticar():
            return

        while True:
            self.exibir_menu()
            entrada = input("Digite o código da operação: ")

            if not entrada.lstrip("-").isdigit():
                print("CÓDIGO INVÁLIDO")
                continue

            codigo = int(entrada)

            if codigo == 1:
                self.conta.exibir_saldo()
            elif codigo == 2:
                valor = self.ler_valor("Informe o valor do depósito: ")
                self.conta.depositar(valor)
            elif codigo == 3:
                valor = self.ler_valor("Informe o valor do saque: ")
                self.conta.sacar(valor)
            elif codigo == 0:
                print("\nEncerrando o sistema. Até logo!")
                break
            else:
                print("CÓDIGO INVÁLIDO")

if __name__ == "__main__":
    cliente1 = Cliente(nome="Vi", senha="1234")
    conta1 = ContaBancaria(cliente=cliente1, saldo_inicial=1000.00)

    sistema = SistemaBancario(conta1)
    sistema.executar()