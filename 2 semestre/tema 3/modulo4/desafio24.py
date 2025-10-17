# nome de uma cidade:= nome
a = input('Digite o nome de uma cidade: ')

if a.strip():
    nome = a.strip()
    print('Você digitou', nome.title())
    vetor = nome.title().split()
    print('O conjunto das palavras do nome da cidade é', vetor)

    if vetor[0] == 'Santo':
        print('Então o nome da cidade começa com "Santo".')
    else:
        print('Então o nome da cidade não começa com "Santo".')
else:
    print('Você não digitou um nome válido.')
