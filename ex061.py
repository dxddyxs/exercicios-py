valores = []
menor = 0
maior = 0
for cont in range(0, 5):
    valores.append(int(input('digite um valor: ')))

print(f'o maior valor digitado foi {max(valores)} que esta na posição {valores.index(max(valores))}')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i} ', end='')
print()

print(f'o menor valor digitado foi {min(valores)} que esta na posição {valores.index(min(valores))}')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}')