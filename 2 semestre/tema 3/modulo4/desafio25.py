a = input('Digite o nome de uma pessoa: ')

if a.strip():
    nome = a.strip()
    print('Você digitou', nome.title())
    vetor = nome.title().split()
    print('O conjunto das palavras do nome da pessoa é', vetor)

    if 'Silva' in vetor:
        print('Então o nome da pessoa tem "Silva".')
    else:
        print('Então o nome da pessoa não tem "Silva".')
else:
    print('Você não digitou um nome válido.')
