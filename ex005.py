num = int(input('Digite um número:'))
a = num -1
s = num +1

#Duas formas de realizar esta análise
print('Analisando o número {}, o seu antecessor é {} e o seu sucessor é {}'.format(num, a, s))
print('Analisando o número {}, o seu antecessor é {} e o seu sucessor é {}'.format(num, (num-1), (num+1)))