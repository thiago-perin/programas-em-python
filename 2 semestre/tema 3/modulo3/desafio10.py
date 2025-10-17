try:
    a = float(input('Quantos reais você tem na carteira? R$ '))
    s = a / 3.27
    print('Você sabia que você pode trocar o seu dinheiro por {:.2f} dólares.'.format(s))

except ValueError:
    print('Você não digitou um número decimal')
