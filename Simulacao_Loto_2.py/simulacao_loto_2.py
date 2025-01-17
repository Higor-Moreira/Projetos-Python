"""
Versao 2 

Faz uma simulação de quanto tempo seria necessario para acertar na loto
considerando que sera repetido o mesmo jogo 

"""

from random import randint 

meu_jogo = [1, 2, 3, 5, 7, 9, 11, 14, 15, 16, 17, 19, 20, 21, 25]
resultado = []
dias_jogados = 0
dias_totais = 0
valor_aposta = 3
total_gasto = 0


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

    # contabiliza os dias levando em consideração o dia que não tem sorteio
    dias_jogados += 1
    total_gasto += valor_aposta
    if dias_jogados == 6:
        dias_totais = dias_totais + (dias_jogados + 1) 
        dias_jogados = 0

    if meu_jogo == resultado:
        print(f'Parabens, voce ganhou apos {dias_totais} dias')
        print(f'Voce gastou R$ {total_gasto}')
        break
    else:
        continue

print('Fim')
