soma = 0
cont = 0
for c in range (1, 7):
    numero = int(input('digite um número inteiro: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f'voce informou {cont} números pares e a soma foi de {soma}')

    