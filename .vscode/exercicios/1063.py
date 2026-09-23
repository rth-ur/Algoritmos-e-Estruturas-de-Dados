while True:
    n = int(input())
    if n == 0:
        break

    entrada = input().split()
    saida = input().split()

    pilha = []
    movimentos = []
    pos_entrada = 0
    pos_saida = 0

    while pos_saida < n:

        if pos_entrada < n:
            pilha.append(entrada[pos_entrada])
            movimentos.append("I")
            pos_entrada += 1

        while (
            pilha
            and pos_saida < n
            and pilha[-1] == saida[pos_saida]
        ):
            pilha.pop()
            movimentos.append("R")
            pos_saida += 1

        if pos_entrada == n:
            if pos_saida < n and (
                not pilha or pilha[-1] != saida[pos_saida]
            ):
                break

    if pos_saida == n:
        print(" ".join(movimentos))
    else:
        print("Impossible")