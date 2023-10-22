#Faça um  programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que encontram no intervalo de 1 até 500.
total = 0
for c in range(0,501):
    if c%2 == 1:
        if c%3 == 0:
            total += c
print(total)
