# Jogo da Forca: 
# 1 - Sorteia uma palavra da lista escolhida pelo usuario
# 2 - Usuario da um palpite, programa verifica se letra esta na palavra

import random
import os
import time

animais = ['cachorro', 'gato', 'elefante', 'tigre', 'leao']
frutas_e_legumes = [
    'abacaxi', 'carambola', 'coco verde', 'figo', 'framboesa', 'fruta do conde', 'laranja-pera',
    'mamao', 'maracuja', 'melancia', 'nectarina', 'uva', 'alface', 'cebolinha', 'couve',
    'salsa', 'abobora', 'abobrinha', 'beterraba', 'pepino', 'pimentao', 'quiabo', 'tomate',
    'abacate', 'ameixa', 'goiaba', 'jaca', 'maca', 'pera', 'pessego', 'seriguela',
    'escarola', 'hortela', 'repolho', 'gengibre', 'milho verde', 'banana-maca', 'caqui',
    'cidra', 'kiwi', 'alho-poro', 'almeirao', 'catalonha', 'berinjela', 'cara', 'chuchu',
    'inhame', 'nabo', 'batata-doce', 'cenoura', 'mandioca', 'mandioquinha', 'rabanete',
    'laranja-lima', 'mangostao', 'marmelo', 'mexerica', 'agriao', 'brocolis', 'ervilha',
    'palmito', 'banana-prata', 'cereja', 'damasco', 'graviola', 'limao', 'lichia', 'manga',
    'melao', 'roma', 'chicoria', 'coentro', 'espinafre', 'mostarda', 'salsao', 'acerola',
    'caju', 'jabuticaba', 'lima', 'endivias', 'folha de uva', 'oregano', 'rucula', 'acelga',
    'aipo', 'alcachofra', 'alho', 'arroz', 'batata', 'jilo', 'feijao', 'salvia', 'tomilho',
    'morango', 'ora-pro-nobis'
]
cidades = ['rio de janeiro', 'sao paulo', 'salvador', 'fortaleza', 'brasilia']

jogando = True

def apresentacao():
    print('=' * 30)
    print('>>>>> JOGO DA FORCA <<<<<'.center(30))
    print('=' * 30)

    print('Escolha uma categoria:')
    print('1 - Animais')
    print('2 - Frutas e Legumes')
    print('3 - Cidades')
    print('4 - Sair')

    return ''

while jogando:
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela

    print(apresentacao())

    escolha = input('Digite o número da categoria desejada: ')

    if len(escolha) > 1:
        print('Digite somente 1 opção')
        continue

    if escolha == '1':
        palavra = random.choice(animais)
    elif escolha == '2':
        palavra = random.choice(frutas_e_legumes)
    elif escolha == '3':
        palavra = random.choice(cidades)
    elif escolha == '4':
        jogando = False
        print('Obrigado por jogar! Até a próxima.')
        continue
    else:
        print('Opção inválida. Tente novamente.')
        continue

    print(f'A palavra escolhida tem {len(palavra)} letras.')

    letras_acertadas = ['_'] * len(palavra) # Multiplica o caractere '_' pelo número de letras da palavra
    tentativas = 3

    # Enquanto houver tentativas e letras não descobertas
    while tentativas > 0 and '_' in letras_acertadas:
        print(' '.join(letras_acertadas)) 
        palpite = input('Digite uma letra: ').lower()

        # verifica se foi digitado somente 1 letra
        if len(palpite) != 1 or not palpite.isalpha():
            print('Por favor, digite apenas uma letra.')
            continue
        
        # verifica se a letra esta na palavra sorteada
        if palpite in palavra:
            for i, letra in enumerate(palavra):
                if letra == palpite:
                    letras_acertadas[i] = palpite
            print(f'Você acertou a letra "{palpite}"!')
        else:
            tentativas -= 1
            print(f'A letra "{palpite}" não está na palavra. Você ainda tem {tentativas} tentativas.')

    # verifica se todas as letras foram descobertas
    if '_' not in letras_acertadas:
        print(f'Parabéns! Você adivinhou a palavra: {palavra}')
        time.sleep(5)
    else:
        print(f'Você perdeu! A palavra era: {palavra}')
        time.sleep(5)
