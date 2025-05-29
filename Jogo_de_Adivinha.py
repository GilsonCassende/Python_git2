from random import choice
from time import sleep


def jogar():
    print("-------- Adivinhe um número de 1 a 5 --------\n")
    pontuacao = 0
    lista_numeros = [1, 2, 3, 4, 5]

    while True:
        n = input("Qual número estou pensando? (entre 1 e 5): ")
        print("Processando......")
        sleep(5)

        if not n.isdigit() or int(n) not in lista_numeros:
            print("Entrada inválida. Digite um número entre 1 e 5.\n")
            continue

        jogador = int(n)
        sorteado = choice(lista_numeros)

        if jogador == sorteado:
            pontuacao += 1
            print(f"🎉 Parabéns! Você acertou. Eu pensei no número {sorteado}.")
        else:
            print(f"❌ Errado! Eu pensei no número {sorteado}.")

        print(f"Pontuação atual: {pontuacao}\n")

        continuar = input("Digite [C] para continuar ou [E] para encerrar: ").strip().upper()
        if continuar == "E":
            print("\nJogo encerrado. Pontuação final:", pontuacao)
            break

    reiniciar = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
    if reiniciar == "S":
        print("\nReiniciando o jogo...\n")
        jogar()
    else:
        print("Obrigado por jogar! Até a próxima.")

# Inicia o jogo
jogar()
