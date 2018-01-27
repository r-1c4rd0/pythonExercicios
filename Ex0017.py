co = float(input('Informe o cateto oposto, CO\n:'))
ca = float(input('Qual é o cateto adjacente, CA\n:'))
h = (co ** 2 + ca ** 2) ** (1/2)
print('a hipitenusa vai medir {:.3f}'.format(h))
