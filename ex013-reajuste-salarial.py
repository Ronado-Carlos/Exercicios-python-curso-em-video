# 13 - Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Digite seu salário atual R$'))
novo_salario = salario + salario * 0.15
print(f'Seu salário de R${salario:.2f} teve um aumento de 15%, agora passou a ser R${novo_salario:.2f}') 