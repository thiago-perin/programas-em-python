import random

n = random.randint(0,5)
print('Pensei em um número inteiro entre 0 e 5!')
print('Você consegue adivinhar?')
print('Vou te dar duas chances!')
a = int(input('Em que número eu pensei? '))

if a == n:
    print('Parabéns! Eu realmente pensei no número {}. Você acertou!'.format(n))
else:
    print('Você tem mais uma chance!')
    b = int(input('Em que número eu pensei? '))
    if b == n:
        print('Parabéns! Eu realmente pensei no número {}. Você acertou!'.format(n))
    else:
        print('Você perdeu!')
        print('Eu pensei no número ', n)
