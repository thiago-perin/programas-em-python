print('#' * 6, 'CADASTRO DE 4 PESSOAS', '#' * 6)
nome = []
idade = []
sexo = []

mulheres_menores_20 = 0

for c in range(0,4):
    novo_nome = str(input('Digite o nome de uma pessoa: '))
    nova_idade = int(input('Digite a idade dessa pessoa: '))
    novo_sexo = str(input('Digite o sexo dessa pessoa [M,F]: ')).upper().strip()
    print('{} tem {} anos de vida e é {}.'.format(novo_nome, nova_idade, novo_sexo))
    nome.append(novo_nome)
    idade.append(nova_idade)
    sexo.append(novo_sexo)
    if novo_sexo == 'F' and nova_idade < 20:
        mulheres_menores_20 = mulheres_menores_20 + 1

print('O grupo tem em média {} anos de idade'.format(sum(idade)/4))

idade_do_mais_velho = max(idade)

# Encontra a posição (índice) da idade máxima
posicao_mais_velho = idade.index(idade_do_mais_velho)

# Usa essa posição para pegar o nome correspondente
nome_mais_velho = nome[posicao_mais_velho]

print('A pessoa mais velha é {}.'.format(nome_mais_velho))

print('Total de mulheres com menos de 20 anos: {}'.format(mulheres_menores_20))
