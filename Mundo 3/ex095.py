jogadores = []

while True:
    dados = dict()
    tot_gols = 0
    dados['nome'] = str(input('Nome do jogador: '))
    dados['gols'] = []

    tot_partidas = int(input('Quantas partidas {} participou? '.format(dados['nome'])))
    for i in range(0, tot_partidas):
        gols = int(input('   Quantos gols na partida {}? '.format(i+1)))
        dados['gols'].append(gols)
        tot_gols += gols
    dados['total'] = tot_gols

    jogadores.append(dados.copy())
    dados.clear()
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
        if opcao in 'SN':
            break
        print('ERRO! Opção inválida.')

    if opcao == 'N':
        break

print('-='*35)
print(f'{"cod"} {"nome":<15}{"gols":<20}{"total":<6}')
print('-'*45)
for i, jogador in enumerate(jogadores):
    print('{:>3} {:<15}{:<20}{:<6}'.format(i, jogador["nome"], str(jogador["gols"]), jogador["total"]))
print('-'*45)

while True:
    while True:
        pos = int(input('Mostrar dado de qual jogador? (999 para parar) '))
        if pos >= 0 and pos < len(jogadores) or pos == 999:
            break
        print(f'ERRO! Não existe jogador com código {pos}.')
    if pos == 999:
        break
    print(f'{"--":>3} LEVANTAMENTO DO JOGADOR {jogadores[pos]["nome"]}:')
    for i, gols in enumerate(jogadores[pos]["gols"]):
        print(f'     No jogo {i+1} fez {gols} gols.')
    print('-'*45)
print('<< VOLTE SEMPRE >>')