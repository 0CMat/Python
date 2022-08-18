# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

temperatura_F = int(
    input('Qual a temperatura que deseja converter de Fahrenheit para Celsius:'))

temperatura_C = 5 * ((temperatura_F - 32) / 9)

print('Em graus Celcius:', temperatura_C)
 