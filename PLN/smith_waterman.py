# É um caso da distância ponderada, mas para a biologia

def smith_waterman(sequencia_x, sequencia_y, match=1, mismatch=-1, gap=-2):
    n = len(sequencia_x)
    m = len(sequencia_y)

    dp = [[0] * (m+1) for _ in range(n+1)]

    best_score = 0
    best_pos = (0, 0)

    for i in range(m+1):
        dp[i][0] = i * gap

    for j in range(n + 1):
        dp[0][j] = j * gap

    for i in range(1, m+1):
        for j in range(1, n+1):
            if sequencia_x == sequencia_y:
                diagonal = dp[i-1][j-1] + match
            else:
                diagonal = dp[i-1][j-1] + mismatch
                # Pode-se fazer uma pequena alteração aqui, adicionar o 0 no max.
                # Isso faz com que tenhamos um algoritmo local, e não global.
                # É a vavriante de Smith-Waterman.
            dp[i][j] = max(
                0,
                dp[i-1][j] + gap,
                dp[i][j-1] + gap,
                diagonal
            )

            if dp[i][j] > best_score:
                best_score = dp[i][j]
                best_pos = (i, j)


    return best_score, best_pos, dp
    '''
    Needleman-Wunsch → começa no canto (M,N), para em (0,0)
    Smith-Waterman   → começa na célula de MAIOR score, para quando chega em zero
    '''
