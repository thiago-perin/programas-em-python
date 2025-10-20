print('Bem vindo ao banco Perin, você selecionou "fazer empréstimo para adquirir uma casa"')
# valor da casa := cas
cas = float(input('Qual o valor da casa? '))
# valor do salário := sal
sal = float(input('Qual o valor do seu salário em reais? '))
# tempo de empréstimo := tem
tem = float(input('Qual o valor do tempo em meses? '))
# amortização := amo
amo = cas / tem
print('O valor da amortização da primeira parcela é R$ {:.2f}.'.format(amo))
# juros mensal = jur
jur = cas * 0.0058
print('O valor do juros da primeira parcela é R$ {:.2f}.'.format(jur))
# seguro total := seg
seg = cas * 0.00024
print('O valor do seguro da primeira parcela é R$ {:.2f}.'.format(seg))
# taxa operacional := tax
tax = 25
print('O valor da taxa peracional da primeira parcela é R$ {:.2f}.'.format(tax))
# valor da parcela := par
par = amo + jur + seg + tax
print('O valor da primeira parcela é R$ {:.2f}.'.format(par))
# O máximo que uma pessoa pode comprometer do seu salário para financiamento é de 30% := div
div = sal * 0.30
print('Observe que 30% do seu salário é R$ {:.2f}'.format(div))
if par < div:
    print('Você pode fazer o financiamento dessa casa')
else:
    print('Você não pode fazer o financiamento dessa casa')
