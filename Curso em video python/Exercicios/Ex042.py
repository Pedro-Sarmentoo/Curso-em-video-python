#Acrescente no ex035 a opção de mostrar qual tipo de triangulo ele é
l1 = float(input('Tamanho 1: '))
l2 = float(input('Tamanho 2: '))
l3 = float(input('Tamanho 3: '))

if l1 + l2 > l3:
    if l1 + l3 > l2:
        if l2 + l3 > l1:
            if l1 == l2 and l1 == l3:
                print('Poderá formar um triangulo equilatero')
            elif l1 == l2 or l1 == l3:
                print('Poderá formar um triangulo isosceles')
            else:
                print('Poderá formar um triangulo escaleno')
else:
    print('Não poderá formar um triangulo')
