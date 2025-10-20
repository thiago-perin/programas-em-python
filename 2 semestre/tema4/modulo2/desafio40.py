print('#'*8, 'BOLETIM', '#'*8)

m = float(input('Qual a sua média? '))

if m < 5:
    print('Você está REPROVADO.')
elif m < 7:
    print('Você está de RECUPERAÇÃO.')
else:
    print('Você está APROVADO')
