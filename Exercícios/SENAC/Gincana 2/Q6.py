'''Escreva um algoritmo que receba 3 valores e escrever o maior deles. '''

valor1 = 22
valor2 = 84
valor3 = 95

if valor1 > valor2:
    valor_maior = valor1
    if valor1 > valor3:
        print('Valor 1 é o maior:', valor1)
    else:
        print('Valor 3 é o maior:', valor3)
if valor2 > valor1:
    valor_maior = valor2
    if valor2 > valor3:
        print('Valor 1 é o maior:', valor2)
    else:
        print('Valor 3 é o maior:', valor3)
