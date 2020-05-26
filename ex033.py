a= float(input('Digite o primeiro valor:'))
b = float(input('Digite o segundo valor:'))
c = float(input('Digite o terceiro valor:'))
#verificando qual é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando qual é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))