cedulas = [50, 20, 10, 1]
qntd = [0, 0, 0, 0]
valor = int(input('digite um valor a ser saacado (minimo 1 real): '))

print(f'saque de R${valor} reais com a seguintes notas:')
for c, cedulas in enumerate(cedulas):
    print(f'{qntd} nota(s) de R${cedulas}')