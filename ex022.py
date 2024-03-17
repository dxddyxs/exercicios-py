n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))
if n1 > n2:
    print(f'{n1} é maior.')
elif n2 > n1:
    print(f'{n2} é maior.')
elif n1 == n2:
    print('não existe valor maior, os dois são iguais.')