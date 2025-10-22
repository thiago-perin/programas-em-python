
a = x = y = 0

while a != 5:
    print('\n \n', '#' * 6, 'SOMAR, MULTIPLICAR E MAIOR VALOR', '#' * 6, '\n')
    print(' ' * 8,'x = {} e y = {}. \n'.format(x, y))
    print('O que quer fazer com os valores de x e y? ')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] DETERMINAR O MAIOR VALOR')
    print('[4] ALTERAR OS VALORES')
    print('[5] SAIR DO PROGRAMA')
    a = int(input('Digite uma opção do menu '))

    if a == 1:
        print('A soma entre {} e {} é {}'.format(x, y, x + y))

    if a == 2:
        print('A multiplicação entre {} e {} é {}'.format(x, y, x * y))

    if a == 3:
        print('O maior valor entre {} e {} é {}'.format(x, y, max(x,y)))

    if a == 4:
        x = int(input('Digite um valor para x: '))
        y = int(input('Digite um valor para y: '))
