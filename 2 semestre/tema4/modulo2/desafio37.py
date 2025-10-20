# numero para ser convertido := num
num = int(input('Escreva um número para converter: '))

print('Para converter para binário digite 1')
print('Para converter para octal digite 2')
print('Para converter para hexadecimal digite 3')
a = int(input('Digite 1, 2 ou 3: '))
if a == 1:
    b = bin(num)
    print('O número {} em binário é {}'.format(num, b))
elif a == 2:
    o = oct(num)
    print('O número {} em octal é {}'.format(num, o))
elif a == 3:
    h = hex(num)
    print('O número {} em hexadecimal é {}'.format(num, h))
else:
    print('Você não digitou uma opção válida')
