from produto import Produto
from carrinho import Carrinho

prod1 = Produto("Arroz", 2.00, 5)
prod2 = Produto("Feijão", 3.00, 3)
prod3 = Produto("Leite", 6.00, 4)
prod4 = Produto("Manteiga", 12, 2)

carrinho_compras = Carrinho()
carrinho_compras.adicionar(prod1)
carrinho_compras.adicionar(prod2)
carrinho_compras.adicionar(prod3)
carrinho_compras.adicionar(prod4)

carrinho_compras.listar()

print(f"Valor total R$ {carrinho_compras.totalCarrinho()}")