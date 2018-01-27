n = input('Informe seu nome\n: ')
v = float(input('\nInforme o valor da casa\n: '))
s = float(input('\nInforme sua renda\n:  '))
t = int(input('\nEm quantos anos deseja fazer o financiamento\n: '))
f = v / (t*12)
if s*30/100 >= f:
    print('{} informamos que:\n:Financiamento aprovado!'.format(n))
else:
    print('{} informamos que:\nReprovado na análise de crédito!!!'.format(n))

