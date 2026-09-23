while True:
    n = int(input())
    if n == 0:
        break

    criancas = []
    for _ in range(n):
        nome, valor = input().split()
        criancas.append([nome, int(valor)])

    posicao = 0

    while len(criancas) > 1:
        valor = criancas[posicao][1]

        if valor % 2 == 1:
            posicao = (posicao + valor) % len(criancas)
        else:
            posicao = (posicao - valor) % len(criancas)

        criancas.pop(posicao)

    print(f"Vencedor(a): {criancas[0][0]}")