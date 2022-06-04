'''num = float (input ( ' Comprimento do cateto oposto: '))
num2 = float ( input (' Comprimento do cateto adjacente: '))
hip = (num ** 2 + num2 ** 2) ** (1/2)
print (' A hipotenusa vai medir {}' .format (hip))'''
import math
num = float (input ( ' Comprimento do cateto oposto: '))
num2 = float ( input (' Comprimento do cateto adjacente: '))
hip = math.hypot (num,num2)
print ('A hipotenusa vai medir {}' .format(hip))  
