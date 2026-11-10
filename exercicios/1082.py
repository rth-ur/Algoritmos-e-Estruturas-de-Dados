
def estruturagrafo(grafo, vertice, aplicacao, componente):
    aplicacao.add(vertice)
    componente.append(vertice)

    for vizinho in grafo[vertice]:
        if vizinho not in aplicacao:
            estruturagrafo(grafo, vizinho, aplicacao, componente)


casos = int(input())

for caso in range(1, casos + 1):
    V, E = map(int, input().split())
    grafo = {}

    for i in range(V):
        letra = chr(ord('a') + i)
        grafo[letra] = []

    for _ in range(E):
        A, B = input().split()
        grafo[A].append(B)
        grafo[B].append(A)

    sequencia = set()
    componentes = []

    for vertice in sorted(grafo):
        if vertice not in sequencia:
            componente = []
            estruturagrafo(grafo, vertice, sequencia, componente)
            componente.sort()
            componentes.append(componente)

    print(f"Case #{caso}:")

    for componente in componentes:
        print(",".join(componente) + ",")

    print(f"{len(componentes)} connected components")
    print()
