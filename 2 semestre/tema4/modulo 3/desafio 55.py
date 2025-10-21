print('#' * 6, 'PESO DE 5 PESSOAS', '#' * 6)
peso = []

for c in range(0,5):
    novo_peso = int(input('Digite o peso de uma pessoa: '))
    print('O peso digitado foi: {}.'.format(novo_peso))
    peso.append(novo_peso)

menor_peso = min(peso)
maior_peso = max(peso)

print('O menor peso foi = ', menor_peso)
print('O maior peso foi = ', maior_peso)

# os pesos em ordem crescente
peso.sort()
print(peso)
