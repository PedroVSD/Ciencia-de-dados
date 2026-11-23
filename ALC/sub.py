import pandas as pd
import numpy as np
from google.colab import files

def eh_triangular_superior(A):
    n = len(A)
    for i in range(n):
        for j in range(i):
            if A[i][j] != 0:
                return False
    return True

def eh_triangular_inferior(A):
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[i][j] != 0:
                return False
    return True

def substituicao_para_frente(A, b):
    n = len(b)
    x = np.zeros(n)

    if not eh_triangular_inferior(A):
        print("A matriz fornecida não é triangular inferior. Não é possível executar a substituição para frente.")
        return None

    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x

def substituicao_para_tras(A, b):
    n = len(b)
    x = np.zeros(n)

    if not eh_triangular_superior(A):
        print("A matriz fornecida não é triangular superior. Não é possível executar a substituição para trás.")
        return None

    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x

# Fazer upload dos arquivos Excel
print("Faça upload do arquivo da matriz A:")
uploaded_A = files.upload()

print("Faça upload do arquivo do vetor b:")
uploaded_b = files.upload()

# Obter os nomes dos arquivos
file_name_A = list(uploaded_A.keys())[0]
file_name_b = list(uploaded_b.keys())[0]

# Ler a matriz A e o vetor b dos arquivos Excel
df_A = pd.read_excel(file_name_A, header=None)
df_b = pd.read_excel(file_name_b, header=None)

# Converter os dataframes para arrays numpy
A = df_A.to_numpy()
b = df_b.to_numpy().flatten()  # Flatten para converter b em um vetor

# Realizar as substituições para frente e para trás
x_frente = substituicao_para_frente(A, b)
x_tras = substituicao_para_tras(A, b)

# Imprimir as soluções
if x_frente is not None:
    print("Solução usando substituição para frente:")
    for i in range(len(x_frente)):
        print(f"x[{i}] = {x_frente[i]}")

if x_tras is not None:
    print("\nSolução usando substituição para trás:")
    for i in range(len(x_tras)):
        print(f"x[{i}] = {x_tras[i]}")
