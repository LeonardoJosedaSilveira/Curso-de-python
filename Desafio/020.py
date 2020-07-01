import random
n0 = str(input('digite o nome do aluno: '))
n1 = str(input('digite o nome do aluno: '))
n2 = str(input('digite o nome do aluno: '))
n3 = str(input('digite o nome do aluno: '))
lista = [n0, n1, n2, n3]
random.shuffle(lista)
print('A ordem das apresentações será {}'.format(lista))