import random
n0 = str(input('\033[02;31;40mdigite o nome do aluno:\033[m '))
n1 = str(input('\033[01;31;40mdigite o nome do aluno:\033[m '))
n2 = str(input('\033[03;31;40mdigite o nome do aluno:\033[m '))
n3 = str(input('digite o nome do aluno: '))
lista = [n0, n1, n2, n3]
random.shuffle(lista)
print('A ordem das apresentações será {}'.format(lista));