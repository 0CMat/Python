'''Escreva um algoritmo que receba um nome de uma pessoa e busque se ele está na lista atual de pessoas aptas a tomar vacina nesta semana. Considere o os seguintes nomes para fazer a busca: “Matuzalén Jr”, “Bichilingo Duarte”, “Miliciano Albuquerque”, “Menino de Recado”, “Joana Darque”, “Dom Quixote de La Mancha”, “Brás Cubas”, “Tati Quebra Barraco”, “Poeta Desconhecido”. '''

from operator import truediv
from pickle import TRUE


lista_pessoas = ['Matuzalén Jr', 'Bichilingo Duarte', 'Miliciano Albuquerque', 'Menino de Recado',
                 'Joana Darque', 'Dom Quixote de La Mancha', 'Brás Cubas', 'Tati Quebra Barraco', 'Poeta Desconhecido']

quant_pessoas_vacina = len(lista_pessoas)
print(quant_pessoas_vacina)

nome = input('Qual o seu nome?')
vacinacao = FALSE

for nomes in lista_pessoas:
    if nomes == nome:
        print('Pessoa pode se vacinar!')
        vacinacao = FALSE


if vacinacao != TRUE:
    print('Não se encotra na lista')
