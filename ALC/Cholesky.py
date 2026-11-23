import pandas as pd
import numpy as np
from google.colab import files

def cholesky(A):
    n = A.shape[0]
    L = np.zeros((n, n))

    # Verificar se A é simétrica
    if not np.allclose(A, A.T):
        print("A matriz fornecida não é simétrica.")
        return None

    # Verificar se A é definida positiva
    for i in range(n):
        sum = 0.0
        for k in range(i):
            sum += L[i][k] ** 2
        diagonal = A[i, i] - sum
        if diagonal <= 0:
            print("A matriz fornecida não é definida positiva.")
            return None
        L[i, i] = np.sqrt(diagonal)
        for j in range(i + 1, n):
            sum = 0.0
            for k in range(i):
                sum += L[i, k] * L[j, k]
            if L[i, i] == 0:
                print("A matriz fornecida não é definida positiva.")
                return None
            L[j, i] = (A[j, i] - sum) / L[i, i]

    return L

def imprimir_matriz(matriz):
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            print(matriz[i, j], end=' ')
        print()

# Carregar o arquivo Excel
uploaded = files.upload()

# Obter o nome do arquivo
file_name = list(uploaded.keys())[0]

# Ler a matriz A do arquivo Excel
df_A = pd.read_excel(file_name, header=None)

# Converter o dataframe para um array numpy
A = df_A.to_numpy()

if __name__ == "__main__":
    print("Matriz original:")
    print(np.matrix(A))

    L = cholesky(A)

    if L is not None:
        print("\nMatriz L (fator de Cholesky):")
        print(np.matrix(L))
