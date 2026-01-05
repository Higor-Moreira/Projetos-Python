'''
Sorteia randomicamente cara ou coroa
'''
from random import choice

faces_moeda = ['Cara', 'Coroa']

continuar = True

def balanceamento():

    contador = 0
    cara = 0
    coroa = 0

    while contador < 1000:
 
        sorteado = choice(faces_moeda)

        if sorteado == 'Cara':
            cara += 1
        else:
            coroa += 1

        contador += 1
    
    print('>>>>> BALANCEAMENTO <<<<<')
    print(f'Cara - {cara}')
    print(f'Coroa - {coroa}')



def jogar_moeda():
    sorteado = choice(faces_moeda)
    print('===== JOGADA ====')
    print(sorteado)


while continuar:

    print('===== MENU =====')
    print('1 - Jogar Moeda')
    print('2 - Balanceamento (realiza mil sorteios registrando cada resultado)')
    print('3 - Sair')

    opcao = input('Digite sua opção: ')

    if opcao == '1':
        jogar_moeda()
    elif opcao == '2':
        balanceamento()
    elif opcao == '3':
        print('Encerrando...')
        continuar = False
    else:
        print('Erro, tente novamente')
