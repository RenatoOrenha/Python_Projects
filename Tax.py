num = float(input('Qual a distância de sua viagem em Km? '))
if num <= 200:
    tarifa1 = num * 0.5
    print('O valor da tarifa é R$ {:.2f}'.format(tarifa1))
else:
    tarifa2 = num * 0.45
    print('O valor da tarifa é R$ {:.2f}'.format(tarifa2))
