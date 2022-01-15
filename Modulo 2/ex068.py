from random import randint

vit_consec = 0

print('=-'*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*25)

while True:
    pc = randint(0, 10)
    jog = int(input('Diga um valor: '))
    opcao = input('Par ou Ímpar? [P/I] ').strip().upper()
    nomenclatura = {'P': 'PAR', 'I': 'ÍMPAR'}

    if (jog+pc) % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'

    print('-'*25)
    print(f'Voce jogou {jog} e o computador {pc}. Total de {jog+pc} DEU {nomenclatura[resultado]}')
    print('-'*25)

    if opcao == resultado:
        print('Voce VENCEU!')
        print('Vamo jogar novamente...')
        vit_consec += 1
    else:
        print('Voce PERDEU!')
        print(f'GAME OVER! Voce venceu {vit_consec} vezes.')
        break