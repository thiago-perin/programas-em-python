n = input('Digite o nome completo de uma pessoa: ')

if n.strip():
    m = n.strip()
    nome = m.title()
    print('Você digitou o nome:', nome)

    vetor = nome.split()
    print('O conjunto de cada palavra do nome dessa pessoa é: ', vetor)

    prim = vetor[0]
    print('O primeiro nome da pessoa é {}.'.format(prim))

    ulti = vetor[-1]
    print('O último nome da pessoa é {}.'.format(ulti))

else:
    print('Você não digitou um nome válido.')
