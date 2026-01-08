"""
Gera dois jogos, uma para servir de aposta e outro de resultado. 
Depois compara ambos até conicidirem. A cada loop é considerado um novo dia. 

Sorteios Terca, Quinta e Sabado
"""

from random import randint 

meu_jogo = []
resultado = []
dias_jogados = 0
dias_totais = 0
valor_aposta = 5
total_gasto = 0


def gerar_jogo():
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
            jogo.sort()
    
    return jogo

while True:

    meu_jogo = gerar_jogo()
    resultado = gerar_jogo()

    # contabiliza os dias levando em consideração o dia que não tem sorteio
    dias_jogados += 1
    total_gasto += valor_aposta
    if dias_jogados == 3:
        dias_totais = dias_totais + (dias_jogados + 4) 
        dias_jogados = 0

    if meu_jogo == resultado:
        print(f'Parabens, voce ganhou apos {dias_totais} dias')
        print(f'Voce gastou R$ {total_gasto}')
        break
    else:
        continue

print('Fim')
