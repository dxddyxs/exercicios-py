numeros = []
for _ in range(0, 5):
    numeros.append(int(input('digite um valor: ')))
    for chave, valor in enumerate(numeros):
        if numeros < valor:
            numeros.insert(chave, numeros)
            break
        else:
            numeros.append(numeros)

print(f'os numeros digitados foram: {numeros}')