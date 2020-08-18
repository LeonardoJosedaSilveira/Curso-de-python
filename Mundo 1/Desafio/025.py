nome = str(input('Digite um nome: '))
silva = nome.split()
print('O nome contem SILVA? {}'.format(silva.__contains__('SILVA')))