retas = []
count = int(0)
maior = int(0)
soma = int(0)
print('O programa precisa de 3 retas')
#laço de repetição para receber as retas
while count < 3:
    retas.append(int(input('Digite o tamanho de  uma reta: ')))
    #escolhe a maior reta
    if maior < retas[count]:
        maior = retas[count]
    #soma as retas
    soma = soma + retas[count]
    count = count + 1
#retira a reta maior da soma
soma = soma - maior
#testa se um triangulo é possivel
print('Elas podem formar um triangulo' if maior <= soma else 'elas nao podem formar um triangulo')
