import numpy as np

# Implementação do método SOR
def metodo_SOR(A, b, omega, epsilon, max_iteracoes):
    n = len(b)
    x = np.zeros(n)  # Vetor inicial (pode ser qualquer valor inicial)
    x_anterior = np.zeros(n)  # Vetor da iteração anterior
    erro = float('inf')
    iteracoes = 0

    while erro > epsilon and iteracoes < max_iteracoes:
        # Realiza uma iteração do método SOR
        for i in range(n):
            x_anterior[i] = x[i]
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - sigma)

        # Calcula o erro
        erro = max(abs(x[i] - x_anterior[i]) for i in range(n))
        iteracoes += 1

    return iteracoes

# Método para encontrar o omega ótimo usando busca linear
def encontrar_WOtimo(A, b, epsilon, max_iteracoes):
    omega_min = 1.0  # Valor mínimo de omega
    omega_max = 2.0  # Valor máximo de omega
    incremento = 0.01  # Incremento para busca linear
    num_iteracoes_min = float('inf')  # Número mínimo de iterações encontrado
    WOtimo = 1.0  # Valor ótimo de omega

    # Realiza a busca linear para encontrar o omega ótimo
    for omega in np.arange(omega_min, omega_max + incremento, incremento):
        num_iteracoes = metodo_SOR(A, b, omega, epsilon, max_iteracoes)
        if num_iteracoes < num_iteracoes_min:
            num_iteracoes_min = num_iteracoes
            WOtimo = omega

    return WOtimo

# Método principal para teste
if __name__ == "__main__":
    # Exemplo de sistema de equações
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]])
    b = np.array([15, 10, 10, 10])

    # Parâmetros do método SOR
    epsilon = 1e-6  # Critério de parada (tolerância para o erro)
    max_iteracoes = 1000  # Número máximo de iterações

    # Encontrar o omega ótimo
    WOtimo = encontrar_WOtimo(A, b, epsilon, max_iteracoes)
    print("WOtimo:", WOtimo)
