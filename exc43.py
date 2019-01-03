'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso - 30 até 40: Obesidade
 - Acima de 40: Obesidade Mórbida '''

from math import pow

print('*' * 20, 'IMC', '*' * 20)

peso = float(input('Digite o peso: '))
altura = float(input('Digita a altura: '))

IMC = peso / pow(altura, 2)


