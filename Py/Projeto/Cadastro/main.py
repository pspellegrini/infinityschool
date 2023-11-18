from infinityschool.Py.Projeto.Cadastro.cadastro import (
    cad_user,
    get_user
)

from getpass import getpass

while True:
    print(f'Olá, bem-vindo ao sistema de cadastro.')
    print(f'1 - Cadastrar usuário.')
    print(f'2 - Exibir usuário.')
    print(f'3 - Sair do programa.')
    
    choice = int(input(f'Digite a sua escolha: '))
    
    if choice == 1:
        name = input(f'Digite o nome do usuário: ')
        age = int(input(f'Digite a idade do usuário: '))
        email = input(f'Digite o e-mail do usuário: ')
        adress = input(f'Digite o endereço do usuário: ')
        print("Cadastre aqui sua senha com os seguintes critérios: \n"
      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n")
        password = getpass(f'Digite sua senha: ')
        print(cad_user(name, age, email, adress, password))
    elif choice == 2:
        email = input(f'Digite o e-mail do usuário: ')
        print(get_user(email))
    elif choice == 3:
        print(f'Tchau parceiro!')
        break
    else:
        print(f'Opção inválida.')
        continue
    '''Install Flake8'''