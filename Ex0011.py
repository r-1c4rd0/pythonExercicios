lg = float(input('Largura da parede: '))
al = float(input('Altura da parede: '))
a = lg * al
lt = a / 2
print('A dimensão da sua parede e {}x{} e sua área é de: {:.0f}m²\n  '.format(lg, al, a))
print('Para pintar a parede, você precisará de {:.2f} Litros de tinta. '.format(lt))
print('Mv'*25)
