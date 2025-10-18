print('Salários superiores a R$ 1250 terá um aumento de 10%')
print('Salários inferiores ou iguais a R$ 1250 terá um aumento de 15%')
s = int(input('Digite o valor do salário do funcionário: '))

if s > 1250:
    ns = s * 1.1
    print('O novo salário desse funcionário será {}.'.format(ns))
else :
    ns = s * 1.15
    print('O novo salário desse funcionário será {}.'.format(ns))
