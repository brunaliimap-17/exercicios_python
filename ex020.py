from random import  shuffle

al1 = str(input('Digite o primeiro nome:'))
al2 = str(input('Digite o segundo nome:'))
al3 = str(input('Digite o terceiro nome:'))
al4 = str(input('Digite o quarto nome:'))
lista = [al1, al2, al3, al4]

shuffle(lista)
print('A ordem de apresentação vai ser:')
print(lista)
