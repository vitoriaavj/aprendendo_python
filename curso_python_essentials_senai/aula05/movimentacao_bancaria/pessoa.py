# Define a classe Pessoa
class Pessoa:

    # Método construtor, chamado automaticamente ao criar um objeto
    def __init__(self, nome, idade, cpf):
        # Chama o setter de nome
        self.nome = nome

        # Chama o setter de idade
        self.idade = idade

        # Chama o setter de cpf
        self.cpf = cpf

    # Getter da propriedade nome
    @property
    def nome(self):
        # Retorna o valor armazenado no atributo privado _nome
        return self._nome

    # Setter da propriedade nome
    @nome.setter
    def nome(self, novo_nome):
        # Verifica se o nome está vazio
        if not novo_nome:
            raise ValueError("O nome não pode ser vazio.")

        # Armazena o nome no atributo privado
        self._nome = novo_nome

    # Getter da propriedade idade
    @property
    def idade(self):
        # Retorna a idade armazenada
        return self._idade

    # Setter da propriedade idade
    @idade.setter
    def idade(self, idade):

        # Verifica se a idade é maior que zero
        if idade > 0:
            # Salva a idade
            self._idade = idade
        else:
            # Gera um erro caso a idade seja inválida
            raise ValueError("Idade inválida.")

    # Getter da propriedade cpf
    @property
    def cpf(self):
        # Retorna o CPF armazenado
        return self._cpf

    # Setter da propriedade cpf
    @cpf.setter
    def cpf(self, cpf):
        # Armazena o CPF
        self._cpf = cpf

    # Método para exibir os dados da pessoa
    def exibeDados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")