
print('\033[1;30;44m-=-\033[m'*20)
print('                   Analisando o Triângulo')
print('\033[1;30;44m-=-\033[m'*20)

r1 = float(input('Entre com o primeiro segmento:'))
r2 = float(input('Entre com o segundo segmento:'))
r3 = float(input('Entre com o terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triângulo!!')
else:
    print('Não forma um triângulo!!')