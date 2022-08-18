'''Armazene o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total. '''

salario_fixo = 1000
valor_vendas = 1600
comissao_minima = valor_vendas + (valor_vendas * 0.03)
comissao_maxima = (valor_vendas - 1500) + (valor_vendas * 0.08)

if valor_vendas <= 1500:
    print('Seu salário mais a comissão mínima de vendas é:\n R$',
          comissao_minima + salario_fixo)
else:
    print('Seu salário mais a comissão máxima de vendas é:\n R$',
          comissao_maxima + salario_fixo)
