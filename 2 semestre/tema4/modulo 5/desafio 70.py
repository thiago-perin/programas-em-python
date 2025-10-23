n = [] # nome do produto cadastrado
p = [] # preço do produto cadastrado
c = t = e = pmb = a = 0
b = 10**100
print('-'*50)
print('#'*15, 'LOJA SUPER BARATAO', '#'*15)
print('-'*50)
while c != 3:
    print('#' * 15, 'MENU DE CADASTRO', '#' * 15)
    print('[1] CADASTRAR UM NOVO PRODUTO')
    print('[2] VISUALIZAR PRODUTOS CADASTRADOS')
    print('[3] SAIR DO CADASTRO')

    while True:
        try:
            c = int(input('Escolha uma das opções: '))

            if c in (1, 2, 3):
                break  # Se for 1, 2 ou 3, sai do loop de validação
            else:
                # Se for um número, mas não 1, 2 ou 3 (ex: 4, 5)
                print('ERRO: Opção inválida. Digite 1, 2 ou 3.')

        except ValueError:
            # Se a pessoa digitou 'y' ou qualquer coisa que não seja um número
            print('ERRO: Entrada inválida. Por favor, digite um NÚMERO.')

    a = 0

    if c == 1:

        n_n = str(input('Qual o nome do produto? '))
        n.append(n_n)

        while True:
            p_n = float(input('Qual o preço desse produto? '))
            if p_n > 0 and p_n <= 10**100:
                break
            print('ERRO: Por favor, digite um valor válido.')
        t += p_n
        p.append(p_n)
        if p_n > 1000:
            e += 1

        if p_n < b:
            b = p_n
            pmb = n_n

    if c == 2:
        print('#' * 10, 'PRODUTOS CADASTRADOS', '#' * 10)
        while a < len(n):
            print(f'O produto {n[a]} custa R$ {p[a]:.2f}.')
            a += 1

    if c == 3:
        break
print(' FIM DO PROGRAMA '.center(50, '-'))

if t > 0: # Ou if len(n) > 0:
    print(f'A) O total da compra é R$ {t:.2f}.')
    print(f'B) Foram comprados {e} produtos acima de 1000 reais.')
    print(f'C) O produto mais barato foi {pmb} que custa R$ {b:.2f}.')
else:
    print('Nenhum produto foi cadastrado.')
