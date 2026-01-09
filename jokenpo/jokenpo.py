'''
1 - Usuario escolhe entre pedra, papel ou tesoura.

2 - Computador sorteia uma jogada

3 - Código compara jogadas e informa ganhador
'''

from random import choice
import emoji

jogadas = ['Pedra', 'Papel', 'Tesoura']

# menu de informações iniciais
def menu():
    print('=' * 20)
    print('>>>>> JOKENPÔ <<<<<')
    print('1 - Pedra \n' 
          '2 - Papel \n' 
          '3 - Tesoura \n'
          '4 - Sair do Jogo')

# ===== 3 - Verifica vencedor =====
def verificar_vencedor(usuario, computador):
    if usuario == computador:
        print(f'Você - {usuario}')
        print(f'Computador - {computador}')
        print(f'Empate!')

    elif usuario == 'Pedra':
        if computador == 'Papel':
            print(f'Você - {usuario}')
            print(f'Computador - {computador}')
            print(emoji.emojize('Computador venceu :trophy:', language='alias'))
        else:
            print(f'Você - {usuario}')
            print(f'Computador - {computador}')
            print(emoji.emojize('Você venceu :trophy:', language='alias'))

    elif usuario == 'Papel':
        if computador == 'Pedra':
            print(f'Você - {usuario}')
            print(f'Computador - {computador}')
            print(emoji.emojize('Você venceu :trophy:', language='alias'))
        else:
            print(f'Você - {usuario}')
            print(f'Computador - {computador}')
            print(emoji.emojize('Computador venceu :trophy:', language='alias'))

    elif usuario == 'Tesoura':
        if computador == 'Papel':
            print(f'Você - {usuario}')
            print(f'Computador - {computador}')
            print(emoji.emojize('Você venceu :trophy:', language='alias'))
        else:
            print(f'Você - {usuario}')
            print(f'Computador - {computador}')
            print(emoji.emojize('Computador venceu :trophy:', language='alias'))


# ===== Loop do jogo =====
while True:

    menu()

    # ===== 1 - jogada do usuario =====
    jogada_usuario = input('Digite o numero da jogada: ')

    # Tenta convertar o str em int
    try:
        jogada_usuario = int(jogada_usuario)
    except:
        print('Erro! Digite o indice da jogada escolhida: 1, 2 ou 3.')
        continue

    # verifica se o numero esta dentro das opções
    if jogada_usuario < 1 or jogada_usuario > 4:
        print('Numero fora das opções disponiveis')
        continue
    elif jogada_usuario == 4:
        print('Obrigado por jogar')
        break

    # transforma o numero da jogada em um item da lista
    jogada_usuario = jogadas[jogada_usuario - 1]

    # ===== 2 - Jogada Computador =====

    # escolhe aleatoriamente uma jogada para o computador
    jogada_computador = choice(jogadas)

    verificar_vencedor(jogada_usuario, jogada_computador)

print('Fim do código')
