tupla = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico - PR', 
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás'
         , 'Bahia', 'Vasco', 'Atlético - MG', 'Fluminense', 'Botafogo'
         , 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'os 5 primeiros colocados são {tupla[0:6]}')

print('-'*30)

print(f'os ultimos 4 colocados são {tupla[16:]}')

print('-'*30)

print(f'a tabela em ordem alfabética {sorted(tupla)}')

print('-'*30)

print(f'Chapecoense esta na posição {tupla.index('Chapecoense')}')