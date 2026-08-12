from collections import deque

while True:
    n = int(input())

    if n == 0:
        break

    fila = deque(range(1, n + 1))

    descartadas = []

    while len(fila) > 1:
        descartadas.append(fila.popleft())
        fila.append(fila.popleft())

    print("Discarded cards:", ", ".join(map(str, descartadas)))

    print("Remaining card:", fila[0])