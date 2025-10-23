i = []
s = []
c = dmaior = macho = fem19 = 0
print('#'*15, 'CADASTRO DE PESSOAS', '#'*15)
while c != 2:
    print('#' * 15, 'MENU DE CADASTRO', '#' * 15)
    print('[1] CADASTRAR UMA NOVA PESSOA')
    print('[2] SAIR DO CADASTRO')
    c = int(input('Quer cadastrar uma nova pessoa? [1] para sim e [2] para não '))

    if c == 1:

        while True:
            i_n = int(input('Qual a idade dessa pessoa? '))
            if i_n < 120 and i_n >= 0:
                break  # Quebra o loop se a entrada for de 0 a 120
            print('ERRO: Por favor, digite uma idade válida.')
        
        i.append(i_n)

        if i_n > 18:
            dmaior += 1

        while True:
            s_n = str(input('Qual o sexo dessa pessoa? [M] para masculino [F] para feminino ')).upper().strip()
            if s_n in 'MF':
                break  # Quebra o loop se a entrada for 'M' ou 'F'
            print('ERRO: Por favor, digite apenas M ou F.')
        s.append(s_n)

        if s_n == 'M':
            macho += 1
        if s_n == 'F' and i_n < 20:
            fem19 += 1

    if c == 2:
        break

print(f'A) Foram cadastradas {dmaior} pessoas com mais de 18 anos.')
print(f'B) Foram cadastradas {macho} homens.')
print(f'C) Foram cadastradas {fem19} mulheres com menos de 20 anos.')
