from math import sin, cos, tan, radians
a = float(input("Digite um Angulo : \n"))
seno = sin(radians(a)) 
cosseno = cos(radians(a)) 
tang = tan(radians(a))
print(f"O seno do Angulo é {seno : .2f}")
print(f"O cosseno do Angulo é {cosseno : .2f}")
print(f"A tangentes do Angulo é {tang : .2f}")