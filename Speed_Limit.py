import random
num = random.randint(0,320)
if num > 80:
    print('O motorista foi multado!')
    multa = (num - 80) * 7
    print('O valor da multa é R$ {:.2f}'.format(multa))
else:
    print('O motorista está dentro do limite de velocidade!')

