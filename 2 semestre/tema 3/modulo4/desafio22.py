# nome de uma pessoa:= nome
nome = input('Qual o seu nome? ')

# verifica se o nome é composto apenas por letras
if nome.replace(' ', '').isalpha():

    print('#' * 8, 'SEU NOME EM LETRAS MAIÚSCULAS', '#' * 8)
    # coloca o nome com todas as letras em maiúscula
    print('O seu nome é {}! \n'.format(nome.upper()))

    print('#' * 8, 'seu nome em letras minúsculas', '#' * 8)
    # coloca o nome com todas as letras em minúsculas
    print('O seu nome é {}! \n'.format(nome.lower()))

    print('#' * 8, 'Quantidade de letras do seu nome', '#' * 8)
    # conta a quantidade de letras do nome
    nomesemespaco = nome.replace(' ', '')
    print('O seu nome "{}" tem {} letras! \n'.format(nome.title(), len(nomesemespaco)))

    print('#' * 8, 'Quantidade de letras do seu primeiro nome', '#' * 8)
    # conta a quantidade de letras do primeiro nome
    vetor = nome.split()
    print('O seu primeiro nome "{}" tem {} letras!'.format(vetor[0].title(), len(vetor[0])))

# caso o usuário tenha digitado um caracter que não é uma letra
else:
    # retorna um erro, dizendo que ele deveria usar apenas letras
    print('Você não digitou um nome válido. Por favor, use apenas letras.')
