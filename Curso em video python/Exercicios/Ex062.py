# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais quantos termos e o programa vai parar quando ele digitar 0 para encerrar

primeiro = int(input('Digite o primeiro valor: '))
razao = int(input('Digite a razão: '))
num = 1
limite = 10
resp = 1

while resp == 1:
    while num <= limite:
        print(primeiro ,end= ' ')
        primeiro += razao
        num += 1
    resp = int(input('Você deseja continuar? [0 para não e 1 para sim]: '))
    if resp == 1:
        x = int(input('Você quer mais quantos termos: '))
        resp = 1
        limite += x
print('Fim')
