preço = float ( input ('Qual o preço do produto R$'))
novo = preço - (preço * 5 / 100)
print ( 'o preço do produto que custava {:.2f}$ na promoçao com 5% de desconto custara {:.2f}' .format (preço, novo))