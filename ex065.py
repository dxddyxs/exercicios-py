lista = []
listaimpar = []
listapar = []
while True:
    x = (int(input('digite um número: ')))
    lista.append(x)
    
    if x % 2 == 0:
        listapar.append(x)
    elif x % 2 >= 1:
        listaimpar.append(x)
    
    condicao = str(input('deseja continuar? \n[S/N]: ')).upper()[0]
    print('-'*40)
    if condicao == 'N':
        break
print(f'lista com tudo {lista}')
print(f'lista com numeros pares {listapar}')
print(f'lista com numeros impares {listaimpar}')