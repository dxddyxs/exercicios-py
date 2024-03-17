from random import randint
n = int(input('tente acertar o número que estou pensando de 0 a 5 : '))
r = randint(0, 5)
if n == r:
    print('acertou parabéns!')
else:
    print('errou! tente novamente.')