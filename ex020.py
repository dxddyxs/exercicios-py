v = int(input('qual o valor da casa? '))
s = float(input('qual o seu salario? '))
a = int(input('em quantos anos irá pagar? '))
p = (a / 12) * 0.30
if s < p:
    print(f'seu empréstimo foi negado')
else:
    print('o empréstimo foi aceito!')