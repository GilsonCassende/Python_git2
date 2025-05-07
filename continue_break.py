k = 0

for j in range(9999999999999999999999999999999999999999999999999):
    r = input("Deseja adicionar 1+ ao contador? S/N: ")
    if r == "S":
        print(k)
        k += 1
    elif r == "N":
        print("Ok")
        break
    elif r != "S" "N":
        print("Inválido")