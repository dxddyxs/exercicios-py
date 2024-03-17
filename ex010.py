n = str(input('digite seu nome: ')).strip()
nome = n.split()
print(f'seu primeiro nome é {nome[0]}')
print(f'seu ulitmo nome é: {nome[len(nome)-1]}')
