'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do camp brasileiro, na ordem de colocação, depois mostra
A) apenas os primeiros colocados 
B) os ultimos 4 colocados da tabela 
C) Uma lista com os times em ordem alfabetica 
D) Em que posição na tabela está o time da cruzeiro.'''

tabela = ('','BOTAFOGO','BRAGANTINO','FLAMENGO','PALMEIRAS','ATHLETICO-PR','GRÊMIO','ATLÉTICO-MG','FORTALEZA','FLUMINENSE','SÃO PAULO','CUIABÁ','INTERNACIONAL','BAHIA','CRUZEIRO','CORINTHIANS','GOIÁS','VASCO DA GAMA','SANTOS','CORITIBA','AMÉRICA-MG')
cont = 0

print('===================================')
print('Top 5 da tabela do brasileirão 2023')
print('===================================')

for c in range (1,6):
    print(f'O {c}º colocado da tabela é o {tabela[c]}')

print('')
print('Os ultimos 4 colocados são:')
for a in range (18,21):
    print(tabela[a])
print('')

print('Os times na ordem alfabetica fica assim: ')
print(sorted(tabela[1:]))

while True:
    if tabela[cont] == 'CRUZEIRO':
        break
    else: cont = cont + 1
print('')
print(f'O cruzeiro está na posição {cont}º')
