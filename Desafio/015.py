dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = dias * 60 + km * 0.15
print('O total a pagar é de R${:.2f}'.format(pago))
#print('\033[1;34;43mteste O corinho\033[m')