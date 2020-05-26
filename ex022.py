nome = str(input('Digite seu nome inteiro:')).strip() #corta os espaços
print('Analisando o seu nome ...')
print('Seu nome em letras maiúscula é {}'.format(nome.upper()))
print('Seu nome com letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

