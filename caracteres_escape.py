
# 1. \n - Nova linha
print("Linha 1\nLinha 2")

# 2. \t - Tabulação (tab)
print("Nome:\tJoão")

# 3. \\ - Barra invertida
print("Caminho: C:\\Users\\Joao")

# 4. \' - Aspas simples
print('Ele disse: \'Oi\'')

# 5. \" - Aspas duplas
print("Ela disse: \"Olá\"")

# 6. \r - Retorno de carro
print("123456\rABC")

# 7. \b - Backspace
print("Hello\b!")

# 8. \f - Alimentação de formulário
print("Texto\fNovo")

# 9. \a - Alerta sonoro
print("Beep\a")

# 10. \v - Tabulação vertical
print("Linha1\vLinha2")

# 11. \ooo - Valor Octal (\141 = a, \142 = b, \143 = c)
print("\141\142\143")  # abc

# 12. \xhh - Valor Hexadecimal (\x61 = a, \x62 = b, \x63 = c)
print("\x61\x62\x63")  # abc

# 13. String raw (ignora os escapes)
print(r"Exemplo com \n e \t e \a")
