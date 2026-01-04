'''
Fatorial (n!) é a multiplicação de um número natural inteiro positivo 
por todos os seus antecessores até 1

Exemplo 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

numero = int(input('Digite um numero inteiro: '))
total_multiplicacao = numero

while numero > 1:
    total_multiplicacao *= (numero - 1)    
    numero -= 1
print(total_multiplicacao)
