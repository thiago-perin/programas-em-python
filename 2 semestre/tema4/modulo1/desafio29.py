print('Um carro passou pelo radar!')
v = int(input('Qual a velocidade que ele passou?'))

print('O limite de velocidade nesse radar é de 80 km/h!')

if v <= 80:
    print('O carro passou a {} km/h. Ele passou abaixo do limite de velocidade!'.format(v))
else:
    print('O carro passou a {} km/h. Ele passou acima do limite!'.format(v))
    print('Envie uma multa digital ao motorista, dizendo que ele foi multado!')
    print('Calculando o valor da multa...')
    print('A multa vai custar 7 reais por cada km acima do limite de velocidade!')
    m = (v-80) * 7
    print('A multa vai custar {} reais!'.format(m))
    n = 'Nome do motorista'
    print('Caro Sr. {}. O Sr. passou a {} km/h'.format(n, v))
    print('A multa nesse caso é de {} reais. Dirija com mais cautela e evite ser multado novamente'.format(m))
