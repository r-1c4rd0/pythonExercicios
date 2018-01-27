distância = int(input('Qual a distÂncia da sua viagem?'))
print('Você esta´ preste a começar uma viajem de {}KM '.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('O preço que será cobrado {:.2f}R$ '.format(distância))
