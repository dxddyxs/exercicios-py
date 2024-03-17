from random import randint
v = 0

def escolha(choice, numero):
    if choice == 'P':
        print(f'impar! meu número é {numero}')
    elif choice == 'I':
        print(f'par! meu numero é {numero}')
    return

while True:
    eu = str(input('par ou impar? \n[P/I] ')).upper()[0]
    y = randint(1, 11)
    x = int(input('diga um valor: '))
    escolha(eu, y)
    numero = (x + y) % 2
    if eu == 'P' and numero == 0:
        print('você venceu!')
        v += 1
    elif eu == 'I' and numero != 0:
        print('você venceu!')
        v += 1
    elif eu == 'I' and numero == 0:
        print('você perdeu!')
    elif eu == 'P' and numero != 0:
        print('você perdeu!')
    elif eu != 'P' or eu != 'I':
        print('opção não disponivel!')
        break
    
    condicao = input('você deseja continuar? \n[S/N] ').upper()[0]
    if condicao == 'N':
        print(f'você teve {v} vitorias.')
        break