vel = float(input('Qual a velocidade do carro:'))
if (vel >= 80):
    mult = (vel - 80) * 7
    print('Multado!! Você excedeu o limite permitido de 80 km/h, e o valor da multa é de R$ {}'. format(mult))
else:
    print('Tenha um Bom dia! Dirija com segurança!')


