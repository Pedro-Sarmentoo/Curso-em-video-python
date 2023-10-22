'''Crie um programa que leia a idade e o sexo de várias pessoa.
 a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
 no final mostre(quantas pessoas tem mais de 18, quantos homens foram cadastrados, quantas mulheres tem menos de 20 anos).
'''
mais18 = 0
man = 0
shemenos20 = 0

while True:
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo: [M/F]: ')).upper().strip()[0]

    if idade > 18:
        mais18 += 1
    if sexo == 'F':
        if idade < 20:
            shemenos20 += 1
    else:
        man += 1
    resp = int(input('Deseja continuar? Digite 1 para sim e 0 para não: '))
    if resp == 0:
        break
print(f'Ao todo teve {mais18} pessoas com mais de 18 anos')
print(f'{man} homens cadastrados')
print(f'{shemenos20} mulher(es) com menos de 20 anos')
print('Fim')
