import random
n0 = input('digite o nome do aluno: ')
n1 = input('digite o nome do aluno: ')
n2 = input('digite o nome do aluno: ')
n3 = input('digite o nome do aluno: ')
lista = [n0, n1, n2, n3]
escolha = random.choice(lista)
print('aluno {} ira limpar o quadro'.format(escolha))