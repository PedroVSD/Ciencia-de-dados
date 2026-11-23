import numpy as np
import pandas as pd
from google.colab import files

def jacobi(A, b, tolerancia, max_iteracoes):
    n = len(A)
    x = np.zeros(n)
    x_novo = np.zeros(n)
    iteracoes = 0
    erro = float('inf')
    
    while erro > tolerancia and iteracoes < max_iteracoes:
        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_novo[i] = (b[i] - soma) / A[i][i]
        
        erro = calcular_erro(x, x_novo)
        x[:] = x_novo
        iteracoes += 1
    
    return x

def calcular_erro(x, x_novo):
    return np.max(np.abs(x_novo - x))

def main():
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
    max_iteracoes = 1000
    
    # Resolver o sistema usando o método Jacobi
    solucao = jacobi(A, b, tolerancia, max_iteracoes)
    
    # Imprimir a solução
    print("Solução aproximada:")
    for i in range(len(solucao)):
        print(f"x[{i}] = {solucao[i]}")

if __name__ == "__main__":
    main()