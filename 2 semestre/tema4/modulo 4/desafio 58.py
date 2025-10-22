import random

print('#' * 6, 'JOGO DA AVIVINHAÇÃO', '#' * 6)

n = random.randint(0,10)
print('Pensei em um número inteiro entre 0 e 10!')
print('Você consegue adivinhar?')
print('Vou contar quantas chances você precisou usar para acertar!')
a = 12
t = [] # vetor de tentativas de a

while a != n:
    a = int(input('Em que número eu pensei? '))
    t.append(a)
    if a != n:
        print('Você errou, eu não pensei no número {}.'.format(a))
print('Parabéns! Eu realmente pensei no número {}.'.format(n))

num_tentativas = len(t)

if num_tentativas == 1:
    print('Você acertou na primeira tentativa.'.format(t))
else:
    print('Você acertou em {} tentativas.'.format(num_tentativas))
