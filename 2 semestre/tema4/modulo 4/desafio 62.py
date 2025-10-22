a = [] # PA
a_1 = int(input('Digite o valor do primeiro termo da PA: '))
a.append(a_1)
r = int(input('Digite o valor da razão da PA: '))
n = t = 2

while n != 11:
    a_n = a[0] + r * (n-1)
    a.append(a_n)
    n += 1
print(a)

while t != 0:
    t = int(input('Você gostaria de ver mais quantos termos? '))
    for _ in range(t):
        a_n = a[0] + r * (n - 1)
        a.append(a_n)
        n += 1
    print(a)

if a[0] > r:
    print('PA = {}n + {}, onde n é o número do termo'.format(r, a[0] - r))
else:
    print('PA = {}n {}, onde n é o número do termo'.format(r, a[0]-r))
