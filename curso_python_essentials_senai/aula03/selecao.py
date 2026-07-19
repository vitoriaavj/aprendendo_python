"""MÚLTIPLA SELEÇÃO"""
op = -1
while True:
    print("1 - OPÇÃO 1 \n 2 - OPÇÃO 2 \n 3 - OPÇÃO 3 \n 4 - OPÇÃO 4 \n 0 sair")
    op = int(input("Escolha uma opção"))

    match op:
        case 1:
            print("Escolha a opção 1")
        case 2:
            print("Escolha a opção 2")
        case 3:
            print("Escolha a opção 3")
        case 4:
            print("Escolha a opção 4")
        case 0:
            break
        case _:
            print("Opção inválida")