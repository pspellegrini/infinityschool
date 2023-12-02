from classes import *

cadastro= []

while True:
    print('''
        1 - qual time deseja cadastrar
        2 - sair
    ''')
    cadstro_de_time = input('Digite sua escolha para cadastra: ')
    
    match cadastro_de_time :
        case '1':
            print('''
                Defina agora:
                1 - nome do time que irá cadstrar
                2 - Cidade cede do Time
                3 - Mascote do Time
                  ''')
            nomeTime = input('Digite o nome do time: ')
            cidade = input('Cidade cede do time: ')
            mascote = input('Mascote do Time')
            time = Time(nomeTime,cidade,mascote)
            print('-'*60)
            print('''
                Defina agora:
                1 - nome do jogador
                2 - numero da camisa
                  ''')
            nomeJogador = input('Nome do Jogador distaque do seu Time: ')
            numeroCamisa = int(input('Numero da Camisa'))
            jogador = Jogador(time.nomeTime,nomeJogador,numeroCamisa)
            print('''
                Defina agora:
                1 - nome do Tecnico
                2 - Seu esquema tatico
                  ''')
            nomeTecnico = input('Digite o nome do Tecnico: ')
            esquema = input('Seu esquema tatico: ')
            tecnico = Tecnico(nomeTecnico,esquema)
            coletiva = ('Seu tecnico dará coletiva? ').lower()
            if coletiva == 's':
                print(tecnico.dar_coletiva())
            cadastro.append({"Time" : time.nomeTime})             
