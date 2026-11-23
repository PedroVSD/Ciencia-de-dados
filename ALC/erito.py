import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.sparse.linalg import svds

# Dados fictícios de usuários e avaliações de filmes
data = {
    'usuarios': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
    'filmes': ['Matrix', 'Toy Story', 'Titanic', 'Inception', 'Avengers'],
    'avaliacoes': [
        [5, 4, 0, 0, 3],  # Alice
        [3, 0, 4, 0, 5],  # Bob
        [0, 2, 5, 0, 0],  # Carol
        [0, 0, 0, 5, 4],  # Dave
        [4, 3, 0, 5, 2],  # Eve
    ]
}

# Transformar os dados em uma matriz de floats
usuarios = data['usuarios']
filmes = data['filmes']
avaliacoes = np.array(data['avaliacoes'], dtype=float)

# Mostrar a matriz original
print("Matriz Original:")
print(pd.DataFrame(avaliacoes, index=usuarios, columns=filmes))

# Plotar a matriz original
plt.figure(figsize=(10, 5))
plt.imshow(avaliacoes, cmap='viridis', aspect='auto')
plt.colorbar()
plt.title('Matriz de Avaliações Original')
plt.xlabel('Filmes')
plt.ylabel('Usuários')
plt.xticks(ticks=np.arange(len(filmes)), labels=filmes)
plt.yticks(ticks=np.arange(len(usuarios)), labels=usuarios)
plt.show()

# Decomposição SVD
U, sigma, Vt = svds(avaliacoes, k=2)
sigma = np.diag(sigma)

# Reconstruir a matriz aproximada
avaliacoes_aprox = np.dot(np.dot(U, sigma), Vt)

# Mostrar a matriz aproximada
print("\nMatriz Aproximada após Decomposição SVD:")
print(pd.DataFrame(avaliacoes_aprox, index=usuarios, columns=filmes))

# Plotar a matriz aproximada
plt.figure(figsize=(10, 5))
plt.imshow(avaliacoes_aprox, cmap='viridis', aspect='auto')
plt.colorbar()
plt.title('Matriz de Avaliações Aproximada')
plt.xlabel('Filmes')
plt.ylabel('Usuários')
plt.xticks(ticks=np.arange(len(filmes)), labels=filmes)
plt.yticks(ticks=np.arange(len(usuarios)), labels=usuarios)
plt.show()

# Prever a avaliação de um filme não avaliado por Alice (por exemplo, "Titanic")
usuario_idx = usuarios.index('Alice')
filme_idx = filmes.index('Titanic')
predicao_avaliacao = avaliacoes_aprox[usuario_idx, filme_idx]
print(f"\nPredição da avaliação de Alice para o filme 'Titanic': {predicao_avaliacao:.2f}")