from math import pi

raio = float(input('Digite o raio do círculo em que deseja saber a área:'))
area = "{:.2f}".format(float(raio + (pi * raio**2)))
print('A área do circulo com o raio de',raio, ' é de ', area, ' a área')