'''
Remove acentuação de strings
'''

import unicodedata
import re # expressões regulares 

def limpar_string(texto):
    if not texto:
        return ""

    # separa os caracteres dos seus acentos 
    texto_normalizado = unicodedata.normalize('NFKD', texto)

    # 2. Remove os caracteres de acentuação
    texto_sem_acento = "".join([c for c in texto_normalizado if not unicodedata.combining(c)])

    # 3. Expressão Regular para manter APENAS letras (a-z, A-Z) e espaços
    # O padrão r'[^a-zA-Z\s]' significa: "Tudo que NÃO for letra ou espaço, substitua por vazio"
    # Para remover também os espaços, remova o '\s' de dentro dos colchetes.
    texto_final = re.sub(r'[^a-zA-Z\s]', '', texto_sem_acento)

    return texto_final

# --- Testando o código ---
entrada = "João gonçalves, Letícia França"
resultado = limpar_string(entrada).upper()

print(f"Original: {entrada}")
print(f"Limpo:    {resultado}")