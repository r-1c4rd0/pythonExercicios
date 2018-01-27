from random import randint
computador = randint(0, 5)
jogador = 0
print('-=-' * 8)
print('Vou  pensar em um número tente adivinhar...')
print('-=-' * 8)
while jogador != computador:
    jogador = int(input('Em que número eu pensei? \n:'))
    if jogador == computador:
        print('PARABÉNS! Você conseguiu me vencer')
    else:
        print('Eu pensei no número {} e não no {}!'.format(computador, jogador))
print('Fim de jogo \n =-=-=- GAME OVER -=-=-= ')
