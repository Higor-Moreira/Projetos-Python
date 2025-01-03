meu_jogo = [2, 4, 5, 6, 8, 9, 10, 11, 16, 18, 19, 21, 23, 24, 25]

sorteio = [9, 10 , 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25]

acertos = 0

for numero in meu_jogo:
    if numero in sorteio:
        acertos += 1

print(f'Voce acertou {acertos} numeros!')

