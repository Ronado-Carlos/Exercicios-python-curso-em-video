# 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

larg = float(input('Digite a largura da área a ser pintada: '))
comp = float(input('Digite o comprimento da área a ser pintada: '))
area = larg * comp
tinta = area / 2
print(f'Você precisa de {tinta} litros de tinta para pintar {area}m² de área')