a1 = int(input('Digite o valor do primeiro termo da PA: '))
r = int(input('Digite o valor da razão da PA: '))
PA = []

for c in range(0,10):
    num = a1 + c * r
    PA.append(num)
print('{} + {}n = {}, onde n é o número do termo'.format(a1-r, r, PA))
