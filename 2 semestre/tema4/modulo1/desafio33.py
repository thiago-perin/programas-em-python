a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

menor = min(a, b, c)
maior = max(a, b, c)

print('O maior deles é {}.'.format(maior))
print('O menor deles é {}.'.format(menor))
