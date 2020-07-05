
print('\033[31mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOla, Mundo!\033[m')
print('\033[7;30mOla, Mundo!\033[m')
a: [] = 3, 0, 0
b: int = 5
c: str = 'teste'
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!! \033[32;44m{}\033[m'.format(a[0], b, c))
nome = 'Guanabara'
print('Olá, valeu {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
nomea = 'truco'
cores = {'limpa':'\033[m', 'azul':'\033[7;30', 'amarelo':'\033[33m', 'pretoebranco':'\033[7:30m'}
print('pede {}{}, {}{}, '.format(cores['amarelo'], nomea, cores['limpa'], nomea))