'''
A Conjectura de Collatz é um famoso problema matemático não resolvido que propõe que, 
ao começar com qualquer número inteiro positivo e aplicar repetidamente as regras abaixo,
a sequência sempre chegará ao número 1.

1 - Escolha um número inteiro positivo (n).

2 - Se o número for par: Divida-o por 2 (n/2).

3 - Se o número for ímpar: Multiplique-o por 3 e adicione 1 (3n + 1).

4 - Repita o processo com o novo número. 
'''

numero = int(input('Digite um numero inteiro: '))

while numero != 1:
    if numero % 2 == 0: # verifica se é par 
        numero = numero / 2
        print(int(numero))
    else:
        numero = numero * 3 + 1
        print(int(numero))
