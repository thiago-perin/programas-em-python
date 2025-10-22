import math

n = a = 0

while a != 3:
    print('\n \n', '#' * 6, 'FATORIAL DE UM VALOR', '#' * 6, '\n')
    print(' ' * 8,'n = {}. \n'.format(n))
    print('O que quer fazer? ')
    print('[1] CALCULAR O FATORIAL')
    print('[2] ALTERAR O VALOR DE N')
    print('[3] SAIR DO PROGRAMA')
    a = int(input('Digite uma opção do menu '))

    if a == 1:
        print('O resultado de {}! = {}'.format(n, math.factorial(n)))

    if a == 2:
        n = int(input('Digite um valor para n: '))
