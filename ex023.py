from datetime import date
a = int(input('digite o ano do seu nascimento: '))
anoat = date.today().year
if anoat - a < 18:
    print(f'você tem {((anoat - a)- 18) * -1} anos para de alistar')
elif anoat - a > 18:
    print(f'você esta atrasado a {(anoat - a)- 18} anos')
elif anoat - a == 18:
    print('esta na hora de voce se alistar!')