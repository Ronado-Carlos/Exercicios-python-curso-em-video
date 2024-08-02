# 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

# Verificando o maior:
if n1 > n2:
    maior = n1
    print(f'O Número {n1} é o maior')
elif n2 > n1:
    maior = n2
    print(f'O Número {n2} é o maior')
else:
    print('Os números são iguais')