from datetime import date

print('*' * 20, 'Alistamento militar ', '*' * 20)
ano_nascimento = int(input('Digite o ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'{idade} anos')

if idade < 18:
    print(f'Ainda faltam {ano_atual - ano_nascimento} anos para o alistamento')
else:
    print(f'Passou {idade - 18} anos para o alistamento. Você deve se alistar imediatamente')


