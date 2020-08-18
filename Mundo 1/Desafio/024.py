cidade = str(input('digite o nome de uma cidade: '))
primeiro = cidade.split()
print('O nome da cidade começa com SANTO? {}'.format(primeiro[0].__eq__('SANTO')))