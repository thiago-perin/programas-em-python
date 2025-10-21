try:
    a = int(input('Digite um número inteiro: '))
    print('A tabuada de {} é'.format(a))
    for c in range(1, 11):
        print('{} * {} = {}'.format(c, a, a*c))

except ValueError:
    print('Você não digitou um número inteiro')
