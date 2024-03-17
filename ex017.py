s = float(input('digite seu salario: '))
if s >= 1250:
    a = s +(s * 0.10)
    print(f'seu salario foi \033[7;30m{s:.0f} reais e depois do aumento foi para \033[7;30m{a:.0f} reais')
else:
    i = s +(s * 0.15)
    print(f'seu salario foi \033[7;30m{s:.0f} reais e foi aumentado para \033[7;30m{i:.0f} reais')