#var = input('\033[2;30;41mDigite algo: \033[m')
var = input('Digite algo: ')
print('O tipo de entrada foi:{}'.format(type(var)))
print('É alpha: {}'.format(var.isalpha()))
print('É númérico: {}'.format(var.isnumeric()))
print('E alpha numérico: {}'.format(var.isalnum()))
print('É ascii: {}'.format(var.isascii()))
print('É decimal: {}'.format(var.isdecimal()))
print('É digit: {}'.format(var.isdigit()))
print('É identifier: {}'.format(var.isidentifier()))
print('É minúscula: {}'.format(var.islower()))
print('É space: {}'.format(var.isspace()))
print('É printavel: {}'.format(var.isprintable()))
print('É title: {}'.format(var.istitle()))
print('É maiúscula: {}'.format(var.isupper()))
