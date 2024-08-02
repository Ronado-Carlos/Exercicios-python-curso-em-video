# 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

casa = float(input('Qual o valor da casa?: '))
salario = float(input('Qual seu salário?: '))
anos = int(input('Em quantos anos pretende pagar?'))
parcelas = anos * 12
valor_parcela = casa / parcelas
minimo = salario * 30/100

print(f'Para financiar uma casa de R${casa:.2f} em {anos} anos')
print(f'{parcelas} prestações de R${valor_parcela:.2f}')

if valor_parcela <= minimo:
    print('Empéstimo aprovado')
else:
    print('Empréstimo negado')
