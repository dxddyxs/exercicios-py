n1 = int(input('digite um número: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
maior = n1 > n2 > n3
menor = n1 < n2 < n3
if maior:
    print(f'{n1} é maior q {n2} e q {n3}')
if menor:
    print(f'{n1} é menor q {n2} e q {n3}')
