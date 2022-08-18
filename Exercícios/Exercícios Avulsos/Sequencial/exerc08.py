# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_Hora = float(input('Quanto você ganha por hora?'))
carga_Horária = int(input('Quantas horas você trabalha?'))

salario= (valor_Hora * carga_Horária)

print('O seu salário é R$ ', salario)
