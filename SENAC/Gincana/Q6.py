'''6) Armazene o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.'''

salario_fixo = 1400
valor_vendas = 1200  # Valor vendido

meta_maxima = 1500  # Valor da meta

bonus_minimo = 3/100  # bonus de 3%
salario_bonificado = salario_fixo + (salario_fixo * bonus_minimo)

bonus_máximo = 5/100  # bonus de 5%
salario_máximo = salario_fixo + (salario_fixo * bonus_máximo)

if valor_vendas >= meta_maxima:
    print('O valor total do salário com o bônus de meta máxima é de:\n R$',
          salario_máximo)
elif valor_vendas < meta_maxima and valor_vendas > 0:
    print('O salário com valor de meta mínima é de:\n R$', salario_bonificado)
else:
    print('Salário sem meta atingida dessa vez!\n R$', salario_fixo)
