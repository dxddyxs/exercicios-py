homi = 0
maioridade = 0
menormu = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo \n[M/F]: ')).upper()[0]
    if idade >= 18 and sexo == 'M':
        maioridade += 1
        homi += 1
    elif idade < 20 and sexo == 'F':
        menormu += 1
        if idade > 18:
            maioridade += 1
    elif idade > 18:
        maioridade += 1
    elif idade > 18 and sexo == 'F':
        maioridade += 1
        
    condição = input('Quer continuar? \n[S/N] ').upper()[0]
    if condição == 'N':
        print(f'total de pessoas com mais de 18 ano: {maioridade}')
        print(f'ao todo temos {homi} homens cadastrados')
        print(f'e temos {menormu} mulheres com menos de 20 anos')
        break
#by daddy