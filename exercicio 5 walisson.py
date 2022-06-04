nome = input ('Qual funcionario: ')
salario = float ( input ('Quanto o funcionario ganha: '))
dias = int ( input ('Quantos dias trabalhou no ultimo mes: '))
mes = int ( input ('Quantos meses trabalhou: '))
diaria = salario / 22 
salarioproporcional = dias * diaria 
fgts = ((salario * 8) / 100) * mes
multa = (fgts * 40) / 100
ferias = ((salario * 30) / 100) + salario
PLR = ((salario * 10 ) /100) + mes
desconto = 2000

print ('*' * 46)
print ('*'* 15 ,'Du Marlie LTDA', '*' * 15 )


print ('Funcionario: {} \nValores rescisorio calculado:  \nFGTS ( Retido + Mults) ${:.2f} \nSalario proporcional ${:.2f} \nFerias ${:.2f} \nPLR ${:.2f}  \nDesconto ${:.2f} \nValor rescisorio liquido ${:.2f}' .format ( nome,fgts,salarioproporcional,ferias,PLR,desconto,fgts+multa+ferias+salarioproporcional+PLR-desconto) )


print ('Assinatura: ')

print ('_' * 46)
print ('Nome do Funcionario')

print ('*' * 46)
print ('*' * 15 ,'Du Marlie LTDA', '*' * 15)