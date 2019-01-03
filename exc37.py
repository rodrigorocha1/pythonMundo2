numero = int(input("Digite um número inteiro: "))
op = int(input('Escolha uma base para converter: \n'
               '[1] -> Binário\n'
               '[2] -> Octal\n'
               '[3] -> Hexadecimal\n'))

if op == 1:
    print(f'{numero} em binário, é igual a {bin(numero)[2:]}')
elif op == 2:
    print(f'{numero} em octal, é igual a {oct(numero)[2:]}')
else:
    print(f'{numero} em Hexadecimal, é igual a {hex(numero)[2:]} ')




