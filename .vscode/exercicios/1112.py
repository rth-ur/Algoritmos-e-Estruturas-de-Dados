while True:
    X, Y, preco = map(int, input().split())

    if X == 0 and Y == 0 and preco == 0:
        break

    Q = int(input())

    bit = [[0] * (Y + 1) for _ in range(X + 1)]

    def atualizar(x, y, valor):
        x += 1
        y += 1

        while x <= X:
            yy = y

            while yy <= Y:
                bit[x][yy] += valor
                yy += yy & -yy

            x += x & -x

    def consultar(x, y):
        x += 1
        y += 1

        resultado = 0

        while x > 0:
            yy = y

            while yy > 0:
                resultado += bit[x][yy]
                yy -= yy & -yy

            x -= x & -x

        return resultado

    def retangulo(x1, y1, x2, y2):
        return (
            consultar(x2, y2)
            - consultar(x1 - 1, y2)
            - consultar(x2, y1 - 1)
            + consultar(x1 - 1, y1 - 1)
        )

    for _ in range(Q):
        dados = input().split()

        if dados[0] == 'A':
            n = int(dados[1])
            x = int(dados[2])
            y = int(dados[3])

            atualizar(x, y, n)

        else:
            x1 = int(dados[1])
            y1 = int(dados[2])
            x2 = int(dados[3])
            y2 = int(dados[4])

            quantidade = retangulo(x1, y1, x2, y2)

            print(quantidade * preco)

    print()
    