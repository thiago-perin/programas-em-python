print('='*30)
nome=input('Qual o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('='*30)
n1=int(input('{}, Digite um valor: '.format(nome)))
n2=int(input('{}, Digite outro valor: '.format(nome)))
print('='*30)
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma vale {}'.format(s))
print('A multiplicação vale {}'.format(m))
print('A divisão vale {:.3f}'.format(d))
print('A divisão inteira vale {}'.format(di))
print('A potencia vale {}'.format(e))

# end='' não quebra linha
# \n quebra linha
