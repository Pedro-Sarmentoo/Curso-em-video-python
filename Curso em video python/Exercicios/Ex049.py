#refaça o ex009 mostrando a tabuada de um usuario quiser usando o for
print('========TABUADA AUTOMÁTICA========')
num = int(input('Digite um número: '))
for c in range(0,11):
    print('{} x {} = {}'.format(num,c,num*c))
