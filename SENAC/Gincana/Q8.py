'''8) Faça um algoritmo para armazenar: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.'''

quant_maxima = 1500
quant_atual = 180
quant_minima = 10

quant_media = (quant_maxima + quant_minima)/2

if quant_atual >= quant_media:
    print('Não efetuar a compra!')
else:
    print('Efetuar a compra!')
