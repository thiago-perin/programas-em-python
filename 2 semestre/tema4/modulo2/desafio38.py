a = int(input('Escreva o primeiro número inteiro: '))
b = int(input('Escreva o segundo número inteiro: '))

print('Comparando agora os dois:')
if a > b:
    print('O número {} é maior que {}'.format(a, b))
elif a < b:
    print('O número {} é menor que {}'.format(a, b))
else:
    print('Os número {} e {} são iguais'.format(a, b))
