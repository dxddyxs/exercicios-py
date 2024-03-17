preço = float(input('preço do produto: '))
print(' Forma de pagamento:\n [ 1 ] à vista dinheiro / cheque\n [ 2 ] à vista cartão\n [ 3 ] 2x no cartão\n [ 4 ] 3x ou mais no cartão')
condição = int(input('qual forma de pagamento? '))
juros = preço / 100
if condição == 1:
    print(f'o desconto será de {preço - (preço * 0.10)}')
elif condição == 2:
    print(f'o desconto será de {preço - (preço * 0.05)}')
elif condição == 3:
    print('não terá desconto')
elif condição == 4:
    print(f'você terá juros de {preço + (preço  * 0.20)}')
