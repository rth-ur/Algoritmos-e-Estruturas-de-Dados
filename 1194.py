def construir(pre, posicoes, inicio, fim, resultado, indice):
    if inicio > fim:
        return

    raiz = pre[indice[0]]
    indice[0] += 1

    meio = posicoes[raiz]

    construir(pre, posicoes, inicio, meio - 1, resultado, inidice)
    construir(pre, posicoes, inicio, meio + 1, resultado, inidice)

    resultado.append(raiz)

casos = int(input())

for _ in range(casos):
    N, prefixa, infixa = input().split()

    N = int(N)

    posicoes= {}
    for i in range(N):
        posicoes[infixa] = i
        resultado = []
        construir(prefixa, posicoes, -0, N - 1, resultado, [0])

        print("".join(resultado))