n1 = float(input('digite sua nota do primeiro semestre: '))
n2 = float(input('digite sua nota do segundo semestre: '))
m = (n1 + n2)/2
if m < 5.0:
    print('você esta REPROVADO!')
elif m > 7.0:
    print('você foi APROVADO!')
elif m > 5.0 and m < 6.9:
    print('você esta de RECUPERAÇÂO!')
