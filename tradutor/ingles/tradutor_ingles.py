'''
codigo recebe uma string e busca em uma lista de palavras inglesas 
uma correspondencia, ao localizar procura o indice da palavra em 
uma segunda lista com palavras em portugues e realiza a troca
'''

original = 'The quick brown fox jumps over the lazy dog'
frase_traduzida = ''

ingles = ['quick', 'brown', 'fox', 'lazy', 'dog']
portugues = ['rapido', 'marrom', 'raposa', 'preguiçoso', 'cachorro']

# Cria um dicionário de tradução
traducao = dict(zip(ingles, portugues))

# Divide a frase em palavras
palavras = original.split()

# Traduz palavra por palavra
palavras_traduzidas = []
for palavra in palavras:
    # Remove possíveis pontuações simples
    palavra_limpa = palavra.lower()
    
    if palavra_limpa in traducao:
        palavras_traduzidas.append(traducao[palavra_limpa])
    else:
        palavras_traduzidas.append(palavra)

# Junta tudo novamente em uma string
frase_traduzida = ' '.join(palavras_traduzidas)

print(frase_traduzida)





