# Crie um programa que calcule a media de duas notas e se for abaxio de 5 é reprovado, 5 até 6,9 recuperação e acima de 7 aprovado
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if (nota1 + nota2)/2 >= 7 :
    print('Aprovado!!')
elif (nota1 + nota2)/2 < 5 :
    print('Reprovado!!')
else :
    print('Recuperação!!')
