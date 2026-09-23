n = int(input())
for _ in range(n):

    linha = input()
    pilha = []
    diamante = 0

    for caractere in linha:
        if caractere == '<':
            pilha.append('<')

        elif caractere == '>':

            if pilha:
                pilha.pop()
                diamante += 1

    print(diamantes)
