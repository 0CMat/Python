# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = int(input("Digite a sua nota do 1 semestre:"))
nota2 = int(input("Digite a sua nota do 2 semestre:"))
nota3 = int(input("Digite a sua nota do 3 semestre:"))
nota4 = int(input("Digite a sua nota do 4 semestre:"))

resultado = ((nota1 + nota2 + nota3 + nota4) / 4)

print('Sua média é:', resultado)
