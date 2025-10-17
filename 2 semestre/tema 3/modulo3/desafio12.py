try:
    # preço de um produto:= pp
    pp = float(input('O preço do produto em reais é: '))
    # desconto de 5% do produto:= des
    des = pp * 0.05
    print('5% de desconto desse produto vale: R$ {:.2f} '.format(des))
    # preco do produto com desconto:= pd
    pd = pp - des
    print('O preço do produto com desconto é R$ {:.2f} '.format(pd))

except ValueError:
    print('Você não deve ter digitado um número decimal')
