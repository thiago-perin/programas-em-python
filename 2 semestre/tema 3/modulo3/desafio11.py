try:
    # altura da parede:= alt
    alt = float(input('Qual a altura da parede em metros? '))
    # largura da parede:= lar
    lar = float(input('Qual a largura da parede em metros? '))
    # area da parede:= ap
    ap = alt * lar
    print('Cada litro de tinta, pinta uma área de 2m²')
    print('A área da parede é {} m * {} m = {:.2f} m²'.format(alt, lar, ap))
    # quantidade de tinta:= qt
    qt = ap / 2
    print('A quantidade de tinta necessária para pintá-la é {} m² / (2 m²/l) = {:.2f} litros.'.format(ap,qt))

except ValueError:
    print('Você não deve ter digitado um número decimal')
