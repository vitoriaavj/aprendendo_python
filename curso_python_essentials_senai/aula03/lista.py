#LISTA/COLEÇÃO DE DADOS
nomes = ["Maria", "Carlos", "Ivy", "Caiu"]

#PEGANDO UM ELEMENTO DE UMA POSIÇÃO
print(nomes[2])

#EXIBINDO UM ELEMENTO DE UMA POSIÇÃO
print(nomes[1])

#ATRIBUINDO UM ELEMENTO DE UMA POSIÇÃO
nomes[1] = "Paula"

#EXIBINDO UM ELEMENTO DE UMA POSIÇÃO
print(nomes[1])

#PERCORRER UMA LISTA
print("*****Percorrendo arreio*****")
for nome in nomes:
    print(nome)

#TAMANHO
print(f"Toatal de elementos {len(nomes)}")