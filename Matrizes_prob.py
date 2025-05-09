l = [

  [],
  [],
  []
]
print("\n \n Numeros da 1 Linha \n \n")
for i in range(4):
    l1 = int(input("Insira os numeros da primeira lista : \n"))
    l[0].append(l1)

print("\n \n Numeros da 2 linha \n \n")

for j in range(4):
    l2 = int(input("Insira os numeros da segunda lista : \n"))
    l[1].append(l2)

print("\n \n Numeros da 3 Lista \n \n")

for a in range(4):
    l3 = int(input("Insira os numeros da Terceira lista : \n"))
    l[2].append(l3) 


print("\nNumeros digitados na linha 1 : \n")
for elem in l[0]:
    print(elem, end=" ")

print("\nNumeros digitados na linha 2 : \n")
for lista2 in l[1]:
    print(lista2, end=" ") 

print("\nNumeros digitados na linha 3 : \n")
for lista3 in l[2]:
    print(lista3, end=" ")