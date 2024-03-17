dados = str(input(('Infome seu sexo \n[M/F]: '))).upper()[0]
while dados not in 'MmFf':
    dados = str(input('Dados invalidos, informe seu sexo: ')).upper()
print(f'Sexo {dados} registrado com sucesso.')
