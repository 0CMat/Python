# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura_C = float(
    input('Digite o grau em Celsius em que deseja converter:'))

temperatura_F = "{:.0f}".format((temperatura_C * (1.8 + 32)))

print('A temperatura em Fahrenheit:', temperatura_F)
