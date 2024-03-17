k = int(input('qual a distancia da sua viagem em km? '))
if k <= 200:
    c = k * 0.50
else:
    c = k * 0.45
print(f'o valor da sua passagem foi: {c}')
