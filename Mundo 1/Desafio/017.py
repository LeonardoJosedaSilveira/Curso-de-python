from math import hypot
n0 = float(input('digite o valor do cateto oposto: '))
n1 = float(input('digite o valor do cateto adjacente: '))
cateto = hypot(n0, n1)
print('a ipotenusa é igual a {:.3f}'.format(cateto))
#print('\033[0;35;41meste é o teste das cores\033[m')