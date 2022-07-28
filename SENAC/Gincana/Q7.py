'''7) Faça um algoritmo para armazenar: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'''

num_conta = 7855  # número da conta

saldo = 400
debito = 400  # saldo negativo da conta
credito = 4000

saldo_atual = saldo - debito + credito  # saldo atual do cliente

if saldo_atual > 0:
    print('O seu saldo está POSITIVO! Valor total em sua conta: \nR$', saldo_atual)
elif saldo_atual == 0:
    print('O seu saldo está ZERADO! Valor total em sua conta: \nR$', saldo_atual)
else:
    print('O seu saldo está NEGATIVO! Valor total em sua conta: \nR$', saldo_atual)
