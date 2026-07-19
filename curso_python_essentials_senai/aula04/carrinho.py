from produto import Produto

class Carrinho:
    def __init__(self):
        self.produtos = []
        
    def adicionar(self, produto: Produto):
        self.produtos.append(produto)
        
    def listar(self):
        for prod in self.produtos:
            print(f"{prod.descricao} R$ {prod.valor_unitario} {prod.quantidade}")
            
    def totalCarrinho(self):
        total = 0.0
        
        for prod in self.produtos:
            total += prod.calc_total()
            
        return total