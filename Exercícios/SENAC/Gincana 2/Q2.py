'''Escreva um algoritmo que receba duas notas das avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). '''

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua psegunda nota: '))

media = (nota1 + nota2) / 2
media_mínima = 6.0
if media >= media_mínima:
    print('Você foi aprovado! Parabéns!')
    print('Sua média:',media)
else:
    print('Você foi reprovado!')
    print('Sua média:',media)


