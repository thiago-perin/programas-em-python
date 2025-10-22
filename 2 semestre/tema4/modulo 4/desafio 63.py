m=1
while m != -1:
    print('#' * 6, 'SEQUENCIA DE FIBONACCI', '#' * 6)
    a = [] # SEQUENCIA DE FIBONACCI
    m = int(input('Quantos termos da sequência de Fibonacci você quer? '))

    a_1 = 1
    a.append(a_1)
    a_2 = 1
    a.append(a_2)
    n = 3
    b = a_n = 0
    if m == 1:
        print('[{}]'.format(a[0]))
    elif m == 2:
        print('[{}, {}]'.format(a[0], a[1]))
    elif m >= 3:
        while n <= m:
            b = len(a)
            a_n = a[b-1] + a[b-2]
            a.append(a_n)
            n += 1
        print(a)
    else:
        print('Você não digitou um número válido')
