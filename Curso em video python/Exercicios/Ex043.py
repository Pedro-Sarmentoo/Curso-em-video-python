#Faça um programa que leia o peso e altura de uma pessoa e calcule o IMC
#abaixo de 18,5 é abaixo do peso, entre 18,5 e 25 é o peso ideal e 25 até 30 é sobrepeso e 30 até 40 é obesidade e acima disso é obesidade morbida
#IMC = peso/altura^2
import math
altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso em Kg? '))
imc = peso/(altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc > 25 and imc < 30:
    print('Você está em sobrepeso')
elif imc > 30 and imc < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade morbida')
