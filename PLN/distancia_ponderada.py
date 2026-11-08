def distancia_ponderada(palavra_x, palavra_y, delecao, insercao, substituicao):
    n = len(palavra_x)
    m = len(palavra_y)

    dp = [[0] * (m + 1) for _ in range(n+1)]

    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] + delecao.get(palavra_x[i-1], 1)

    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] + insercao.get(palavra_y[j-1], 1)

    for i in range(1, m+1):
        for j in range(1, n+1):
            s = palavra_x[i-1]
            t = palavra_y[j-1]

            if s == t:
                dp[i][j] = dp[i-1][j-1]
            else:
                custo_delecao = dp[i-1][j] + delecao.get(s,1)
                custo_insercao = dp[i][j-1] + insercao.get(t,1)
                custo_sub = dp[i-1][j-1] + substituicao.get((s,t),2)

                dp[i][j] = min(custo_delecao, custo_insercao, custo_sub)

    return dp[m][n]
