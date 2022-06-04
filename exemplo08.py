import math
num = int ( input ( 'Digite um numero: '))
raiz = math.sqrt (num)
print (' A raiz de {} e igual a {} ' .format(num,raiz))
print (' A raiz de {} e igual a {} ' .format(num,math.ceil(raiz))) #a redonda para cima
print (' A raiz de {} e igual a {} ' .format(num,math.floor(raiz))) #a redonda para baixo
