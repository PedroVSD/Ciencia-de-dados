import pandas as pd
import numpy as np

# Gerar uma matriz 1000x1000 triangular inferior ou superior com números aleatórios entre 1 e 10
def generate_triangular_matrix(size, is_upper):
    matrix = np.random.randint(1, 11, size=(size, size))  # Gera uma matriz com números aleatórios entre 1 e 10
    if is_upper:
        for i in range(size):
            for j in range(i + 1, size):
                matrix[i][j] = 0  # Define como zero os elementos acima da diagonal principal para torná-la triangular superior
    else:
        for i in range(size):
            for j in range(i):
                matrix[i][j] = 0  # Define como zero os elementos abaixo da diagonal principal para torná-la triangular inferior
    return matrix

# Gerar uma matriz triangular inferior
matriz = generate_triangular_matrix(1000, is_upper=False)

# Criar um DataFrame do pandas com a matriz
df = pd.DataFrame(matriz)

# Salvar o DataFrame em um arquivo Excel
df.to_excel('matriz_triangular.xlsx', index=False)

print("Matriz triangular inferior salva com sucesso em matriz_triangular.xlsx")
