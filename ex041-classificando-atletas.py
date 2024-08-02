# 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
# e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

import datetime

ano_nascimento = int(input('Qual o ano de nascimento?: '))
agora = datetime.datetime.now()
ano_atual = agora.year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'Você tem {idade} anos de idade, sua categoria é MIRIM')
elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} anos de idade, sua categoria é INFANTIL')
elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} anos de idade, sua categoria é JÚNIOR')
elif idade > 19  and idade <= 25:
    print(f'Você tem {idade} anos de idade, sua categoria é SÊNIOR')
elif idade > 25:
    print(f'Você tem {idade} anos de idade, sua categoria é MASTER')