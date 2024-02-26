'''Crie um programa onde o usuario possa digitar 7 valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente
OBS: fazer uma lista com duas listas internas'''

pares = list()
impares = list()
total = list()
total.append(pares)
total.append(impares)

for c in range(0,7):
    num = int(input('Digite um número: '))
    if num%2 == 0:
      pares.append(num)
    else:
      impares.append(num)
      pares.sort()
      impares.sort()
for par in range(0,len(pares)):
  if par == 0:
      print('Os valores pares são: ',end='')
  print(total[0][par],end=', ')
print('')
for impar in range(0,len(impares)):
  if impar == 0:
    print('Os valores impares são: ',end='')
  print(total[1][impar],end=', ')
 