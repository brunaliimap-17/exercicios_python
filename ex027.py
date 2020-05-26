name = str(input('Digite seu nome completo:')).strip()
n = name.split()   #joga numa lista
print(n)
print('Prazer em conhece-lo!')
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[len(n)-1]))
