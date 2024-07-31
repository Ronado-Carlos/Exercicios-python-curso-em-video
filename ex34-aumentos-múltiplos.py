# 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de R$ 15%.
salario = float(input('Qual seu salário: '))

if salario > 1250:
    novo_salario = salario + (salario * 10/100)
    print(f'Com um aumento de 10%, seu salário passou de {salario} para R${novo_salario:.2f}')
if salario <= 1250:
    novo_salario = novo_salario = salario + (salario * 15/100)
    print(f'Com um aumento de 15%, seu salário passou de {salario} para R${novo_salario:.2f}')