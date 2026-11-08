# Programação dinâmica bottom-up
#
def distancia_min(palavra_X, palavra_Y, levenshtein=2):
    n = len(palavra_X)
    m = len(palavra_Y)

    # Criando a borda da matriz [0] * (n+1) é a parte da linha, o for são as colunas
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Jogando as palavras na matriz
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if palavra_X[i - 1] == palavra_Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # O de cima
                    dp[i][j - 1] + 1,  # O da esquerda
                    dp[i - 1][j - 1] + levenshtein,  # Diagonal
                )

    return dp[n][m]


distancia = distancia_min("execution", "intention")
print(distancia)
