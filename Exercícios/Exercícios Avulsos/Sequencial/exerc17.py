'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''
nota = int(input('Informe uma nota entre 0 a 10.\n Sua nota: '))

while (nota > 10) or (nota < 0):
    print('ERRO!\nDigite dentro do parametro pedido!')
    nota = int(input('Informe uma nota entre 0 a 10.\n Sua nota: '))
else:
    print("Sua nota foi enviada.")
    
