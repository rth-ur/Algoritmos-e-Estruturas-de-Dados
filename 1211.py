while True:
    try:
        n = int(input())
    except EOFError:
        break

    numero = []

    for _ in range(n):
        numero.append(input().strip())

    numero.sort()

    economia = 0

    for i in range(1, n):
        anterior = numero[i - 1]
        atual = numero[i]

        j = 0

        while j < len(atual) and atual[j] == anterior[j]:
            j += 1

        economia += j

    print(economia)