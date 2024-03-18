lista = []
while True:
    lista.append(int(input('digite um numero: ')))
    
    condicao = str(input('deseja continuar? \n[S/N]: ')).upper()[0]
    print('-'*40)
    
        
    if condicao == 'N':
        if 5 not in lista:    
            print('o numero 5 não esta na lista')
        break
lista_reversa = reversed(lista)
print(lista)
print(f'você digitou {len(lista)} elementos')
print(f'o numero 5 esta na lista na posição {lista.index(5)}')
print(f'a lista em descrescente fica : {lista_reversa}')