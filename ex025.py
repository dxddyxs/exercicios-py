from datetime import date
a = int(input('diga seu ano de nascimento: '))
anoat = date.today().year
if anoat - a <= 9:
    print('você se encaixa na categoria mirim')
elif anoat - a <= 14 and anoat > 9:
    print('você se encaixa na categoria infantil')
elif anoat - a <= 19 and anoat > 14 and anoat > 9:
    print('você se encaixa na categoria junior')
elif anoat - a <= 20 and anoat > 19 and anoat > 14 and anoat > 9:
    print('você se encaixa na categoria senior')
elif anoat - a > 20:
    print('voce se encaixa na categoria master')
