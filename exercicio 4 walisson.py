nome = input (' Qual o nome do funcionario: ')
horas = float ( input (' Quantas horas o funcionario trabalhou: '))
salario = horas * 8.5

print (' O valor a ser pago ao {}, é de ${:.2f}' .format(nome , salario))
