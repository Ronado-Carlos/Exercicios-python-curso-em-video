# 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o valor do produto: '))
menu = int(input('''Qual a forma de pagamento?
      [1] a vista dinheiro ou cheque: 10% de desconto
      [2] a vista no cartão: 5% de desconto
      [3] Parcelado cartão 2x: preço formal
      [4] 3x ou mais no cartão: 20% de juros     
      '''))
if menu == 1:
    desconto = preco * 10/100
    print(f'Pagando a vista você tem um desconto de 10%, o produto que custava R${preco:.2f} com o desconto você paga R${preco - desconto:.2f}')
elif menu == 2:
    desconto = preco * 5/100
    print(f'Pagando a vista no cartão você tem um desconto de 5%, o produto que custava R${preco:.2f} com o desconto você paga R${preco - desconto:.2f}')
elif menu == 3:
    print(f'Para pagamentos parcelados no cartão em 2x não há desconto, o valor do produto é o preço original R${preco:.2f}')
elif menu == 4:
    juros = preco * 20/100
    novo_valor = preco + juros
    print(f'Para pagamentos em 3x no cartão há um acréscimo de 20%, o poduto de R${preco} passa a custar R${novo_valor:.2f}, 3x de R${novo_valor / 3:.2f}')