q = s = 0
while True:
    b = int(input('Digite um número: (999 para parar) '))
    if b == 999:
        break
    s += b
    q += 1
print(f'A soma vale {s}.')
print(f'Foram digitados {q} números.')
