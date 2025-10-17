a = input('Informe a temperatura em ºC: ')

tempC = float(a)
print('Você digitou {}ºC'.format(tempC))

tempF = float(tempC * 1.8) + 32
print('Essa temperatura é equivalente a {}ºF.'.format(tempF))
