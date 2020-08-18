cont = int(0)
maior = int(0)
menor = int(999999999999999999999999999999999999999999999999999999999999999999999999999999999)
while cont < 3:
    num = int(input('digite um numero: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont = cont + 1
print('o numero maior é {} e o numero menor é {}'.format(maior, menor))
