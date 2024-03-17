while True:
    from time import sleep
    n1 = int(input('digite um número: '))
    n2 = int(input('digite um número: '))
    op = int(input('MENU\n[ 1 ]somar\n[ 2 ]multiplicar\n[ 3 ]maior\n[ 4 ]novos números\n[ 5 ]sair do programa\ndigite o número para fazer as respectivas ações: '))
    if op == 1:
        soma = n1 + n2
        print(f'a soma é igual a {soma}')
        print('_'*30)
        break    
    elif op == 2:
        mult = n1 * n2
        print(f'{n1} multiplicado por {n2} é igual a {mult}')
        print('_'*30)
        break

    def numberLen(x , y): # função pra dizer se o nmr é maior ou menor
        n1 = x
        n2 = y
        if n1 > n2:
            print(f'{n2} é menor que {n1}')
        elif n1 < n2:
            print(f'{n2} é maior que {n1}')  
        return
        
    if op == 3:
        numberLen(n1 , n2)
        print('_'*30)
        break

    elif op == 4:
        n3 = int(input('primeiro número: '))
        n4 = int(input('segundo número: '))
    
    elif op == 5:
        print('você saira em 3'), sleep(1)
        print('2'), sleep(1)
        print('1')
        print('_'*30)
        break