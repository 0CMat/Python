'''Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

# Nome: maior que 3 caracteres;
nome = input('Digite o seu nome:\nNome:')
while len(nome) < 3:
    nome = input('Digite o seu nome:\nNome:')

# Idade: entre 0 e 150;
idade = int(input('Digite sua idade:\nIdade: '))
while (idade < 0) or (idade > 150):
    idade = int(input('Digite sua idade:\nIdade: '))

# Salário: maior que zero;
salario = float(input('Digite o valor do seu salario:\nR$ '))
while salario < 0:
    salario = float(input('Digite o valor do seu salario:\nR$ '))

# Sexo: 'f' ou 'm';
sexo = str(input('Digite seu sexo:\nSexo: '))
while sexo != "M" and sexo != "F":
    print(sexo)
    sexo = str(input('Digite seu sexo:\nSexo: '))

# Estado Civil: 's', 'c', 'v', 'd';'''
estado_civil = str(input(
    'Qual seu estado cívil? \nSolteiro: (S)\nCasado: (C)\nViuvo(a): (V)\nDivorciado: (D)\n  Qual o seu estado? (Use a letra inicial):'))
while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    estado_civil = str(input(
        'Qual seu estado cívil? \nSolteiro: (S)\nCasado: (C)\nViuvo(a): (V)\nDivorciado: (D)\n  Qual o seu estado? (Use a letra inicial):'))

# Resumo
print('\nCaracteristicas:')
print('Nome:', nome, '\nIdade:', idade, '\nSalario: R$',
      salario, '\nSexo:', sexo, '\nEstado Cívil:', estado_civil)
