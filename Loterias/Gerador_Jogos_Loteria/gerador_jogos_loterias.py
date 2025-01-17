from random import randint 

def Menu():
    print('=' * 25)
    print('>>> GERADOR DE JOGOS <<<')
    print('=' * 25)
    print('Selecione um opcao:')
    print('1 - Mega Sena')
    print('2 - Lotofacil')
   

while True:
    Menu()

    lista_sorteio = []

    opcao = input('Digite o numero da operacao: ')

    if opcao == '1':
        for loop in range(6):
            numero_randomico = randint(1, 60)

            if numero_randomico in lista_sorteio:
                continue
            else:
                lista_sorteio.append(numero_randomico)

        print('Os numeros do seu jogo da Mega-Sena sao:')
        for numero in lista_sorteio:
            print(numero, end=' ')
        print()
    
    elif opcao == '2':
        for loop in range(15):
            numero_randomico = randint(1, 25)

            if numero_randomico in lista_sorteio:
                continue
            else:
                lista_sorteio.append(numero_randomico)

        print('Os numeros do seu jogo da Lotofacil sao:')
        for numero in lista_sorteio:
            print(numero, end=' ')
        print()
    
    