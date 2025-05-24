from random import choice
""""
n1 = input("Insira o primeiro nome : \n")
n2 = input("Insira o segundo nome : \n")
n3 = input("Insira o treicero nome : \n")
n4 = input("Insira o quarto nome : \n")
l = [n1, n2, n3, n4]
s = choice(l)
print(f"Nome sorteado : {s}")
"""
l = []

for i in range(4):
    n = input(f"Insira o Nome {i} : \n")
    l.append(n)
s = choice(l) 

print(f"O nome Sorteado é : {s}")

