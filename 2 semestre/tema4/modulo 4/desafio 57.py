n = 0
while n != 'M' and n != 'F':
    n = str(input('Qual o seu sexo: M ou F? ')).upper()
if n == 'M':
    print('Voce é do sexo Masculino!')
else:
    print('Voce é do sexo Feminino!')
