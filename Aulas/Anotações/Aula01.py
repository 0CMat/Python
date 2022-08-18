
# Python tem uma linguagem dinâmica, sendo possível alterar o tipo e o valor fácilmente.

# executar arquivo .py  > Atalho: Ctrl + alt + N

print('Olá Mundo!')

# NÚMEROS
# inteiros
# int = são números como: -2 -1, 0, 1, 2, 3, 4 ...

# pontos fllutuantes
# float = são números como: 1.0, 2.5, --1.0, -0.5;

# VARIÁVEIS
# exemplo:
x = 5   # x recebe o valor 5
# x é uma variável com valor int
w = "Ana"
# ou
w = 'Ana'

# Como setar uma variável
# Deve iniciar com uma letra
# A-z e 0-9 e _

# altura, Altura e ALTURA são diferentes!

# STRINGS

'''COMENTÀRIO'''

# print de texto em bloco:

print('---------------------  PRINTANDO --------------------------------------')
a = """Olá, 
este é o curso de
Python3"""

print(a)

# método de Strings

print('---------------------  MÉTODOS DE STRINGS --------------------------------------')

b = " Olá Mundo! "
print(b)

c = " Olá Mundo! "
print(c.strip())  # Método que ignora espços

c = " Olá Mundo! "
print(c.lower())  # Método que reduz todas as letras para minusculo

d = " Olá Mundo! "
print(d.upper())  # Método que reduz todas as letras para maiusculo

# TYPE
print('---------------------  TYPE --------------------------------------')

a = "Olá Mundo!"
b = 5
c = 3.
d = 5+3j

# Como descobrir o tipo:

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Escopo de Variáveis
print('---------------------  ESCOPO DE VARIÁVEL --------------------------------------')

# VARIÁVEL GLOBAL:
x = 5

print('Variável Global:', x)

# VARIÁVEL LOCAL - EXISTE APENAS DENTRO DE UMA FUNÇÃO


def funcao():
    x = 7
    print('Variável Local:', x)


funcao()
print('Variável Global:', x)  # CHAMANDO NOVAMENTE
