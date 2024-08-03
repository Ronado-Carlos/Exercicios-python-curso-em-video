# 45: Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha uma opção:
      [0] Pedra
      [1] Papel
      [2] Tesoura
      ''')
jogador = int(input('Qual é a sua Jogada?: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-' * 30)
print(f'O Computador jogou {itens[computador]}')
print(f'O Jogador Jogou {itens[jogador]}')
print('-' * 30)

if computador == 0: # Computador jogou Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Computador Venceu!')
    else:
        print('Jogada Inválida!')

elif computador == 1: # Computador jogou Papel
    if jogador == 0:
        print('Computador Venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Computador Venceu')

elif computador == 2: # Computador jogou Tesoura
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')