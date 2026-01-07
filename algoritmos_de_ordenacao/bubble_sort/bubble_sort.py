'''
Algoritmo de ordenação ideal para listas pequenas 

'''

def bubble_sort(lista):
    n = len(lista)
    
    # Percorre toda a lista
    for i in range(n):
        trocou = False
        
        # O último i elementos já estão no lugar certo
        for j in range(0, n - i - 1):
            
            # Percorre a lista de 0 a n-i-1
            # Troca se o elemento for maior que o proximo
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        
        # Se não houve troca no loop interno, significa que a lista já esta ordenada
        if not trocou:
            break
            
    return lista

# Exemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
numeros_ordenados = bubble_sort(numeros)

print("Lista Ordenada:")
print(numeros_ordenados)