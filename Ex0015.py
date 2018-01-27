km = float(input('Iforme a quantidade de km percorridos:\n '))
d = int(input('Quantos dias alugados:\n '))
p = (d * 60) + (km * 0.15)
print('O valor da sua fatura é no total de {:.2f}'.format(p))
