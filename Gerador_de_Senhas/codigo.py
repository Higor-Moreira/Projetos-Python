"""
Programa gera senhas fortes usando listas com letras e caracteres especiais
e escolhendo os caracteres de forma aleatorias. 

A senha final contem letras minusculas, maiusculas, caracteres especiais e digitos. 

"""
from random import randint

#alfabeto =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç']

#caractere_especiais =  ['!', '@', '#', '$', '%', '&', '*', '?', '+', '=']

alfabeto = 'abcdefghijklmnopqrstuwvxyzç' # len = 27
caractere_especiais = '!@#$%&*?+'        # len = 9 

# fucao gera senha aleatoriamente
def Gerar_Senha():

    nova_senha = []

    while len(nova_senha) < 9:
        alfabeto_randomico = randint(1, 27)

        nova_senha.append(alfabeto[alfabeto_randomico])

        if len(nova_senha) == 2 or len(nova_senha) == 5:
            especial_randomico = randint(1, 9)
            nova_senha.append(caractere_especiais[especial_randomico])
    
    return nova_senha


print(Gerar_Senha())