from random import choice
from time import sleep


print('*' * 20, 'JOKENPO', '*' * 20)
cpu = choice(['pedra', 'papel', 'tesoura'])

palpiteJogador = str(input('Escolha o palpite'
                           '\n[1] = Pedra'
                           '\n[2] = Papel'
                           '\n[3] = Tesoura: '))

print('*' * 6, 'JO', '*' * 6)
sleep(2)
print('*' * 6, 'KEN', '*' * 6)
sleep(2)
print('*' * 6, 'PO', '*' * 6)

if palpiteJogador == 1:  # pedra
    if cpu == 'pedra':
        print(f'Jogador jogou pedra\nComputador jogou {cpu}\nEmpate')  # empate na pedra
    if cpu == 'papel':
        print(f'Jogador jogou pedra\nComputador jogou {cpu}\nComputador Vence')  # Computador ganha na pedra
    if cpu == 'tesousa':
        print(f'Jogador jogou pedra\nComputador jogou {cpu}\nJogador Vence')  # Jogador ganha na pedra
elif palpiteJogador == 2:  # papel
    if cpu == 'pedra':
        print(f'Jogador jogou Papel\nComputador jogou {cpu}\nJogador Vence')  # Jogador ganha no papel
    if cpu == 'papel':
        print(f'Jogador jogou Papel\nComputador jogou {cpu}\nEmpate')  # empate no papel
    if cpu == 'tesousa':
        print(f'Jogador jogou Papel\nComputador jogou {cpu}\nComputador Vence')  # Computador ganha na tesoura
else:  # Tesoura
    if cpu == 'pedra':
        print(f'Jogador jogou Tesoura\nComputador jogou {cpu}\nComputador Vence')  # Computador ganha na pedra
    if cpu == 'papel':
        print(f'Jogador jogou Tesoura\nComputador jogou {cpu}\nJogador Vence')  # Jogador ganha no tesoura
    if cpu == 'tesousa':
        print(f'Jogador jogou Tesoura\nComputador jogou {cpu}\nEmpate')  # empate no papel






