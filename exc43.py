from math import pow

print('*' * 20, 'IMC', '*' * 20)

peso = float(input('Digite o peso: '))
altura = float(input('Digita a altura: '))

IMC = peso / pow(altura, 2)

if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 <= IMC <= 25.0:
    print('Peso ideal')
elif 25.0 < IMC <= 30.0:
    print("Sobrepeso")
elif 30 < IMC <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')





