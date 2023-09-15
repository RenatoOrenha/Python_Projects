salary = float(input('Digite o valor do seu salário em R$: '))
if salary > 1250:
    ns1 = salary * 1.1
    print('O seu novo salário é R$ {:.2f}'.format(ns1))
else:
    ns2 = salary * 1.15
    print('O seu novo salário é R$ {:.2f}'.format(ns2))
