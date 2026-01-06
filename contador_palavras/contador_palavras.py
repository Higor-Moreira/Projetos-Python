'''
Código analisa um texto e conta quantas vezes uma palavra aparece

'''

arquivo = open('gato.txt') # arquivo deve estar na mesma pasta

conteudo = arquivo.read() # variavel que armazena o conteudo do arquivo 

palavra = 'gato' # palavra procurada

contagem = conteudo.count(palavra)

print(f'A palavra {palavra} aparece {contagem} vezes no arquivo {arquivo.name}')