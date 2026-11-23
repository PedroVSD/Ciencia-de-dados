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
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - sigma)

        # Calcula o erro
        erro = np.linalg.norm(x - x_anterior, ord=np.inf)
        x_anterior[:] = x
        iteracoes += 1

    return x, iteracoes

# Método para encontrar o omega ótimo usando busca linear
def encontrar_WOtimo(A, b, epsilon, max_iteracoes):
    omega_min = 1.0  # Valor mínimo de omega
    omega_max = 2.0  # Valor máximo de omega
    incremento = 0.01  # Incremento para busca linear
    num_iteracoes_min = float('inf')  # Número mínimo de iterações encontrado
    WOtimo = omega_min  # Valor ótimo de omega

    # Realiza a busca linear para encontrar o omega ótimo
    for omega in np.arange(omega_min, omega_max + incremento, incremento):
        _, num_iteracoes = metodo_SOR(A, b, omega, epsilon, max_iteracoes)
        if num_iteracoes < num_iteracoes_min:
            num_iteracoes_min = num_iteracoes
            WOtimo = omega

    return WOtimo

# Método principal para teste
if __name__ == "__main__":
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

    # Parâmetros do método SOR
    epsilon = 1e-6  # Critério de parada (tolerância para o erro)
    max_iteracoes = 1000  # Número máximo de iterações

    # Encontrar o omega ótimo
    WOtimo = encontrar_WOtimo(A, b, epsilon, max_iteracoes)
    print("WOtimo:", WOtimo)

    # Solução do sistema usando o omega ótimo
    x, num_iteracoes = metodo_SOR(A, b, WOtimo, epsilon, max_iteracoes)
    print("Solução do sistema usando WOtimo:")
    for i in range(len(x)):
        print(f"x[{i}] = {x[i]}")

    print(f"Convergência atingida em {num_iteracoes} iterações com WOtimo = {WOtimo}")