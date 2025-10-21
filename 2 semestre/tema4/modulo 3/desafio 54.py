print('#' * 6, 'MAIORIDADE e MENORIDADE', '#' * 6)
ano_nasc = []
idade = []
dmenor = 0
dmaior = 0

for c in range(0,7):
    novo_ano_nasc = int(input('Digite um ano de nascimento: '))
    print('Ano de nascimento: {}.'.format(novo_ano_nasc))
    ano_nasc.append(novo_ano_nasc)
    novo_idade = 2025 - novo_ano_nasc
    idade.append(novo_idade)
    if novo_idade >= 21:
        print('Já tem {} anos de idade'.format(novo_idade))
        print('É maior de idade')
        dmaior += 1
        print('Quantidade de pessoas que atingiram a maioridade: ', dmaior)
    else:
        print('Já tem {} anos de idade'.format(novo_idade))
        print('É menor de idade')
        dmenor += 1
        print('Quantidade que é menor de idade: ', dmenor)
print('Vetor dos anos de nascimento = ', ano_nasc)
print('Vetor das idades = ', idade)
print('Quantidade de pessoas com maioridade = ', dmaior)
print('Quantidade de pessoas com menoridade = ', dmenor)
