print('#' * 6, 'VERIFICANDO SE É UM PALÍNDROMO', '#' * 6)

frase = str(input('Digite uma frase: '))

# 1. Tratar a frase (remover espaços e ignorar maiúsculas/minúsculas)
frase_tratada = frase.replace(' ', '').lower()

# 2. Criar o vetor de caracteres (lista)
v = list(frase_tratada)

# 3. Criar a versão invertida
v_invertido = v[::-1]

# 4. Comparar
if v == v_invertido:
    print('É um palíndromo!')
else:
    print('NÃO é um palíndromo.')

# (Opcional) Você pode mostrar as listas para entender melhor:
print('Original:', v)
print('Invertido:', v_invertido)
