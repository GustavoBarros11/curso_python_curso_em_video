from random import randint

nums_sorteados = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram ', end='')
for i, num in enumerate(nums_sorteados):
    if i == 0:
        print(f'{num}', end='')
    else:
        print(f', {num}', end='')
    
print(f'\nO maior valor sorteado foi {max(nums_sorteados)}')
print(f'O menor valor sorteado foi {min(nums_sorteados)}')
