# numero digitado:= num
a = (input('Digite um número de 0 a 9999: '))
if a.isnumeric():
    num = int(a)

    # verifica se o numero digitado é um inteiro de 0 a 9999
    if 0 <= num <= 9999 :

        print('#' * 8, 'numero digitado', '#' * 8)
        print('A decomposição do numero digitado é:')

        unidade = num %10
        print('Unidades: {}.'.format(unidade))

        dezena = (num % 100 - unidade) / 10
        print('Dezenas: {}.'.format(int(dezena)))

        centena = (num % 1000 - (num % 100)) / 100
        print('Centenas: {}.'.format(int(centena)))

        milhar = num / 1000
        print('Unidades de Milhar: {}.'.format(int(milhar)))

    # caso o usuário tenha digitado errado
    else:
        # retorna um erro
        print('Você não digitou um numero inteiro de 0 a 9999.')
else:
    print('Você não digitou um numero.')
