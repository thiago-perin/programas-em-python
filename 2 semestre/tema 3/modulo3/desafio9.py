try:
    a = int(input('Digite um número inteiro: '))
    print('A tabuada de {} é'.format(a))
    for i in range(1, 11):
        print('{} * {} = {}'.format(i, a, a*i))

except ValueError:
    print('Você não digitou um número inteiro')
