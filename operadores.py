n1 = 0000
n2 = 000
soma = 0000
divisao = 000.000
multiplicacao = 000000000
subtracao = 00000

n1 = int(input("Digite o primeiro numero: \n"))
n2 = int(input("Digite o segundo numero : \n"))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

print(f"soma = {soma} \n subtração = {subtracao} \n multiplicação  = {multiplicacao} \n divisão = {divisao : .2f}")
soma += soma

print(f" incremento da soma = {soma}")
soma -= soma

print(f"Decremente da soma = {soma}")


