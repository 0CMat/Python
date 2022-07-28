'''3) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra. Obs. = 10 maças foram compradas.'''

macas = int(input('Digite quantas maças deseja comprar:\n Resposta:'))

if macas < 12:
    print('Quantidade de maças:', macas, '\n Valor: R$ ', macas * 1.30)
elif macas > 12:
    print('Quantidade de maças:', macas, '\n Valor: R$ ', macas * 1.00)
else:
    print('Algo deu errado!')
