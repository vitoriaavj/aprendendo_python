# Importa a classe Pessoa do arquivo pessoa.py
# (Neste caso, a importação é usada apenas para referência do tipo Pessoa)
from pessoa import Pessoa

# Define a classe Conta
class Conta:
    # Método construtor da classe Conta
    # É executado automaticamente quando criamos uma conta
    def __init__(self, pessoa):
        # Guarda o objeto Pessoa que é dono da conta
        # Exemplo: conta.pessoa.nome
        self.pessoa = pessoa
        # Cria o atributo privado saldo iniciando com R$ 0,00
        # Os dois _ (_ _saldo) indicam que o atributo é privado
        self.__saldo = 0

    # Cria um getter para acessar o saldo
    # Permite consultar o saldo usando: conta.saldo
    @property
    def saldo(self):
        # Retorna o valor armazenado no atributo privado __saldo
        return self.__saldo

    # Método responsável por realizar depósitos
    def depositar(self, valor):
        # Verifica se o valor do depósito é positivo
        if valor > 0:
            # Soma o valor depositado ao saldo atual
            self.__saldo += valor
        else:
            # Exibe mensagem caso o valor seja inválido
            print(f"{self.pessoa.nome}, o depósito deve ser maior que R$ 0,00.")

    # Método responsável por realizar saques
    def sacar(self, valor):
        # Verifica se existe saldo suficiente para o saque
        if valor <= self.__saldo:
            # Diminui o valor sacado do saldo da conta
            self.__saldo -= valor
        else:
            # Exibe mensagem quando o saldo é insuficiente
            print(f"{self.pessoa.nome}, sua conta não possui saldo suficiente.")