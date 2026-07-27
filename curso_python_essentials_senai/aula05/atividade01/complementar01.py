class Cliente:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha


class ContaBancaria:
    def __init__(self, numero, cliente, saldo_inicial=0.0):
        self.numero = numero
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


class Banco:
    def __init__(self):
        self.contas = {}
        self._proximo_numero = 1

    def cadastrar_cliente(self, nome, senha, saldo_inicial=0.0):
        numero = self._proximo_numero
        cliente = Cliente(nome, senha)
        conta = ContaBancaria(numero, cliente, saldo_inicial)
        self.contas[numero] = conta
        self._proximo_numero += 1
        print(f"\nCLIENTE CADASTRADO COM SUCESSO! Número da conta: {numero}")
        return numero

    def buscar_conta(self, numero):
        return self.contas.get(numero)


class SistemaBancario:
    TENTATIVAS_MAXIMAS = 3

    def __init__(self, banco):
        self.banco = banco

    def ler_valor(self, mensagem):
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("CÓDIGO INVÁLIDO")

    def ler_inteiro(self, mensagem):
        while True:
            entrada = input(mensagem)
            if entrada.lstrip("-").isdigit():
                return int(entrada)
            print("CÓDIGO INVÁLIDO")

    def cadastrar_novo_cliente(self):
        print("\n----- CADASTRO DE NOVO CLIENTE -----")
        nome = input("Nome do cliente: ")
        senha = input("Defina uma senha: ")
        saldo_inicial = self.ler_valor("Saldo inicial (0 se não houver): ")
        self.banco.cadastrar_cliente(nome, senha, saldo_inicial)

    def autenticar(self, conta):
        tentativas = 0
        while tentativas < self.TENTATIVAS_MAXIMAS:
            senha_digitada = input("Digite sua senha: ")
            if senha_digitada == conta.cliente.senha:
                return True
            print("SENHA INVÁLIDA")
            tentativas += 1

        print("O SISTEMA ENCERROU POR EXCESSO DE 3(TRÊS) TENTATIVAS DE ACESSO INVÁLIDOS")
        return False

    def exibir_menu_operacoes(self):
        print("\n===== MOVIMENTAÇÃO BANCÁRIA =====")
        print("1 - Saldo")
        print("2 - Depósito")
        print("3 - Saque")
        print("0 - Sair")

    def operar_conta(self, conta):
        if not self.autenticar(conta):
            return

        print(f"\nBem-vindo(a), {conta.cliente.nome}!")
        while True:
            self.exibir_menu_operacoes()
            codigo = self.ler_inteiro("Digite o código da operação: ")

            if codigo == 1:
                conta.exibir_saldo()
            elif codigo == 2:
                valor = self.ler_valor("Informe o valor do depósito: ")
                conta.depositar(valor)
            elif codigo == 3:
                valor = self.ler_valor("Informe o valor do saque: ")
                conta.sacar(valor)
            elif codigo == 0:
                print("\nSaindo da conta...")
                break
            else:
                print("CÓDIGO INVÁLIDO")

    def acessar_conta(self):
        numero = self.ler_inteiro("Número da conta: ")
        conta = self.banco.buscar_conta(numero)
        if conta is None:
            print("CONTA NÃO ENCONTRADA")
            return
        self.operar_conta(conta)

    def exibir_menu_principal(self):
        print("\n========== BANCO SENAI ==========")
        print("1 - Acessar minha conta")
        print("2 - Cadastrar novo cliente")
        print("0 - Sair do sistema")

    def executar(self):
        while True:
            self.exibir_menu_principal()
            codigo = self.ler_inteiro("Digite o código da operação: ")

            if codigo == 1:
                self.acessar_conta()
            elif codigo == 2:
                self.cadastrar_novo_cliente()
            elif codigo == 0:
                print("\nEncerrando o sistema. Até logo!")
                break
            else:
                print("CÓDIGO INVÁLIDO")


if __name__ == "__main__":
    banco = Banco()
    banco.cadastrar_cliente(nome="Vi", senha="1234", saldo_inicial=1000.00)

    sistema = SistemaBancario(banco)
    sistema.executar()