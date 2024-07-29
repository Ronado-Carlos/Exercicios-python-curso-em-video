# 31- Desenvolva um programa que pergunte a distância de uma viagem em KM. 
# Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200 km e R$0,45 para viagens mais longas.
distancia = float(input('Digite a  distância em KM: '))
if distancia <= 200:
    viagem_curta = distancia * 0.50
    print(f'Para uma viagem de {distancia:.0f} km o valor da passagem é R${distancia * 0.50:.2f}')
elif distancia > 200:
    viagem_longa = distancia * 0.45
    print(f'Para uma viagem de {distancia:.0f} km o valor da passagem é R${distancia * 0.45:.2f}')