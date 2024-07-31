# 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

# Verificando o menor número:
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando o maior número:
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c

print(f'Foram digitados os números {a, b, c} o maior número entre eles é {maior} e o menor dentre eles é {menor}')