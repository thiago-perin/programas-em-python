print('#'*8, 'CALCULO DO IMC', '#'*8)

a = float(input('Qual a sua altura em metros? '))
p = float(input('Qual o seu peso em kg? '))
imc = p / (a * a)
print('Sua altura é {:.2f} m, seu peso é {:.2f} kg e seu IMC é {:.2f} kg/m²'.format(a, p, imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 35:
    print('Você está com obesidade grau I.')
elif imc < 40:
    print('Você está com obesidade grau II.')
else:
    print('Você está com obesidade grau III.')
