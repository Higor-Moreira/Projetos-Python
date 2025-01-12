jogo_1 = [2, 4, 5, 6, 8, 9, 10, 11, 16, 18, 19, 21, 23, 24, 25]

jogo_2 = [2, 3, 5, 7, 8, 10, 11, 13, 15, 16, 18, 20, 21, 23, 24]

jogo_3 = [1, 2, 5, 6, 7, 9, 11, 13, 15, 16, 18, 19, 21, 24, 25]

resultado = [1, 3, 4, 5, 6, 7, 10, 12, 14, 15, 16, 17, 18, 20, 23]

acertos = 0

for numero in jogo_1:
    if numero in resultado:
        acertos += 1

print(f'Voce acertou {acertos} numeros no jogo 1!')
acertos = 0

for numero in jogo_2:
    if numero in resultado:
        acertos += 1

print(f'Voce acertou {acertos} numeros no jogo 2!')
acertos = 0

for numero in jogo_3:
    if numero in resultado:
        acertos += 1

print(f'Voce acertou {acertos} numeros no jogo 3!')
acertos = 0
