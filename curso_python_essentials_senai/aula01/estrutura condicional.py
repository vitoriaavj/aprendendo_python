#Estrutura condicional (if/elif/else)
valor = float(input("Digite um valor \n"))

if valor < 100:
    print(f"Desconto fr 10% de {valor} é {valor * 0.10}")
elif (valor < 500):
    print(f"Desconto de 15% de {valor} é {valor * 0.15}")
else:
    print(f"Desconto de 20% de {valor} é {valor * 0.20}")