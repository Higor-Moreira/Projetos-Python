'''
Ordena uma lista de valores por meio de seleção e troca
'''

def selection_sort(lista):

    tamanho_lista = len(lista)
    
    # Loop externo: Percorre toda a lista
    # Esse índice 'i' marca onde começa a parte "não ordenada"
    for i in range(tamanho_lista):
        
        # Inicialmente, assumimos que o primeiro elemento da parte
        # não ordenada é o menor de todos
        indice_menor = i
        
        # Loop interno: Procura o verdadeiro menor elemento no restante da lista
        # Começa de i + 1 até o final
        for j in range(i + 1, tamanho_lista):
            if lista[j] < lista[indice_menor]:
                indice_menor = j # Encontramos um novo menor, atualizamos o índice
        
        # Após varrer tudo, fazemos a troca
        # Trocamos o elemento na posição 'i' com o menor elemento encontrado
        # Sintaxe Pythonica para troca: a, b = b, a
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
        
        # Opcional: Mostrar o estado da lista a cada passo para visualizar
        # print(f"Passo {i}: {lista}")

    return lista

# ===== Teste =====
numeros = [64, 25, 12, 22, 11]
print(f"Original: {numeros}")

resultado = selection_sort(numeros)
print(f"Ordenado: {resultado}")