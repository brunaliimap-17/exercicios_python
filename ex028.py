from random import randint
from time import  sleep
computador = randint(0,5) #Faz o computador  pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar ...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))
print('PROCESSANDO ...')
sleep(5)
if jogador == computador:
    print('Parabéns você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'. format(computador, jogador))
