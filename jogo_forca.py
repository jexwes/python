import random

palavras = ["abacaxi", "banana", "cenoura", "dente", "elefante", "futebol", "guitarra", "hospital", "igreja", "janela"]

palavra = random.choice(palavras)

letras_certas = []
letras_erradas = []
tentativas = 6

while tentativas > 0:
    for letra in palavra:
        if letra in letras_certas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

    print("Letras erradas:", letras_erradas)

    letra = input("Digite uma letra: ").lower()

    if letra in letras_certas or letra in letras_erradas:
        print("Você já escolheu essa letra. Tente outra.")
    elif letra in palavra:
        print("Acertou!")
        letras_certas.append(letra)
    else:
        print("Errou.")
        letras_erradas.append(letra)
        tentativas -= 1

    if set(palavra) <= set(letras_certas):
        print("Parabéns, você ganhou!")
        break

    if tentativas == 0:
        print("Que pena, você perdeu. A palavra era", palavra)