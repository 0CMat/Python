''''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo'''

num1 = int(input('Digite um valor:'))
num2 = int(input('Digite um valor:'))
num3 = int(input('Digite um valor:'))

# Questão A
resultado1 = (num1 + num1) + (num2 / 2)

# Questão B
resultado2 = ((num1 * 3) + num3)

# Questão C
resultado3 = (num3 * num3 * num3 * num3)

print('O produto do dobro do primeiro com metade do segundo:', resultado1)
print('A soma do triplo do primeiro com o terceiro:', resultado2)
print('O terceiro elevado ao cubo:', resultado3)
