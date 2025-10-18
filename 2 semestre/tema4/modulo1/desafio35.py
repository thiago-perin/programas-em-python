print('Vamos verificar se é possível formar um triângulo sabendo o valor de 3 lados:')
a = int(input('Digite o valor do primeiro lado em cm: '))
b = int(input('Digite o valor do segundo lado em cm: '))
c = int(input('Digite o valor do terceiro lado em cm: '))

menor = min(a, b, c)
maior = max(a, b, c)
mediano = a + b + c - menor - maior

if menor + mediano <= maior:
    print('O Triangulo não pode ser formado pelos 3 lados de tamanhos {} cm, {} cm e {} cm.'.format(a, b, c))
else :
    print('O Triangulo pode ser formado pelos 3 lados de tamanhos {} cm, {} cm e {} cm.'.format(a, b, c))
