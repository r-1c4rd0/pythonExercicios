from math import hypot
co = float(input('Informe o cateto oposto, CO\n:'))
ca = float(input('Qual é o cateto adjacente, CA\n:'))
h = hypot(co, ca)
print('A hipotenusa é {:.3f}'.format(h))

