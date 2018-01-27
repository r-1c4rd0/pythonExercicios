n = int(input('Digite um número inteiro'))
print('''Esolha uma das bases 
[ 1 ] converter para BINÁRIO 
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção'))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.fomat(n, bin(n)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)))
else:
    print('Opção inválida!!!')