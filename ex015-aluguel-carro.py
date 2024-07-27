# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar.
# Sabendo que o aluguel custa R$60, por dia e R$0,15 por KM rodado.

km_rodado = float(input('Digite a quantidade de KM rodados: '))
dias = int(input('Quantos dias?: '))
valor_diaria = 60
valor_km = 0.15
km = km_rodado * valor_km
diaria = dias * valor_diaria
print(f'Você rodou {km_rodado} em {dias} dias, o valor do aluguel é R${km + diaria:.2f}')