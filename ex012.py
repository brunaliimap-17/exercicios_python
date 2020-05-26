#Calculando desconto de um produto
nome = str(input('Qual é o produto?'))
preco = float(input('Qual é o preço do produto? R$'))
desconto = float(input('Qual é o desconto?'))

valor1 = desconto/100
nvpreco = preco - (preco * valor1)

print('O item {} com valor R${} tem {}% de desconto \nReceber do cliente R${}'.format(nome, preco, desconto, nvpreco))