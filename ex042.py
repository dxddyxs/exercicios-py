from time import sleep
from random import randint
while True:
    np = 0 # var para cada erros / palpites
    sleep(1) # tempo de 1 sec para cada print / input
    print('estou pensando em um número de 0 a 10...')
    jogador = int(input('qual número estou pensando? '))
    r = randint(0, 10) # um número aleatório de 0 a 10


    def numberLen(x , y): # função pra dizer se o nmr é maior ou menor
        jogador = x
        r = y
        if jogador > r:
            print(f'meu número é menor que {jogador}')
        elif jogador < r:
            print(f'meu número é maior que {jogador}')  
        return


    while jogador != r: # enquanto a var r for diferente da var jogador ira imprimir... 
        numberLen(jogador, r)
        p = int(input(('chute outro número: ')))
        np += 1
        sleep(1)
        if np > 1:
            print(f'acertou em {np} chutes lerdao')
        elif np == 1:
            print(f'acertou em {np} chute ai sim ')
        elif np == 0:
            print(f'acertou em cheio mlk')
        print('_'*20)
        break
