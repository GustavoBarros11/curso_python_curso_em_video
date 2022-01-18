dados = dict()
tot_gols = 0
dados['nome'] = str(input('Nome do jogador: '))
dados['gols'] = []

tot_partidas = int(input('Quantas partidas {} participou? '.format(dados['nome'])))
for i in range(0, tot_partidas):
    gols = int(input('   Quantos gols na partida {}? '.format(i)))
    dados['gols'].append(gols)
    tot_gols += gols
dados['total'] = tot_gols
print('-='*30)
print(dados)
print('-='*30)
print('O campo nome tem o valor {}'.format(dados['nome']))
print('O campo gols tem o valor {}'.format(dados['gols']))
print('O campo total tem o valor {}'.format(dados['total']))
print('-='*30)
print('O jogador {} jogou {} partidas.'.format(dados['nome'], len(dados['gols'])))
for i, gols in enumerate(dados['gols']):
    print('    => Na partida {}, fez {} gols.'.format(i, gols))
print('Foi um total de {} gols.'.format(dados['total']))
