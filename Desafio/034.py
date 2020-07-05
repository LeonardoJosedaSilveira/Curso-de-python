sal = float(input('Qual o seu salario? '))
if sal > 1250.00:
    print('Com o aumento seu salario sera R${:.2f}'.format(sal + (sal / 100) * 10))
else:
    print('Com o aumento seu salario sera R${:.2f}'.format(sal + (sal / 100) * 15))