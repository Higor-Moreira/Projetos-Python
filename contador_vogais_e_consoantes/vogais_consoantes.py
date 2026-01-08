'''
Conta quantas vogais e quantas consoantes tem na 
frase, palavra ou nome digitado pelo usuario.

Antes de contar as letras, remove a acentuação.
'''

import unicodedata
import re

# ===== 1 - variaveis =====

digitado = input('Digite algo para contar: ')
vogais = 'aeiou'
consoantes = 'bcdfghjklmnpqrstvxywz'
contador_vogais = 0
contador_consoantes = 0

# ===== 2 - remover acentos =====

# separa os caracteres dos seus acentos 
texto_normalizado = unicodedata.normalize('NFKD', digitado)

# 2. Remove os caracteres de acentuação
texto_sem_acento = "".join([c for c in texto_normalizado if not unicodedata.combining(c)])

# 3. Expressão Regular para manter APENAS letras (a-z, A-Z) e espaços
# O padrão r'[^a-zA-Z\s]' significa: "Tudo que NÃO for letra ou espaço, substitua por vazio"
# Para remover também os espaços, remova o '\s' de dentro dos colchetes.
texto_final = re.sub(r'[^a-zA-Z\s]', '', texto_sem_acento)


# ===== 3 - loop =====

for letra in texto_sem_acento:
    if letra in vogais:
        contador_vogais += 1
    elif letra in consoantes:
        contador_consoantes += 1
    else:
        print(f'{letra} não identificada')

# ===== 4 - resultados =====

print('=' * 25)
print('=== ANALISE CONCLUIDA ===')
print(f'Total letras {len(digitado)}')
print(f'Vogais: {contador_vogais}')
print(f'Consoantes: {contador_consoantes}')

