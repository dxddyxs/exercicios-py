from random import choice
fala = str(input('joken...pô '))
lista = ['pedra', 'tesoura', 'papel'] 
r = choice(lista)
print(f'vou de {r}')
if fala == 'pedra' and r == 'tesoura':
    print('você me venceu!')
elif fala == 'tesoura' and r == 'pedra':
    print('ganhei de você')
elif fala == 'papel' and r == 'pedra':
    print('você me venceu!')
elif fala == 'pedra' and r == 'papel':
    print('ganhei de você!')
elif fala == 'papel' and r == 'tesoura':
    print('ganhei de você!')
elif fala == 'tesoura' and r == 'papel':
    print('você me venceu!')
