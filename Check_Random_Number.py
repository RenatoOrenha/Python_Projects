import random
num = random.randint(0,5)
frase = int(input('Digite um número inteiro entre 0 e 5: '))
if frase == num:
    print('Parabéns você acertou!')
else:
    print('Que pena, tente novamente!')
print('--FIM--')

