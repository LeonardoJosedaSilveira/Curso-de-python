frase = str(input('Digite uma frase: '))
#conta quantas veses 'A' aparece na frase
print('A frase contem {} letras A'.format(frase.count('A')))
#encontra a primeira letra 'A'
print('Contem uma primeira letra A na posição {}'.format(frase.find('A')))
#encontra a ultima letra 'A'
print('Contem uma ultima letra A na posição {}'.format(frase.rfind('A')))