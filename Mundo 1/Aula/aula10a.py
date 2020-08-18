#testa se a string tem o nome escolhido
"""
nome = str(input('Qual o seu nome? '))
if nome == 'Leo':
    print('Que nome lindo vicê tem')
else:
    print('Seu nome é tão normal!')
# condicional simples
if nome == 'Leo':
    print('Que nome lindo vicê tem')
print('Bom dia, {}'.format(nome))
"""
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2)/2
print('a sua media é {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('sua media foi ruim! estude mais!')
#versao simplificada
#print('parabens' if m >=6 else 'ESTUDE MAIS')