frase = input('Digite uma frase: ').strip().lower()

pos_prim = frase.find('a') + 1
pos_ult = frase.rfind('a') + 1
print("A letra 'A' aparece {} vezes na frase.".format(frase.count('a')))
print("A primeira letra 'A' apareceu na posicao", pos_prim)
print("A ultima letra 'A' apareceu na posicao", pos_ult)
