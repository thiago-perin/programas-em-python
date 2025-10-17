n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 9.0:
    print('Parabéns')
else:
    if m >= 6.0:
        print('Não fez mais do que a sua obrigação')
    else:
        print('Estude mais')
