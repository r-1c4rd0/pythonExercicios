from random import randint
from time import sleep
n = 1
while n != 0:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('''\33[0;33mSuas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA ''')
    jogador = int(input('Qual é a sua jogada? \n: '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('=-'*12)
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    print('=-'*12)
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('O JOGADOR GANHOU!!!')
        elif jogador == 2:
            print('O COMPUTADOR GANHOU !!!')
        else:
            print('OPÇÃO INVÁLIDA!!!')
    elif computador == 1:
        if jogador == 0:
            print('O COMPUTADOR GANHOU!!!')
        elif jogador == 1:
            print('EMPATE!!!')
        elif jogador == 2:
            print('O JOGADOR GANHOU!!!')
        else:
            print('OPÇÃO INVÁLIDA!!!')
    elif computador == 2:
        if jogador == 0:
            print('O JOGADOR GANHOU!!!')
        elif jogador == 1:
            print('O COMPUTADOR GANHOU')
        elif jogador == 2:
            print('EMPATE')
        else:
            print('OPÇÃO INVÁLIDA!!!')
    print('=-'*12)
    n = int(input('\n\nPARA SAIR DIGITE [0]'))
