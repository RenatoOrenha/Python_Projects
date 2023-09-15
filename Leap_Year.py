import math
ano = int(input('Digite um ano qualquer: '))
if math.remainder(ano,4) == 0:
    print('Ano Bisiesto!')
else:
    print('Não é Ano Bisiesto!')
