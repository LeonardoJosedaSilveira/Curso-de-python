# recebe o nome  coloca maiuscula e minuscula
nome = str(input('Digite o nome completo: '))
print(nome.upper())
print((nome.lower()))
# corta o nome, retira espaços, e conta carecteres
parte = nome.strip().split()
print(parte)
print(len(''.join(parte)))
# conta o primeiro nome
primeiro = parte[0]
print(len(primeiro))
