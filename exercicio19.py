from random import random


import random
aluno = input ('Primeiro aluno: ')
aluno2= input ('Segundo aluno: ')
aluno3= input ('Terceiro aluno: ')
aluno4= input ('Quarto aluno: ')
lista = [aluno, aluno2, aluno3, aluno4]
escolhido= random.choice(lista)

print (' O aluno escolhido foi {} ' .format(escolhido))