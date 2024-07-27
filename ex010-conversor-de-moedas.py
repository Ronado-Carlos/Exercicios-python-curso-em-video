# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US 1,00 R$ 5,66
real = float(input('Quantos Reais você tem na carteira?: '))
dolar = real * 5.66
print(f'R${real} equivalem a US{dolar} dólares')