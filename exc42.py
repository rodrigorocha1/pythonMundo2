print('*' * 20, 'Classificação do triângulo', '*' * 20)

l1 = float(input('Digite o lado do triângulo: '))
l2 = float(input('Digite o lado do triângulo: '))
l3 = float(input('Digite o lado do triângulo: '))

if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    if l1 == l2 == l3:
        print(f'Os lados {l1}, {l2}, {l3} formam um triângulo equilatero')
    elif l1 != l2 != l3 != l1:
        print(f'Os lados {l1}, {l2}, {l3} formam um triângulo escaleno ')
    else:
        print(f'Os lados {l1}, {l2}, {l3} formam um triângulo isórceles')
else:
    print(f'Os lados {l1}, {l2}, {l3} não podem formar um triângulo')




