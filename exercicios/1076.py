
casos = int(input())

for _ in range(casos):
    inicio = int(input())
    V, A = map(int, input().split())

    arestas = set()

    for _ in range(A):
        X, Y = map(int, input().split())
        aresta = tuple(sorted((X, Y)))
        arestas.add(aresta)

    mapeamento = len(arestas) * 2
    print(mapeamento)
