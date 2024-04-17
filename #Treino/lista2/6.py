import random

def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([random.randint(0, 100) for _ in range(colunas)])
    return matriz

def somar_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("Não é possível somar matrizes de dimensões diferentes.")
        return None

    matriz_soma = []
    for i in range(len(matriz1)):
        linha_soma = []
        for j in range(len(matriz1[0])):
            elemento_soma = matriz1[i][j] + matriz2[i][j]
            linha_soma.append(elemento_soma)
        matriz_soma.append(linha_soma)

    return matriz_soma

# Criando duas matrizes aleatórias
linhas, colunas = 3, 3
matriz1 = criar_matriz(linhas, colunas)
matriz2 = criar_matriz(linhas, colunas)

# Somando as matrizes
matriz_resultante = somar_matrizes(matriz1, matriz2)

# Exibindo as matrizes e a matriz resultante
print("Matriz 1:")
for linha in matriz1:
    print(linha)

print("\nMatriz 2:")
for linha in matriz2:
    print(linha)

print("\nMatriz Resultante (Soma):")
for linha in matriz_resultante:
    print(linha)
