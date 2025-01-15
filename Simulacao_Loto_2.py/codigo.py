"""
Versao 2 

Faz uma simulação de quanto tempo seria necessario para acertar na loto
considerando que sera repetido o mesmo jogo 

"""

from random import randint 

meu_jogo = [1, 2, 3, 5, 7, 9, 11, 14, 15, 16, 17, 19, 20, 21, 25]
resultado = []
dias = 0


def gerar_jogo():
    jogo = []
    while len(jogo) < 15:
        numero = randint(1, 25)
        if numero not in jogo:
            jogo.append(numero)
            jogo.sort()
    
    return jogo

while True:

    resultado = gerar_jogo()

    dias += 1

    if meu_jogo == resultado:
        print(f'Parabéns, você ganou após {dias} jogos feitos')
        break
    else:
        continue

print('Fim')
