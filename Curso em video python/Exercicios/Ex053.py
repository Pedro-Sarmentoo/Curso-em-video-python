#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.

novafrase = ''
frase = str(input('Digite uma frase: ').strip())
extra = frase
quebra = frase.split()# quebra a frase e transforma em uma lista com cada palavra
frase = ''.join(quebra)# o join junta as strings separando ela com que estiver nas ' '
quantiletra = len(frase)# conta a quantidade de caracteres incluindo espaços etc...
for c in range (quantiletra - 1,-1,-1):
    novafrase = novafrase + frase[c]
frase = frase.lower()
novafrase = novafrase.lower()
if frase == novafrase:
    print('A frase ou palavra: "{}" é um palidromo'.format(extra))
else:
    print('A palavra ou frase "{}" não é um palidromo'.format(extra))
