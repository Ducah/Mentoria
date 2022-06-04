p = float ( input (' Qual e o preço do produto: '))
d = (p * 7) / 100
t = p - ((p * 7 )/ 100)

print ( 'valor da compra sem desconto: R${} \nvalor do desconto: R${} \nvalor da compra com desconto: R${} ' .format (p,d,t))