#Aluguel de carro

dias = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos KM rodado?'))

pago = (dias * 60) + (km * 0.15)

print('O total a pagar é de R$ {:.2f}'.format(pago))