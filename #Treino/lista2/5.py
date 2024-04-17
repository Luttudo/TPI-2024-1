def k_maiores(lista, k):
    # # Verifica se a lista tem pelo menos k elementos
    # if len(lista) < k:
    #     return None
    
    # Ordena a lista em ordem decrescente
    lista_ordenada = sorted(lista, reverse=True)
    
    # Retorna os k primeiros elementos da lista ordenada
    return lista_ordenada[:k]

# Exemplo de uso
minha_lista = [10, 5, 8, 3, 12, 7]
k = 3
resultado = k_maiores(minha_lista, k)
print(f"Os {k} maiores elementos são: {resultado}")


def maiores(lista, k):

    ordenada = sorted(lista, reverse=True) 

    return ordenada[:k]


