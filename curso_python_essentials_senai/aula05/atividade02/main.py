"""
Sistema de Gerenciamento de uma Loja Virtual de Produtos Eletrônicos
---------------------------------------------------------------------
Trabalho: PYTHON ESSENTIALS - SENAI
Docente: Alisson Freire Batista

Programa único (sem dependência de outros arquivos) que simula o
funcionamento básico de uma loja virtual, utilizando Programação
Orientada a Objetos (POO) com as classes:
    - Produto
    - Cliente
    - Venda
    - Loja (organiza e integra as demais classes)

COMO EXECUTAR:
    1) Salve este arquivo como main.py (ou qualquer nome).
    2) Abra o terminal na pasta onde ele está salvo.
    3) Digite:  python main.py
       (em alguns sistemas o comando é "python3 main.py")
"""

from datetime import datetime


# =========================================================
# CLASSE 1 - PRODUTO
# =========================================================
class Produto:
    """Representa um produto cadastrado na loja."""

    def __init__(self, codigo, nome, categoria, preco, estoque):
        self._codigo = codigo
        self._nome = nome
        self._categoria = categoria
        self._preco = preco
        self._estoque = estoque

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @property
    def estoque(self):
        return self._estoque

    def exibir_dados(self):
        """Apresenta as informações do produto."""
        print("-" * 40)
        print(f"Código   : {self._codigo}")
        print(f"Nome     : {self._nome}")
        print(f"Categoria: {self._categoria}")
        print(f"Preço    : R$ {self._preco:.2f}")
        print(f"Estoque  : {self._estoque} unidade(s)")
        print("-" * 40)

    def adicionar_estoque(self, quantidade):
        """Aumenta o estoque do produto."""
        if quantidade <= 0:
            print("Quantidade inválida para adicionar ao estoque.")
            return
        self._estoque += quantidade
        print(f"Estoque de '{self._nome}' atualizado: {self._estoque} unidade(s).")

    def remover_estoque(self, quantidade):
        """Reduz o estoque quando houver venda. Retorna True/False."""
        if quantidade <= 0:
            print("Quantidade inválida para remover do estoque.")
            return False
        if quantidade > self._estoque:
            print(
                f"Estoque insuficiente para '{self._nome}'. "
                f"Disponível: {self._estoque}, solicitado: {quantidade}."
            )
            return False
        self._estoque -= quantidade
        return True


# =========================================================
# CLASSE 2 - CLIENTE
# =========================================================
class Cliente:
    """Representa um cliente cadastrado na loja."""

    def __init__(self, nome, cpf, email):
        self._nome = nome
        self._cpf = cpf
        self._email = email

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    def exibir_dados(self):
        """Mostra os dados do cliente."""
        print("-" * 40)
        print(f"Nome : {self._nome}")
        print(f"CPF  : {self._cpf}")
        print(f"Email: {self._email}")
        print("-" * 40)


# =========================================================
# CLASSE 3 - VENDA (associação entre Cliente e Produto)
# =========================================================
class Venda:
    """Representa uma venda realizada, associando Cliente e Produto."""

    def __init__(self, cliente, produto, quantidade):
        self._cliente = cliente
        self._produto = produto
        self._quantidade = quantidade
        self._valor_total = 0.0
        self._data = datetime.now()
        self.calcular_total()

    @property
    def valor_total(self):
        return self._valor_total

    def calcular_total(self):
        """Calcula o valor total da compra."""
        self._valor_total = self._produto.preco * self._quantidade
        return self._valor_total

    def exibir_venda(self):
        """Mostra os dados da venda realizada."""
        print("-" * 40)
        print(f"Data      : {self._data.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Cliente   : {self._cliente.nome}")
        print(f"Produto   : {self._produto.nome}")
        print(f"Quantidade: {self._quantidade}")
        print(f"Valor total: R$ {self._valor_total:.2f}")
        print("-" * 40)


# =========================================================
# CLASSE 4 - LOJA (gerencia tudo e aplica as regras de negócio)
# =========================================================
class Loja:
    """Gerencia produtos, clientes e vendas da loja virtual."""

    def __init__(self, nome="Loja Virtual"):
        self._nome = nome
        self._produtos = []
        self._clientes = []
        self._vendas = []

    # ---------- Produto ----------
    def cadastrar_produto(self, codigo, nome, categoria, preco, estoque):
        if self.buscar_produto(codigo) is not None:
            print(f"Já existe um produto com o código '{codigo}'.")
            return None
        produto = Produto(codigo, nome, categoria, preco, estoque)
        self._produtos.append(produto)
        print(f"Produto '{nome}' cadastrado com sucesso!")
        return produto

    def buscar_produto(self, codigo):
        for produto in self._produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def listar_produtos(self):
        if not self._produtos:
            print("Nenhum produto cadastrado.")
            return
        print("\n===== LISTA DE PRODUTOS =====")
        for produto in self._produtos:
            produto.exibir_dados()

    # ---------- Cliente ----------
    def cadastrar_cliente(self, nome, cpf, email):
        if self.buscar_cliente(cpf) is not None:
            print(f"Já existe um cliente com o CPF '{cpf}'.")
            return None
        cliente = Cliente(nome, cpf, email)
        self._clientes.append(cliente)
        print(f"Cliente '{nome}' cadastrado com sucesso!")
        return cliente

    def buscar_cliente(self, cpf):
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def listar_clientes(self):
        if not self._clientes:
            print("Nenhum cliente cadastrado.")
            return
        print("\n===== LISTA DE CLIENTES =====")
        for cliente in self._clientes:
            cliente.exibir_dados()

    # ---------- Venda ----------
    def realizar_venda(self, cpf_cliente, codigo_produto, quantidade):
        cliente = self.buscar_cliente(cpf_cliente)
        if cliente is None:
            print("Cliente não encontrado. Cadastre o cliente antes de vender.")
            return None

        produto = self.buscar_produto(codigo_produto)
        if produto is None:
            print("Produto não encontrado.")
            return None

        if not produto.remover_estoque(quantidade):
            print("Venda não realizada: estoque insuficiente.")
            return None

        venda = Venda(cliente, produto, quantidade)
        self._vendas.append(venda)
        print("Venda realizada com sucesso!")
        venda.exibir_venda()
        return venda

    def exibir_vendas(self):
        if not self._vendas:
            print("Nenhuma venda realizada até o momento.")
            return
        print("\n===== RELATÓRIO DE VENDAS =====")
        total_geral = 0.0
        for venda in self._vendas:
            venda.exibir_venda()
            total_geral += venda.valor_total
        print(f"\nTotal de vendas realizadas: {len(self._vendas)}")
        print(f"Valor total acumulado     : R$ {total_geral:.2f}")


# =========================================================
# FUNÇÕES DO MENU / INTERFACE
# =========================================================
def exibir_menu():
    print("\n========= LOJA VIRTUAL =========")
    print("1 - Cadastrar produto")
    print("2 - Cadastrar cliente")
    print("3 - Realizar venda")
    print("4 - Listar produtos")
    print("5 - Listar clientes")
    print("6 - Exibir vendas")
    print("0 - Sair")


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número (ex: 10.50).")


def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def cadastrar_produto(loja):
    print("\n--- Cadastro de Produto ---")
    codigo = input("Código: ").strip()
    nome = input("Nome: ").strip()
    categoria = input("Categoria: ").strip()
    preco = ler_float("Preço: R$ ")
    estoque = ler_int("Estoque inicial: ")
    loja.cadastrar_produto(codigo, nome, categoria, preco, estoque)


def cadastrar_cliente(loja):
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    email = input("Email: ").strip()
    loja.cadastrar_cliente(nome, cpf, email)


def realizar_venda(loja):
    print("\n--- Realizar Venda ---")
    cpf = input("CPF do cliente: ").strip()
    codigo = input("Código do produto: ").strip()
    quantidade = ler_int("Quantidade: ")
    loja.realizar_venda(cpf, codigo, quantidade)


def main():
    loja = Loja("Loja Virtual de Produtos Eletrônicos")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto(loja)
        elif opcao == "2":
            cadastrar_cliente(loja)
        elif opcao == "3":
            realizar_venda(loja)
        elif opcao == "4":
            loja.listar_produtos()
        elif opcao == "5":
            loja.listar_clientes()
        elif opcao == "6":
            loja.exibir_vendas()
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
