import math
num1 = float(input('Digite o valor do cateto oposto: '))
num2 = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(num1, num2)
print('O valor da hipotenusa é igual a {:.0f}'.format(hip))
