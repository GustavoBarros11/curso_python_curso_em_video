classificacao = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará',
 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print('=-='*10)
print('Lista de time do Brasileirão: ', end='')
print(classificacao)
print('=-='*10)
print(f'Os 5 primeiros são {classificacao[0:5]}')
print('=-='*10)
print(f'Os 4 ultimos são {classificacao[-4:]}')
print('=-='*10)
print(f'Times em ordem alfabética: ', end='')
print(sorted(classificacao))
print('=-='*10)
print(f'O chapecoense está na {classificacao.index("Chapecoense")+1}* posição')