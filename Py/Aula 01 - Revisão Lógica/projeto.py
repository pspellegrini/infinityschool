'''Crie um sistema de cadastro, onde o usuário vai precisar digitar seu email e sua senha, esse sistema deve rodar sem parar e armazenar todos esses usuários, além disso, é necessário que a senha do usuário possua caracteres especiais, números e letras, e você deve verificar se tem tudo isso.'''

# Cadastro
# user_email
# password
    #caracteres especiais, números e letras
    #verificação
    
#Entrada
arq = open('registrados.txt', 'a')
print('Olá vamos cadastrar seu usuário!')
nome_usuario = input('Digite o nome de usuário: ')
senha_usuario = input('Digite sua senha: ')

arq.write('{}\n'.format(nome_usuario))
arq.write('{}\n'.format(senha_usuario))
print('Cadastro realizado com sucesso!\n')
arq.close()
arq = open('registrados.txt')
print('Efetue o seu login')
nome_login = input('Digite o seu nome de usuario: ')
senha_login = input('Digite a senha do usuario: ')
registrados = arq.readlines()
if nome_login + '\n' in registrados:
    print('Bem vindo, {}!'.format(nome_login))
else:
    print('Você deve ter digitado seu nome de usuario errado, por favor verifique.')
arq.close()