'''Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final,mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente
OBS: é uma lista de lista e a segunda lista é composta por nome, notas(essa nota parece ser uma lista a mais) e media'''

diario = list()
alunos = list()
notas = list()
n1 = list()
n2 = list()
notas.append(n1)
notas.append(n2)
diario.append(alunos)
diario.append(notas)
# Inserção dos dados
quant_alunos = int(input('Serão quantos alunos? '))
for c in range(0,quant_alunos):
    alunos.append(input('Digite o nome do aluno: '))
    n1.append(int(input('Digite a primeira nota: ')))
    n2.append(int(input('Digite a segunda nota: ')))
# Parte para manipular todos os dados
print('=-'*20)
print('No.   NOME              MÉDIA')
print('--------------------------------')
for c in range(0,quant_alunos):
    media = (n1[c]+n2[c])/2
    print(c,end='     ')
    print(alunos[c],end='              ')
    print(f'{media}')
# Parte de mostrar a nota de uma aluna em especifico
while True:
    entrada = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if entrada == 999:
        break
    else:
        print(f'Notas de {alunos[entrada]} são {notas[entrada]}')