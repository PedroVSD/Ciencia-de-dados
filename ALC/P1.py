import numpy as np

def gerar_matriz_tridiagonal_positiva_definida(n):
    # Gerar uma matriz tridiagonal com valores aleatórios entre 1 e 9
    lower_diag = np.random.randint(1, 10, size=n-1)
    main_diag = np.random.randint(1, 10, size=n)
    upper_diag = np.random.randint(1, 10, size=n-1)
    
    matriz = np.diag(lower_diag, -1) + np.diag(main_diag) + np.diag(upper_diag, 1)
    
    # Ajustar os elementos para garantir que a matriz seja positiva definida
    for i in range(n):
        if i > 0:
            matriz[i, i-1] = np.random.randint(1, matriz[i, i] + 1)
        if i < n-1:
            matriz[i, i+1] = np.random.randint(1, matriz[i, i] + 1)
    
    # Garantir positividade definida
    while not np.all(np.linalg.eigvals(matriz) > 0):
        for i in range(n):
            if i > 0:
                matriz[i, i-1] = np.random.randint(1, matriz[i, i] + 1)
            if i < n-1:
                matriz[i, i+1] = np.random.randint(1, matriz[i, i] + 1)
    
    return matriz

# Gerar uma matriz tridiagonal positiva definida com 5 linhas e 5 colunas
matriz = gerar_matriz_tridiagonal_positiva_definida(5)
print("Matriz tridiagonal positiva definida:")
print(matriz)



B = np.linalg.cholesky(matriz)
print(B)