b = s = 0
n = 0
print('#' * 6, 'SOMA DE N NUMEROS', '#' * 6)
print('Para sair do programa digite 999 a qualquer momento')
while b != 999:
    b = int(input('Digite um número inteiro: '))
    s += b
    n += 1
    if n == 1:
        print('O número que você digitou é {}'.format(s))
    elif b != 999:
        print('A soma dos {} números que você digitou é {}'.format(n, s))
print('A soma dos {} números que você digitou é {}'.format(n-1, s-999))
