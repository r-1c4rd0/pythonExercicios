velocidade = float(input('Qual a velocidade atual do veículo?'))
if velocidade > 80:
    print('\33[31;47mVocê foi MULTADO, pois execeu o limite de velocidade!!!\33[m')
    multa = (velocidade - 80) * 7
print('Tenha um bom dia e \33[33;40mDIRIJA COM SEGURANÇA!\33[m')
