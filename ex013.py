#Reajuste salarial de um funcionário

funcionario = str(input('Nome do funcionário:'))
salario = float(input('Qual é o salário:'))
aumento = float(input('Qual a porcentagem de aumento:'))

nvsalario = salario + (salario * (aumento/100))

print('O funcionário {} que tinha um salário de R$ {} e recebeu um aumento de {}% tem seu novo salário de R${}'.format(funcionario, salario, aumento, nvsalario))

