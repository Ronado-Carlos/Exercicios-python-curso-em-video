# 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
# O Alistamento é realizado no período de 1º de janeiro a 30 de junho,do ano em que o jovem completar 18 (anos)

import datetime

ano_nascimento = int(input('Qual o ano de nascimento?: '))
agora = datetime.datetime.now()
ano_atual = agora.year
mes_atual = agora.month
idade = ano_atual - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')
if idade < 18:
    saldo = 18 - idade
    print('Você ainda não atingiu a idade para alistamento ')
    print(f'Ainda faltam {saldo} anos para você se alistar')
elif idade > 18:
    saldo = idade - 18
    print(f'O período de alistamento já passou')
    print(f'Seu período de alistamento foi a {saldo} anos')
else: 
    print(f'Você está dentro do período de alistamento, APRESENTE-SE!')