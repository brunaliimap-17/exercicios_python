dis = float(input('Qual é a distância da viagem?'))
print('Você está preste a iniciar uma viagem de {}km'.format(dis))

if( dis <= 200):
    pas = dis * 0.50

else:
    pas = dis * 0.45

print('O valor da passagem é R${}'. format(pas))