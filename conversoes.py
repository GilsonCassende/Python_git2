print("-------------Bemvindo  ao seu Conversor------------ \n \n ")
print("Seleciona o tipo de conversão : \n \n")
op = input("1.Kilometro para Metro \n 2.Centrimentro para Metro \n")

if op == "1":
    v1 = int(input("Insiara o valor a converter : \n"))
    c = v1 * 100
    print(f"{c} Metro")
elif op == "2":
     v1 = int(input("Insiara o valor a converter: \n"))
     c = float(v1 * 0.01)
     print(f"{c} Metro")


