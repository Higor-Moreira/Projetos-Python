'''
FizzBuzz é um jogo de palavras infantil que envolve contar, 
substituindo múltiplos de 3 por "Fizz", múltiplos de 5 por "Buzz", 
e múltiplos de ambos por "FizzBuzz", enquanto o restante dos números 
são impressos normalmente, testando lógica básica de programação e divisão. 

'''

numero_digitado = int(input('Digite até que numero deseja contar: '))
contador = 0

for numero in range(numero_digitado):
    
    # verifica os numeros que são multiplos de 3 e 5
    if numero % 3 == 0 and numero % 5 == 0:
        print('FizzBuzz')

    # verifica os numeros multiplos de 3
    elif numero % 3 == 0:
        if numero % 5 != 0:
            print('Fizz')

    # verifica os numeros multiplos de 5
    elif numero % 5 == 0:
        if numero % 3 != 0:
            print('Buzz')
    
    # caso não se encaixe em nenhuma das condições acima, é impresso na tela.
    else:
        print(numero)
