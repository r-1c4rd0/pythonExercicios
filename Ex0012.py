preço = float(input('Digite o preço do produto?\n R$ '))
novo = preço - (preço * 5 / 100)
print('O produto custava R${:.2f}, no desconto de 5% vai custar R${:.2f}'.format(preço, novo))
