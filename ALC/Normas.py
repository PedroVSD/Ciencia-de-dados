import numpy as np
import pandas as pd

def jacobi(A, b, tolerancia, maxIteracoes):
    n = A.shape[0]
    x = np.zeros(n)
    x_novo = np.zeros(n)
    iter = 0
    erro = float('inf')
    
    while erro > tolerancia and iter < maxIteracoes:
        np.copyto(x_novo, x)
        
        for i in range(n):
            soma = 0.0
            for j in range(n):
                if j != i:
                    soma += A[i, j] * x[j]
            x_novo[i] = (b[i] - soma) / A[i, i]
        
        erro = np.max(np.abs(x_novo - x))
        np.copyto(x, x_novo)
        iter += 1
    
    return x

def calcular_norma_euclidiana(matriz):
    soma_quadrados = np.sum(matriz**2)
    return np.sqrt(soma_quadrados)

def calcular_norma_p(matriz, p):
    soma_potencias = np.sum(np.abs(matriz)**p)
    return soma_potencias**(1/p)

def calcular_norma_um(matriz):
    return np.sum(np.abs(matriz))

def calcular_norma_infinito(matriz):
    return np.max(np.sum(np.abs(matriz), axis=1))

def calcular_norma_frobenius(matriz):
    return np.sqrt(np.sum(matriz**2))

def calcular_norma_linha(matriz):
    return np.max(np.sum(np.abs(matriz), axis=1))

def calcular_norma_coluna(matriz):
    return np.max(np.sum(np.abs(matriz), axis=0))

def ler_arquivo_excel(caminho_arquivo, nome_aba):
    df = pd.read_excel(caminho_arquivo, sheet_name=nome_aba, header=None)
    return df.values

if __name__ == "__main__":
    # Carregar arquivos Excel
    print("Faça upload dos arquivos Excel.")
    uploaded_A = files.upload()
    uploaded_b = files.upload()
    
    # Ler a matriz A e o vetor b dos arquivos Excel
    nome_arquivo_A = list(uploaded_A.keys())[0]
    nome_arquivo_b = list(uploaded_b.keys())[0]
    
    df_A = pd.read_excel(nome_arquivo_A, header=None)
    df_b = pd.read_excel(nome_arquivo_b, header=None)
    
    A = df_A.to_numpy()
    b = df_b.to_numpy().flatten()  # Flatten para converter b em um vetor

    # Parâmetros do método Jacobi
    tolerancia = 1e-6
    maxIteracoes = 1000

    # Resolver o sistema usando o método de Jacobi
    solucao = jacobi(A, b, tolerancia, maxIteracoes)

    # Imprimir a solução
    print("Solução aproximada:")
    for i in range(len(solucao)):
        print(f"x[{i}] = {solucao[i]}")

    # Calcular e imprimir as normas da matriz A
    print("\nNormas da matriz A:")
    print(f"Norma Euclidiana: {calcular_norma_euclidiana(A)}")
    print(f"Norma P (p=2): {calcular_norma_p(A, 2)}")
    print(f"Norma 1: {calcular_norma_um(A)}")
    print(f"Norma Infinito: {calcular_norma_infinito(A)}")
    print(f"Norma Frobenius: {calcular_norma_frobenius(A)}")
    print(f"Norma de Linha: {calcular_norma_linha(A)}")
    print(f"Norma de Coluna: {calcular_norma_coluna(A)}")