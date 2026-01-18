'''
Docstring para blackjack

====== 🎯 Objetivo do jogo: ======

Chegar o mais próximo possível de 21 pontos sem ultrapassar esse valor.

➡️ Se passar de 21 → estoura e perde.
➡️ Se fizer exatamente 21 → ótimo, é a melhor pontuação possível.


====== 🃏 Valores das cartas ======

Cartas numeradas (2 a 10) → valem o número que mostram

➡️ Valete (J), Dama (Q) e Rei (K) → valem 10 pontos
➡️ Ás (A) → vale 1 ou 11, você escolhe o valor que for mais vantajoso


====== 👥 Participantes ======

➡️ Jogadores
➡️ Dealer (banca)


====== 🧠 Decisão do jogador ======

Depois de ver suas cartas, o jogador pode:

➡️ Pedir carta (Hit) → recebe mais uma carta
➡️ Parar (Stand) → mantém a pontuação atual
➡️ O jogador pode pedir cartas quantas vezes quiser, desde que não ultrapasse 21.


====== 🤖 Regra do dealer ======

➡️ O dealer deve comprar cartas até atingir pelo menos 17 pontos
➡️ Se fizer 17 ou mais → obrigatoriamente para
➡️ Se ultrapassar 21 → estoura e perde


====== 🏆 Quem ganha? ======

➡️ Quem tiver pontuação maior, sem ultrapassar 21
➡️ Se o jogador estourar → perde automaticamente
➡️ Se o dealer estourar → jogadores restantes ganham
➡️ Empate → push (ninguém ganha nem perde)



====== ⭐ Blackjack (21 natural) ======

➡️ e o jogador fizer 21 com apenas duas cartas (Ás + carta de valor 10):
➡️ Isso é chamado de Blackjack
➡️ Normalmente paga mais do que uma vitória comum

'''

# Pendente:
# 1 - Quantas cartas tem um baralho e a quantidade de cada uma para 
# definir a probabilidade de cada carta aparecer. 

# Naipes = 4 (Copas ♥, Paus ♣, Ouros ♦, Espadas ♠).
# Cada naipe possui 13 cartas (Ás, 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete (J), Dama (Q), Rei (K))

import random

blackjack = 21
pontos_jogador = 0
pontos_dealer = 0
continuar_jogando = True

lista_cartas = ['Às', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
mao_jogador = []
mao_dealer = []

def receber_carta():
    randomico = random.randint(0, 12)
    carta = lista_cartas[randomico]
    return carta

def menu():
    print('=' * 35)
    print('1 - Hit (Pedir carta) \n''2 - Stand (Mantém pontuação atual)')


for num in range (0, 10):
    
    carta = receber_carta()
    if carta in 'ValeteDamaRei':
        mao_jogador.append(10)
    elif carta == 'Às':
        print('Escolha o valor do Às - 1 ou 11')
        carta = int(input('Valor escolhido -> '))
        mao_jogador.append(carta)
    else:
        mao_jogador.append(int(carta))

    mao_jogador.append(receber_carta())

    mao_dealer.append(receber_carta())
    mao_dealer.append(receber_carta())

    
    print(f'Suas cartas: {mao_jogador[0]}, {mao_jogador[1]}')
    print(f'Cartas Dealer: {mao_dealer[0]}')
    print()

    mao_dealer.clear()
    mao_jogador.clear()
