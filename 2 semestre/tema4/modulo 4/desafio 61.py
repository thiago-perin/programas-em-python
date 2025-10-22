a = [] # PA
a_1 = int(input('Digite o valor do primeiro termo da PA: '))
a.append(a_1)
r = int(input('Digite o valor da razão da PA: '))
n = 1

while n != 11:
    if n == 1:
        print('a_1 = {}'.format(a[0]))
        n += 1
    else:
        print('a_{} = {}'.format(n, a[0] + (n-1) * r))
        n += 1
if a[0] > r:
    print('PA = {}n + {}, onde n é o número do termo'.format(r, a[0] - r))
else:
    print('PA = {}n {}, onde n é o número do termo'.format(r, a[0]-r))
