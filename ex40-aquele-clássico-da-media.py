# 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {media:.2f}')

if media < 5:
    print('Sua média ficou abaixo de 5.0, você foi Reprovado!')
elif media >= 5 and media < 6.9:
    print('você ficou de recuperação!')
else:
    print('Parabéns você foi Aprovado!')