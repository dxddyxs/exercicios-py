valores = []

def remover_repetidos(valores):
    l = []
    for i in valores:
        if i not in valores:
            l.append(i)
    l.sort()
    return l

while True:
    
    x = int(input('digite um valor: '))
    
    if x in valores:
        remover_repetidos(valores)
        print('não é possivel adicionar numeros repetidos')
    else:
        valores.append(x)
        print('valor adicionado com sucesso!')
    
    condicao = str(input('deseja continuar? \n[S/N]: ')).upper()[0]
    print('-'*40)
    if condicao == 'N':
        print(f'você digitou os valores {sorted(valores)}')
        break