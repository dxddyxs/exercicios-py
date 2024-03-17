import math
o = float(input('comprimento do cateto oposto: '))
a = float(input('comprimento do cateto adjacente: '))
h = math.hypot(o, a)
print(f'a hipotenusa do seu angulo é: {h:.2f}cm')