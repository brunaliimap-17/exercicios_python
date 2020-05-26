#Conversor de Temperatura

grau = float(input('Qual a temperatura de hoje?'))
conversor = str(input('Informe se está em Celsius ou Fahrenheit (C ou F):'))

if (conversor == 'C'):
    f = ((9*grau)/5)+32
    print('A temperatura é {}F'.format(f))
elif (conversor == 'F'):
    c = (grau-32) * (5/9)
    print('A temperatura em celsius é {}°C'.format(c))

