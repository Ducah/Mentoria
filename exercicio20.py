import random
nome = input ('Primeiro aluno: ')
nome2= input ('Segundo aluno: ')
nome3= input ('Terceiro aluno: ')
nome4= input ('Quarto aluno:')
lista= [nome, nome2, nome3, nome4]
random.shuffle(lista)

print ('A ordem de apresentaçao sera')
print (lista)
