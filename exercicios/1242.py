def pode_ligar(a, b):
    return (a == 'B' and b == 'S') or \
           (a == 'S' and b == 'B') or \
           (a == 'C' and b == 'F') or \
           (a == 'F' and b == 'C')


while True:
    try:
        fita = input().strip()
    except EOFError:
        break

    n = len(fita)
    dp = [[0] * n for _ in range(n)]

    for tamanho in range(2, n + 1):
        for i in range(n - tamanho + 1):
            j = i + tamanho - 1

            melhor = dp[i + 1][j]

            for k in range(i + 1, j + 1):
                if pode_ligar(fita[i], fita[k]):

                    esquerda = 0
                    direita = 0

                    if i + 1 <= k - 1:
                        esquerda = dp[i + 1][k - 1]

                    if k + 1 <= j:
                        direita = dp[k + 1][j]

                    total = 1 + esquerda + direita
                    melhor = max(melhor, total)

            dp[i][j] = melhor

    print(dp[0][n - 1])
    