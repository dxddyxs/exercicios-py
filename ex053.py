total = 0
pmil = 0
nomebarato = ' '
somavalor = 0
cont = 0
while True:
    p = str(input('qual o nome do produto? ')).upper()
    vp = float(input('qual o valor dele? '))
    cont += 1
    somavalor += vp

    if vp < 1000:
        pmil += 1

    if cont == 1:
         nomebarato = p

    condicao = input('quer continuar? \n[S/N]: ').upper()[0]
    if condicao == 'N':
            print(f'o total gasto foi {somavalor}')
            print(f'{pmil} produtos que custam mais de 1000')
            print(f'{nomebarato} é o nome do produto mais barato')
            break

