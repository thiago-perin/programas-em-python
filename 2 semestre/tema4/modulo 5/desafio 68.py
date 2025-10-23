import random
a = s = t = v = 0
print('=-' * 15)
print('Vamos jogar PAR OU IMPAR')
print('=-' * 15)
while True:
    j = int(input('Digite um valor: ')) # j := jogador
    p = input('Par ou impar? [P, I] ').upper()  # p := palpite
    if p == 'P':
        p = 'PAR'
    else:
        p = 'IMPAR'
    print('-' * 25)
    a = random.randint(0,21) # a := autobot
    s = a + j
    if s % 2 == 0:
        t = 'PAR'
    else:
        t = 'IMPAR'
    print(f'Você jogou {j} e o computador {a}. Total de {s} deu {t}')
    print('-' * 25)
    if p == t:
        print('Você venceu!')
        v += 1
        print('Vamos jogar novamente...')
    else:
        print('Você perdeu!')
        if v == 1:
            palav = 'vez'
        else:
            palav = 'vezes'
        print(f'GAME OVER! Voce venceu {v} {palav}!')
        break
    print('=-' * 15)
