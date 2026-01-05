'''
Numero primo é aquele que é divisivel somente por 1 e por ele mesmo 

'''

while True:
    numero = int(input('Digite um numero positivo: '))

    # numeros negativos, zero e 1 não são primos
    if numero < 2:
        print(f'{numero} não é um numero primo')

    # 2 é o unico numero par que é primo
    elif numero == 2:
        print('2 é um numero primo')

    # eliminando outros numeros pares
    elif numero % 2 == 0:
        print(f'{numero} não é primo')

    # demais numeros 
    