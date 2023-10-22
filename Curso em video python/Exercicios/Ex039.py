# Faça um programa que leia o ano de nascimento e informe de acordo com sua idade se ele ainda vai se alistar
# se é hora de se alistar e se já passou da hora de alistar e falar o tempo que falta ou o tempo que passou(usa o ano do sistema)
import datetime
ano = int(input('Em qual ano você nasceu? '))
mes = int(input('Em qual mês você nasceu? '))
dia = int(input('Em qual dia você nasceu? '))
ano_atual = datetime.date.today().year
mes_atual = datetime.date.today().month
dia_atual = datetime.date.today().day
idade = ano_atual - ano

if mes <= mes_atual :
    if mes == mes_atual and dia <= dia_atual :
        idade = idade + 1
    else :
        idade = idade + 1
else :
    idade = idade - 1

if idade == 18 :
    print('Está na hora de você se alistar!!')
elif idade > 18 :
    print('Caso não tenha se alistado, você devia ter se alistado a {} anos!!'.format(idade - 18))
else :
    print('Falta {} anos para você se alistar ainda!!'.format(18 - idade))
