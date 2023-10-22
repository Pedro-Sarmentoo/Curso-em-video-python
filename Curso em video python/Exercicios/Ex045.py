#faça um pedra(1),papel(2) e tesoura(3)
from random import randint
num = randint(1,3)
esc = 0
mao = (input('Pedra,papel ou tesoura? '))

if mao == 'pedra':
    esc = 1
elif mao == 'papel':
    esc = 2
elif mao == 'tesoura':
    esc = 3

if num == esc:
    print('Deu empate')

elif esc == 1 and num == 2:
    print('Eu escolhi papel, você perdeu!!')
elif esc == 1 and num == 3:
    print('Eu escolhi tesoura, você ganhou!!')

elif esc == 2 and num == 1:
    print('Eu escolhi pedra, você ganhou!!')
elif esc == 2 and num == 3:
    print('Eu escolhi tesoura, você perdeu!!')

elif esc == 3 and num == 1:
    print('Eu escolhi pedra, você perdeu!!')
elif esc == 3 and num == 2:
    print('Eu escolhi papel, você ganhou!!')
