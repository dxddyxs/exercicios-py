n1 = int(input('digite um número: '))
print(''' escolha uma das bases para converção:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('sua opção: '))
if opção == 1:
    print(f'seu número em binário é {bin(n1)[2:]}')
elif opção == 2:
    print(f'seu número em octal é {oct(n1)[2:]}')
elif opção == 3:
    print(f'seu número para hexadecimal é {hex(n1)[2:]}')