# 29- Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Digite a velocidade em Km/h: '))
permitido = 80
acima_limite = vel - permitido
if vel > permitido:
    print(f'Você está acima do limite de velocidade permitido!, você foi multado em R${acima_limite * 7:.2f}')
else:
    print('Você está dentro do limite de velocidade permitido')