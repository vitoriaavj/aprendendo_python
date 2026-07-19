class Produto:
    def __init__(self, descricao, valor_unitario, quantidade):
        self.descricao = descricao
        self.valor_unitario = valor_unitario
        self.quantidade = quantidade
        
    def calc_total(self):
        return self.valor_unitario * self.quantidade