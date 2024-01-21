'''
Ex01:

'''

#trabalho = {'entrada': 8, 'saída': 18}
#trabalho2 = {'entrada': 8, 'saída': 18}

#trabalho.clear()

#trabalho['ident'] = 123456
#trabalho3 = trabalho.copy()
#print(trabalho)
#print(trabalho2)
#print(trabalho3)

#lista_nomes = ['Felipe', 'Mauricio', 'Rosana']
#dict_nomes = dic.fromkeys(lista_nomes)
#print(dict_nomes)

#tecnologias = {
#    'backend': ['Python', 'Java', 'PHP'],
#    'frontend': ['JS', 'React', 'Vue'],
#    'DataScience': ['Python', 'Pandas', 'R']
#}

#print(tecnologias.get('Infra', 'Não tem não man'))
#print(tecnologias.get('backend'))
#print(tecnologias['backend'])

#print(tecnologias.items())
#for chave, valor in tecnologias.items():
#    print(f'{chave} = {valor}')

#for tecnologia in tecnologias.keys():
#    print(tecnologias[tecnologia])

#print(tecnologias['backend'])


tecnologias = {
    'backend': ['Python', 'Java', 'PHP'],
    'frontend': ['JS', 'React', 'Vue'],
    'DataScience': ['Python', 'Pandas', 'R']
}
print(tecnologias.pop('backend'), 'tchau')
print(tecnologias)
print(tecnologias.values())
for valores in tecnologias.values():
    print(f'Valor = {valores}')