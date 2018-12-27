'''Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. '''

print('*' * 10, 'Emprestimo', '*' * 10)

valorCasa = float(input('Qual o valor da casa R$? '))
salario = float(input('Qual o salário do comprador R$? '))
totalAnos = int(input('Quantos anos ele vai pagar a casa? '))

prestacao = valorCasa / (totalAnos * 12) #Valor da casa dividido pelo tempo convertido em meses = prestação

if prestacao >= (salario * 0.30):
    print(f'Valor da Casa: R$ {valorCasa:.2f}\nSalário: R$ {salario:.2f}\nPrestação: R$ {prestacao:.2f}\nTotal de anos: {totalAnos}\nResultado: Emprestimo negado')
else:
    print(
        f'Valor da Casa: R$ {valorCasa:.2f}\nSalário: R$ {salario:.2f}\nPrestação: R$ {prestacao:.2f}\nTotal de anos: {totalAnos}\nResultado: Emprestimo aceito')



