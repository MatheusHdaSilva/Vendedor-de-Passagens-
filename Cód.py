
viagem =  float(input('Qual a distância da sua viagem?'))
s1 = (viagem * 0.50)
s2 = (viagem * 0.45)
print('voçê está a começar um viagem de {:.1f}KM'.format(viagem))
if viagem > 200:
  print('E o preço da sua viagem será de R$:{:.2f}'.format(s2))
else:
  print('E o preço da sua viajem será de {:.2f}'.format(s1))