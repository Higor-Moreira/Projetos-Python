'''
Verifica se o nome ou palavra digitada pelo usuario
'''

palavra = input('Digite um nome ou palavra: ').strip()

numero_letras = len(palavra)

inverso = ''

for letra in palavra:
    inverso += palavra[numero_letras - 1]
    numero_letras -= 1

if palavra == inverso:
    print(f'{palavra} é um palíndromo')
else:
    print(f'{palavra} NÃO é um palíndromo')

