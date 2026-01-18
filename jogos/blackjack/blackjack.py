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
cartas = {1: 'Às',
          2: '2',
          3: '3',
          4: '4',
          5: '5',
          6: '6',
          7: '7',
          8: '8',
          9: '9',
          10: '10',
          }

lista_cartas = ['Às', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

randomico = random.randint(1, 12)

print(lista_cartas[randomico])