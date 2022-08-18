'''10) Armazene 3 valores (A, B e C igual a 100, -1 e 37) e escreva a soma dos 2 maiores.'''

A = 100
B = -1
C = 37

if A > B:
    valor1 = A
    if B > C:
        valor2 = B
        resultado = valor1 + valor2
        print('Resultado dos valores maiores é:', resultado)
    else:
        valor2 = C
        resultado = valor1 + valor2
        print('Resultado dos valores maiores é:', resultado)
elif B > A:
    valor1 = B
    if A > C:
        valor2 = A
        resultado = valor1 + valor2
        print('Resultado dos valores maiores é:', resultado)
    else:
        valor2 = C
        resultado = valor1 + valor2
        print('Valor maior é:', resultado)
else:
    valor1 = C
    if B > A:
        valor2 = B
        resultado = valor1 + valor2
        print('Resultado dos valores maiores é:', resultado)
    else:
        valor2 = A
        resultado = valor1 + valor2
        print('Valor maior é:', resultado)
