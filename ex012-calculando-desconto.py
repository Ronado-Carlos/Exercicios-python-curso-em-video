# 12 - Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto R$ '))
desconto = preco * 5/100
valor_desconto = preco - desconto
print(f'O produto tinha o preço de R${preco:.2f}, com o desconto de 5% o novo preço ficou R${valor_desconto:.2f} ')
