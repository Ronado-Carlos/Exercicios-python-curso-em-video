# 005 - Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor
numero = int(input('Digite um número inteiro para descobrir seu sucessor e seu antecessor:'))
antecessor = numero - 1
sucessor = numero + 1
print(f'O antecessor de {numero} é {antecessor}, e seu sucessor é {sucessor}')