a = input('Digite algo: ')
print('O tipo primitivo de {} é do tipo {}'.format(a, type(a)))
print('É um número?{}'.format(a.isnumeric()))
print('É alfabético?{}'.format(a.isalpha()))
print('Tem só espaços?{}'.format(a.isspace()))
print('É somente maiúsculas?{}'.format(a.isupper()))
print('É somente minúsculas?{}'.format(a.islower()))
print('É capitalizada?{}'.format(a.istitle()))
print('É alfanúmerica?{}'.format(a.isalnum()))


