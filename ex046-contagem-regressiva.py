# 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

resultado = ""
for contador in range(10, -1, -1):
    resultado += f"{contador} "
    print(f'\r{resultado}', end='')
    sleep(1)
print('\nAcabou!')
