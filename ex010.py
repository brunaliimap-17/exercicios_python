#Conversor de moeda

din = float(input('Quanto de dinheiro você tem disponível? R$'))
dolar = float(input('Entre com a cotação do dólar do dia? U$'))

x= (din*1)/dolar

print('Com R$ {:.2f} você pode comprar {:.2f} doláres'.format(din, x))



#  5,50(dolar) - 1 dolar    x= (din*1)/dolar
#  10 reais (din) - x