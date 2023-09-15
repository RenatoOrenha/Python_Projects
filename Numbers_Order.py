n1 = int(input('Digite um número inteiro quaquer: '))
n2 = int(input('Digite um segundo número inteiro: '))
n3 = int(input('Digite um terceiro número inteiro: '))
if n1 > n2 and n1 > n3:
    print('Este é o maior número: {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('Este é o maior número: {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('Este é o maior número: {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('Este é o menor número: {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('Este é o menor número: {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('Este é o menor número: {}'.format(n3))

