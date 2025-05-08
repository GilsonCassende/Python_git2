v = []
s = 0


for i in range(5):
    dado = int(input(f"Insira o numero para a unidade {i} \t "))
    v.append(dado)
    s += dado

media = s / 3
for elem in v:
    print(elem, end="")
print(f"A soma dos valores é : {s} e a media do valores é : {media: .2} ")

  

