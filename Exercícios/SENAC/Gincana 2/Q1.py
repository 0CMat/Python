'''Escreva um algoritmo que receba a idade (em número) e indique se a pessoas é maior de idade.'''

idade = int(input('Digite sua idade: '))
maior_idade = 18

if idade > maior_idade:
    print('Você já é de maior! Cuidado com a prisão!')
else:
    print('Você é de menor! Mas, tome cuidado com o reformatório.')
