# 28- Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. o programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
computador = randint(0 ,5)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')

jogador = int(input('Qual número pensei? : '))
if jogador == computador:
    print('Parabéns você acertou!')
else:
    print(f'Você errou! pensei no número {computador}')