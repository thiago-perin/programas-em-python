print('#'*8, 'CONFEDERAÇÃO NACIONAL DE NATAÇÃO', '#'*8)

ano = int(input('Qual o seu ano de nascimento? '))
i = 2025 - ano

if i < 10:
    print('Você é da categoria MIRIM.')
elif i < 15:
    print('Você é da categoria INFANTIL.')
elif i < 20:
    print('Você é da categoria JUNIOR.')
elif i < 21:
    print('Você é da categoria SENIOR.')
else:
    print('Você é da categoria MASTER.')
