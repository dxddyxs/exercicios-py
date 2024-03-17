while True:
    numero = int(input('digite um número inteiro: '))
    if numero <= 0:
        print('sistema encerrado.')
        break
    for tabuada in range (1, 11):
        print(f'{numero} x {tabuada} = {numero * tabuada}')
    