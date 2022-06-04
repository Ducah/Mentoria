fun = float ( input (' Qual e o salario do funcionario: '))
novo = fun + (fun * 15 / 100)
print ('um funcionario que ganhava {:.2f}$, com 15% de aumento, passara a ganhar {:.2f}$ ' .format (fun , novo))