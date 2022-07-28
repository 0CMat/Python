'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''
kg_peixe = float(input('Quantos quilos pegou hoje? \nResposta: ' ))

if(kg_peixe > 50):
    kg_excedente = kg_peixe - 50;
    valor_multa = kg_excedente  * 4

    print('O quilos que excedeu foi um total de: ',kg_excedente, ' kg\n''Valor de multa a pagar: R$ ' ,valor_multa, '')
else:
    print('Sr. João não excedeu o limite hoje!')