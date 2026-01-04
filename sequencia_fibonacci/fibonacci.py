'''
Docstring para fibonacci

Sequencia de numeros onde o próximo elemento é a soma dos 2 elementos anteriores

'''

contador = 0 

elemento1 = 0
elemento2 = 1
elemento3 = 1

print(elemento1)
print(elemento2)
print(elemento3)

while contador < 10:
    print(elemento2 + elemento3)

    elemento1 = elemento2
    elemento2 = elemento3
    elemento3 = elemento1 + elemento2

    contador += 1
