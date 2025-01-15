"""
Faz uma simulação de quanto tempo seria necessario para acertar na loto
considerando que cada sorteio corresponde a 1 dia e em cada dia 
será feito um sorteio novo. 

"""

from random import randint 

meu_jogo = []
resultado = []
dias = 0

def gerar_jogo():
    jogo = []
    while len(jogo) < 15:
        numero = randint(1, 25)
        if numero not in jogo:
            jogo.append(numero)
    
    return jogo

while True:

    meu_jogo = gerar_jogo()
    resultado = gerar_jogo()

    dias += 1

    if meu_jogo == resultado:
        print(f'Parabéns, você ganou após {dias} jogos feitos')
        break
    else:
        continue

print('Fim')