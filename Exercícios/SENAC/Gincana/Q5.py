'''5) Armazene o ano atual e o ano de nascimento de uma pessoa. Escolha um ano de nascimento da sua preferência. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu)'''

ano_atual = 2022
ano_nascimento = 1973

idade = ano_atual - ano_nascimento  

if idade < 16:
    print('Você é de menor, ainda não pode votar!')
else:
    print('Você já pode votar!')
