n1 = int(input('Digite um valor: '))
print('Tabuada do {}'.format(n1))
print('--'*6)
for x in range(11):
    print('{} * {:2} = {}'.format(n1, x, x*n1))
print('--'*6)
