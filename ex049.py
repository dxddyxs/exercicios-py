n = s = c = 0
while True:
    n = int(input('digite um valor (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'fora digitados {c} numeros')
print(f'os numeros somados dão {s}')