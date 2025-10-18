print('Bem vindo a Perin turismo')
print('Viagens até 200 km custam R$ 0.50 / km.')
print('Viagens acima de 200 km custam R$ 0.45 / km.')
d = int(input('Quantos km você viajará conosco? '))

if d > 200:
    c1 = 0.45 * d
    print('O custo da viagem será {} reais'.format(c1))
else:
    c2 = 0.5 * d
    print('O custo da viagem será {} reais'.format(c2))
