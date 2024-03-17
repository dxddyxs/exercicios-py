r1 = int(input('digite um comprimento: '))
r2 = int(input('digite um comprimento: '))
r3 = int(input('digite um comprimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 == r3:
    print('esse comprimento forma um triangulo equilatero')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 != r3 and r2 == r3 != r1 and r1 == r3 != r2:
    print('esse comprimento forma um triangulo isósceles')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 != r2 != r3:
    print('esse comprimento forma um triangulo escaleno')
else:
    print('esse comprimento não forma um triangulo')