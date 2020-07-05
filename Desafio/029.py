#velocidade
vel = int(input('Qual a velocidade atual do seu carro? '))
#limite , multa de R$7,00 por cada km acima do limite
if vel > 80:
    valor = (vel - 80) * 7.00
    print('Voce foi multado, o valor é R${:.2f}'.format(valor))