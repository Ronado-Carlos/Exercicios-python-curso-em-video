# 26 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra A
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
vezes = frase.count('A')
posicao1 = frase.find('A') + 1
ultimapos = frase.rfind('A') + 1
print(f'A letra A aparece {vezes} vezes')
print(f'A letra A aparece primeiro na posição {posicao1}')
print(f'A letra A aparece pela última vez na posição {ultimapos}')