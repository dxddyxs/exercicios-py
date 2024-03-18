num = (int(input('digite um valor: ')),
        int(input('digite um valor: ')),
        int(input('digite um valor: ')),
        int(input('digite um valor: ')))

print(f'o numero 9 apareceu {num.count(9)} vezes')
print(f'o valor primeiro valor 3 foi digitado em posição {num.index(3)}')
print('os valoress pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
