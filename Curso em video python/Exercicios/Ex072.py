'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostra-lo por extenso.'''

cont = 0
numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
resp = int(input('Digite um número entre 0 e 20: '))

while True:
    if resp == cont:
        break
    else:
        cont = cont + 1
print(f'O numero {resp} em extenso é {numeros[cont]}!')
