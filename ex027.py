p = float(input('diga seu peso: '))
a = float(input('diga sua altura: '))
imc = p/(a * a)
if imc <= 18.5:
    print('você esta abaixo do peso.')
elif imc > 18.5 and imc <= 25:
    print('você esta no peso ideal.')
elif imc > 25 and imc <= 30:
    print('você esta com sobrepeso.')
elif imc > 30 and imc <= 40:
    print('você esta com obesidade.')
elif imc > 40:
    print('você esta com obesidade mórbida.')