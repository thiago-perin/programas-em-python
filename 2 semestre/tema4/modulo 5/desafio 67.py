print('#'*15, 'TABUADA', '#'*15)
while True:
    a = int(input('Quer ver a tabuada de qual valor? '))
    if a < 0:
        break
    else:
        print('-' * 30)
        for c in range(1, 11):
            print(f'{a} x {c} = {a*c}')
        print('-' * 30)
print('Programa TABUADA encerrado. Volte sempre!')
