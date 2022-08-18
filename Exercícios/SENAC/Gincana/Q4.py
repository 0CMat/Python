'''4) Armazene as notas 1 igual a 10 e 2 sendo igual a 5.5. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado).'''

nota1 = 10
nota2 = 5.5

media = (nota1 + nota2) / 2

if media >= 6:
    print(media)
    print('Aluno está aprovado!')
else:
    print('Aluno está reprovado!')
