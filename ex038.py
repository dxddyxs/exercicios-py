from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for c in range (1, 8):
    nasc = int(input('digite um ano de nascimento: '))
    idade = ano - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'e tambem tivemos {totmenor} pessoas menores de idade')