#MÉTODOS PARA LISTA
import os

cidades = []

op = -1

while True:
    print("1 - ADICIONAR \n 2- LISTA \n 3 - LISTA NUMERADA \n 4 - REMOVER PELO INDICI \n 5 - REMOVER PELO ELEMENTO \n 6- ALTERAR \n 0 - SAIR")

    op = int(input("Escolha sua opção"))
    
    match op:
        case 1:
            cidade = input("Digite o nome de uma cidade \n")
            cidades.append(cidade)
            os.system("cls")
        case 2:
            os.system("cls")
            for cidade in cidades:
                print(cidade)
        case 3: 
            os.system("cls")

            print("*****Lista numerada*****")
            for i in range(len(cidades)):
                print(f"{i + 1} - {cidades[i]}")

            print("************************ \n")

        case 4:
            pos = int(input("Digite a opção do elemento"))
            #A FUNÇÃO pop REMOVE O ELEMENTO A PARTIR DA POSIÇÃO DO ÍNDICE DA LISTA
            cidades.pop(pos)

        case 5:
            cidade = input("Digite o nome da cidade")
            #A FUNÇÃO remove REMOVE O ELEMENTO A PARTIR DO NOME DO ELEMENTO
            cidades.remove(cidade)

        case 6:
            pos =  int(input("Digite a posição do elemento"))
            cidades[pos] = input("Digite o nome da cidade \n")


        case 0:
            break
        case _:
            print("Opção inválida!")