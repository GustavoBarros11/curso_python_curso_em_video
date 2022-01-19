from time import sleep

def maior(*nums):
    print('-='*25)
    print('Analisando os valores passado...')
    for num in nums:
        sleep(0.4)
        print(f'{num}', end=' ')
    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {max(nums) if len(nums) > 0 else 0}.')
    

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
