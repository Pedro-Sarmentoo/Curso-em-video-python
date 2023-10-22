#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex --> 5! = 5 x 4 x 3 x 2 x 1

num = int(input('Digite um número: '))
x = 1
fatorial = 0
while x <= num:
    if x == 1:
        fatorial = x * (x+1)
        x += 2
    else:
        fatorial = fatorial * x
        x += 1
print(fatorial) 