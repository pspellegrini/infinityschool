from usuarios import *

print('''
      Bem-vindo ao sistema de cadastro de usurários
      #############################################
''')

while True:
    print('''
          1 - Cadastro
          2 - Ler usuário
          3 - Atualizar usuário
          4 - Deletar usuário
    ''')
    escolha = int(input('Digite o que deseja fazer: '))
    if escolha == 1:
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        usuario = Usuario(nome, email, senha)
        usuario.inserir_usuario()
        print('usuário inserido com sucesso!')
    elif escolha == 2:
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        usuario = Usuario(nome, email, senha)
        email_desejado = input('Digite o email que você deseja ler: ')
        print(usuario.pegar_usuario(email_desejado))
    elif escolha == 3:
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        usuario = Usuario(nome, email, senha)
        email_desejado = input('Digite o email que você deseja ler: ')
        print(usuario.pegar_usuario(email_desejado))
        escolha2 = input('Qual deseja atualizar? ').lower()
        if escolha2 == 'email':
            novo_email = input('Novo email: ')
            usuario.update_usuario(email = novo_email)
            print(usuario.pegar_usuario(novo_email))
        elif escolha2 == 'nome':
            novo_nome = input('Novo nome: ')
            usuario.update_usuario(nome = novo_nome)
            print(usuario.pegar_usuario(novo_nome))
        elif escolha2 == 'senha':
            nova_senha = input('Nova senha: ')
            usuario.update_usuario(senha = nova_senha)
            print(usuario.update_usuario(nova_senha))
    elif escolha == 4:
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        usuario = Usuario(nome, email, senha)
        print(usuario.pegar_usuario(email_desejado))
        usuario.deletar_usuario(email)