a = int(input('Estamos em que ano? '))

if a % 4 == 0:
    print('Você sabia que esse ano é bissexto')
else:
    b = a + 4 - (a % 4)
    print('Você sabia que o próximo ano bissexto é {}'.format(b))

c = int(input('Me diga um ano e eu direi se ele foi ou será bissexto: '))

#futuro
if c > a:
    if c % 4 == 0:
        print('O ano {} será bissexto'.format(c))
    else:
        print('O ano {} não será bissexto'.format(c))
else:
    if c % 4 == 0:
        print('O ano {} foi bissexto'.format(c))
    else:
        print('O ano {} não foi bissexto'.format(c))
