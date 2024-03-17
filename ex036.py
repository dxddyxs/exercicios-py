n = int(input('digite um numero : '))
tot = 0
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(f'{c}', end=' 3')
print(f'o número {n} foi divisivel {tot} vezes')