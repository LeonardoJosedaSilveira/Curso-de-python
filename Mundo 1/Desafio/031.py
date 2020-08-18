km = float(input('Em KM qual a distancia da sua viagem? '))
if km <= 200:
    print('O custo é R${:.2f}'.format(km * 0.50))
else:
    print('O custo é R${:.2f}'.format(km * 0.45))