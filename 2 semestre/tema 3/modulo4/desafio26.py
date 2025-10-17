f = input('Digite uma frase qualquer: ')

if f.strip():
    frase = f.strip()
    print('Você digitou', frase.capitalize())
    conta = frase.count('a')

    if conta == 0:
        print('A sua frase não possui letra "a".')
    else:
        print('A letra "a" apareceu {} vezes na frase digitada.'.format(conta))

        ppos = frase.find('a')
        print('A letra "a" apareceu pela primeira vez na frase na {} posição.'.format(ppos))

        upos = frase.rfind('a')
        print('A letra "a" apareceu pela ultima vez na frase na {} posição.'.format(upos))
else:
    print('Você não digitou um frase válida.')
