"""
Programa gera senhas fortes usando listas com letras e caracteres especiais
e escolhendo os caracteres de forma aleatorias. 

A senha final contem letras minusculas, maiusculas, caracteres especiais e digitos. 

"""
from random import randint

alfabeto =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç']
caractere_especiais =  ['!', '@', '#', '$', '%', '&', '*', '?', '+', '=']

# fucao gera senha aleatoriamente
def Gerar_Senha():

    nova_senha = []

    while nova_senha < 9:
