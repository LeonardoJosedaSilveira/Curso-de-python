n0 = float(input('Qual o preço do produto? '))
n1 = (n0/100)*5
print('O produto com desconto fica {:.2f}'.format(n0-n1))
print('\033[2;31;42mO produto com desconto fica \033[m{:.2f}'.format(n0-n1))