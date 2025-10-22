b = s = 0
n = 0
men = 10**5
mai = -10**5
print('#' * 6, 'SOMA DE N NUMEROS', '#' * 6)
print('Para sair do programa digite 999 a qualquer momento')
while b != 999:
    b = int(input('Digite um número inteiro: '))
    if b != 999:
        s += b
        mai = max(b, mai)
        men = min(b, men)
        n += 1
        media = s / n
if n > 0:
    print('O menor número que você digitou é {}'.format(men))
    print('O maior número que você digitou é {}'.format(mai))
    print('A média dos {} números que você digitou é {}'.format(n, media))
else:
    print('Nenhum número válido foi digitado para gerar resultados')
