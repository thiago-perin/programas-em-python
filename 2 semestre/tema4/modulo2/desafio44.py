print('#'*8, 'CALCULO DO PREÇO DO PRODUTO', '#'*8)

p = float(input('Qual o preço do produto? '))

print('O preço à vista em dinheiro/cheque tem 10% de desconto: R$ {:.2f}'.format(p*0.9))
print('O preço à vista no cartão de crédito tem 5% de desconto: R$ {:.2f}'.format(p*0.95))
print('O preço no cartão de crédito até 2x não tem desconto/juros: 1 x R$ {:.2f} ou 2 x {:.2f}'.format(p, p / 2))
print('O preço no cartão de crédito em 3x (com juros de 20%): 3 x R$ {:.2f}'.format(p * 1.2 / 3))
