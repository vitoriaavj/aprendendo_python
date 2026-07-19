menor18 = 0
maior65 = 0
masculino = 0
feminino = 0

for i in range(20):
    print(f"\nPessoa {i + 1}")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    if idade < 18:
        menor18 += 1

    if idade > 65:
        maior65 += 1

    if sexo == "M":
        masculino += 1
    elif sexo == "F":
        feminino += 1

print("\nRESULTADO")
print("Pessoas com menos de 18 anos:", menor18)
print("Pessoas com mais de 65 anos:", maior65)
print("Total do sexo masculino:", masculino)
print("Total do sexo feminino:", feminino)

quantidade = 0
soma = 0

while True:
    produto = input("\nNome do produto: ")
    valor = float(input("Valor do produto: R$ "))

    quantidade += 1
    soma += valor

    continuar = input("Deseja cadastrar outro produto? (S/N): ").strip().upper()

    if continuar == "N":
        break

media = soma / quantidade

print("\nRESULTADO")
print("Total de produtos:", quantidade)
print(f"Soma dos valores: R$ {soma:.2f}")
print(f"Média dos valores: R$ {media:.2f}")