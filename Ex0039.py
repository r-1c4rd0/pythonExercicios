from datetime import date
hj = date.today().year
ns = int(input('Ano do seu nascimento: '))
i = hj - ns
print('Quem nasceu em {} tem {} anos em {}'.format((ns, i, hj)))
