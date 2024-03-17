v = input('qual a velocidade do carro? ')
multa = (v - 80) * 7
if v <= 80:
    print('você esta dentro da lei')
else:
    print(f'você será multado em \033[7;30m{multa}')