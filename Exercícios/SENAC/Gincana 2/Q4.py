'''Faça um algoritmo para armazenar: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também tesar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'. '''

numero_conta = 1000
saldo = 100
debito = 500
credito = 800

saldo_atual = saldo - debito + credito
if saldo_atual < 0:
    print('Você está negativado!')
    print('Seu saldo:', saldo_atual)
elif saldo_atual == 0:
    print('Você está ZERADO!')
    print('Seu saldo:', saldo_atual)
else:
    print('Você está com saldo positivo!')
    print('Seu saldo:', saldo_atual)
