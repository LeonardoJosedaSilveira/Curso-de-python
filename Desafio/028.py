from random import randrange
n0 = int(randrange(6))
n1 = int(input('O computador pensou em um numero de 0 a 5 qual você acha que foi? '))
print('Venceu' if n0 == n1 else 'Perdeu')