# Importa o módulo 'locale' para formatar números (dinheiro) no padrão brasileiro (R$ 5.000,00)
import locale

# Configura o programa para usar a formatação local do sistema (R$, vírgula, ponto)
# A string vazia '' significa "use a formatação padrão deste computador"
locale.setlocale(locale.LC_ALL, '')

# --- CABEÇALHO DO BANCO ---
print('=' * 50)
print('BANCO CEV'.center(50, ' '))
print('=' * 50)
print('Olá Senhor Thiago')
# A senha não está sendo usada para validação neste momento, apenas coletada.
senha = str(input('Digite sua senha: '))

# --- INICIALIZAÇÃO DAS VARIÁVEIS GLOBAIS ---

# 'c' controla o loop principal do menu (começa com 0 para entrar no loop)
c = 0
# 'saldo' é uma LISTA que armazena o histórico de saldos. 
# Começa com o saldo inicial de 5 milhões. Cada saque adicionará um novo saldo no final.
saldo = [5000000.0]
# 'saque' é uma LISTA que armazena o histórico de todos os saques realizados.
saque = []

# --- LOOP PRINCIPAL DO CAIXA ELETRÔNICO ---
# O programa fica aqui dentro até o usuário digitar '3' (Sair)
while c != 3:
    print('CAIXA ELETRONICO'.center(50, '#'))
    print('[1] SACAR UM VALOR')
    print('[2] SALDO')
    print('[3] SAIR DA SUA CONTA')

    # --- VALIDAÇÃO DA ENTRADA DO MENU ---
    # Loop infinito (while True) que só é quebrado (break) se a entrada for válida.
    while True:
        try:
            # Tenta converter a entrada para um número inteiro
            c = int(input('Escolha uma das opções: '))

            # Se for um inteiro, verifica se é uma das opções válidas (1, 2 ou 3)
            if c in (1, 2, 3):
                break  # Entrada válida (1, 2 ou 3), quebra o loop de validação
            else:
                # É um número, mas não é uma opção válida (ex: 4, 5, 0)
                print('ERRO: Opção inválida. Digite 1, 2 ou 3.')

        except ValueError:
            # Se o 'try' falhou (usuário digitou 'y', 'abc', etc.),
            # o programa pula para cá em vez de quebrar.
            print('ERRO: Entrada inválida. Por favor, digite um NÚMERO.')

    # --- OPÇÃO [1]: SACAR UM VALOR ---
    if c == 1:
        # Zera as contagens de notas para este saque específico
        not100 = not50 = not10 = 0
        # Pede o valor do saque e converte para float (número com decimal)
        saque_n = float(input('Quanto deseja sacar? R$ '))

        # --- Verificações de Erro do Saque ---

        # 1. Verifica se o valor é múltiplo de 10 (resto da divisão por 10 tem que ser 0)
        #    Usamos != 0 (diferente de zero) para pegar o caso de erro.
        if saque_n % 10 != 0:
            print('Não é possível sacar esse valor (Notas disponíveis: R$ 100, R$ 50, R$ 10).')

        # 2. Verifica se o usuário tem saldo suficiente.
        #    saldo[-1] é um atalho para pegar o ÚLTIMO item da lista (o saldo atual).
        elif saque_n > saldo[-1]:
            print('Não tem saldo disponível na conta')

        # 3. Se passou nas duas verificações, o saque é válido.
        else:

            # --- Bloco de Cálculo de Notas ---
            # 'valor_restante' começa com o valor total do saque
            valor_restante = saque_n

            # Calcula notas de R$ 100 (// é divisão inteira)
            not100 = int(valor_restante // 100)
            # Atualiza o 'valor_restante' com o que SOBROU (% é módulo/resto)
            valor_restante = valor_restante % 100

            # Calcula notas de R$ 50 com o valor que sobrou
            not50 = int(valor_restante // 50)
            # Atualiza o 'valor_restante'
            valor_restante = valor_restante % 50

            # O que sobrou só pode ser pago com notas de R$ 10
            not10 = int(valor_restante // 10)

            # --- Bloco de Impressão Inteligente das Notas ---

            # 'partes' vai guardar as strings das notas (ex: "5 notas de R$ 100")
            partes = []

            # Só adiciona na lista se a quantidade for maior que zero
            if not100 > 0:
                # Operador Ternário: define o plural da palavra 'nota'
                texto_nota = 'nota' if not100 == 1 else 'notas'
                partes.append(f'{not100} {texto_nota} de R$ 100')

            if not50 > 0:
                texto_nota = 'nota' if not50 == 1 else 'notas'
                partes.append(f'{not50} {texto_nota} de R$ 50')

            if not10 > 0:
                texto_nota = 'nota' if not10 == 1 else 'notas'
                partes.append(f'{not10} {texto_nota} de R$ 10')

            # --- Formatação final da string de notas (com ',' e 'e') ---
            print('Total de ', end='')  # 'end=""' impede o print de pular linha

            if len(partes) > 1:
                # Junta todos os itens, MENOS o último, usando ", "
                primeiros = ', '.join(partes[:-1])
                # Pega o último item
                ultimo = partes[-1]
                print(f'{primeiros} e {ultimo}')
            elif len(partes) == 1:
                # Se só tem um tipo de nota, imprime só ele
                print(partes[0])
            # --- Fim do Bloco de Impressão ---

            # --- Bloco de Atualização do Saldo ---
            # Se o saque foi bem-sucedido, registramos tudo.

            saque.append(saque_n)  # Adiciona o valor sacado ao histórico 'saque'
            saldo_atual = saldo[-1]  # Pega o saldo que está no fim da lista
            novo_saldo = saldo_atual - saque_n
            saldo.append(novo_saldo)  # Adiciona o NOVO saldo no fim da lista 'saldo'

    # --- OPÇÃO [2]: SALDO ---
    elif c == 2:
        print('SALDO'.center(50, '#'))
        print('-' * 50)

        # Verifica se já houve algum saque.
        # Se len(saldo) > 1, significa que temos o saldo inicial [0] e +1 saldo novo [1]
        if len(saldo) > 1:
            # saldo[-2] é o penúltimo item (o saldo ANTERIOR)
            # saque[-1] é o último saque realizado
            # locale.currency() formata o número como R$ 0.000,00
            print(f'SALDO ANTERIOR: {locale.currency(saldo[-2], grouping=True)}')
            print(f'SAQUE: {locale.currency(saque[-1], grouping=True)}')
            print('-' * 50)
            # saldo[-1] é o último item (o saldo ATUAL)
            print(f'SALDO: {locale.currency(saldo[-1], grouping=True)}')
            print('-' * 50)
        else:
            # Se len(saldo) ainda é 1, nenhum saque foi feito.
            # Mostra apenas o saldo inicial (que é o último e único item, saldo[-1])
            print(f'SALDO: {locale.currency(saldo[-1], grouping=True)}')
            print('-' * 50)

    # --- OPÇÃO [3]: SAIR ---
    # Se c == 3, o 'while c != 3' lá de cima vai falhar e o loop principal termina.
    # O 'break' garante que o loop pare imediatamente.
    elif c == 3:
        break

# --- FIM DO PROGRAMA ---
# Esta linha só é executada quando o loop principal termina (quando c == 3)
print(' Volte sempre ao BANCO CEV! Tenha um bom dia')
