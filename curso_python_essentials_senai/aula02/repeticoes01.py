#Repetição com For

"""
for i in range(5):
    print(i)
"""
    
print("For definido intervalo")
for i in range (1, 6):
    print(i)

print("For saltando de dois em dois números")
for i in range (0, 10, 2):
    print(i)

print("For descrementando valor")
for i in range (10, 0, -1):
    print(i)


print("For percorrendo listas(Array)")
frutas = ["Manga", "Umbu", "Mangaba", "Laranja", "Caju"]

for item in frutas:
    print(item)