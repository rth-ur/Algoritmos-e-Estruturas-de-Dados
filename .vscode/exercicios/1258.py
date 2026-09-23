while True:
    n = int(input())
    if n == 0:
        break

    camisetas = []

    for _ in range(n):
        nome = input()
        cor, tamanho = input().split()

        camisetas.append((cor, tamanho, nome))

    camisetas.sort(
        key=lambda x: (
            x[0],
            {"P": 0, "M": 1, "G": 2}[x[1]],
            x[2]
        )
    )

    for cor, tamanho, nome in camisetas:
        print(cor, tamanho, nome)

    print()