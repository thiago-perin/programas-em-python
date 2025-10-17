dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km foram rodados? '))

total = (dias * 60) + (km * 0.15)
print('O total a pagar é de R$ {}.'.format(total))
