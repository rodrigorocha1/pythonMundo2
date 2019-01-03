print('*' * 20, 'Cálculo de Média', '*' * 20)

nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Reprovado com média {media:.1f}')
elif 5.0 <= media <= 6.9:
    print(f'Recuperação com média {media:.1f}')
else:
    print(f'Aprovado com média {media:.1f}')

