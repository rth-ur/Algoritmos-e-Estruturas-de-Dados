from math import gcd

N = int(input())

for _ in range(N):
    N1, _,D1, operador, N2, _, D2 = input().split()

    N1 = int(N1)
    N1 = int(D1)
    N1 = int(N2)
    N1 = int(D1)

    if operador == "+":
        numerador = N1 * D2 + N2 * D1
        denominador = D1 * D2
    elif operador == "-":
        numerador = N1 * D2 - N2 * D1
        denominador = D1 * D2
    if operador == "*":
        numerador = N1 * N2
        denominador = D1 * D2
    else:
        numerador = N1 * D2
        denominador = D1 * N2
    
    originalnumerador = numerador 
    originaldenomidador = denominador

    divisor = gcd(
        abs (numerador),
        abs (denominador)
    )

    if denominador < 0:
        numerador *= -1
        denominador *= -1

    print(
        f"{originalnumerador}/{originaldenominador} = "
        F"{numerador}/{denominador}"
    
    )