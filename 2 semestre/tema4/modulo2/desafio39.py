print('#'*8, 'ALISTAMENTO MILITAR', '#'*8)

d = int(input('Qual o dia do seu nascimento? '))
m = int(input('Qual o mês do seu nascimento? '))
a = int(input('Qual o ano do seu nascimento? (com 4 dígitos) '))

mesa = m - 10
mesb = 10 - m
mesc = 10 + 12 - m
anoa = 2025 - a
anob = a + 18

if mesa < 0:
    print('Você tem {} anos e {} meses de idade.'.format(anoa,mesb))
elif mesa == 0:
    print('Esse mês você fez {} anos de idade.'.format(anoa))
else:
    print('Você tem {} anos e {} meses de idade.'.format(anoa - 1, mesc))
    
print('O alistamento é em julho e você deve alistar no ano que você faz 18 anos')

if anoa < 17:
    print('Você só deve se alista no ano de de {}, daqui a {} anos.'.format(anob, anob - 2025))
elif anoa == 17:
    print('Ano que vem você deve se alistar em julho.')
elif anoa == 18:
    print('Esse ano você deveria ter se alistado em julho, procure uma agencia militar urgente.')
else:
    print('Você deveria ter se alistado em {}. Procure uma agencia militar urgente'.format(anob))
