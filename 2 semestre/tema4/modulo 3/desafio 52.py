print('#' * 6, 'VERIFICANDO SE UM NÚMERO É PRIMO', '#' * 6)
num = int(input('Digite um número: '))
d = []
for c in range(2, num):
    if num % c == 0:
        print('{} é divísivel por {}'.format(num, c))
        d.append(c)
if d == []: # se o conjunto de divisores for vazio
    print('Os únicos divisores de {} é 1 e {}'.format(num, num))
    print('Logo {} é um número primo'.format(num))
else:
    print(d, 'são os divisões de {}'.format(num))
    print('Logo {} não é um número primo'.format(num))
