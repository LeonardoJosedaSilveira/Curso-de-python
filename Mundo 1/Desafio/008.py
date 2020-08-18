n1 = float(input('Digite a quantidade de metros '))
n2 = n1*100
n3 = n1*1000
print('São {:.0f} centímetros ou {:.0f} milímetros'.format(n2, n3))
print('\033[1;37;42mSão {:.0f} centímetros ou {:.0f} milímetros\033[m'.format(n2, n3))