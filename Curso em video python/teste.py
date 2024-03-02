from random import randint 

palpite = list()
num = 0
for numeros in range (0,6):
    if numeros == 0:
        num = randint(0,60)
        palpite.append(num)
    else:
        while num in palpite:
           num = randint(0,60)
        palpite.append(num) 
print(palpite)