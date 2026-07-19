#Contador e acumulador

cont =  0
acum = 0
num = 0

while num >= 0:
    num = int(input("Digite um número \n"))

    #Contador
    cont += 1

    #Acumulador
    acum += num 

print(f"Total de números digitado {cont}")
print(f"A soma dos números digitados {acum}")
