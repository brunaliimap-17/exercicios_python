#Quantos litros de tintas é necessário para pintar a parede?

largura = float(input('Entre com a largura:'))
altura = float(input('Entre com a altura da parede:'))

area = largura * altura
tinta = area / 2

print('Sua parede tem a seguinte dimesão {}x{} e sua área é de {}m².'.format(largura,altura,area))
print(' Vai ser necessário {} litros de tintas para pintar sua parede'.format(tinta))
