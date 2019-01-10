''' Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros '''
print('*' * 20, 'Lojas ', '*' * 20)
precoProduto = float(input('Preço das compras: '))
print('Formas de pagamento')


op = int(input('[1] - à vista dinheiro cheque\n'
               '[2] - à vista no cartão\n'
               '[3] - Em até duas vezes\n'
               '[4] - 3x ou maix no cartão\n'))

if op == 1:
    valorFinal = precoProduto - (precoProduto * 0.10)
    print(f'Com 10% de desconto, o valor final fica R$ {valorFinal:.2f}')
elif op == 2:
    valorFinal = precoProduto - (precoProduto * 0.05)
    print(f'Com 10% de desconto, o valor final fica R$ {valorFinal:.2f}')
elif op == 3:
    print(f'Valor final R${precoProduto:.2f}\n parcelado em duas vezes\nValor das parcelas R$ {(precoProduto/2):.2f}')
else:
    valorFinal = precoProduto + (precoProduto * 0.20)
    print(f'Valor final: R$ {valorFinal:.2f}\n'
          f'Total de juros: R$ {precoProduto * 0.20}'
          f'\nValor das parcelas: R$ {(valorFinal * 3):.2f}')





