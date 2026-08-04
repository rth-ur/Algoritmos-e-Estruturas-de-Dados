n = int(input())

for _ in range(n):
    mina = input()

    abertos = 0
    diamantes = 0

    for c in mina:
        if c == "<":
            abertos += 1
        elif c == ">":
            if abertos > 0:
                diamantes += 1
                abertos -= 1

    print(diamantes)