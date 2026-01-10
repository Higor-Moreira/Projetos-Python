'''
Percorre uma lista e identifica o maior e o menor valor 

'''

lista_valores = [10, 8, 22, 17, 36, 45]
maior, menor = lista_valores[0], lista_valores[0]


for numero in lista_valores:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f'Maior = {maior} \n'
      f'Menor = {menor}')

