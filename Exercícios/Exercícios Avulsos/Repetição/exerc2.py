'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

nome_user = input('Digite um nome para usuário:\n')
senha_user = input('Cadastre uma senha para o usuário:\n')
while nome_user == senha_user:
    print('Digite uma senha válida, que seja diferente do nome do usuário!')
    senha_user = input('Digite senha VÁLIDA para o usuário: \n')

print('Cadastro Concluído!')
