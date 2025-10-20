import random

print('#'*8, 'JOKENPO', '#'*8)

print('Vamos jogar JOKENPO?')

print('Escreva 0 para pedra')
print('Escreva 1 para papel')
print('Escreva 2 para tesoura')

a = int(input('Qual você escolheu? '))

if a == 0:
    print('Voce escolheu pedra')
elif a == 1:
    print('Voce escolheu papel')
elif a == 2:
    print('Voce escolheu tesoura')

b = random.randint(0,2)

if b == 0:
    print('Eu escolhi pedra')
elif b == 1:
    print('Eu escolhi papel')
elif a == 2:
    print('Eu escolhi tesoura')

if a == b:
    print('Nós empatamos, vamos de novo?')
elif (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
    print('Você ganhou, vamos de novo?')
else:
    print('Eu ganhei, vamos de novo?')
