print("\t\t CAIXA REGISTRADORA\n")

total_compra = 0
total_produtos = 0

while True:
    try:
        nome = input("Insira o nome do produto (ou 'fim' para encerrar):\n").strip()
        if nome.lower() == "fim":
            break
        if nome == "":
            print("Erro: Produto sem nome.")
            continue

        qt = int(input("Insira a quantidade do produto:\n"))
        pr = float(input("Insira o preço do produto:\n"))

        valor_produto = qt * pr
        total_compra += valor_produto
        total_produtos += 1

        print(f"{nome} | Quantidade: {qt} | Total: R${valor_produto:.2f}\n")

    except ValueError:
        print("Erro: Digite apenas números válidos para quantidade e preço.\n")

print("=== RESUMO DA COMPRA ===")
print(f"Total de produtos cadastrados: {total_produtos}")
print(f"Valor total da compra: R${total_compra:.2f}")
if total_produtos > 0:
    print(f"Valor médio por produto: R${total_compra / total_produtos:.2f}")
else:
    print("Nenhum produto foi cadastrado.")
