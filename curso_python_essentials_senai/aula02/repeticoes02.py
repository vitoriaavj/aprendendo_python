#Repetições 02

msg =  input("Digite uma mensagem \n")
quat = int(input("Digite a quantidade de vezes para repetir a mensagem \n"))

for i in range(0, quat):
    print(msg)

"""
for i in range(0, quat):
    print(f"Mensagem {i + 1} - {msg}")
"""