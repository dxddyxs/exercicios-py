f = str(input('digite uma frase: ')).upper().strip()
print(f'a letra A aparece {f.count("A")} vezes na frase.')
print(f'a letra A apareceu na posição {f.find("A")+1}')
print(f'a letra A apareu na ultima vez em {f.rfind("A")+1}')