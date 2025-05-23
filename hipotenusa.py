from math import hypot

co = float(input("Insira o valor do Cosseno : \n"))
ca = float(input("Insira o valor do Cateto : \n"))
h = hypot(co, ca)
print(f"O valor da Hipotenusa é {h : .2f}")