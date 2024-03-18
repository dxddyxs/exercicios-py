tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    x = int(input('Digite um número de 0 a 20: '))
    if x < 0 or x >20:
        print('tente novamente.', end=' ')
    else:
        print(f'você digitou o número {tupla[x]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? \n[S/N]')).upper()[0]
    if resp == 'N':
        break
print('FIM')

