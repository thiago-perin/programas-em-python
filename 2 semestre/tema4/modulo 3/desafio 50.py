a=[]
b=[]
s=0
for c in range(0,6):
    num = int(input('digite um numero: '))
    a.append(num)
    if a[c] % 2 == 0:
        print(a[c], ' é par')
        b.append(num)
        s += a[c]
    else:
        print(a[c], ' é impar')
print(a, 'são os números que você digitou')
print(b, 'são os números pares que você digitou')
print(s, 'é a soma dos números pares que você digitou')
