# 16 - crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc
num = float(input('Digite um valor qualquer: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')