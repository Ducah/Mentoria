peso = float ( input  ('Digite o seu peso: '))
altura = float ( input ('Digite sua altura: '))
imc =  peso / (altura  ** 2)
print ('O IMC dessa pessoa é de {:.1f}' .format(imc))

if 18.5 <= imc < 25:
      print ('Seu peso esta normal')
elif 25 <= imc < 30:
    print ('Voce esta SOBREPESO')
elif 30 <= imc < 40:
    print ('Voce esta em OBESIDADE , Cuidado!')
elif imc > 40:
    print ('Voce esta em OBESIDADE GRAVE, Cuidado! ')

