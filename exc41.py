from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = ano_atual - ano_nascimento
if idade > 9:
    print('Mirin')
elif 9 <= idade <= 14:
    print('Infantil')
elif 14 < idade < 19:
    print('Júnior')
elif 19 <= idade < 25:
    print('Sênior')
else:
    print('Master')



