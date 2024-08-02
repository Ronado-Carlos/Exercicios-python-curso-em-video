# 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
# IMC = peso/(altura x altura)
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura * altura)

print('Seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
  print('Você está abaixo do peso ideal')
elif imc >= 18.5 and imc < 25:
  print('PARABÉNS, Você está no peso ideal')
elif imc > 25 and imc < 30:
  print('Você está com sobrepeso')
elif 30 <= imc < 40:
  print('Você está com OBESIDADE')
else:
  print('Você está com obesidade mórbida!')