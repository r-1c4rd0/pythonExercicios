frase = str(input('Digite uma frase:')).upper().split()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A') + 1))
print('A última posição da letra A está na posição: {}'.format(frase.rfind('A') + 1))
