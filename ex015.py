a = int(input('digite um ano: '))
bi = (a / 100)% 4
if bi == 0:
    print('o seu ano é bissexto')
else:
    print('seu ano não é bissexto')
