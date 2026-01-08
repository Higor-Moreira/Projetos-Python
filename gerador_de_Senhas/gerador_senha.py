"""
Programa gera senhas fortes usando listas com letras e caracteres especiais
e escolhendo os caracteres de forma aleatorias. 

"""
from random import randint


alfabeto = 'abcdefghijklmnopqrstuwvxyz' # len = 25
especiais = '!@#$%&*?'
numeros = '0123456789'


# fucao gera senha aleatoriamente
def Gerar_Senha():

    nova_senha = []

    while len(nova_senha) < 10:
        randomico = randint(1, 25)

        maiscula = randint(1, 4)
        if maiscula == 2:
            nova_senha.append(alfabeto[randomico].upper()) 
        else:
            nova_senha.append(alfabeto[randomico])     
  
    return nova_senha

senha = Gerar_Senha()
senha = senha + list(especiais[randint(0, 7)]) + list(numeros[randint(0, 9)])
print(''.join(senha))