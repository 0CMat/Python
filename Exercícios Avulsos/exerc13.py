'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7'''

h = float(input('Digite sua altura:'))
genero = int(input('Digite:\n 1 - Para Homem \n 2 - Para Mulher \n Resposta: '))

if(genero == 1):
    resultado = ((72.7*h) - 58)
    print('O peso ideal é:', resultado)
elif(genero == 2):
    resultado = ((62.1*h) - 44.7)
    print('O peso ideal é:', resultado)
else:
    print('Digite um valor válido!')
