print('#'*8, 'TIPO DE TRIÂNGULO', '#'*8)

a = int(input('Qual o comprimento de um lado do triângulo? '))
b = int(input('Qual o comprimento do segundo lado do triângulo? '))
c = int(input('Qual o comprimento do terceiro lado do triângulo? '))

min = min(a, b, c)
max = max(a, b, c)
med = a + b + c - max - min

exis = max - min - med

if exis >= 0:
    print('O triângulo não existe.')
elif min == max:
    print('O triângulo é EQUILÁTERO.')
elif min == med or med == max:
    print('O triângulo é ISÓSCELES.')
else:
    print('O triângulo é ESCALENO.')
