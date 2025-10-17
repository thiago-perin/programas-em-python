try:
    # salário de um funcionário:= sf
    sf = float(input('O salário de um funcionário em reais é: '))
    # aumento de 15% no salário de um funcionário:= as
    asf = sf * 0.15
    print('15% de aumento no salário de um funcionário vale: R$ {:.2f} '.format(asf))
    # salário de um funcionário com aumento:= sa
    sa = sf + asf
    print('O salário de um funcionário com aumento de 15% vale R$ {:.2f} '.format(sa))

except ValueError:
    print('Você não deve ter digitado um número decimal')
