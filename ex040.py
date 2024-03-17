somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range (1, 5):
    n = str(input('digite seu nome: ')).upper().replace(' ', '')
    i = int(input('digite a idade: '))
    s = str(input('digite o sexo: ')).upper().replace(' ', '')
    somaidade += i
    if c == 1 and s in 'masculino':
        maioridadehomem = i
        nomevelho = n
    if s in 'masculino' and i > maioridadehomem:
        maioridadehomem = i
        nomevelho = n
    if s in 'feminino' and i < 20:
        totmulher20 += 1
    mediaidade = somaidade / 4
    print(f'a média de idade do grupo é {mediaidade} anos.')
    print(f'o nome do mais velho/a é {nomevelho},  e tem {maioridadehomem} anos')
    print(f'tem {totmulher20} mulheres com menos de 20 anos')
